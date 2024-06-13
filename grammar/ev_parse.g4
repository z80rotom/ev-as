parser grammar ev_parse;

options {
    tokenVocab = ev_lex;
}

program: EOL* statementList EOL* EOF;
statementList: statement (EOL statement)* |;
statement:
    expression         # ExpressionStatement
    | label expression # LabeledStatement;
expression:
    operand                # OperandExpression
    | unary                # UnaryExpression
    | expression arguments # CallExpression;
unary: operand # OperandUnary | OPERATOR unary # OperatorUnary;
operand:
    IDENTIFIER # IdentifierOperand
    | literal  # LiteralOperand;
expressionList: expression (COMMA expression)* |;
arguments: PAREN_LEFT expressionList? PAREN_RIGHT;
label: IDENTIFIER COLON EOL?;
literal:
    STRING_LIT
    | DECIMAL_INT_LIT
    | HEX_INT_LIT
    | BIN_INT_LIT
    | DECIMAL_FLOAT_LIT;