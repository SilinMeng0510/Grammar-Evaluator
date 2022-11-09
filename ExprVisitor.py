# Generated from Expr.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ExprParser import ExprParser
else:
    from ExprParser import ExprParser

# This class defines a complete generic visitor for a parse tree produced by ExprParser.

class ExprVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ExprParser#prog.
    def visitProg(self, ctx:ExprParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#expr.
    def visitExpr(self, ctx:ExprParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#create_stmt.
    def visitCreate_stmt(self, ctx:ExprParser.Create_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#select_stmt.
    def visitSelect_stmt(self, ctx:ExprParser.Select_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#insert_stmt.
    def visitInsert_stmt(self, ctx:ExprParser.Insert_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#colum_index.
    def visitColum_index(self, ctx:ExprParser.Colum_indexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#row_index.
    def visitRow_index(self, ctx:ExprParser.Row_indexContext):
        return self.visitChildren(ctx)



del ExprParser