# Generated from ev.g4 by ANTLR 4.9.3
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\20")
        buf.write("_\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16\t")
        buf.write("\16\4\17\t\17\4\20\t\20\3\2\5\2\"\n\2\3\2\6\2%\n\2\r\2")
        buf.write("\16\2&\3\3\5\3*\n\3\3\3\5\3-\n\3\3\3\5\3\60\n\3\3\4\3")
        buf.write("\4\3\4\3\5\3\5\3\6\3\6\5\69\n\6\3\7\3\7\3\7\3\7\7\7?\n")
        buf.write("\7\f\7\16\7B\13\7\5\7D\n\7\3\7\3\7\3\b\3\b\3\t\3\t\3\t")
        buf.write("\3\t\3\t\5\tO\n\t\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3")
        buf.write("\16\3\16\3\17\3\17\3\20\3\20\3\20\2\2\21\2\4\6\b\n\f\16")
        buf.write("\20\22\24\26\30\32\34\36\2\2\2[\2$\3\2\2\2\4)\3\2\2\2")
        buf.write("\6\61\3\2\2\2\b\64\3\2\2\2\n\66\3\2\2\2\f:\3\2\2\2\16")
        buf.write("G\3\2\2\2\20N\3\2\2\2\22P\3\2\2\2\24R\3\2\2\2\26T\3\2")
        buf.write("\2\2\30V\3\2\2\2\32X\3\2\2\2\34Z\3\2\2\2\36\\\3\2\2\2")
        buf.write(" \"\5\4\3\2! \3\2\2\2!\"\3\2\2\2\"#\3\2\2\2#%\7\17\2\2")
        buf.write("$!\3\2\2\2%&\3\2\2\2&$\3\2\2\2&\'\3\2\2\2\'\3\3\2\2\2")
        buf.write("(*\5\n\6\2)(\3\2\2\2)*\3\2\2\2*,\3\2\2\2+-\5\6\4\2,+\3")
        buf.write("\2\2\2,-\3\2\2\2-/\3\2\2\2.\60\5\36\20\2/.\3\2\2\2/\60")
        buf.write("\3\2\2\2\60\5\3\2\2\2\61\62\5\b\5\2\62\63\5\f\7\2\63\7")
        buf.write("\3\2\2\2\64\65\7\b\2\2\65\t\3\2\2\2\668\5\16\b\2\679\7")
        buf.write("\3\2\28\67\3\2\2\289\3\2\2\29\13\3\2\2\2:C\7\4\2\2;@\5")
        buf.write("\20\t\2<=\7\5\2\2=?\5\20\t\2><\3\2\2\2?B\3\2\2\2@>\3\2")
        buf.write("\2\2@A\3\2\2\2AD\3\2\2\2B@\3\2\2\2C;\3\2\2\2CD\3\2\2\2")
        buf.write("DE\3\2\2\2EF\7\6\2\2F\r\3\2\2\2GH\5\24\13\2H\17\3\2\2")
        buf.write("\2IO\5\26\f\2JO\5\30\r\2KO\5\32\16\2LO\5\34\17\2MO\5\22")
        buf.write("\n\2NI\3\2\2\2NJ\3\2\2\2NK\3\2\2\2NL\3\2\2\2NM\3\2\2\2")
        buf.write("O\21\3\2\2\2PQ\7\16\2\2Q\23\3\2\2\2RS\7\7\2\2S\25\3\2")
        buf.write("\2\2TU\7\t\2\2U\27\3\2\2\2VW\7\n\2\2W\31\3\2\2\2XY\7\13")
        buf.write("\2\2Y\33\3\2\2\2Z[\7\f\2\2[\35\3\2\2\2\\]\7\r\2\2]\37")
        buf.write("\3\2\2\2\13!&),/8@CN")
        return buf.getvalue()


class evParser ( Parser ):

    grammarFileName = "ev.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "':'", "'('", "','", "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "NAME", "EVCMD", "NUMBER", "WORK", "FLAG", 
                      "SYS_FLAG", "COMMENT", "STRING", "EOL", "WS" ]

    RULE_prog = 0
    RULE_line = 1
    RULE_instruction = 2
    RULE_evCmd = 3
    RULE_lbl = 4
    RULE_expressionlist = 5
    RULE_label = 6
    RULE_argument = 7
    RULE_string_ = 8
    RULE_name = 9
    RULE_number = 10
    RULE_work = 11
    RULE_flag = 12
    RULE_sysFlag = 13
    RULE_comment = 14

    ruleNames =  [ "prog", "line", "instruction", "evCmd", "lbl", "expressionlist", 
                   "label", "argument", "string_", "name", "number", "work", 
                   "flag", "sysFlag", "comment" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    NAME=5
    EVCMD=6
    NUMBER=7
    WORK=8
    FLAG=9
    SYS_FLAG=10
    COMMENT=11
    STRING=12
    EOL=13
    WS=14

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOL(self, i:int=None):
            if i is None:
                return self.getTokens(evParser.EOL)
            else:
                return self.getToken(evParser.EOL, i)

        def line(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(evParser.LineContext)
            else:
                return self.getTypedRuleContext(evParser.LineContext,i)


        def getRuleIndex(self):
            return evParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)




    def prog(self):

        localctx = evParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 31
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                if la_ == 1:
                    self.state = 30
                    self.line()


                self.state = 33
                self.match(evParser.EOL)
                self.state = 36 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << evParser.NAME) | (1 << evParser.EVCMD) | (1 << evParser.COMMENT) | (1 << evParser.EOL))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lbl(self):
            return self.getTypedRuleContext(evParser.LblContext,0)


        def instruction(self):
            return self.getTypedRuleContext(evParser.InstructionContext,0)


        def comment(self):
            return self.getTypedRuleContext(evParser.CommentContext,0)


        def getRuleIndex(self):
            return evParser.RULE_line

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLine" ):
                listener.enterLine(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLine" ):
                listener.exitLine(self)




    def line(self):

        localctx = evParser.LineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_line)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==evParser.NAME:
                self.state = 38
                self.lbl()


            self.state = 42
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==evParser.EVCMD:
                self.state = 41
                self.instruction()


            self.state = 45
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==evParser.COMMENT:
                self.state = 44
                self.comment()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstructionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def evCmd(self):
            return self.getTypedRuleContext(evParser.EvCmdContext,0)


        def expressionlist(self):
            return self.getTypedRuleContext(evParser.ExpressionlistContext,0)


        def getRuleIndex(self):
            return evParser.RULE_instruction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstruction" ):
                listener.enterInstruction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstruction" ):
                listener.exitInstruction(self)




    def instruction(self):

        localctx = evParser.InstructionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_instruction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self.evCmd()
            self.state = 48
            self.expressionlist()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EvCmdContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EVCMD(self):
            return self.getToken(evParser.EVCMD, 0)

        def getRuleIndex(self):
            return evParser.RULE_evCmd

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEvCmd" ):
                listener.enterEvCmd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEvCmd" ):
                listener.exitEvCmd(self)




    def evCmd(self):

        localctx = evParser.EvCmdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_evCmd)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self.match(evParser.EVCMD)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LblContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def label(self):
            return self.getTypedRuleContext(evParser.LabelContext,0)


        def getRuleIndex(self):
            return evParser.RULE_lbl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLbl" ):
                listener.enterLbl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLbl" ):
                listener.exitLbl(self)




    def lbl(self):

        localctx = evParser.LblContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_lbl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self.label()
            self.state = 54
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==evParser.T__0:
                self.state = 53
                self.match(evParser.T__0)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def argument(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(evParser.ArgumentContext)
            else:
                return self.getTypedRuleContext(evParser.ArgumentContext,i)


        def getRuleIndex(self):
            return evParser.RULE_expressionlist

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionlist" ):
                listener.enterExpressionlist(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionlist" ):
                listener.exitExpressionlist(self)




    def expressionlist(self):

        localctx = evParser.ExpressionlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_expressionlist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self.match(evParser.T__1)
            self.state = 65
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << evParser.NUMBER) | (1 << evParser.WORK) | (1 << evParser.FLAG) | (1 << evParser.SYS_FLAG) | (1 << evParser.STRING))) != 0):
                self.state = 57
                self.argument()
                self.state = 62
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==evParser.T__2:
                    self.state = 58
                    self.match(evParser.T__2)
                    self.state = 59
                    self.argument()
                    self.state = 64
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 67
            self.match(evParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LabelContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def name(self):
            return self.getTypedRuleContext(evParser.NameContext,0)


        def getRuleIndex(self):
            return evParser.RULE_label

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLabel" ):
                listener.enterLabel(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLabel" ):
                listener.exitLabel(self)




    def label(self):

        localctx = evParser.LabelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_label)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self.name()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def number(self):
            return self.getTypedRuleContext(evParser.NumberContext,0)


        def work(self):
            return self.getTypedRuleContext(evParser.WorkContext,0)


        def flag(self):
            return self.getTypedRuleContext(evParser.FlagContext,0)


        def sysFlag(self):
            return self.getTypedRuleContext(evParser.SysFlagContext,0)


        def string_(self):
            return self.getTypedRuleContext(evParser.String_Context,0)


        def getRuleIndex(self):
            return evParser.RULE_argument

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgument" ):
                listener.enterArgument(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgument" ):
                listener.exitArgument(self)




    def argument(self):

        localctx = evParser.ArgumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_argument)
        try:
            self.state = 76
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [evParser.NUMBER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 71
                self.number()
                pass
            elif token in [evParser.WORK]:
                self.enterOuterAlt(localctx, 2)
                self.state = 72
                self.work()
                pass
            elif token in [evParser.FLAG]:
                self.enterOuterAlt(localctx, 3)
                self.state = 73
                self.flag()
                pass
            elif token in [evParser.SYS_FLAG]:
                self.enterOuterAlt(localctx, 4)
                self.state = 74
                self.sysFlag()
                pass
            elif token in [evParser.STRING]:
                self.enterOuterAlt(localctx, 5)
                self.state = 75
                self.string_()
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


    class String_Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(evParser.STRING, 0)

        def getRuleIndex(self):
            return evParser.RULE_string_

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterString_" ):
                listener.enterString_(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitString_" ):
                listener.exitString_(self)




    def string_(self):

        localctx = evParser.String_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_string_)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            self.match(evParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(evParser.NAME, 0)

        def getRuleIndex(self):
            return evParser.RULE_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterName" ):
                listener.enterName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitName" ):
                listener.exitName(self)




    def name(self):

        localctx = evParser.NameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self.match(evParser.NAME)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NumberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(evParser.NUMBER, 0)

        def getRuleIndex(self):
            return evParser.RULE_number

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumber" ):
                listener.enterNumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumber" ):
                listener.exitNumber(self)




    def number(self):

        localctx = evParser.NumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_number)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            self.match(evParser.NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WorkContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WORK(self):
            return self.getToken(evParser.WORK, 0)

        def getRuleIndex(self):
            return evParser.RULE_work

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWork" ):
                listener.enterWork(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWork" ):
                listener.exitWork(self)




    def work(self):

        localctx = evParser.WorkContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_work)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            self.match(evParser.WORK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FlagContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FLAG(self):
            return self.getToken(evParser.FLAG, 0)

        def getRuleIndex(self):
            return evParser.RULE_flag

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFlag" ):
                listener.enterFlag(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFlag" ):
                listener.exitFlag(self)




    def flag(self):

        localctx = evParser.FlagContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_flag)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            self.match(evParser.FLAG)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SysFlagContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SYS_FLAG(self):
            return self.getToken(evParser.SYS_FLAG, 0)

        def getRuleIndex(self):
            return evParser.RULE_sysFlag

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSysFlag" ):
                listener.enterSysFlag(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSysFlag" ):
                listener.exitSysFlag(self)




    def sysFlag(self):

        localctx = evParser.SysFlagContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_sysFlag)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88
            self.match(evParser.SYS_FLAG)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CommentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMENT(self):
            return self.getToken(evParser.COMMENT, 0)

        def getRuleIndex(self):
            return evParser.RULE_comment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComment" ):
                listener.enterComment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComment" ):
                listener.exitComment(self)




    def comment(self):

        localctx = evParser.CommentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_comment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
            self.match(evParser.COMMENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





