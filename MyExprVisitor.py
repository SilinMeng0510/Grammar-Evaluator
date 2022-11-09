from ExprParser import ExprParser
from ExprVisitor import ExprVisitor
import pandas as pd

class MyExprVisitor(ExprVisitor):
    def __init__(self):
        self.tables = []
        self.data = {}
        self.ctx = {'Create' : None , 'Insert' : None , 'Select' : None}
        self.stack = []
        self.val = None

    # Visit a parse tree produced by ExprParser#prog.
    def visitProg(self, ctx: ExprParser.ProgContext):
        return self.visitChildren(ctx)  # Just visit the self expression

    # Visit a parse tree produced by ExprParser#create_stmt.
    def visitCreate_stmt(self, ctx: ExprParser.Create_stmtContext):
        table_id = str(ctx.ID())
        if table_id in self.tables:
            raise ValueError(f"error: table {ctx.ID()} is already created")
        else:
            self.tables.append(table_id)
            self.data[table_id] = []
            self.ctx['Create'] = ctx
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ExprParser#select_stmt.
    def visitSelect_stmt(self, ctx: ExprParser.Select_stmtContext):
        table_id = str(ctx.ID())
        if table_id not in self.tables:
            raise ValueError(f"error: table {ctx.ID()} is not created")
        else:
            self.ctx['Select'] = ctx
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ExprParser#insert_stmt.
    def visitInsert_stmt(self, ctx: ExprParser.Insert_stmtContext):
        table_id = str(ctx.ID())
        if table_id not in self.tables:
            raise ValueError(f"error: table {ctx.ID()} is not created")
        else:
            self.val = str(ctx.STRING())
            self.ctx['Insert'] = ctx
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ExprParser#colum_index.
    def visitColum_index(self, ctx: ExprParser.Colum_indexContext):
        start = str(ctx.COL()[0])
        end = str(ctx.COL()[1])

        if ctx.parentCtx == self.ctx['Create']:
            col_arr = []
            for column in range(ord(start), ord(end) + 1):
                col_arr.append(chr(column))
            self.stack.append(col_arr)
        elif ctx.parentCtx == self.ctx['Select']:
            col_arr = []
            for column in range(ord(start), ord(end) + 1):
                col_arr.append(chr(column))
            self.stack.append(col_arr)
        elif ctx.parentCtx == self.ctx['Insert']:
            col_arr = []
            for column in range(ord(start), ord(end) + 1):
                col_arr.append(chr(column))
            self.stack.append(col_arr)

        return self.visitChildren(ctx)

    # Visit a parse tree produced by ExprParser#row_index.
    def visitRow_index(self, ctx: ExprParser.Row_indexContext):
        start = str(ctx.ROW()[0])
        end = str(ctx.ROW()[1])

        if ctx.parentCtx == self.ctx['Create']:
            col_arr = self.stack.pop()
            row_arr = []
            for row in range(ord(start), ord(end) + 1):
                row_arr.append(chr(row))
            self.data[str(ctx.parentCtx.ID())] = pd.DataFrame(None, col_arr, row_arr)
        elif ctx.parentCtx == self.ctx['Select']:
            col_arr = self.stack.pop()
            row_arr = []
            for row in range(ord(start), ord(end) + 1):
                row_arr.append(chr(row))
            df = self.data[str(ctx.parentCtx.ID())]
            print(df.loc[col_arr,row_arr])
        elif ctx.parentCtx == self.ctx['Insert']:
            col_arr = self.stack.pop()
            row_arr = []
            for row in range(ord(start), ord(end) + 1):
                row_arr.append(chr(row))
            df = self.data[str(ctx.parentCtx.ID())]
            df.loc[col_arr, row_arr] = self.val


        return self.visitChildren(ctx)