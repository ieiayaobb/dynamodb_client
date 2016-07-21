# Generated from C:/pyprojects/hackathon/src/parser\MySQLParser.g4 by ANTLR 4.5.3
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO

def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3")
        buf.write(u"Nz\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4")
        buf.write(u"\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write(u"\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t")
        buf.write(u"\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\3\2\3\2\5")
        buf.write(u"\2\61\n\2\3\3\3\3\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\5\5")
        buf.write(u"=\n\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\t\5\tH\n\t\3")
        buf.write(u"\n\3\n\3\13\3\13\3\13\6\13O\n\13\r\13\16\13P\3\f\3\f")
        buf.write(u"\3\r\3\r\5\rW\n\r\3\16\3\16\3\16\3\16\3\16\3\17\3\17")
        buf.write(u"\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\21\3")
        buf.write(u"\21\3\22\3\22\3\23\3\23\3\24\3\24\3\25\3\25\3\26\3\26")
        buf.write(u"\3\27\3\27\3\27\5\27x\n\27\3\27\2\2\30\2\4\6\b\n\f\16")
        buf.write(u"\20\22\24\26\30\32\34\36 \"$&(*,\2\4\4\2+.\60\61\4\2")
        buf.write(u"\n\f//j\2\60\3\2\2\2\4\62\3\2\2\2\6\64\3\2\2\2\b\67\3")
        buf.write(u"\2\2\2\n>\3\2\2\2\f@\3\2\2\2\16B\3\2\2\2\20G\3\2\2\2")
        buf.write(u"\22I\3\2\2\2\24K\3\2\2\2\26R\3\2\2\2\30V\3\2\2\2\32X")
        buf.write(u"\3\2\2\2\34]\3\2\2\2\36f\3\2\2\2 h\3\2\2\2\"j\3\2\2\2")
        buf.write(u"$l\3\2\2\2&n\3\2\2\2(p\3\2\2\2*r\3\2\2\2,w\3\2\2\2.\61")
        buf.write(u"\5\b\5\2/\61\5\6\4\2\60.\3\2\2\2\60/\3\2\2\2\61\3\3\2")
        buf.write(u"\2\2\62\63\7J\2\2\63\5\3\2\2\2\64\65\7\5\2\2\65\66\5")
        buf.write(u"\n\6\2\66\7\3\2\2\2\678\7\3\2\289\5\20\t\29:\7\b\2\2")
        buf.write(u":<\5\n\6\2;=\5\30\r\2<;\3\2\2\2<=\3\2\2\2=\t\3\2\2\2")
        buf.write(u">?\7J\2\2?\13\3\2\2\2@A\7J\2\2A\r\3\2\2\2BC\7J\2\2C\17")
        buf.write(u"\3\2\2\2DH\5\22\n\2EH\5\24\13\2FH\5\26\f\2GD\3\2\2\2")
        buf.write(u"GE\3\2\2\2GF\3\2\2\2H\21\3\2\2\2IJ\7J\2\2J\23\3\2\2\2")
        buf.write(u"KN\7J\2\2LM\7\63\2\2MO\7J\2\2NL\3\2\2\2OP\3\2\2\2PN\3")
        buf.write(u"\2\2\2PQ\3\2\2\2Q\25\3\2\2\2RS\7$\2\2S\27\3\2\2\2TW\5")
        buf.write(u"\32\16\2UW\5\34\17\2VT\3\2\2\2VU\3\2\2\2W\31\3\2\2\2")
        buf.write(u"XY\7\t\2\2YZ\5\36\20\2Z[\5&\24\2[\\\5\"\22\2\\\33\3\2")
        buf.write(u"\2\2]^\7\t\2\2^_\5\36\20\2_`\5&\24\2`a\5\"\22\2ab\5(")
        buf.write(u"\25\2bc\5 \21\2cd\5&\24\2de\5$\23\2e\35\3\2\2\2fg\7J")
        buf.write(u"\2\2g\37\3\2\2\2hi\7J\2\2i!\3\2\2\2jk\7J\2\2k#\3\2\2")
        buf.write(u"\2lm\7J\2\2m%\3\2\2\2no\t\2\2\2o\'\3\2\2\2pq\t\3\2\2")
        buf.write(u"q)\3\2\2\2rs\7\30\2\2s+\3\2\2\2tx\7\r\2\2uv\7\r\2\2v")
        buf.write(u"x\7/\2\2wt\3\2\2\2wu\3\2\2\2x-\3\2\2\2\b\60<GPVw")
        return buf.getvalue()


class MySQLParser ( Parser ):

    grammarFileName = "MySQLParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ u"<INVALID>", u"'select'", u"'insert'", u"'desc'", 
                     u"'into'", u"'values'", u"'from'", u"'where'", u"<INVALID>", 
                     u"<INVALID>", u"'xor'", u"'is'", u"'null'", u"'like'", 
                     u"'in'", u"'exists'", u"'all'", u"'any'", u"'true'", 
                     u"'false'", u"<INVALID>", u"<INVALID>", u"'between'", 
                     u"'regexp'", u"'+'", u"'-'", u"'~'", u"'|'", u"'&'", 
                     u"'^'", u"'binary'", u"'<<'", u"'>>'", u"'escape'", 
                     u"'*'", u"')'", u"'('", u"']'", u"'['", u"':'", u"'.*'", 
                     u"'='", u"'<'", u"'>'", u"'!='", u"'not'", u"'<='", 
                     u"'>='", u"';'", u"','", u"'.'", u"'collate'", u"'inner'", 
                     u"'outer'", u"'join'", u"'cross'", u"'using'", u"'index'", 
                     u"'key'", u"'order'", u"'group'", u"'by'", u"'for'", 
                     u"'use'", u"'ignore'", u"'partition'", u"'straight_join'", 
                     u"'natural'", u"'left'", u"'right'", u"'oj'", u"'on'" ]

    symbolicNames = [ u"<INVALID>", u"SELECT", u"INSERT", u"DESC", u"INTO", 
                      u"VALUES", u"FROM", u"WHERE", u"AND", u"OR", u"XOR", 
                      u"IS", u"NULL", u"LIKE", u"IN", u"EXISTS", u"ALL", 
                      u"ANY", u"TRUE", u"FALSE", u"DIVIDE", u"MOD", u"BETWEEN", 
                      u"REGEXP", u"PLUS", u"MINUS", u"NEGATION", u"VERTBAR", 
                      u"BITAND", u"POWER_OP", u"BINARY", u"SHIFT_LEFT", 
                      u"SHIFT_RIGHT", u"ESCAPE", u"ASTERISK", u"RPAREN", 
                      u"LPAREN", u"RBRACK", u"LBRACK", u"COLON", u"ALL_FIELDS", 
                      u"EQ", u"LTH", u"GTH", u"NOT_EQ", u"NOT", u"LET", 
                      u"GET", u"SEMI", u"COMMA", u"DOT", u"COLLATE", u"INNER", 
                      u"OUTER", u"JOIN", u"CROSS", u"USING", u"INDEX", u"KEY", 
                      u"ORDER", u"GROUP", u"BY", u"FOR", u"USE", u"IGNORE", 
                      u"PARTITION", u"STRAIGHT_JOIN", u"NATURAL", u"LEFT", 
                      u"RIGHT", u"OJ", u"ON", u"ID", u"INT", u"NEWLINE", 
                      u"WS", u"USER_VAR" ]

    RULE_stat = 0
    RULE_schema_name = 1
    RULE_desc_clause = 2
    RULE_select_clause = 3
    RULE_table_name = 4
    RULE_column_name = 5
    RULE_column_name_alias = 6
    RULE_column_list_clause = 7
    RULE_single_column = 8
    RULE_multi_column = 9
    RULE_all_column = 10
    RULE_where_clause = 11
    RULE_hash_expression = 12
    RULE_hash_range_expression = 13
    RULE_hash_key = 14
    RULE_range_key = 15
    RULE_hash_value = 16
    RULE_range_value = 17
    RULE_relational_op = 18
    RULE_expr_op = 19
    RULE_between_op = 20
    RULE_is_or_is_not = 21

    ruleNames =  [ u"stat", u"schema_name", u"desc_clause", u"select_clause", 
                   u"table_name", u"column_name", u"column_name_alias", 
                   u"column_list_clause", u"single_column", u"multi_column", 
                   u"all_column", u"where_clause", u"hash_expression", u"hash_range_expression", 
                   u"hash_key", u"range_key", u"hash_value", u"range_value", 
                   u"relational_op", u"expr_op", u"between_op", u"is_or_is_not" ]

    EOF = Token.EOF
    SELECT=1
    INSERT=2
    DESC=3
    INTO=4
    VALUES=5
    FROM=6
    WHERE=7
    AND=8
    OR=9
    XOR=10
    IS=11
    NULL=12
    LIKE=13
    IN=14
    EXISTS=15
    ALL=16
    ANY=17
    TRUE=18
    FALSE=19
    DIVIDE=20
    MOD=21
    BETWEEN=22
    REGEXP=23
    PLUS=24
    MINUS=25
    NEGATION=26
    VERTBAR=27
    BITAND=28
    POWER_OP=29
    BINARY=30
    SHIFT_LEFT=31
    SHIFT_RIGHT=32
    ESCAPE=33
    ASTERISK=34
    RPAREN=35
    LPAREN=36
    RBRACK=37
    LBRACK=38
    COLON=39
    ALL_FIELDS=40
    EQ=41
    LTH=42
    GTH=43
    NOT_EQ=44
    NOT=45
    LET=46
    GET=47
    SEMI=48
    COMMA=49
    DOT=50
    COLLATE=51
    INNER=52
    OUTER=53
    JOIN=54
    CROSS=55
    USING=56
    INDEX=57
    KEY=58
    ORDER=59
    GROUP=60
    BY=61
    FOR=62
    USE=63
    IGNORE=64
    PARTITION=65
    STRAIGHT_JOIN=66
    NATURAL=67
    LEFT=68
    RIGHT=69
    OJ=70
    ON=71
    ID=72
    INT=73
    NEWLINE=74
    WS=75
    USER_VAR=76

    def __init__(self, input):
        super(MySQLParser, self).__init__(input)
        self.checkVersion("4.5.3")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class StatContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MySQLParser.StatContext, self).__init__(parent, invokingState)
            self.parser = parser

        def select_clause(self):
            return self.getTypedRuleContext(MySQLParser.Select_clauseContext,0)


        def desc_clause(self):
            return self.getTypedRuleContext(MySQLParser.Desc_clauseContext,0)


        def getRuleIndex(self):
            return MySQLParser.RULE_stat

        def enterRule(self, listener):
            if hasattr(listener, "enterStat"):
                listener.enterStat(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitStat"):
                listener.exitStat(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitStat"):
                return visitor.visitStat(self)
            else:
                return visitor.visitChildren(self)




    def stat(self):

        localctx = MySQLParser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_stat)
        try:
            self.state = 46
            token = self._input.LA(1)
            if token in [MySQLParser.SELECT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 44
                self.select_clause()

            elif token in [MySQLParser.DESC]:
                self.enterOuterAlt(localctx, 2)
                self.state = 45
                self.desc_clause()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Schema_nameContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MySQLParser.Schema_nameContext, self).__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MySQLParser.ID, 0)

        def getRuleIndex(self):
            return MySQLParser.RULE_schema_name

        def enterRule(self, listener):
            if hasattr(listener, "enterSchema_name"):
                listener.enterSchema_name(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitSchema_name"):
                listener.exitSchema_name(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitSchema_name"):
                return visitor.visitSchema_name(self)
            else:
                return visitor.visitChildren(self)




    def schema_name(self):

        localctx = MySQLParser.Schema_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_schema_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self.match(MySQLParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Desc_clauseContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MySQLParser.Desc_clauseContext, self).__init__(parent, invokingState)
            self.parser = parser

        def DESC(self):
            return self.getToken(MySQLParser.DESC, 0)

        def table_name(self):
            return self.getTypedRuleContext(MySQLParser.Table_nameContext,0)


        def getRuleIndex(self):
            return MySQLParser.RULE_desc_clause

        def enterRule(self, listener):
            if hasattr(listener, "enterDesc_clause"):
                listener.enterDesc_clause(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitDesc_clause"):
                listener.exitDesc_clause(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitDesc_clause"):
                return visitor.visitDesc_clause(self)
            else:
                return visitor.visitChildren(self)




    def desc_clause(self):

        localctx = MySQLParser.Desc_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_desc_clause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self.match(MySQLParser.DESC)
            self.state = 51
            self.table_name()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Select_clauseContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MySQLParser.Select_clauseContext, self).__init__(parent, invokingState)
            self.parser = parser

        def SELECT(self):
            return self.getToken(MySQLParser.SELECT, 0)

        def column_list_clause(self):
            return self.getTypedRuleContext(MySQLParser.Column_list_clauseContext,0)


        def FROM(self):
            return self.getToken(MySQLParser.FROM, 0)

        def table_name(self):
            return self.getTypedRuleContext(MySQLParser.Table_nameContext,0)


        def where_clause(self):
            return self.getTypedRuleContext(MySQLParser.Where_clauseContext,0)


        def getRuleIndex(self):
            return MySQLParser.RULE_select_clause

        def enterRule(self, listener):
            if hasattr(listener, "enterSelect_clause"):
                listener.enterSelect_clause(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitSelect_clause"):
                listener.exitSelect_clause(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitSelect_clause"):
                return visitor.visitSelect_clause(self)
            else:
                return visitor.visitChildren(self)




    def select_clause(self):

        localctx = MySQLParser.Select_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_select_clause)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self.match(MySQLParser.SELECT)
            self.state = 54
            self.column_list_clause()
            self.state = 55
            self.match(MySQLParser.FROM)
            self.state = 56
            self.table_name()
            self.state = 58
            _la = self._input.LA(1)
            if _la==MySQLParser.WHERE:
                self.state = 57
                self.where_clause()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Table_nameContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MySQLParser.Table_nameContext, self).__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MySQLParser.ID, 0)

        def getRuleIndex(self):
            return MySQLParser.RULE_table_name

        def enterRule(self, listener):
            if hasattr(listener, "enterTable_name"):
                listener.enterTable_name(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitTable_name"):
                listener.exitTable_name(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitTable_name"):
                return visitor.visitTable_name(self)
            else:
                return visitor.visitChildren(self)




    def table_name(self):

        localctx = MySQLParser.Table_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_table_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            self.match(MySQLParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Column_nameContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MySQLParser.Column_nameContext, self).__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MySQLParser.ID, 0)

        def getRuleIndex(self):
            return MySQLParser.RULE_column_name

        def enterRule(self, listener):
            if hasattr(listener, "enterColumn_name"):
                listener.enterColumn_name(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitColumn_name"):
                listener.exitColumn_name(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitColumn_name"):
                return visitor.visitColumn_name(self)
            else:
                return visitor.visitChildren(self)




    def column_name(self):

        localctx = MySQLParser.Column_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_column_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            self.match(MySQLParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Column_name_aliasContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MySQLParser.Column_name_aliasContext, self).__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MySQLParser.ID, 0)

        def getRuleIndex(self):
            return MySQLParser.RULE_column_name_alias

        def enterRule(self, listener):
            if hasattr(listener, "enterColumn_name_alias"):
                listener.enterColumn_name_alias(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitColumn_name_alias"):
                listener.exitColumn_name_alias(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitColumn_name_alias"):
                return visitor.visitColumn_name_alias(self)
            else:
                return visitor.visitChildren(self)




    def column_name_alias(self):

        localctx = MySQLParser.Column_name_aliasContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_column_name_alias)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self.match(MySQLParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Column_list_clauseContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MySQLParser.Column_list_clauseContext, self).__init__(parent, invokingState)
            self.parser = parser

        def single_column(self):
            return self.getTypedRuleContext(MySQLParser.Single_columnContext,0)


        def multi_column(self):
            return self.getTypedRuleContext(MySQLParser.Multi_columnContext,0)


        def all_column(self):
            return self.getTypedRuleContext(MySQLParser.All_columnContext,0)


        def getRuleIndex(self):
            return MySQLParser.RULE_column_list_clause

        def enterRule(self, listener):
            if hasattr(listener, "enterColumn_list_clause"):
                listener.enterColumn_list_clause(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitColumn_list_clause"):
                listener.exitColumn_list_clause(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitColumn_list_clause"):
                return visitor.visitColumn_list_clause(self)
            else:
                return visitor.visitChildren(self)




    def column_list_clause(self):

        localctx = MySQLParser.Column_list_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_column_list_clause)
        try:
            self.state = 69
            self._errHandler.sync(self);
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 66
                self.single_column()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 67
                self.multi_column()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 68
                self.all_column()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Single_columnContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MySQLParser.Single_columnContext, self).__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MySQLParser.ID, 0)

        def getRuleIndex(self):
            return MySQLParser.RULE_single_column

        def enterRule(self, listener):
            if hasattr(listener, "enterSingle_column"):
                listener.enterSingle_column(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitSingle_column"):
                listener.exitSingle_column(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitSingle_column"):
                return visitor.visitSingle_column(self)
            else:
                return visitor.visitChildren(self)




    def single_column(self):

        localctx = MySQLParser.Single_columnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_single_column)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self.match(MySQLParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Multi_columnContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MySQLParser.Multi_columnContext, self).__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i=None):
            if i is None:
                return self.getTokens(MySQLParser.ID)
            else:
                return self.getToken(MySQLParser.ID, i)

        def COMMA(self, i=None):
            if i is None:
                return self.getTokens(MySQLParser.COMMA)
            else:
                return self.getToken(MySQLParser.COMMA, i)

        def getRuleIndex(self):
            return MySQLParser.RULE_multi_column

        def enterRule(self, listener):
            if hasattr(listener, "enterMulti_column"):
                listener.enterMulti_column(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitMulti_column"):
                listener.exitMulti_column(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitMulti_column"):
                return visitor.visitMulti_column(self)
            else:
                return visitor.visitChildren(self)




    def multi_column(self):

        localctx = MySQLParser.Multi_columnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_multi_column)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            self.match(MySQLParser.ID)
            self.state = 76 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 74
                self.match(MySQLParser.COMMA)
                self.state = 75
                self.match(MySQLParser.ID)
                self.state = 78 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==MySQLParser.COMMA):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class All_columnContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MySQLParser.All_columnContext, self).__init__(parent, invokingState)
            self.parser = parser

        def ASTERISK(self):
            return self.getToken(MySQLParser.ASTERISK, 0)

        def getRuleIndex(self):
            return MySQLParser.RULE_all_column

        def enterRule(self, listener):
            if hasattr(listener, "enterAll_column"):
                listener.enterAll_column(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitAll_column"):
                listener.exitAll_column(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitAll_column"):
                return visitor.visitAll_column(self)
            else:
                return visitor.visitChildren(self)




    def all_column(self):

        localctx = MySQLParser.All_columnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_all_column)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self.match(MySQLParser.ASTERISK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Where_clauseContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MySQLParser.Where_clauseContext, self).__init__(parent, invokingState)
            self.parser = parser

        def hash_expression(self):
            return self.getTypedRuleContext(MySQLParser.Hash_expressionContext,0)


        def hash_range_expression(self):
            return self.getTypedRuleContext(MySQLParser.Hash_range_expressionContext,0)


        def getRuleIndex(self):
            return MySQLParser.RULE_where_clause

        def enterRule(self, listener):
            if hasattr(listener, "enterWhere_clause"):
                listener.enterWhere_clause(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitWhere_clause"):
                listener.exitWhere_clause(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitWhere_clause"):
                return visitor.visitWhere_clause(self)
            else:
                return visitor.visitChildren(self)




    def where_clause(self):

        localctx = MySQLParser.Where_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_where_clause)
        try:
            self.state = 84
            self._errHandler.sync(self);
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 82
                self.hash_expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 83
                self.hash_range_expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Hash_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MySQLParser.Hash_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def WHERE(self):
            return self.getToken(MySQLParser.WHERE, 0)

        def hash_key(self):
            return self.getTypedRuleContext(MySQLParser.Hash_keyContext,0)


        def relational_op(self):
            return self.getTypedRuleContext(MySQLParser.Relational_opContext,0)


        def hash_value(self):
            return self.getTypedRuleContext(MySQLParser.Hash_valueContext,0)


        def getRuleIndex(self):
            return MySQLParser.RULE_hash_expression

        def enterRule(self, listener):
            if hasattr(listener, "enterHash_expression"):
                listener.enterHash_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitHash_expression"):
                listener.exitHash_expression(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitHash_expression"):
                return visitor.visitHash_expression(self)
            else:
                return visitor.visitChildren(self)




    def hash_expression(self):

        localctx = MySQLParser.Hash_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_hash_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            self.match(MySQLParser.WHERE)
            self.state = 87
            self.hash_key()
            self.state = 88
            self.relational_op()
            self.state = 89
            self.hash_value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Hash_range_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MySQLParser.Hash_range_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def WHERE(self):
            return self.getToken(MySQLParser.WHERE, 0)

        def hash_key(self):
            return self.getTypedRuleContext(MySQLParser.Hash_keyContext,0)


        def relational_op(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MySQLParser.Relational_opContext)
            else:
                return self.getTypedRuleContext(MySQLParser.Relational_opContext,i)


        def hash_value(self):
            return self.getTypedRuleContext(MySQLParser.Hash_valueContext,0)


        def expr_op(self):
            return self.getTypedRuleContext(MySQLParser.Expr_opContext,0)


        def range_key(self):
            return self.getTypedRuleContext(MySQLParser.Range_keyContext,0)


        def range_value(self):
            return self.getTypedRuleContext(MySQLParser.Range_valueContext,0)


        def getRuleIndex(self):
            return MySQLParser.RULE_hash_range_expression

        def enterRule(self, listener):
            if hasattr(listener, "enterHash_range_expression"):
                listener.enterHash_range_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitHash_range_expression"):
                listener.exitHash_range_expression(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitHash_range_expression"):
                return visitor.visitHash_range_expression(self)
            else:
                return visitor.visitChildren(self)




    def hash_range_expression(self):

        localctx = MySQLParser.Hash_range_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_hash_range_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            self.match(MySQLParser.WHERE)
            self.state = 92
            self.hash_key()
            self.state = 93
            self.relational_op()
            self.state = 94
            self.hash_value()
            self.state = 95
            self.expr_op()
            self.state = 96
            self.range_key()
            self.state = 97
            self.relational_op()
            self.state = 98
            self.range_value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Hash_keyContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MySQLParser.Hash_keyContext, self).__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MySQLParser.ID, 0)

        def getRuleIndex(self):
            return MySQLParser.RULE_hash_key

        def enterRule(self, listener):
            if hasattr(listener, "enterHash_key"):
                listener.enterHash_key(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitHash_key"):
                listener.exitHash_key(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitHash_key"):
                return visitor.visitHash_key(self)
            else:
                return visitor.visitChildren(self)




    def hash_key(self):

        localctx = MySQLParser.Hash_keyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_hash_key)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self.match(MySQLParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Range_keyContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MySQLParser.Range_keyContext, self).__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MySQLParser.ID, 0)

        def getRuleIndex(self):
            return MySQLParser.RULE_range_key

        def enterRule(self, listener):
            if hasattr(listener, "enterRange_key"):
                listener.enterRange_key(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitRange_key"):
                listener.exitRange_key(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitRange_key"):
                return visitor.visitRange_key(self)
            else:
                return visitor.visitChildren(self)




    def range_key(self):

        localctx = MySQLParser.Range_keyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_range_key)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            self.match(MySQLParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Hash_valueContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MySQLParser.Hash_valueContext, self).__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MySQLParser.ID, 0)

        def getRuleIndex(self):
            return MySQLParser.RULE_hash_value

        def enterRule(self, listener):
            if hasattr(listener, "enterHash_value"):
                listener.enterHash_value(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitHash_value"):
                listener.exitHash_value(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitHash_value"):
                return visitor.visitHash_value(self)
            else:
                return visitor.visitChildren(self)




    def hash_value(self):

        localctx = MySQLParser.Hash_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_hash_value)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 104
            self.match(MySQLParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Range_valueContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MySQLParser.Range_valueContext, self).__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MySQLParser.ID, 0)

        def getRuleIndex(self):
            return MySQLParser.RULE_range_value

        def enterRule(self, listener):
            if hasattr(listener, "enterRange_value"):
                listener.enterRange_value(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitRange_value"):
                listener.exitRange_value(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitRange_value"):
                return visitor.visitRange_value(self)
            else:
                return visitor.visitChildren(self)




    def range_value(self):

        localctx = MySQLParser.Range_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_range_value)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            self.match(MySQLParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Relational_opContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MySQLParser.Relational_opContext, self).__init__(parent, invokingState)
            self.parser = parser

        def EQ(self):
            return self.getToken(MySQLParser.EQ, 0)

        def LTH(self):
            return self.getToken(MySQLParser.LTH, 0)

        def GTH(self):
            return self.getToken(MySQLParser.GTH, 0)

        def NOT_EQ(self):
            return self.getToken(MySQLParser.NOT_EQ, 0)

        def LET(self):
            return self.getToken(MySQLParser.LET, 0)

        def GET(self):
            return self.getToken(MySQLParser.GET, 0)

        def getRuleIndex(self):
            return MySQLParser.RULE_relational_op

        def enterRule(self, listener):
            if hasattr(listener, "enterRelational_op"):
                listener.enterRelational_op(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitRelational_op"):
                listener.exitRelational_op(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitRelational_op"):
                return visitor.visitRelational_op(self)
            else:
                return visitor.visitChildren(self)




    def relational_op(self):

        localctx = MySQLParser.Relational_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_relational_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 108
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MySQLParser.EQ) | (1 << MySQLParser.LTH) | (1 << MySQLParser.GTH) | (1 << MySQLParser.NOT_EQ) | (1 << MySQLParser.LET) | (1 << MySQLParser.GET))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Expr_opContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MySQLParser.Expr_opContext, self).__init__(parent, invokingState)
            self.parser = parser

        def AND(self):
            return self.getToken(MySQLParser.AND, 0)

        def XOR(self):
            return self.getToken(MySQLParser.XOR, 0)

        def OR(self):
            return self.getToken(MySQLParser.OR, 0)

        def NOT(self):
            return self.getToken(MySQLParser.NOT, 0)

        def getRuleIndex(self):
            return MySQLParser.RULE_expr_op

        def enterRule(self, listener):
            if hasattr(listener, "enterExpr_op"):
                listener.enterExpr_op(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitExpr_op"):
                listener.exitExpr_op(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitExpr_op"):
                return visitor.visitExpr_op(self)
            else:
                return visitor.visitChildren(self)




    def expr_op(self):

        localctx = MySQLParser.Expr_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_expr_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MySQLParser.AND) | (1 << MySQLParser.OR) | (1 << MySQLParser.XOR) | (1 << MySQLParser.NOT))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Between_opContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MySQLParser.Between_opContext, self).__init__(parent, invokingState)
            self.parser = parser

        def BETWEEN(self):
            return self.getToken(MySQLParser.BETWEEN, 0)

        def getRuleIndex(self):
            return MySQLParser.RULE_between_op

        def enterRule(self, listener):
            if hasattr(listener, "enterBetween_op"):
                listener.enterBetween_op(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitBetween_op"):
                listener.exitBetween_op(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitBetween_op"):
                return visitor.visitBetween_op(self)
            else:
                return visitor.visitChildren(self)




    def between_op(self):

        localctx = MySQLParser.Between_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_between_op)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self.match(MySQLParser.BETWEEN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Is_or_is_notContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MySQLParser.Is_or_is_notContext, self).__init__(parent, invokingState)
            self.parser = parser

        def IS(self):
            return self.getToken(MySQLParser.IS, 0)

        def NOT(self):
            return self.getToken(MySQLParser.NOT, 0)

        def getRuleIndex(self):
            return MySQLParser.RULE_is_or_is_not

        def enterRule(self, listener):
            if hasattr(listener, "enterIs_or_is_not"):
                listener.enterIs_or_is_not(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitIs_or_is_not"):
                listener.exitIs_or_is_not(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitIs_or_is_not"):
                return visitor.visitIs_or_is_not(self)
            else:
                return visitor.visitChildren(self)




    def is_or_is_not(self):

        localctx = MySQLParser.Is_or_is_notContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_is_or_is_not)
        try:
            self.state = 117
            self._errHandler.sync(self);
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 114
                self.match(MySQLParser.IS)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 115
                self.match(MySQLParser.IS)
                self.state = 116
                self.match(MySQLParser.NOT)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





