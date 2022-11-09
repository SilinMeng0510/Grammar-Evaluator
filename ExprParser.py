# Generated from Expr.g4 by ANTLR 4.11.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,16,63,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,1,0,5,0,16,8,0,10,0,12,0,19,9,0,1,0,1,0,1,1,1,1,1,1,3,1,26,8,1,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,
        1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,6,
        1,6,1,6,1,6,1,6,0,0,7,0,2,4,6,8,10,12,0,0,58,0,17,1,0,0,0,2,25,1,
        0,0,0,4,27,1,0,0,0,6,36,1,0,0,0,8,43,1,0,0,0,10,54,1,0,0,0,12,58,
        1,0,0,0,14,16,3,2,1,0,15,14,1,0,0,0,16,19,1,0,0,0,17,15,1,0,0,0,
        17,18,1,0,0,0,18,20,1,0,0,0,19,17,1,0,0,0,20,21,5,0,0,1,21,1,1,0,
        0,0,22,26,3,4,2,0,23,26,3,8,4,0,24,26,3,6,3,0,25,22,1,0,0,0,25,23,
        1,0,0,0,25,24,1,0,0,0,26,3,1,0,0,0,27,28,5,1,0,0,28,29,5,2,0,0,29,
        30,5,13,0,0,30,31,5,3,0,0,31,32,3,10,5,0,32,33,5,4,0,0,33,34,3,12,
        6,0,34,35,5,5,0,0,35,5,1,0,0,0,36,37,5,6,0,0,37,38,3,10,5,0,38,39,
        5,4,0,0,39,40,3,12,6,0,40,41,5,7,0,0,41,42,5,13,0,0,42,7,1,0,0,0,
        43,44,5,8,0,0,44,45,5,9,0,0,45,46,5,13,0,0,46,47,5,3,0,0,47,48,3,
        10,5,0,48,49,5,4,0,0,49,50,3,12,6,0,50,51,5,4,0,0,51,52,5,14,0,0,
        52,53,5,5,0,0,53,9,1,0,0,0,54,55,5,12,0,0,55,56,5,10,0,0,56,57,5,
        12,0,0,57,11,1,0,0,0,58,59,5,11,0,0,59,60,5,10,0,0,60,61,5,11,0,
        0,61,13,1,0,0,0,2,17,25
    ]

class ExprParser ( Parser ):

    grammarFileName = "Expr.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'CREATE'", "'table'", "'('", "','", "')'", 
                     "'SELECT'", "'FROM'", "'INSERT'", "'INTO'", "':'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "ROW", "COL", 
                      "ID", "STRING", "WS", "NEWLINE" ]

    RULE_prog = 0
    RULE_expr = 1
    RULE_create_stmt = 2
    RULE_select_stmt = 3
    RULE_insert_stmt = 4
    RULE_colum_index = 5
    RULE_row_index = 6

    ruleNames =  [ "prog", "expr", "create_stmt", "select_stmt", "insert_stmt", 
                   "colum_index", "row_index" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    ROW=11
    COL=12
    ID=13
    STRING=14
    WS=15
    NEWLINE=16

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(ExprParser.EOF, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)


        def getRuleIndex(self):
            return ExprParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = ExprParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 17
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la) & ~0x3f) == 0 and ((1 << _la) & 322) != 0:
                self.state = 14
                self.expr()
                self.state = 19
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 20
            self.match(ExprParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def create_stmt(self):
            return self.getTypedRuleContext(ExprParser.Create_stmtContext,0)


        def insert_stmt(self):
            return self.getTypedRuleContext(ExprParser.Insert_stmtContext,0)


        def select_stmt(self):
            return self.getTypedRuleContext(ExprParser.Select_stmtContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = ExprParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_expr)
        try:
            self.state = 25
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 22
                self.create_stmt()
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 2)
                self.state = 23
                self.insert_stmt()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 3)
                self.state = 24
                self.select_stmt()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Create_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ExprParser.ID, 0)

        def colum_index(self):
            return self.getTypedRuleContext(ExprParser.Colum_indexContext,0)


        def row_index(self):
            return self.getTypedRuleContext(ExprParser.Row_indexContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_create_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCreate_stmt" ):
                listener.enterCreate_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCreate_stmt" ):
                listener.exitCreate_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCreate_stmt" ):
                return visitor.visitCreate_stmt(self)
            else:
                return visitor.visitChildren(self)




    def create_stmt(self):

        localctx = ExprParser.Create_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_create_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27
            self.match(ExprParser.T__0)
            self.state = 28
            self.match(ExprParser.T__1)
            self.state = 29
            self.match(ExprParser.ID)
            self.state = 30
            self.match(ExprParser.T__2)
            self.state = 31
            self.colum_index()
            self.state = 32
            self.match(ExprParser.T__3)
            self.state = 33
            self.row_index()
            self.state = 34
            self.match(ExprParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Select_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def colum_index(self):
            return self.getTypedRuleContext(ExprParser.Colum_indexContext,0)


        def row_index(self):
            return self.getTypedRuleContext(ExprParser.Row_indexContext,0)


        def ID(self):
            return self.getToken(ExprParser.ID, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_select_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSelect_stmt" ):
                listener.enterSelect_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSelect_stmt" ):
                listener.exitSelect_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSelect_stmt" ):
                return visitor.visitSelect_stmt(self)
            else:
                return visitor.visitChildren(self)




    def select_stmt(self):

        localctx = ExprParser.Select_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_select_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            self.match(ExprParser.T__5)
            self.state = 37
            self.colum_index()
            self.state = 38
            self.match(ExprParser.T__3)
            self.state = 39
            self.row_index()
            self.state = 40
            self.match(ExprParser.T__6)
            self.state = 41
            self.match(ExprParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Insert_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ExprParser.ID, 0)

        def colum_index(self):
            return self.getTypedRuleContext(ExprParser.Colum_indexContext,0)


        def row_index(self):
            return self.getTypedRuleContext(ExprParser.Row_indexContext,0)


        def STRING(self):
            return self.getToken(ExprParser.STRING, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_insert_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInsert_stmt" ):
                listener.enterInsert_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInsert_stmt" ):
                listener.exitInsert_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInsert_stmt" ):
                return visitor.visitInsert_stmt(self)
            else:
                return visitor.visitChildren(self)




    def insert_stmt(self):

        localctx = ExprParser.Insert_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_insert_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self.match(ExprParser.T__7)
            self.state = 44
            self.match(ExprParser.T__8)
            self.state = 45
            self.match(ExprParser.ID)
            self.state = 46
            self.match(ExprParser.T__2)
            self.state = 47
            self.colum_index()
            self.state = 48
            self.match(ExprParser.T__3)
            self.state = 49
            self.row_index()
            self.state = 50
            self.match(ExprParser.T__3)
            self.state = 51
            self.match(ExprParser.STRING)
            self.state = 52
            self.match(ExprParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Colum_indexContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COL(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.COL)
            else:
                return self.getToken(ExprParser.COL, i)

        def getRuleIndex(self):
            return ExprParser.RULE_colum_index

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterColum_index" ):
                listener.enterColum_index(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitColum_index" ):
                listener.exitColum_index(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitColum_index" ):
                return visitor.visitColum_index(self)
            else:
                return visitor.visitChildren(self)




    def colum_index(self):

        localctx = ExprParser.Colum_indexContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_colum_index)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            self.match(ExprParser.COL)
            self.state = 55
            self.match(ExprParser.T__9)
            self.state = 56
            self.match(ExprParser.COL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Row_indexContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ROW(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.ROW)
            else:
                return self.getToken(ExprParser.ROW, i)

        def getRuleIndex(self):
            return ExprParser.RULE_row_index

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRow_index" ):
                listener.enterRow_index(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRow_index" ):
                listener.exitRow_index(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRow_index" ):
                return visitor.visitRow_index(self)
            else:
                return visitor.visitChildren(self)




    def row_index(self):

        localctx = ExprParser.Row_indexContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_row_index)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self.match(ExprParser.ROW)
            self.state = 59
            self.match(ExprParser.T__9)
            self.state = 60
            self.match(ExprParser.ROW)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





