# Generated from Expr.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ExprParser import ExprParser
else:
    from ExprParser import ExprParser

# This class defines a complete listener for a parse tree produced by ExprParser.
class ExprListener(ParseTreeListener):

    # Enter a parse tree produced by ExprParser#prog.
    def enterProg(self, ctx:ExprParser.ProgContext):
        pass

    # Exit a parse tree produced by ExprParser#prog.
    def exitProg(self, ctx:ExprParser.ProgContext):
        pass


    # Enter a parse tree produced by ExprParser#expr.
    def enterExpr(self, ctx:ExprParser.ExprContext):
        pass

    # Exit a parse tree produced by ExprParser#expr.
    def exitExpr(self, ctx:ExprParser.ExprContext):
        pass


    # Enter a parse tree produced by ExprParser#create_stmt.
    def enterCreate_stmt(self, ctx:ExprParser.Create_stmtContext):
        pass

    # Exit a parse tree produced by ExprParser#create_stmt.
    def exitCreate_stmt(self, ctx:ExprParser.Create_stmtContext):
        pass


    # Enter a parse tree produced by ExprParser#select_stmt.
    def enterSelect_stmt(self, ctx:ExprParser.Select_stmtContext):
        pass

    # Exit a parse tree produced by ExprParser#select_stmt.
    def exitSelect_stmt(self, ctx:ExprParser.Select_stmtContext):
        pass


    # Enter a parse tree produced by ExprParser#insert_stmt.
    def enterInsert_stmt(self, ctx:ExprParser.Insert_stmtContext):
        pass

    # Exit a parse tree produced by ExprParser#insert_stmt.
    def exitInsert_stmt(self, ctx:ExprParser.Insert_stmtContext):
        pass


    # Enter a parse tree produced by ExprParser#colum_var.
    def enterColum_var(self, ctx:ExprParser.Colum_varContext):
        pass

    # Exit a parse tree produced by ExprParser#colum_var.
    def exitColum_var(self, ctx:ExprParser.Colum_varContext):
        pass


    # Enter a parse tree produced by ExprParser#colum_index.
    def enterColum_index(self, ctx:ExprParser.Colum_indexContext):
        pass

    # Exit a parse tree produced by ExprParser#colum_index.
    def exitColum_index(self, ctx:ExprParser.Colum_indexContext):
        pass


    # Enter a parse tree produced by ExprParser#row_index.
    def enterRow_index(self, ctx:ExprParser.Row_indexContext):
        pass

    # Exit a parse tree produced by ExprParser#row_index.
    def exitRow_index(self, ctx:ExprParser.Row_indexContext):
        pass



del ExprParser