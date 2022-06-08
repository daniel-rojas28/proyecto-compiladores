import os
from codeGen import codeGen
from codeContext import CodeContext
from gen.minipythonLexer import minipythonLexer
from gen.minipythonParser import minipythonParser

from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener


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


def print_tokens(tokens):
    tokens_response = []
    print("---TOKENS---")
    for token in tokens:
        token_text = str(token.type) + "-" + token.text
        tokens_response.append(token_text)
        print(token_text)
    return tokens_response


def generate_bytecode(code):
    f = open('./bytecode.txt', 'w')
    cont = 0
    for instr in code:
        if instr.arg is None:
            f.write("{} {}\n".format(str(cont), instr.instr))
        else:
            f.write("{} {} {}\n".format(str(cont), instr.instr, instr.arg))
        cont += 1
    f.close()


def main():
    try:
        my_listener = MyErrorListener()
        file_input = FileStream('./test.txt')
        inst = minipythonLexer(file_input)
        tokens = CommonTokenStream(inst)
        parser = minipythonParser(tokens)

        inst.removeErrorListeners()
        inst.addErrorListener(my_listener)

        parser.removeErrorListeners()
        parser.addErrorListener(my_listener)
        tree = parser.program()

        print("------------------ CODE GEN ------------------")
        code_gen_visitor = codeGen()
        generate_bytecode(code_gen_visitor.visit(tree))

        print("------------------ CODE CONTEXT ------------------")
        code_context = CodeContext()

        for i in code_context.errors:
            print(i)

        errors = my_listener.newErrors

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
