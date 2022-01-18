from __future__ import annotations

import antlr4
from antlr4.tree.Tree import INVALID_INTERVAL

from evlang.antlr.ev_lex import ev_lex
from evlang.antlr.ev_parse import ev_parse
from evlang.antlr.ev_parseListener import ev_parseListener
from evlang.partial import partial, snake
from evlang.ast import (
    Call,
    Expression,
    LabeledStatement,
    Literal,
    Operator,
    Program,
    SourceInfo,
    Statement,
    Unary,
)


class Listener(ev_parseListener):
    def __init__(self):
        self.partial_program = partial(Program)
        self.stack = [self.partial_program]

    def getsrcinfo(self, ctx):
        interval = ctx.getSourceInterval()
        if interval is INVALID_INTERVAL:
            return None
        return SourceInfo(startpos=interval[0], endpos=interval[1])

    def push(self, args):
        self.stack.append(args)

    def call(self, *args, **kwargs):
        i = 0
        while self.stack and args or len(self.stack) >= 2 and i == 0:
            try:
                ret = self.stack[-1](*args, **kwargs)
            except StopIteration:
                if len(self.stack) == 1:
                    return
                ret = self.stack[-1]()
            else:
                if (
                    i != 0
                    or ret == self.stack[-1]
                    or ret == None
                    or len(self.stack) == 1
                ):
                    return
            self.stack.pop()
            args, kwargs = (ret,), {}
            i += 1

    def enterProgram(self, ctx: ev_parse.ProgramContext):
        self.call(self.getsrcinfo(ctx))

    def enterStatementList(self, _):
        self.push(snake(Statement))

    def exitStatementList(self, _):
        self.call()

    def enterLabeledStatement(self, ctx: ev_parse.LabeledStatementContext):
        self.push(
            partial(LabeledStatement)(
                self.getsrcinfo(ctx),
                ctx.label().IDENTIFIER().getText(),
            )
        )

    def enterOperatorUnary(self, ctx: ev_parse.OperatorUnaryContext):
        self.push(
            partial(Unary)(
                self.getsrcinfo(ctx),
                Operator(
                    self.getsrcinfo(ctx.OPERATOR()),
                    ctx.OPERATOR().getText(),
                ),
            )
        )

    def enterExpressionList(self, _):
        self.push(snake(Expression))

    def exitExpressionList(self, _):
        self.call()

    def enterCallExpression(self, ctx: ev_parse.CallExpressionContext):
        self.push(partial(Call)(self.getsrcinfo(ctx)))

    def enterIdentifierOperand(self, ctx: ev_parse.IdentifierOperandContext):
        self.call(Literal.Identifier(self.getsrcinfo(ctx), ctx.IDENTIFIER().getText()))

    def enterLiteral(self, ctx: ev_parse.LiteralContext):
        self.call(
            {
                ev_parse.STRING_LIT: Literal.String,
                ev_parse.DECIMAL_INT_LIT: Literal.DecimalInt,
                ev_parse.HEX_INT_LIT: Literal.HexInt,
                ev_parse.BIN_INT_LIT: Literal.BinInt,
                ev_parse.DECIMAL_FLOAT_LIT: Literal.DecimalFloat,
            }[ctx.children[0].symbol.type](
                self.getsrcinfo(ctx),
                ctx.children[0].getText(),
            )
        )


def parse(src: str):
    input_stream = antlr4.InputStream(src)
    lexer = ev_lex(input_stream)
    stream = antlr4.CommonTokenStream(lexer)
    parser = ev_parse(stream)
    tree = parser.program()
    listener = Listener()
    walker = antlr4.ParseTreeWalker()
    walker.walk(listener, tree)
    return listener.partial_program()
