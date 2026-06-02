# Generated from grammar/ev_parse.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ev_parse import ev_parse
else:
    from ev_parse import ev_parse

# This class defines a complete listener for a parse tree produced by ev_parse.
class ev_parseListener(ParseTreeListener):

    # Enter a parse tree produced by ev_parse#program.
    def enterProgram(self, ctx:ev_parse.ProgramContext):
        pass

    # Exit a parse tree produced by ev_parse#program.
    def exitProgram(self, ctx:ev_parse.ProgramContext):
        pass


    # Enter a parse tree produced by ev_parse#statementList.
    def enterStatementList(self, ctx:ev_parse.StatementListContext):
        pass

    # Exit a parse tree produced by ev_parse#statementList.
    def exitStatementList(self, ctx:ev_parse.StatementListContext):
        pass


    # Enter a parse tree produced by ev_parse#ExpressionStatement.
    def enterExpressionStatement(self, ctx:ev_parse.ExpressionStatementContext):
        pass

    # Exit a parse tree produced by ev_parse#ExpressionStatement.
    def exitExpressionStatement(self, ctx:ev_parse.ExpressionStatementContext):
        pass


    # Enter a parse tree produced by ev_parse#LabeledStatement.
    def enterLabeledStatement(self, ctx:ev_parse.LabeledStatementContext):
        pass

    # Exit a parse tree produced by ev_parse#LabeledStatement.
    def exitLabeledStatement(self, ctx:ev_parse.LabeledStatementContext):
        pass


    # Enter a parse tree produced by ev_parse#UnaryExpression.
    def enterUnaryExpression(self, ctx:ev_parse.UnaryExpressionContext):
        pass

    # Exit a parse tree produced by ev_parse#UnaryExpression.
    def exitUnaryExpression(self, ctx:ev_parse.UnaryExpressionContext):
        pass


    # Enter a parse tree produced by ev_parse#CallExpression.
    def enterCallExpression(self, ctx:ev_parse.CallExpressionContext):
        pass

    # Exit a parse tree produced by ev_parse#CallExpression.
    def exitCallExpression(self, ctx:ev_parse.CallExpressionContext):
        pass


    # Enter a parse tree produced by ev_parse#OperandExpression.
    def enterOperandExpression(self, ctx:ev_parse.OperandExpressionContext):
        pass

    # Exit a parse tree produced by ev_parse#OperandExpression.
    def exitOperandExpression(self, ctx:ev_parse.OperandExpressionContext):
        pass


    # Enter a parse tree produced by ev_parse#OperandUnary.
    def enterOperandUnary(self, ctx:ev_parse.OperandUnaryContext):
        pass

    # Exit a parse tree produced by ev_parse#OperandUnary.
    def exitOperandUnary(self, ctx:ev_parse.OperandUnaryContext):
        pass


    # Enter a parse tree produced by ev_parse#OperatorUnary.
    def enterOperatorUnary(self, ctx:ev_parse.OperatorUnaryContext):
        pass

    # Exit a parse tree produced by ev_parse#OperatorUnary.
    def exitOperatorUnary(self, ctx:ev_parse.OperatorUnaryContext):
        pass


    # Enter a parse tree produced by ev_parse#IdentifierOperand.
    def enterIdentifierOperand(self, ctx:ev_parse.IdentifierOperandContext):
        pass

    # Exit a parse tree produced by ev_parse#IdentifierOperand.
    def exitIdentifierOperand(self, ctx:ev_parse.IdentifierOperandContext):
        pass


    # Enter a parse tree produced by ev_parse#LiteralOperand.
    def enterLiteralOperand(self, ctx:ev_parse.LiteralOperandContext):
        pass

    # Exit a parse tree produced by ev_parse#LiteralOperand.
    def exitLiteralOperand(self, ctx:ev_parse.LiteralOperandContext):
        pass


    # Enter a parse tree produced by ev_parse#expressionList.
    def enterExpressionList(self, ctx:ev_parse.ExpressionListContext):
        pass

    # Exit a parse tree produced by ev_parse#expressionList.
    def exitExpressionList(self, ctx:ev_parse.ExpressionListContext):
        pass


    # Enter a parse tree produced by ev_parse#arguments.
    def enterArguments(self, ctx:ev_parse.ArgumentsContext):
        pass

    # Exit a parse tree produced by ev_parse#arguments.
    def exitArguments(self, ctx:ev_parse.ArgumentsContext):
        pass


    # Enter a parse tree produced by ev_parse#label.
    def enterLabel(self, ctx:ev_parse.LabelContext):
        pass

    # Exit a parse tree produced by ev_parse#label.
    def exitLabel(self, ctx:ev_parse.LabelContext):
        pass


    # Enter a parse tree produced by ev_parse#literal.
    def enterLiteral(self, ctx:ev_parse.LiteralContext):
        pass

    # Exit a parse tree produced by ev_parse#literal.
    def exitLiteral(self, ctx:ev_parse.LiteralContext):
        pass



del ev_parse