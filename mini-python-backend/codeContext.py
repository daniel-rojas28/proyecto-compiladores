from gen.minipythonParser import minipythonParser
from gen.minipythonVisitor import minipythonVisitor
from SymbolTable import SymbolTable


class CodeContext(minipythonVisitor):
    def __init__(self):
        self.table = SymbolTable()
        self.errors = []

    def visitAstProgram(self, ctx: minipythonParser.AstProgramContext):
        for i in range(len(ctx.statement())):
            self.visit(ctx.statement(i))
        return None

    def visitAstStatementDef(self, ctx: minipythonParser.AstStatementDefContext):
        self.visit(ctx.defStatement())
        return None

    def visitStatement(self, ctx: minipythonParser.StatementContext):
        return super().visitStatement(ctx)

    def visitAstDefStatment(self, ctx: minipythonParser.AstDefStatmentContext):
        self.table.openScope()
        self.table.insertTable(ctx.IDENTIFIER(), self.table.getLevel(), ctx, 1)
        self.visit(ctx.sequence())
        self.table.closeScope()
        return None

    def visitAstArgList(self, ctx: minipythonParser.AstArgListContext):
        return super().visitAstArgList(ctx)

    def visitAstWhileStatment(self, ctx: minipythonParser.AstWhileStatmentContext):
        self.visit(ctx.expression())
        self.visit(ctx.sequence())
        return None

    def visitAstForStatement(self, ctx: minipythonParser.AstForStatementContext):
        self.visit(ctx.expression())
        self.visit(ctx.expressionList())
        self.visit(ctx.sequence())
        return None

    def visitAstIfStatment(self, ctx: minipythonParser.AstIfStatmentContext):
        self.visit(ctx.expression())
        self.visit(ctx.sequence(0))
        self.visit(ctx.sequence(1))
        return None

    def visitAstReturnStatement(self, ctx: minipythonParser.AstReturnStatementContext):
        self.visit(ctx.expression())
        return None

    def visitAstPrintStatement(self, ctx: minipythonParser.AstPrintStatementContext):
        self.visit(ctx.expression())
        return None

    def visitAstAssignStatment(self, ctx: minipythonParser.AstAssignStatmentContext):
        self.table.insertTable(ctx.IDENTIFIER(), self.table.getLevel(), ctx, 1)
        self.visit(ctx.expression())
        return None

    def visitAstFunctionCallStatement(self, ctx: minipythonParser.AstFunctionCallStatementContext):
        item = self.table.search(ctx.IDENTIFIER())
        if item is None:
            self.errors.append("ERROR CONTEXTO - No existe el método " + str(ctx.IDENTIFIER()))
        else:
            self.visit(ctx.expressionList())
        return None

    def visitAstExpressionStatement(self, ctx: minipythonParser.AstExpressionStatementContext):
        self.visit(ctx.expressionList())
        return None

    def visitAstSequence(self, ctx: minipythonParser.AstSequenceContext):
        self.visit(ctx.moreStatements())
        return None

    def visitAstMoreStatements(self, ctx: minipythonParser.AstMoreStatementsContext):
        for i in range(len(ctx.statement())):
            self.visit(ctx.statement(i))
        return None

    def visitAstExpression(self, ctx: minipythonParser.AstExpressionContext):
        self.visit(ctx.additionExpression())
        self.visit(ctx.comparison())
        return None

    def visitAstAdditionExpression(self, ctx: minipythonParser.AstAdditionExpressionContext):
        self.visit(ctx.multiplicationExpression())
        self.visit(ctx.additionFactor())
        return None

    def visitAstMultiplicationExpression(self, ctx: minipythonParser.AstMultiplicationExpressionContext):
        self.visit(ctx.elementExpression())
        self.visit(ctx.multiplicationFactor())
        return None

    def visitAstElementExpression(self, ctx: minipythonParser.AstElementExpressionContext):
        self.visit(ctx.primitiveExpression())
        self.visit(ctx.elementAccess())
        return None

    def visitAstExpressionList(self, ctx: minipythonParser.AstExpressionListContext):
        if (ctx.parentCtx.__class__.__name__ == "AstFunctionCallStatementArgsContext"):
            item = self.table.search(ctx.parentCtx.IDENTIFIER())
            argList = []
            argList.append(ctx.expression())
            if (ctx.moreExpressions(0)):
                for i in ctx.moreExpressions(0).COMMA():
                    argList.append(i)
            if (len(item.value) != len(argList)):
                self.errors.append("ERROR CONTEXTO - Se esperaban " + str(len(item.value)) +
                                   " párametros y se ingresaron " + str(len(argList)) +
                                   " en el método " + str(ctx.parentCtx.IDENTIFIER()))
        return None

    def visitAstNumPEAST(self, ctx: minipythonParser.AstNumPEASTContext):
        return super().visitAstNumPEAST(ctx)

    def visitAstStringPEAST(self, ctx: minipythonParser.AstStringPEASTContext):
        return super().visitAstStringPEAST(ctx)

    def visitAstDesignatorPEAST(self, ctx: minipythonParser.AstDesignatorPEASTContext):
        return super().visitAstDesignatorPEAST(ctx)

    def visitAstBlockPEAST(self, ctx: minipythonParser.AstBlockPEASTContext):
        return super().visitAstBlockPEAST(ctx)

    def visitAstListPEAST(self, ctx: minipythonParser.AstListPEASTContext):
        return super().visitAstListPEAST(ctx)

    def visitAstLenPEAST(self, ctx: minipythonParser.AstLenPEASTContext):
        return super().visitAstLenPEAST(ctx)

    def visitAstDesignatorAST(self, ctx: minipythonParser.AstDesignatorASTContext):
        return super().visitAstDesignatorAST(ctx)

