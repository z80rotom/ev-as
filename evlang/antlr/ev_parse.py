# Generated from grammar/ev_parse.g4 by ANTLR 4.9.3
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\27")
        buf.write("d\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\3\2\7\2\30\n\2\f\2\16\2")
        buf.write("\33\13\2\3\2\3\2\7\2\37\n\2\f\2\16\2\"\13\2\3\2\3\2\3")
        buf.write("\3\3\3\3\3\7\3)\n\3\f\3\16\3,\13\3\3\3\5\3/\n\3\3\4\3")
        buf.write("\4\3\4\3\4\5\4\65\n\4\3\5\3\5\3\5\5\5:\n\5\3\5\3\5\7\5")
        buf.write(">\n\5\f\5\16\5A\13\5\3\6\3\6\3\6\5\6F\n\6\3\7\3\7\5\7")
        buf.write("J\n\7\3\b\3\b\3\b\7\bO\n\b\f\b\16\bR\13\b\3\b\5\bU\n\b")
        buf.write("\3\t\3\t\5\tY\n\t\3\t\3\t\3\n\3\n\3\n\5\n`\n\n\3\13\3")
        buf.write("\13\3\13\2\3\b\f\2\4\6\b\n\f\16\20\22\24\2\3\4\2\4\7\t")
        buf.write("\t\2f\2\31\3\2\2\2\4.\3\2\2\2\6\64\3\2\2\2\b9\3\2\2\2")
        buf.write("\nE\3\2\2\2\fI\3\2\2\2\16T\3\2\2\2\20V\3\2\2\2\22\\\3")
        buf.write("\2\2\2\24a\3\2\2\2\26\30\7\20\2\2\27\26\3\2\2\2\30\33")
        buf.write("\3\2\2\2\31\27\3\2\2\2\31\32\3\2\2\2\32\34\3\2\2\2\33")
        buf.write("\31\3\2\2\2\34 \5\4\3\2\35\37\7\20\2\2\36\35\3\2\2\2\37")
        buf.write("\"\3\2\2\2 \36\3\2\2\2 !\3\2\2\2!#\3\2\2\2\" \3\2\2\2")
        buf.write("#$\7\2\2\3$\3\3\2\2\2%*\5\6\4\2&\'\7\20\2\2\')\5\6\4\2")
        buf.write("(&\3\2\2\2),\3\2\2\2*(\3\2\2\2*+\3\2\2\2+/\3\2\2\2,*\3")
        buf.write("\2\2\2-/\3\2\2\2.%\3\2\2\2.-\3\2\2\2/\5\3\2\2\2\60\65")
        buf.write("\5\b\5\2\61\62\5\22\n\2\62\63\5\b\5\2\63\65\3\2\2\2\64")
        buf.write("\60\3\2\2\2\64\61\3\2\2\2\65\7\3\2\2\2\66\67\b\5\1\2\67")
        buf.write(":\5\f\7\28:\5\n\6\29\66\3\2\2\298\3\2\2\2:?\3\2\2\2;<")
        buf.write("\f\3\2\2<>\5\20\t\2=;\3\2\2\2>A\3\2\2\2?=\3\2\2\2?@\3")
        buf.write("\2\2\2@\t\3\2\2\2A?\3\2\2\2BF\5\f\7\2CD\7\13\2\2DF\5\n")
        buf.write("\6\2EB\3\2\2\2EC\3\2\2\2F\13\3\2\2\2GJ\7\3\2\2HJ\5\24")
        buf.write("\13\2IG\3\2\2\2IH\3\2\2\2J\r\3\2\2\2KP\5\b\5\2LM\7\r\2")
        buf.write("\2MO\5\b\5\2NL\3\2\2\2OR\3\2\2\2PN\3\2\2\2PQ\3\2\2\2Q")
        buf.write("U\3\2\2\2RP\3\2\2\2SU\3\2\2\2TK\3\2\2\2TS\3\2\2\2U\17")
        buf.write("\3\2\2\2VX\7\16\2\2WY\5\16\b\2XW\3\2\2\2XY\3\2\2\2YZ\3")
        buf.write("\2\2\2Z[\7\17\2\2[\21\3\2\2\2\\]\7\3\2\2]_\7\f\2\2^`\7")
        buf.write("\20\2\2_^\3\2\2\2_`\3\2\2\2`\23\3\2\2\2ab\t\2\2\2b\25")
        buf.write("\3\2\2\2\17\31 *.\649?EIPTX_")
        return buf.getvalue()


class ev_parse ( Parser ):

    grammarFileName = "ev_parse.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "':'", "','", "'('", "')'", 
                     "<INVALID>", "<INVALID>", "'+'", "'-'", "'@'", "'#'", 
                     "'$'", "'!'" ]

    symbolicNames = [ "<INVALID>", "IDENTIFIER", "STRING_LIT", "HEX_INT_LIT", 
                      "BIN_INT_LIT", "DECIMAL_INT_LIT", "DECIMAL_EXPONENT", 
                      "DECIMAL_FLOAT_LIT", "DECIMAL_FLOAT_EXPONENT", "OPERATOR", 
                      "COLON", "COMMA", "PAREN_LEFT", "PAREN_RIGHT", "EOL", 
                      "WS", "PLUS", "MINUS", "AT", "HASHTAG", "DOLLAR", 
                      "EXCLAM" ]

    RULE_program = 0
    RULE_statementList = 1
    RULE_statement = 2
    RULE_expression = 3
    RULE_unary = 4
    RULE_operand = 5
    RULE_expressionList = 6
    RULE_arguments = 7
    RULE_label = 8
    RULE_literal = 9

    ruleNames =  [ "program", "statementList", "statement", "expression", 
                   "unary", "operand", "expressionList", "arguments", "label", 
                   "literal" ]

    EOF = Token.EOF
    IDENTIFIER=1
    STRING_LIT=2
    HEX_INT_LIT=3
    BIN_INT_LIT=4
    DECIMAL_INT_LIT=5
    DECIMAL_EXPONENT=6
    DECIMAL_FLOAT_LIT=7
    DECIMAL_FLOAT_EXPONENT=8
    OPERATOR=9
    COLON=10
    COMMA=11
    PAREN_LEFT=12
    PAREN_RIGHT=13
    EOL=14
    WS=15
    PLUS=16
    MINUS=17
    AT=18
    HASHTAG=19
    DOLLAR=20
    EXCLAM=21

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statementList(self):
            return self.getTypedRuleContext(ev_parse.StatementListContext,0)


        def EOF(self):
            return self.getToken(ev_parse.EOF, 0)

        def EOL(self, i:int=None):
            if i is None:
                return self.getTokens(ev_parse.EOL)
            else:
                return self.getToken(ev_parse.EOL, i)

        def getRuleIndex(self):
            return ev_parse.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = ev_parse.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 20
                    self.match(ev_parse.EOL) 
                self.state = 25
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

            self.state = 26
            self.statementList()
            self.state = 30
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ev_parse.EOL:
                self.state = 27
                self.match(ev_parse.EOL)
                self.state = 32
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 33
            self.match(ev_parse.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ev_parse.StatementContext)
            else:
                return self.getTypedRuleContext(ev_parse.StatementContext,i)


        def EOL(self, i:int=None):
            if i is None:
                return self.getTokens(ev_parse.EOL)
            else:
                return self.getToken(ev_parse.EOL, i)

        def getRuleIndex(self):
            return ev_parse.RULE_statementList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatementList" ):
                listener.enterStatementList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatementList" ):
                listener.exitStatementList(self)




    def statementList(self):

        localctx = ev_parse.StatementListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statementList)
        try:
            self.state = 44
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ev_parse.IDENTIFIER, ev_parse.STRING_LIT, ev_parse.HEX_INT_LIT, ev_parse.BIN_INT_LIT, ev_parse.DECIMAL_INT_LIT, ev_parse.DECIMAL_FLOAT_LIT, ev_parse.OPERATOR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 35
                self.statement()
                self.state = 40
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 36
                        self.match(ev_parse.EOL)
                        self.state = 37
                        self.statement() 
                    self.state = 42
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

                pass
            elif token in [ev_parse.EOF, ev_parse.EOL]:
                self.enterOuterAlt(localctx, 2)

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


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ev_parse.RULE_statement

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class LabeledStatementContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ev_parse.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def label(self):
            return self.getTypedRuleContext(ev_parse.LabelContext,0)

        def expression(self):
            return self.getTypedRuleContext(ev_parse.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLabeledStatement" ):
                listener.enterLabeledStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLabeledStatement" ):
                listener.exitLabeledStatement(self)


    class ExpressionStatementContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ev_parse.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(ev_parse.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionStatement" ):
                listener.enterExpressionStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionStatement" ):
                listener.exitExpressionStatement(self)



    def statement(self):

        localctx = ev_parse.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_statement)
        try:
            self.state = 50
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                localctx = ev_parse.ExpressionStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 46
                self.expression(0)
                pass

            elif la_ == 2:
                localctx = ev_parse.LabeledStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 47
                self.label()
                self.state = 48
                self.expression(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ev_parse.RULE_expression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class UnaryExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ev_parse.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def unary(self):
            return self.getTypedRuleContext(ev_parse.UnaryContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnaryExpression" ):
                listener.enterUnaryExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnaryExpression" ):
                listener.exitUnaryExpression(self)


    class CallExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ev_parse.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(ev_parse.ExpressionContext,0)

        def arguments(self):
            return self.getTypedRuleContext(ev_parse.ArgumentsContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCallExpression" ):
                listener.enterCallExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCallExpression" ):
                listener.exitCallExpression(self)


    class OperandExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ev_parse.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def operand(self):
            return self.getTypedRuleContext(ev_parse.OperandContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperandExpression" ):
                listener.enterOperandExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperandExpression" ):
                listener.exitOperandExpression(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ev_parse.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                localctx = ev_parse.OperandExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 53
                self.operand()
                pass

            elif la_ == 2:
                localctx = ev_parse.UnaryExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 54
                self.unary()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 61
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ev_parse.CallExpressionContext(self, ev_parse.ExpressionContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                    self.state = 57
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 58
                    self.arguments() 
                self.state = 63
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class UnaryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ev_parse.RULE_unary

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class OperatorUnaryContext(UnaryContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ev_parse.UnaryContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def OPERATOR(self):
            return self.getToken(ev_parse.OPERATOR, 0)
        def unary(self):
            return self.getTypedRuleContext(ev_parse.UnaryContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperatorUnary" ):
                listener.enterOperatorUnary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperatorUnary" ):
                listener.exitOperatorUnary(self)


    class OperandUnaryContext(UnaryContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ev_parse.UnaryContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def operand(self):
            return self.getTypedRuleContext(ev_parse.OperandContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperandUnary" ):
                listener.enterOperandUnary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperandUnary" ):
                listener.exitOperandUnary(self)



    def unary(self):

        localctx = ev_parse.UnaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_unary)
        try:
            self.state = 67
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ev_parse.IDENTIFIER, ev_parse.STRING_LIT, ev_parse.HEX_INT_LIT, ev_parse.BIN_INT_LIT, ev_parse.DECIMAL_INT_LIT, ev_parse.DECIMAL_FLOAT_LIT]:
                localctx = ev_parse.OperandUnaryContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 64
                self.operand()
                pass
            elif token in [ev_parse.OPERATOR]:
                localctx = ev_parse.OperatorUnaryContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 65
                self.match(ev_parse.OPERATOR)
                self.state = 66
                self.unary()
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


    class OperandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ev_parse.RULE_operand

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class LiteralOperandContext(OperandContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ev_parse.OperandContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def literal(self):
            return self.getTypedRuleContext(ev_parse.LiteralContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteralOperand" ):
                listener.enterLiteralOperand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteralOperand" ):
                listener.exitLiteralOperand(self)


    class IdentifierOperandContext(OperandContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ev_parse.OperandContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IDENTIFIER(self):
            return self.getToken(ev_parse.IDENTIFIER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdentifierOperand" ):
                listener.enterIdentifierOperand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdentifierOperand" ):
                listener.exitIdentifierOperand(self)



    def operand(self):

        localctx = ev_parse.OperandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_operand)
        try:
            self.state = 71
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ev_parse.IDENTIFIER]:
                localctx = ev_parse.IdentifierOperandContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 69
                self.match(ev_parse.IDENTIFIER)
                pass
            elif token in [ev_parse.STRING_LIT, ev_parse.HEX_INT_LIT, ev_parse.BIN_INT_LIT, ev_parse.DECIMAL_INT_LIT, ev_parse.DECIMAL_FLOAT_LIT]:
                localctx = ev_parse.LiteralOperandContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 70
                self.literal()
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


    class ExpressionListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ev_parse.ExpressionContext)
            else:
                return self.getTypedRuleContext(ev_parse.ExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(ev_parse.COMMA)
            else:
                return self.getToken(ev_parse.COMMA, i)

        def getRuleIndex(self):
            return ev_parse.RULE_expressionList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionList" ):
                listener.enterExpressionList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionList" ):
                listener.exitExpressionList(self)




    def expressionList(self):

        localctx = ev_parse.ExpressionListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_expressionList)
        self._la = 0 # Token type
        try:
            self.state = 82
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ev_parse.IDENTIFIER, ev_parse.STRING_LIT, ev_parse.HEX_INT_LIT, ev_parse.BIN_INT_LIT, ev_parse.DECIMAL_INT_LIT, ev_parse.DECIMAL_FLOAT_LIT, ev_parse.OPERATOR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 73
                self.expression(0)
                self.state = 78
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==ev_parse.COMMA:
                    self.state = 74
                    self.match(ev_parse.COMMA)
                    self.state = 75
                    self.expression(0)
                    self.state = 80
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [ev_parse.PAREN_RIGHT]:
                self.enterOuterAlt(localctx, 2)

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


    class ArgumentsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PAREN_LEFT(self):
            return self.getToken(ev_parse.PAREN_LEFT, 0)

        def PAREN_RIGHT(self):
            return self.getToken(ev_parse.PAREN_RIGHT, 0)

        def expressionList(self):
            return self.getTypedRuleContext(ev_parse.ExpressionListContext,0)


        def getRuleIndex(self):
            return ev_parse.RULE_arguments

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArguments" ):
                listener.enterArguments(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArguments" ):
                listener.exitArguments(self)




    def arguments(self):

        localctx = ev_parse.ArgumentsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_arguments)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            self.match(ev_parse.PAREN_LEFT)
            self.state = 86
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 85
                self.expressionList()


            self.state = 88
            self.match(ev_parse.PAREN_RIGHT)
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

        def IDENTIFIER(self):
            return self.getToken(ev_parse.IDENTIFIER, 0)

        def COLON(self):
            return self.getToken(ev_parse.COLON, 0)

        def EOL(self):
            return self.getToken(ev_parse.EOL, 0)

        def getRuleIndex(self):
            return ev_parse.RULE_label

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLabel" ):
                listener.enterLabel(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLabel" ):
                listener.exitLabel(self)




    def label(self):

        localctx = ev_parse.LabelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_label)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
            self.match(ev_parse.IDENTIFIER)
            self.state = 91
            self.match(ev_parse.COLON)
            self.state = 93
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ev_parse.EOL:
                self.state = 92
                self.match(ev_parse.EOL)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING_LIT(self):
            return self.getToken(ev_parse.STRING_LIT, 0)

        def DECIMAL_INT_LIT(self):
            return self.getToken(ev_parse.DECIMAL_INT_LIT, 0)

        def HEX_INT_LIT(self):
            return self.getToken(ev_parse.HEX_INT_LIT, 0)

        def BIN_INT_LIT(self):
            return self.getToken(ev_parse.BIN_INT_LIT, 0)

        def DECIMAL_FLOAT_LIT(self):
            return self.getToken(ev_parse.DECIMAL_FLOAT_LIT, 0)

        def getRuleIndex(self):
            return ev_parse.RULE_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteral" ):
                listener.enterLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteral" ):
                listener.exitLiteral(self)




    def literal(self):

        localctx = ev_parse.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ev_parse.STRING_LIT) | (1 << ev_parse.HEX_INT_LIT) | (1 << ev_parse.BIN_INT_LIT) | (1 << ev_parse.DECIMAL_INT_LIT) | (1 << ev_parse.DECIMAL_FLOAT_LIT))) != 0)):
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



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[3] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 1)
         




