from codeGen import codeGen
from gen.minipythonLexer import minipythonLexer
from gen.minipythonParser import minipythonParser

from antlr4 import *

import sys
import os

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


if __name__ == '__main__':
    main()