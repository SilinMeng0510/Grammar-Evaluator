from ExprParser import ExprParser
from ExprVisitor import ExprVisitor

class MyExprVisitor(ExprVisitor):
    def __init__(self):
        super(MyExprVisitor, self).__init__()
        self.stack = []  # Stack to evaluate the expression
        self.variables = {}  # Dictionary to keep track of the variables

    # Visit a parse tree produced by ExprParser#prog.
    def visitProg(self, ctx: ExprParser.ProgContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ExprParser#expr.
    def visitExpr(self, ctx: ExprParser.ExprContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ExprParser#create_stmt.
    def visitCreate_stmt(self, ctx: ExprParser.Create_stmtContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ExprParser#select_stmt.
    def visitSelect_stmt(self, ctx: ExprParser.Select_stmtContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ExprParser#insert_stmt.
    def visitInsert_stmt(self, ctx: ExprParser.Insert_stmtContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ExprParser#colum_var.
    def visitColum_var(self, ctx: ExprParser.Colum_varContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ExprParser#colum_index.
    def visitColum_index(self, ctx: ExprParser.Colum_indexContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ExprParser#row_index.
    def visitRow_index(self, ctx: ExprParser.Row_indexContext):
        return self.visitChildren(ctx)