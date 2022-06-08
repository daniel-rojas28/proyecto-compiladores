# Generated from C:/Users/geral/Desktop/proyecto-compiladores/mini-python-backend\minipython.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .minipythonParser import minipythonParser
else:
    from minipythonParser import minipythonParser

# This class defines a complete listener for a parse tree produced by minipythonParser.
class minipythonListener(ParseTreeListener):

    # Enter a parse tree produced by minipythonParser#astProgram.
    def enterAstProgram(self, ctx:minipythonParser.AstProgramContext):
        pass

    # Exit a parse tree produced by minipythonParser#astProgram.
    def exitAstProgram(self, ctx:minipythonParser.AstProgramContext):
        pass


    # Enter a parse tree produced by minipythonParser#astStatementDef.
    def enterAstStatementDef(self, ctx:minipythonParser.AstStatementDefContext):
        pass

    # Exit a parse tree produced by minipythonParser#astStatementDef.
    def exitAstStatementDef(self, ctx:minipythonParser.AstStatementDefContext):
        pass


    # Enter a parse tree produced by minipythonParser#statement.
    def enterStatement(self, ctx:minipythonParser.StatementContext):
        pass

    # Exit a parse tree produced by minipythonParser#statement.
    def exitStatement(self, ctx:minipythonParser.StatementContext):
        pass


    # Enter a parse tree produced by minipythonParser#astDefStatment.
    def enterAstDefStatment(self, ctx:minipythonParser.AstDefStatmentContext):
        pass

    # Exit a parse tree produced by minipythonParser#astDefStatment.
    def exitAstDefStatment(self, ctx:minipythonParser.AstDefStatmentContext):
        pass


    # Enter a parse tree produced by minipythonParser#astArgList.
    def enterAstArgList(self, ctx:minipythonParser.AstArgListContext):
        pass

    # Exit a parse tree produced by minipythonParser#astArgList.
    def exitAstArgList(self, ctx:minipythonParser.AstArgListContext):
        pass


    # Enter a parse tree produced by minipythonParser#astWhileStatment.
    def enterAstWhileStatment(self, ctx:minipythonParser.AstWhileStatmentContext):
        pass

    # Exit a parse tree produced by minipythonParser#astWhileStatment.
    def exitAstWhileStatment(self, ctx:minipythonParser.AstWhileStatmentContext):
        pass


    # Enter a parse tree produced by minipythonParser#astForStatement.
    def enterAstForStatement(self, ctx:minipythonParser.AstForStatementContext):
        pass

    # Exit a parse tree produced by minipythonParser#astForStatement.
    def exitAstForStatement(self, ctx:minipythonParser.AstForStatementContext):
        pass


    # Enter a parse tree produced by minipythonParser#astIfStatment.
    def enterAstIfStatment(self, ctx:minipythonParser.AstIfStatmentContext):
        pass

    # Exit a parse tree produced by minipythonParser#astIfStatment.
    def exitAstIfStatment(self, ctx:minipythonParser.AstIfStatmentContext):
        pass


    # Enter a parse tree produced by minipythonParser#astReturnStatement.
    def enterAstReturnStatement(self, ctx:minipythonParser.AstReturnStatementContext):
        pass

    # Exit a parse tree produced by minipythonParser#astReturnStatement.
    def exitAstReturnStatement(self, ctx:minipythonParser.AstReturnStatementContext):
        pass


    # Enter a parse tree produced by minipythonParser#astPrintStatement.
    def enterAstPrintStatement(self, ctx:minipythonParser.AstPrintStatementContext):
        pass

    # Exit a parse tree produced by minipythonParser#astPrintStatement.
    def exitAstPrintStatement(self, ctx:minipythonParser.AstPrintStatementContext):
        pass


    # Enter a parse tree produced by minipythonParser#astAssignStatment.
    def enterAstAssignStatment(self, ctx:minipythonParser.AstAssignStatmentContext):
        pass

    # Exit a parse tree produced by minipythonParser#astAssignStatment.
    def exitAstAssignStatment(self, ctx:minipythonParser.AstAssignStatmentContext):
        pass


    # Enter a parse tree produced by minipythonParser#astFunctionCallStatement.
    def enterAstFunctionCallStatement(self, ctx:minipythonParser.AstFunctionCallStatementContext):
        pass

    # Exit a parse tree produced by minipythonParser#astFunctionCallStatement.
    def exitAstFunctionCallStatement(self, ctx:minipythonParser.AstFunctionCallStatementContext):
        pass


    # Enter a parse tree produced by minipythonParser#astExpressionStatement.
    def enterAstExpressionStatement(self, ctx:minipythonParser.AstExpressionStatementContext):
        pass

    # Exit a parse tree produced by minipythonParser#astExpressionStatement.
    def exitAstExpressionStatement(self, ctx:minipythonParser.AstExpressionStatementContext):
        pass


    # Enter a parse tree produced by minipythonParser#astSequence.
    def enterAstSequence(self, ctx:minipythonParser.AstSequenceContext):
        pass

    # Exit a parse tree produced by minipythonParser#astSequence.
    def exitAstSequence(self, ctx:minipythonParser.AstSequenceContext):
        pass


    # Enter a parse tree produced by minipythonParser#astMoreStatements.
    def enterAstMoreStatements(self, ctx:minipythonParser.AstMoreStatementsContext):
        pass

    # Exit a parse tree produced by minipythonParser#astMoreStatements.
    def exitAstMoreStatements(self, ctx:minipythonParser.AstMoreStatementsContext):
        pass


    # Enter a parse tree produced by minipythonParser#astExpression.
    def enterAstExpression(self, ctx:minipythonParser.AstExpressionContext):
        pass

    # Exit a parse tree produced by minipythonParser#astExpression.
    def exitAstExpression(self, ctx:minipythonParser.AstExpressionContext):
        pass


    # Enter a parse tree produced by minipythonParser#astAdditionExpression.
    def enterAstAdditionExpression(self, ctx:minipythonParser.AstAdditionExpressionContext):
        pass

    # Exit a parse tree produced by minipythonParser#astAdditionExpression.
    def exitAstAdditionExpression(self, ctx:minipythonParser.AstAdditionExpressionContext):
        pass


    # Enter a parse tree produced by minipythonParser#astMultiplicationExpression.
    def enterAstMultiplicationExpression(self, ctx:minipythonParser.AstMultiplicationExpressionContext):
        pass

    # Exit a parse tree produced by minipythonParser#astMultiplicationExpression.
    def exitAstMultiplicationExpression(self, ctx:minipythonParser.AstMultiplicationExpressionContext):
        pass


    # Enter a parse tree produced by minipythonParser#astElementExpression.
    def enterAstElementExpression(self, ctx:minipythonParser.AstElementExpressionContext):
        pass

    # Exit a parse tree produced by minipythonParser#astElementExpression.
    def exitAstElementExpression(self, ctx:minipythonParser.AstElementExpressionContext):
        pass


    # Enter a parse tree produced by minipythonParser#astExpressionList.
    def enterAstExpressionList(self, ctx:minipythonParser.AstExpressionListContext):
        pass

    # Exit a parse tree produced by minipythonParser#astExpressionList.
    def exitAstExpressionList(self, ctx:minipythonParser.AstExpressionListContext):
        pass


    # Enter a parse tree produced by minipythonParser#astNumPEAST.
    def enterAstNumPEAST(self, ctx:minipythonParser.AstNumPEASTContext):
        pass

    # Exit a parse tree produced by minipythonParser#astNumPEAST.
    def exitAstNumPEAST(self, ctx:minipythonParser.AstNumPEASTContext):
        pass


    # Enter a parse tree produced by minipythonParser#astStringPEAST.
    def enterAstStringPEAST(self, ctx:minipythonParser.AstStringPEASTContext):
        pass

    # Exit a parse tree produced by minipythonParser#astStringPEAST.
    def exitAstStringPEAST(self, ctx:minipythonParser.AstStringPEASTContext):
        pass


    # Enter a parse tree produced by minipythonParser#astDesignatorPEAST.
    def enterAstDesignatorPEAST(self, ctx:minipythonParser.AstDesignatorPEASTContext):
        pass

    # Exit a parse tree produced by minipythonParser#astDesignatorPEAST.
    def exitAstDesignatorPEAST(self, ctx:minipythonParser.AstDesignatorPEASTContext):
        pass


    # Enter a parse tree produced by minipythonParser#astBlockPEAST.
    def enterAstBlockPEAST(self, ctx:minipythonParser.AstBlockPEASTContext):
        pass

    # Exit a parse tree produced by minipythonParser#astBlockPEAST.
    def exitAstBlockPEAST(self, ctx:minipythonParser.AstBlockPEASTContext):
        pass


    # Enter a parse tree produced by minipythonParser#astListPEAST.
    def enterAstListPEAST(self, ctx:minipythonParser.AstListPEASTContext):
        pass

    # Exit a parse tree produced by minipythonParser#astListPEAST.
    def exitAstListPEAST(self, ctx:minipythonParser.AstListPEASTContext):
        pass


    # Enter a parse tree produced by minipythonParser#astLenPEAST.
    def enterAstLenPEAST(self, ctx:minipythonParser.AstLenPEASTContext):
        pass

    # Exit a parse tree produced by minipythonParser#astLenPEAST.
    def exitAstLenPEAST(self, ctx:minipythonParser.AstLenPEASTContext):
        pass


    # Enter a parse tree produced by minipythonParser#astDesignatorAST.
    def enterAstDesignatorAST(self, ctx:minipythonParser.AstDesignatorASTContext):
        pass

    # Exit a parse tree produced by minipythonParser#astDesignatorAST.
    def exitAstDesignatorAST(self, ctx:minipythonParser.AstDesignatorASTContext):
        pass



del minipythonParser