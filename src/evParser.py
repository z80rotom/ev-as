# Generated from ev.g4 by ANTLR 4.13.1
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
        4,1,14,100,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,1,0,3,0,
        28,8,0,1,0,4,0,31,8,0,11,0,12,0,32,1,0,1,0,1,1,1,1,3,1,39,8,1,1,
        2,1,2,1,2,1,3,1,3,1,3,4,3,47,8,3,11,3,12,3,48,1,4,1,4,1,4,1,4,1,
        4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,63,8,4,1,5,1,5,1,5,1,5,5,5,69,
        8,5,10,5,12,5,72,9,5,3,5,74,8,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,3,6,
        83,8,6,1,7,1,7,1,8,1,8,1,8,1,9,1,9,1,9,1,10,1,10,1,10,1,11,1,11,
        1,12,1,12,1,12,0,0,13,0,2,4,6,8,10,12,14,16,18,20,22,24,0,1,1,0,
        9,10,98,0,30,1,0,0,0,2,38,1,0,0,0,4,40,1,0,0,0,6,43,1,0,0,0,8,62,
        1,0,0,0,10,64,1,0,0,0,12,82,1,0,0,0,14,84,1,0,0,0,16,86,1,0,0,0,
        18,89,1,0,0,0,20,92,1,0,0,0,22,95,1,0,0,0,24,97,1,0,0,0,26,28,3,
        2,1,0,27,26,1,0,0,0,27,28,1,0,0,0,28,29,1,0,0,0,29,31,5,13,0,0,30,
        27,1,0,0,0,31,32,1,0,0,0,32,30,1,0,0,0,32,33,1,0,0,0,33,34,1,0,0,
        0,34,35,3,2,1,0,35,1,1,0,0,0,36,39,3,8,4,0,37,39,3,6,3,0,38,36,1,
        0,0,0,38,37,1,0,0,0,39,3,1,0,0,0,40,41,3,22,11,0,41,42,3,10,5,0,
        42,5,1,0,0,0,43,44,3,22,11,0,44,46,5,1,0,0,45,47,3,4,2,0,46,45,1,
        0,0,0,47,48,1,0,0,0,48,46,1,0,0,0,48,49,1,0,0,0,49,7,1,0,0,0,50,
        51,5,2,0,0,51,52,3,18,9,0,52,53,3,24,12,0,53,63,1,0,0,0,54,55,5,
        2,0,0,55,56,3,20,10,0,56,57,3,24,12,0,57,63,1,0,0,0,58,59,5,2,0,
        0,59,60,3,16,8,0,60,61,3,24,12,0,61,63,1,0,0,0,62,50,1,0,0,0,62,
        54,1,0,0,0,62,58,1,0,0,0,63,9,1,0,0,0,64,73,5,3,0,0,65,70,3,12,6,
        0,66,67,5,4,0,0,67,69,3,12,6,0,68,66,1,0,0,0,69,72,1,0,0,0,70,68,
        1,0,0,0,70,71,1,0,0,0,71,74,1,0,0,0,72,70,1,0,0,0,73,65,1,0,0,0,
        73,74,1,0,0,0,74,75,1,0,0,0,75,76,5,5,0,0,76,11,1,0,0,0,77,83,3,
        24,12,0,78,83,3,16,8,0,79,83,3,18,9,0,80,83,3,20,10,0,81,83,3,14,
        7,0,82,77,1,0,0,0,82,78,1,0,0,0,82,79,1,0,0,0,82,80,1,0,0,0,82,81,
        1,0,0,0,83,13,1,0,0,0,84,85,5,12,0,0,85,15,1,0,0,0,86,87,5,6,0,0,
        87,88,7,0,0,0,88,17,1,0,0,0,89,90,5,7,0,0,90,91,7,0,0,0,91,19,1,
        0,0,0,92,93,5,8,0,0,93,94,7,0,0,0,94,21,1,0,0,0,95,96,5,9,0,0,96,
        23,1,0,0,0,97,98,5,10,0,0,98,25,1,0,0,0,8,27,32,38,48,62,70,73,82
    ]

class evParser ( Parser ):

    grammarFileName = "ev.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "':'", "'.define'", "'('", "','", "')'", 
                     "'@'", "'#'", "'$'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "NAME", "NUMBER", "COMMENT", "STRING", 
                      "EOL", "WS" ]

    RULE_prog = 0
    RULE_line = 1
    RULE_instruction = 2
    RULE_lbl = 3
    RULE_define = 4
    RULE_expressionlist = 5
    RULE_argument = 6
    RULE_string_ = 7
    RULE_work = 8
    RULE_flag = 9
    RULE_sysFlag = 10
    RULE_name = 11
    RULE_number = 12

    ruleNames =  [ "prog", "line", "instruction", "lbl", "define", "expressionlist", 
                   "argument", "string_", "work", "flag", "sysFlag", "name", 
                   "number" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    NAME=9
    NUMBER=10
    COMMENT=11
    STRING=12
    EOL=13
    WS=14

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def line(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(evParser.LineContext)
            else:
                return self.getTypedRuleContext(evParser.LineContext,i)


        def EOL(self, i:int=None):
            if i is None:
                return self.getTokens(evParser.EOL)
            else:
                return self.getToken(evParser.EOL, i)

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
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 27
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==2 or _la==9:
                        self.state = 26
                        self.line()


                    self.state = 29
                    self.match(evParser.EOL)

                else:
                    raise NoViableAltException(self)
                self.state = 32 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

            self.state = 34
            self.line()
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

        def define(self):
            return self.getTypedRuleContext(evParser.DefineContext,0)


        def lbl(self):
            return self.getTypedRuleContext(evParser.LblContext,0)


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
        try:
            self.state = 38
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 36
                self.define()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 37
                self.lbl()
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


    class InstructionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def name(self):
            return self.getTypedRuleContext(evParser.NameContext,0)


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
            self.state = 40
            self.name()
            self.state = 41
            self.expressionlist()
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

        def name(self):
            return self.getTypedRuleContext(evParser.NameContext,0)


        def instruction(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(evParser.InstructionContext)
            else:
                return self.getTypedRuleContext(evParser.InstructionContext,i)


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
        self.enterRule(localctx, 6, self.RULE_lbl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self.name()
            self.state = 44
            self.match(evParser.T__0)
            self.state = 46 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 45
                self.instruction()
                self.state = 48 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==9):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DefineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def flag(self):
            return self.getTypedRuleContext(evParser.FlagContext,0)


        def number(self):
            return self.getTypedRuleContext(evParser.NumberContext,0)


        def sysFlag(self):
            return self.getTypedRuleContext(evParser.SysFlagContext,0)


        def work(self):
            return self.getTypedRuleContext(evParser.WorkContext,0)


        def getRuleIndex(self):
            return evParser.RULE_define

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDefine" ):
                listener.enterDefine(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDefine" ):
                listener.exitDefine(self)




    def define(self):

        localctx = evParser.DefineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_define)
        try:
            self.state = 62
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 50
                self.match(evParser.T__1)
                self.state = 51
                self.flag()
                self.state = 52
                self.number()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 54
                self.match(evParser.T__1)
                self.state = 55
                self.sysFlag()
                self.state = 56
                self.number()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 58
                self.match(evParser.T__1)
                self.state = 59
                self.work()
                self.state = 60
                self.number()
                pass


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
            self.state = 64
            self.match(evParser.T__2)
            self.state = 73
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 5568) != 0):
                self.state = 65
                self.argument()
                self.state = 70
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==4:
                    self.state = 66
                    self.match(evParser.T__3)
                    self.state = 67
                    self.argument()
                    self.state = 72
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 75
            self.match(evParser.T__4)
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
            self.state = 82
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                self.enterOuterAlt(localctx, 1)
                self.state = 77
                self.number()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 2)
                self.state = 78
                self.work()
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 3)
                self.state = 79
                self.flag()
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 4)
                self.state = 80
                self.sysFlag()
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 5)
                self.state = 81
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
            self.state = 84
            self.match(evParser.STRING)
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

        def NAME(self):
            return self.getToken(evParser.NAME, 0)

        def NUMBER(self):
            return self.getToken(evParser.NUMBER, 0)

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
        self.enterRule(localctx, 16, self.RULE_work)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            self.match(evParser.T__5)
            self.state = 87
            _la = self._input.LA(1)
            if not(_la==9 or _la==10):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
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

        def NAME(self):
            return self.getToken(evParser.NAME, 0)

        def NUMBER(self):
            return self.getToken(evParser.NUMBER, 0)

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
        self.enterRule(localctx, 18, self.RULE_flag)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            self.match(evParser.T__6)
            self.state = 90
            _la = self._input.LA(1)
            if not(_la==9 or _la==10):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
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

        def NAME(self):
            return self.getToken(evParser.NAME, 0)

        def NUMBER(self):
            return self.getToken(evParser.NUMBER, 0)

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
        self.enterRule(localctx, 20, self.RULE_sysFlag)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 92
            self.match(evParser.T__7)
            self.state = 93
            _la = self._input.LA(1)
            if not(_la==9 or _la==10):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
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
        self.enterRule(localctx, 22, self.RULE_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
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
        self.enterRule(localctx, 24, self.RULE_number)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            self.match(evParser.NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





