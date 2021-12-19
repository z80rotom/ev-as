lexer grammar ev_lex;

channels {
    COMMENTS
}

IDENTIFIER: '_'? [a-zA-Z] [_a-zA-Z0-9]*;

STRING_LIT: '\u0027' ~'\u0027'* '\u0027';

HEX_INT_LIT: '0x' [0-9a-fA-F]+;
BIN_INT_LIT: '0b' [01]+;
DECIMAL_INT_LIT: [0-9]+ DECIMAL_EXPONENT?;
DECIMAL_EXPONENT: [eE] [0-9]+;

DECIMAL_FLOAT_LIT: [0-9]+ '.' [0-9]* (DECIMAL_FLOAT_EXPONENT)?;
DECIMAL_FLOAT_EXPONENT: [eE] [+-]? [0-9]+;

OPERATOR: PLUS | MINUS | AT | HASHTAG | DOLLAR | EXCLAM;

COLON: ':';
COMMA: ',';
PAREN_LEFT: '(';
PAREN_RIGHT: ')';
EOL: [\r\n]+;
WS: [ \t] -> skip;
PLUS: '+';
MINUS: '-';
AT: '@';
HASHTAG: '#';
DOLLAR: '$';
EXCLAM: '!';