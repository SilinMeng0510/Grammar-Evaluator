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
        4,1,16,71,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,1,0,5,0,18,8,0,10,0,12,0,21,9,0,1,0,1,0,1,1,1,1,1,1,3,
        1,28,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,
        1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,6,
        1,6,1,6,1,6,3,6,63,8,6,1,7,1,7,1,7,1,7,3,7,69,8,7,1,7,0,0,8,0,2,
        4,6,8,10,12,14,0,0,67,0,19,1,0,0,0,2,27,1,0,0,0,4,29,1,0,0,0,6,38,
        1,0,0,0,8,45,1,0,0,0,10,56,1,0,0,0,12,62,1,0,0,0,14,68,1,0,0,0,16,
        18,3,2,1,0,17,16,1,0,0,0,18,21,1,0,0,0,19,17,1,0,0,0,19,20,1,0,0,
        0,20,22,1,0,0,0,21,19,1,0,0,0,22,23,5,0,0,1,23,1,1,0,0,0,24,28,3,
        4,2,0,25,28,3,8,4,0,26,28,3,6,3,0,27,24,1,0,0,0,27,25,1,0,0,0,27,
        26,1,0,0,0,28,3,1,0,0,0,29,30,5,1,0,0,30,31,5,2,0,0,31,32,5,13,0,
        0,32,33,5,3,0,0,33,34,3,12,6,0,34,35,5,4,0,0,35,36,3,14,7,0,36,37,
        5,5,0,0,37,5,1,0,0,0,38,39,5,6,0,0,39,40,3,12,6,0,40,41,5,4,0,0,
        41,42,3,14,7,0,42,43,5,7,0,0,43,44,5,13,0,0,44,7,1,0,0,0,45,46,5,
        8,0,0,46,47,5,9,0,0,47,48,5,13,0,0,48,49,5,3,0,0,49,50,3,12,6,0,
        50,51,5,4,0,0,51,52,3,14,7,0,52,53,5,4,0,0,53,54,3,10,5,0,54,55,
        5,5,0,0,55,9,1,0,0,0,56,57,5,14,0,0,57,11,1,0,0,0,58,59,5,12,0,0,
        59,60,5,10,0,0,60,63,5,12,0,0,61,63,5,12,0,0,62,58,1,0,0,0,62,61,
        1,0,0,0,63,13,1,0,0,0,64,65,5,11,0,0,65,66,5,10,0,0,66,69,5,11,0,
        0,67,69,5,11,0,0,68,64,1,0,0,0,68,67,1,0,0,0,69,15,1,0,0,0,4,19,
        27,62,68
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
    RULE_colum_var = 5
    RULE_colum_index = 6
    RULE_row_index = 7

    ruleNames =  [ "prog", "expr", "create_stmt", "select_stmt", "insert_stmt", 
                   "colum_var", "colum_index", "row_index" ]

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
            self.state = 19
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la) & ~0x3f) == 0 and ((1 << _la) & 322) != 0:
                self.state = 16
                self.expr()
                self.state = 21
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 22
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
            self.state = 27
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 24
                self.create_stmt()
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 2)
                self.state = 25
                self.insert_stmt()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 3)
                self.state = 26
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
            self.state = 29
            self.match(ExprParser.T__0)
            self.state = 30
            self.match(ExprParser.T__1)
            self.state = 31
            self.match(ExprParser.ID)
            self.state = 32
            self.match(ExprParser.T__2)
            self.state = 33
            self.colum_index()
            self.state = 34
            self.match(ExprParser.T__3)
            self.state = 35
            self.row_index()
            self.state = 36
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
            self.state = 38
            self.match(ExprParser.T__5)
            self.state = 39
            self.colum_index()
            self.state = 40
            self.match(ExprParser.T__3)
            self.state = 41
            self.row_index()
            self.state = 42
            self.match(ExprParser.T__6)
            self.state = 43
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


        def colum_var(self):
            return self.getTypedRuleContext(ExprParser.Colum_varContext,0)


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
            self.state = 45
            self.match(ExprParser.T__7)
            self.state = 46
            self.match(ExprParser.T__8)
            self.state = 47
            self.match(ExprParser.ID)
            self.state = 48
            self.match(ExprParser.T__2)
            self.state = 49
            self.colum_index()
            self.state = 50
            self.match(ExprParser.T__3)
            self.state = 51
            self.row_index()
            self.state = 52
            self.match(ExprParser.T__3)
            self.state = 53
            self.colum_var()
            self.state = 54
            self.match(ExprParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Colum_varContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(ExprParser.STRING, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_colum_var

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterColum_var" ):
                listener.enterColum_var(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitColum_var" ):
                listener.exitColum_var(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitColum_var" ):
                return visitor.visitColum_var(self)
            else:
                return visitor.visitChildren(self)




    def colum_var(self):

        localctx = ExprParser.Colum_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_colum_var)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self.match(ExprParser.STRING)
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
        self.enterRule(localctx, 12, self.RULE_colum_index)
        try:
            self.state = 62
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 58
                self.match(ExprParser.COL)
                self.state = 59
                self.match(ExprParser.T__9)
                self.state = 60
                self.match(ExprParser.COL)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 61
                self.match(ExprParser.COL)
                pass


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
        self.enterRule(localctx, 14, self.RULE_row_index)
        try:
            self.state = 68
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 64
                self.match(ExprParser.ROW)
                self.state = 65
                self.match(ExprParser.T__9)
                self.state = 66
                self.match(ExprParser.ROW)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 67
                self.match(ExprParser.ROW)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





