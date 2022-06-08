from gen.minipythonVisitor import minipythonVisitor
from gen.minipythonLexer import minipythonLexer 
from gen.minipythonParser import minipythonParser
from SymbolTable import SymbolTable
from antlr4 import *

class codeGen(minipythonVisitor):

    class Instr:
        def __init__(self, i, a):
            self.instr = i
            self.arg = a

    def __init__(self):
        self.table = SymbolTable()
        self.errors = []

        self.codigo = []
        self.instActual = 0
        self.variablesLocalesDefinidas = []

    def generate(self, instr, arg):
        self.codigo.append(codeGen.Instr(instr, arg))
        self.instActual += 1

    def printCode(self):
        print("----- CODIGO GENERADO ------\n")
        index = 0
        for x in self.codigo:
            print(str(index) + " " + x.instr, end = '')
            index+=1
            if (x.arg):
                print(" " + x.arg)
            else:
                print("")

    def agregarVariableDefinida(self, nombre, lista):
        if (self.buscarVariableDefinida(nombre,lista) == False):
            lista.append(nombre)

    def buscarVariableDefinida(self, nombre, lista):
        for v in lista:
            if v == nombre:
                return True
        return False

    def visitAstProgram(self, ctx: minipythonParser.AstProgramContext):
        super().visitAstProgram(ctx)
        self.printCode()
        return self.codigo

    def visitAstStatementDef(self, ctx: minipythonParser.AstStatementDefContext):
        return super().visitAstStatementDef(ctx)

    def visitStatement(self, ctx: minipythonParser.StatementContext):
        return super().visitStatement(ctx)

    def visitAstDefStatment(self, ctx: minipythonParser.AstDefStatmentContext):
        if (ctx.IDENTIFIER().getText() == "main"):
            self.generate("DEF", "Main")
        else:
            self.generate("DEF", ctx.IDENTIFIER().getText())
        if (ctx.argList()):
            self.visit(ctx.argList())

        self.visit(ctx.sequence())
        if (ctx.IDENTIFIER().getText() == "main"):
            self.generate("END", None)
        else:
            self.generate("RETURN", None)

        return None

    def visitAstArgList(self, ctx: minipythonParser.AstArgListContext):
        for i in ctx.IDENTIFIER():
            self.generate("PUSH_LOCAL", i.getText())
            self.agregarVariableDefinida(i.getText(), self.variablesLocalesDefinidas)
        return None

    def visitAstIfStatment(self, ctx: minipythonParser.AstIfStatmentContext):
        self.visit(ctx.expression())
        etiq1 = self.instActual
        self.generate("JUMP_IF_FALSE", "0")
        self.visit(ctx.sequence(0))
        if (ctx.ELSE()):
            etiq2 = self.instActual
            self.generate("JUMP_ABSOLUTE", "0")
            self.codigo[etiq1].arg = str(self.instActual)
            self.visit(ctx.sequence(1))
            self.codigo[etiq2].arg = str(self.instActual)
        else:
            self.codigo[etiq1].arg = str(self.instActual)
        return None

    def visitAstWhileStatment(self, ctx: minipythonParser.AstWhileStatmentContext):
        etiq1 = self.instActual
        self.generate("JUMP_ABSOLUTE", "0")
        etiq2 = self.instActual
        self.visit(ctx.sequence())
        self.codigo[etiq1].arg = str(self.instActual)
        self.visit(ctx.expression())
        self.generate("JUMP_IF_TRUE", str(etiq2))

        return None

    def visitAstForStatement(self, ctx: minipythonParser.AstForStatementContext):
        return super().visitAstForStatement(ctx)

    def visitAstReturnStatement(self, ctx: minipythonParser.AstReturnStatementContext):
        self.visit(ctx.expression())
        self.generate("RETURN_VALUE", None)
        return None

    def visitAstPrintStatement(self, ctx: minipythonParser.AstPrintStatementContext):
        self.visit(ctx.expression())
        self.generate("LOAD_GLOBAL", "print")
        self.generate("CALL_FUNCTION", "1")
        return None

    def visitAstAssignStatment(self, ctx: minipythonParser.AstAssignStatmentContext):
        if (self.buscarVariableDefinida(ctx.IDENTIFIER().getText(), self.variablesLocalesDefinidas) == False):
            self.generate("PUSH_LOCAL", ctx.IDENTIFIER().getText())
        self.visit(ctx.expression())
        self.generate("STORE_FAST", ctx.IDENTIFIER().getText())
        return None

    def visitAstFunctionCallStatement(self, ctx: minipythonParser.AstFunctionCallStatementContext):
        cant_params = 0
        if (ctx.expressionList()):
            cant_params = self.visit(ctx.expressionList())
        if (ctx.IDENTIFIER().getText() != "main"):
            self.generate("LOAD_GLOBAL", ctx.IDENTIFIER().getText())
            self.generate("CALL_FUNCTION", str(cant_params))
        return None

    def visitAstExpressionStatement(self, ctx: minipythonParser.AstExpressionStatementContext):
        return super().visitAstExpressionStatement(ctx)

    def visitAstSequence(self, ctx: minipythonParser.AstSequenceContext):
        return super().visitAstSequence(ctx)

    def visitAstMoreStatements(self, ctx: minipythonParser.AstMoreStatementsContext):
        return super().visitAstMoreStatements(ctx)

    def visitAstExpression(self, ctx: minipythonParser.AstExpressionContext):
        self.visit(ctx.getChild(0))
        i = 1
        while i < len(ctx.children):
            oper = ctx.children[i]
            i += 1
            self.visit(ctx.getChild(i))
            self.generate("COMPARE_OP", oper.getText())
            i += 1

        return None

    def visitAstAdditionExpression(self, ctx: minipythonParser.AstAdditionExpressionContext):
        self.visit(ctx.getChild(0))
        i = 1
        while i < len(ctx.children):
            oper = ctx.children[i]
            i += 1
            self.visit(ctx.getChild(i))
            if (oper.getText() == "+"):
                self.generate("BINARY_ADD", None)
            elif (oper.getText() == "-"):
                self.generate("BINARY_SUBSTRACT", None)
            i += 1

        return None

    def visitAstMultiplicationExpression(self, ctx: minipythonParser.AstMultiplicationExpressionContext):
        self.visit(ctx.getChild(0))
        i = 1
        while i < len(ctx.children):
            oper = ctx.children[i]
            i += 1
            self.visit(ctx.getChild(i))
            if (oper.getText() == "*"):
                self.generate("BINARY_MULTIPLY", None)
            elif (oper.getText() == "/"):
                self.generate("BINARY_DIVIDE", None)
            i += 1

        return None

    def visitAstElementExpression(self, ctx: minipythonParser.AstElementExpressionContext):
        return super().visitAstElementExpression(ctx)

    def visitAstExpressionList(self, ctx: minipythonParser.AstExpressionListContext):
        for e in ctx.expression():
            self.visit(e)
        return len(ctx.expression())

    def visitAstNumPEAST(self, ctx: minipythonParser.AstNumPEASTContext):
        self.generate("LOAD_CONST", ctx.NUM().getText())
        return None

    def visitAstStringPEAST(self, ctx: minipythonParser.AstStringPEASTContext):
        self.generate("LOAD_CONST", ctx.STRING().getText())
        return None

    def visitAstDesignatorPEAST(self, ctx: minipythonParser.AstDesignatorPEASTContext):
        return super().visitAstDesignatorPEAST(ctx)

    def visitAstBlockPEAST(self, ctx: minipythonParser.AstBlockPEASTContext):
        return super().visitAstBlockPEAST(ctx)

    def visitAstListPEAST(self, ctx: minipythonParser.AstListPEASTContext):
        return super().visitAstListPEAST(ctx)

    def visitAstLenPEAST(self, ctx: minipythonParser.AstLenPEASTContext):
        return super().visitAstLenPEAST(ctx)

    def visitAstDesignatorAST(self, ctx: minipythonParser.AstDesignatorASTContext):
        if (ctx.expressionList() == None):
            self.generate("LOAD_FAST", ctx.IDENTIFIER().getText())
        else:
            cant_params = self.visit(ctx.expressionList())
            self.generate("LOAD_GLOBAL", ctx.IDENTIFIER().getText())
            self.generate("CALL_FUNCTION", str(cant_params))
        return None


