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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\17")
        buf.write("U\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16\t")
        buf.write("\16\3\2\5\2\36\n\2\3\2\6\2!\n\2\r\2\16\2\"\3\3\5\3&\n")
        buf.write("\3\3\3\5\3)\n\3\3\3\5\3,\n\3\3\4\3\4\3\4\3\5\3\5\3\6\3")
        buf.write("\6\3\7\3\7\3\7\3\7\7\79\n\7\f\7\16\7<\13\7\5\7>\n\7\3")
        buf.write("\7\3\7\3\b\3\b\3\b\3\b\3\b\5\bG\n\b\3\t\3\t\3\n\3\n\3")
        buf.write("\13\3\13\3\f\3\f\3\r\3\r\3\16\3\16\3\16\2\2\17\2\4\6\b")
        buf.write("\n\f\16\20\22\24\26\30\32\2\2\2R\2 \3\2\2\2\4%\3\2\2\2")
        buf.write("\6-\3\2\2\2\b\60\3\2\2\2\n\62\3\2\2\2\f\64\3\2\2\2\16")
        buf.write("F\3\2\2\2\20H\3\2\2\2\22J\3\2\2\2\24L\3\2\2\2\26N\3\2")
        buf.write("\2\2\30P\3\2\2\2\32R\3\2\2\2\34\36\5\4\3\2\35\34\3\2\2")
        buf.write("\2\35\36\3\2\2\2\36\37\3\2\2\2\37!\7\16\2\2 \35\3\2\2")
        buf.write("\2!\"\3\2\2\2\" \3\2\2\2\"#\3\2\2\2#\3\3\2\2\2$&\5\n\6")
        buf.write("\2%$\3\2\2\2%&\3\2\2\2&(\3\2\2\2\')\5\6\4\2(\'\3\2\2\2")
        buf.write("()\3\2\2\2)+\3\2\2\2*,\5\32\16\2+*\3\2\2\2+,\3\2\2\2,")
        buf.write("\5\3\2\2\2-.\5\b\5\2./\5\f\7\2/\7\3\2\2\2\60\61\7\7\2")
        buf.write("\2\61\t\3\2\2\2\62\63\7\6\2\2\63\13\3\2\2\2\64=\7\3\2")
        buf.write("\2\65:\5\16\b\2\66\67\7\4\2\2\679\5\16\b\28\66\3\2\2\2")
        buf.write("9<\3\2\2\2:8\3\2\2\2:;\3\2\2\2;>\3\2\2\2<:\3\2\2\2=\65")
        buf.write("\3\2\2\2=>\3\2\2\2>?\3\2\2\2?@\7\5\2\2@\r\3\2\2\2AG\5")
        buf.write("\22\n\2BG\5\24\13\2CG\5\26\f\2DG\5\30\r\2EG\5\20\t\2F")
        buf.write("A\3\2\2\2FB\3\2\2\2FC\3\2\2\2FD\3\2\2\2FE\3\2\2\2G\17")
        buf.write("\3\2\2\2HI\7\r\2\2I\21\3\2\2\2JK\7\b\2\2K\23\3\2\2\2L")
        buf.write("M\7\t\2\2M\25\3\2\2\2NO\7\n\2\2O\27\3\2\2\2PQ\7\13\2\2")
        buf.write("Q\31\3\2\2\2RS\7\f\2\2S\33\3\2\2\2\n\35\"%(+:=F")
        return buf.getvalue()


class evParser ( Parser ):

    grammarFileName = "ev.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "','", "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "LABEL", "EVCMD", "NUMBER", "WORK", "FLAG", "SYS_FLAG", 
                      "COMMENT", "STRING", "EOL", "WS" ]

    RULE_prog = 0
    RULE_line = 1
    RULE_instruction = 2
    RULE_evCmd = 3
    RULE_lbl = 4
    RULE_expressionlist = 5
    RULE_argument = 6
    RULE_string_ = 7
    RULE_number = 8
    RULE_work = 9
    RULE_flag = 10
    RULE_sysFlag = 11
    RULE_comment = 12

    ruleNames =  [ "prog", "line", "instruction", "evCmd", "lbl", "expressionlist", 
                   "argument", "string_", "number", "work", "flag", "sysFlag", 
                   "comment" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    LABEL=4
    EVCMD=5
    NUMBER=6
    WORK=7
    FLAG=8
    SYS_FLAG=9
    COMMENT=10
    STRING=11
    EOL=12
    WS=13

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
            self.state = 30 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 27
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                if la_ == 1:
                    self.state = 26
                    self.line()


                self.state = 29
                self.match(evParser.EOL)
                self.state = 32 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << evParser.LABEL) | (1 << evParser.EVCMD) | (1 << evParser.COMMENT) | (1 << evParser.EOL))) != 0)):
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
            self.state = 35
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==evParser.LABEL:
                self.state = 34
                self.lbl()


            self.state = 38
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==evParser.EVCMD:
                self.state = 37
                self.instruction()


            self.state = 41
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==evParser.COMMENT:
                self.state = 40
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
            self.state = 43
            self.evCmd()
            self.state = 44
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
            self.state = 46
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

        def LABEL(self):
            return self.getToken(evParser.LABEL, 0)

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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self.match(evParser.LABEL)
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
            self.state = 50
            self.match(evParser.T__0)
            self.state = 59
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << evParser.NUMBER) | (1 << evParser.WORK) | (1 << evParser.FLAG) | (1 << evParser.SYS_FLAG) | (1 << evParser.STRING))) != 0):
                self.state = 51
                self.argument()
                self.state = 56
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==evParser.T__1:
                    self.state = 52
                    self.match(evParser.T__1)
                    self.state = 53
                    self.argument()
                    self.state = 58
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 61
            self.match(evParser.T__2)
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
        self.enterRule(localctx, 12, self.RULE_argument)
        try:
            self.state = 68
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [evParser.NUMBER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 63
                self.number()
                pass
            elif token in [evParser.WORK]:
                self.enterOuterAlt(localctx, 2)
                self.state = 64
                self.work()
                pass
            elif token in [evParser.FLAG]:
                self.enterOuterAlt(localctx, 3)
                self.state = 65
                self.flag()
                pass
            elif token in [evParser.SYS_FLAG]:
                self.enterOuterAlt(localctx, 4)
                self.state = 66
                self.sysFlag()
                pass
            elif token in [evParser.STRING]:
                self.enterOuterAlt(localctx, 5)
                self.state = 67
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
        self.enterRule(localctx, 14, self.RULE_string_)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self.match(evParser.STRING)
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
        self.enterRule(localctx, 16, self.RULE_number)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
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
        self.enterRule(localctx, 18, self.RULE_work)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
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
        self.enterRule(localctx, 20, self.RULE_flag)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
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
        self.enterRule(localctx, 22, self.RULE_sysFlag)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
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
        self.enterRule(localctx, 24, self.RULE_comment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self.match(evParser.COMMENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





