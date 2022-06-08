# Generated from C:/Users/geral/Desktop/Proyecto Compi/mini-python-backend/tarea4\minipython.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .minipythonParser import minipythonParser
else:
    from minipythonParser import minipythonParser

# This class defines a complete generic visitor for a parse tree produced by minipythonParser.

class minipythonVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by minipythonParser#astProgram.
    def visitAstProgram(self, ctx:minipythonParser.AstProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by minipythonParser#astStatementDef.
    def visitAstStatementDef(self, ctx:minipythonParser.AstStatementDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by minipythonParser#statement.
    def visitStatement(self, ctx:minipythonParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by minipythonParser#astDefStatment.
    def visitAstDefStatment(self, ctx:minipythonParser.AstDefStatmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by minipythonParser#astArgList.
    def visitAstArgList(self, ctx:minipythonParser.AstArgListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by minipythonParser#astIfStatment.
    def visitAstIfStatment(self, ctx:minipythonParser.AstIfStatmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by minipythonParser#astWhileStatment.
    def visitAstWhileStatment(self, ctx:minipythonParser.AstWhileStatmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by minipythonParser#astForStatement.
    def visitAstForStatement(self, ctx:minipythonParser.AstForStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by minipythonParser#astReturnStatement.
    def visitAstReturnStatement(self, ctx:minipythonParser.AstReturnStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by minipythonParser#astPrintStatement.
    def visitAstPrintStatement(self, ctx:minipythonParser.AstPrintStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by minipythonParser#astAssignStatment.
    def visitAstAssignStatment(self, ctx:minipythonParser.AstAssignStatmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by minipythonParser#astFunctionCallStatement.
    def visitAstFunctionCallStatement(self, ctx:minipythonParser.AstFunctionCallStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by minipythonParser#astExpressionStatement.
    def visitAstExpressionStatement(self, ctx:minipythonParser.AstExpressionStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by minipythonParser#astSequence.
    def visitAstSequence(self, ctx:minipythonParser.AstSequenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by minipythonParser#astMoreStatements.
    def visitAstMoreStatements(self, ctx:minipythonParser.AstMoreStatementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by minipythonParser#astExpression.
    def visitAstExpression(self, ctx:minipythonParser.AstExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by minipythonParser#astAdditionExpression.
    def visitAstAdditionExpression(self, ctx:minipythonParser.AstAdditionExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by minipythonParser#astMultiplicationExpression.
    def visitAstMultiplicationExpression(self, ctx:minipythonParser.AstMultiplicationExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by minipythonParser#astElementExpression.
    def visitAstElementExpression(self, ctx:minipythonParser.AstElementExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by minipythonParser#astExpressionList.
    def visitAstExpressionList(self, ctx:minipythonParser.AstExpressionListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by minipythonParser#astNumPEAST.
    def visitAstNumPEAST(self, ctx:minipythonParser.AstNumPEASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by minipythonParser#astStringPEAST.
    def visitAstStringPEAST(self, ctx:minipythonParser.AstStringPEASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by minipythonParser#astDesignatorPEAST.
    def visitAstDesignatorPEAST(self, ctx:minipythonParser.AstDesignatorPEASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by minipythonParser#astBlockPEAST.
    def visitAstBlockPEAST(self, ctx:minipythonParser.AstBlockPEASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by minipythonParser#astListPEAST.
    def visitAstListPEAST(self, ctx:minipythonParser.AstListPEASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by minipythonParser#astLenPEAST.
    def visitAstLenPEAST(self, ctx:minipythonParser.AstLenPEASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by minipythonParser#astDesignatorAST.
    def visitAstDesignatorAST(self, ctx:minipythonParser.AstDesignatorASTContext):
        return self.visitChildren(ctx)



del minipythonParser