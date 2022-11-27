from ExprParser import ExprParser
from ExprVisitor import ExprVisitor
import pandas as pd


class MyExprVisitor(ExprVisitor):
    def __init__(self):
        self.tables = []
        self.data = {}
        self.ctx = {'Create': None, 'Insert': None, 'Select': None, 'Delete': None}
        self.stack = []
        self.val = None
        self.desc = False
        self.registered_colum = []
        self.registered_row = []

    # Visit a parse tree produced by ExprParser#prog.
    def visitProg(self, ctx: ExprParser.ProgContext):
        return self.visitChildren(ctx)  # Just visit the self expression

    # Visit a parse tree produced by ExprParser#create_stmt.
    def visitCreate_stmt(self, ctx: ExprParser.Create_stmtContext):
        #import pdb;pdb.set_trace()
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
            #import pdb;pdb.set_trace()
            if len(ctx.COL()) > 0:
                if str(ctx.BOOL(0)) == 't':
                    self.val = str(ctx.COL(0))
                    self.desc = True
                elif str(ctx.BOOL(0)) == 'f':
                    self.val = str(ctx.COL(0))
            else:
                self.val = None
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

    # Visit a parse tree produced by ExprParser#delete_stmt.
    def visitDelete_stmt(self, ctx: ExprParser.Delete_stmtContext):
        table_id = str(ctx.ID())
        if table_id not in self.tables:
            raise ValueError(f"error: table {ctx.ID()} is not existed")
        else:
            self.tables.remove(table_id)
            df = self.data[table_id]
            del self.data[table_id]
            for column in list(df.columns):
                self.registered_colum.remove(column)
            for row in list(df.index):
                self.registered_row.remove(row)
        return self.visitChildren(ctx)

    def visitDelete_data_stmt(self, ctx: ExprParser.Delete_stmtContext):
        table_id = str(ctx.ID())
        if table_id not in self.tables:
            raise ValueError(f"error: table {ctx.ID()} is not created")
        else:
            self.val = None
            self.ctx['Delete'] = ctx
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ExprParser#colum_index.
    def visitColum_index(self, ctx: ExprParser.Colum_indexContext):
        start = str(ctx.COL()[0])
        end = str(ctx.COL()[1])
        if ord(start) > ord(end):
            raise ValueError(f"error: {start} is bigger than {end}, invalid sequence in column")

        if ctx.parentCtx == self.ctx['Create']:
            col_arr = []
            for column in range(ord(start), ord(end) + 1):
                if chr(column) in self.registered_colum:
                    raise ValueError(f"error: column {chr(column)} is registered")
                else:
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
        elif ctx.parentCtx == self.ctx['Delete']:
            col_arr = []
            for column in range(ord(start), ord(end) + 1):
                col_arr.append(chr(column))
            self.stack.append(col_arr)
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ExprParser#row_index.
    def visitRow_index(self, ctx: ExprParser.Row_indexContext):
        start = str(ctx.ROW()[0])
        end = str(ctx.ROW()[1])
        if ord(start) > ord(end):
            raise ValueError(f"error: {start} is bigger than {end}, invalid sequence in row")

        if ctx.parentCtx == self.ctx['Create']:
            col_arr = self.stack.pop()
            row_arr = []
            for row in range(ord(start), ord(end) + 1):
                if chr(row) in self.registered_row:
                    raise ValueError(f"error: row {chr(row)} is registered")
                else:
                    row_arr.append(chr(row))
            self.data[str(ctx.parentCtx.ID())] = pd.DataFrame(None, row_arr, col_arr)
            self.registered_colum.extend(col_arr)
            self.registered_row.extend(row_arr)
        elif ctx.parentCtx == self.ctx['Select']:
            col_arr = self.stack.pop()
            row_arr = []
            for row in range(ord(start), ord(end) + 1):
                row_arr.append(chr(row))
            df = self.data[str(ctx.parentCtx.ID())]
            #import pdb;pdb.set_trace()
            if self.val is not None:
                if self.desc:
                    print(df.loc[row_arr, col_arr].sort_values(by=self.val, ascending=False))
                    self.desc = False
                elif not self.desc:
                    print(df.loc[row_arr, col_arr].sort_values(by=self.val))
            else:
                print(df.loc[row_arr, col_arr])
        elif ctx.parentCtx == self.ctx['Insert']:
            col_arr = self.stack.pop()
            row_arr = []
            for row in range(ord(start), ord(end) + 1):
                row_arr.append(chr(row))
            df = self.data[str(ctx.parentCtx.ID())]
            for column in col_arr:
                if column not in list(df.columns):
                    raise ValueError(f"error: column {column} is not included in table")
            df.loc[row_arr, col_arr] = self.val
        elif ctx.parentCtx == self.ctx['Delete']:
            col_arr = self.stack.pop()
            row_arr = []
            for row in range(ord(start), ord(end) + 1):
                row_arr.append(chr(row))
            df = self.data[str(ctx.parentCtx.ID())]
            for column in col_arr:
                if column not in list(df.columns):
                    raise ValueError(f"error: column {column} is not included in table")
            df.loc[row_arr, col_arr] = self.val
        return self.visitChildren(ctx)
