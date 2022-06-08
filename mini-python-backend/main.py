from codeGen import codeGen
from gen.minipythonLexer import minipythonLexer
from gen.minipythonParser import minipythonParser

from antlr4 import *
from flask import Flask, request
from flask_cors import CORS
from antlr4.error.ErrorListener import ErrorListener


import sys
import os

# Initialize server
app = Flask(__name__, static_url_path='')
UPLOAD_FOLDER = './UPLOAD_FOLDER'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
path = os.getcwd() + "/UPLOAD_FOLDER"
if not os.path.exists(path):
    os.mkdir(path)
CORS(app)

class MyErrorListener(ErrorListener):

    def __init__(self):

        self.newErrors = []
        super(MyErrorListener, self).__init__()

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        if isinstance(recognizer, minipythonParser):
            self.newErrors.append("PARSER ERROR - line " + str(line) + ":" + str(column) + " " + msg)
        else:
            if isinstance(recognizer, minipythonLexer):
                self.newErrors.append("SCANNER ERROR - line " + str(line) + ":" + str(column) + " " + msg)
            else:
                self.newErrors.append("OTHER ERROR - line " + str(line) + ":" + str(column) + " " + msg)



@app.route('/checkFile', methods=["POST"])
def checkFile():
    try:
        myListener = MyErrorListener()
        file = request.files['file']
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
        path = "./UPLOAD_FOLDER/" + file.filename

        input = FileStream(path)

        inst = minipythonLexer(input)
        tokens = CommonTokenStream(inst)
        parser = minipythonParser(tokens)

        inst.removeErrorListeners()
        inst.addErrorListener(myListener)

        parser.removeErrorListeners()
        parser.addErrorListener(myListener)

        print("ARBOL")
        tree = parser.program()
        # print(Trees.toStringTree(tree, None, parser))

        print("VISITOR")
        v = codeGen()
        generar_bytecode(v.visit(tree))

        for i in v.errors:
            print(i)

        # tokensList = printTokens(inst.getAllTokens())

        if os.path.exists(path):
            os.remove(path)
        errors = myListener.newErrors
        return {'tokens': "tokens",
                'errors': errors}, 200
    except Exception as e:
        return {'message': str(e)}, 400


def printTokens(tokens):
    tokensResponse = []
    print("---TOKENS---")
    for token in tokens:
        tokenText = str(token.type) + "-" + token.text
        tokensResponse.append(tokenText)
        print(tokenText)
    return tokensResponse


def generar_bytecode(codigo):
    f = open('./bytecode.txt', 'w')
    cont = 0
    for instr in codigo:
        if (instr.arg == None):
            f.write("{} {}\n".format(str(cont), instr.instr))
        else:
            f.write("{} {} {}\n".format(str(cont), instr.instr, instr.arg))
        cont += 1
    f.close()

def main():
    input = FileStream('./test.txt')
    lexer = minipythonLexer(input)
    stream = CommonTokenStream(lexer)
    parser = minipythonParser(stream)
    tree = parser.program()
    v = codeGen()
    generar_bytecode(v.visit(tree))
    
    print("\nEJECUCIÓN: ")
    os.system("MiniPy bytecode.txt")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
