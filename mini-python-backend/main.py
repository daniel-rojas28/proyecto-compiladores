from codeGen import codeGen
from codeContext import CodeContext
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
    # lexer = minipythonLexer(input)
    # stream = CommonTokenStream(lexer)
    # parser = minipythonParser(stream)
    # tree = parser.program()
    # code_gen_visitor = codeGen()
    # generar_bytecode(code_gen_visitor.visit(tree))
    try:


        myListener = MyErrorListener()
        input = FileStream('./test.txt')
        inst = minipythonLexer(input)
        tokens = CommonTokenStream(inst)
        parser = minipythonParser(tokens)

        inst.removeErrorListeners()
        inst.addErrorListener(myListener)

        parser.removeErrorListeners()
        parser.addErrorListener(myListener)

        # print("ARBOL")
        tree = parser.program()
        # print(tree)
        # print(Trees.toStringTree(tree, None, parser))

        print("------------------ CODE GEN ------------------")
        code_gen_visitor = codeGen()
        generar_bytecode(code_gen_visitor.visit(tree))

        print("------------------ CODE CONTEXT ------------------")
        code_context = CodeContext()

        for i in code_context.errors:
            print(i)

        # tokensList = printTokens(inst.getAllTokens())

        errors = myListener.newErrors

        print("------- CONTEXT ERRORS -------")
        print(errors)

        print("--------------")
        print("EJECUCIÓN: ")
        os.system("MiniPy bytecode.txt")
    except Exception as e:
        print({'message': str(e)})


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
