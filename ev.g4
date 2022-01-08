/*
BSD License

Copyright (c) 2018, Tom Everett
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions
are met:

1. Redistributions of source code must retain the above copyright
   notice, this list of conditions and the following disclaimer.
2. Redistributions in binary form must reproduce the above copyright
   notice, this list of conditions and the following disclaimer in the
   documentation and/or other materials provided with the distribution.
3. Neither the name of Tom Everett nor the names of its contributors
   may be used to endorse or promote products derived from this software
   without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
"AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
*/
/*
* http://fms.komkon.org/comp/CPUs/z80.txt
*/

// EvScript is a modified version of Tom Everett's grammar for Z80 assembler

grammar ev;

prog
   : (line? EOL)+ line
   ;

line
   : lbl? (instruction)? comment?
   ;

instruction
   : name expressionlist
   ;

lbl
   : name ':'
   ;

expressionlist
   : '(' (argument (',' argument)*)? ')'
   ;

argument
   : number
   | work
   | flag
   | sysFlag
   | string_
   ;

string_
   : STRING
   ;

work
   : '@' (name | number)
   ;

flag
   : '#' (name | number)
   ;

sysFlag
   : '$' (name | number)
   ;

name
  : NAME
  ;

number
   : NUMBER
   ;

comment
   : COMMENT
   ;

NAME
   : ('_' | [a-zA-Z]) ('_' | [a-zA-Z0-9])+ 
   ;

NUMBER
   : '-'? DIGIT+ ( '.' DIGIT+ )?
   ;

COMMENT
   : ';' ~ [\r\n]* -> skip
   ;


STRING
   : '\u0027' ~'\u0027'* '\u0027'
   ;


EOL
   : [\r\n] +
   ;


WS
   : [ \t] -> skip
   ;

fragment DIGIT: [0-9] ;

fragment PERIOD
   : '.'
   ;

// Fragments
fragment A
   : ('a' | 'A')
   ;


fragment B
   : ('b' | 'B')
   ;


fragment C
   : ('c' | 'C')
   ;


fragment D
   : ('d' | 'D')
   ;


fragment E
   : ('e' | 'E')
   ;


fragment F
   : ('f' | 'F')
   ;


fragment G
   : ('g' | 'G')
   ;


fragment H
   : ('h' | 'H')
   ;


fragment I
   : ('i' | 'I')
   ;


fragment J
   : ('j' | 'J')
   ;


fragment K
   : ('k' | 'K')
   ;


fragment L
   : ('l' | 'L')
   ;


fragment M
   : ('m' | 'M')
   ;


fragment N
   : ('n' | 'N')
   ;


fragment O
   : ('o' | 'O')
   ;


fragment P
   : ('p' | 'P')
   ;


fragment Q
   : ('q' | 'Q')
   ;


fragment R
   : ('r' | 'R')
   ;


fragment S
   : ('s' | 'S')
   ;


fragment T
   : ('t' | 'T')
   ;


fragment U
   : ('u' | 'U')
   ;


fragment V
   : ('v' | 'V')
   ;


fragment W
   : ('w' | 'W')
   ;


fragment X
   : ('x' | 'X')
   ;


fragment Y
   : ('y' | 'Y')
   ;


fragment Z
   : ('z' | 'Z')
   ;

fragment UBAR
    : ('_')
    ;

fragment ZERO
    : ('0')
    ;

fragment ONE
    : ('1')
    ;

fragment TWO
    : ('2')
    ;

fragment THREE
    : ('3')
    ;

fragment FOUR
    : ('4')
    ;

fragment FIVE
    : ('5')
    ;

fragment SIX
    : ('6')
    ;

fragment SEVEN
    : ('7')
    ;

fragment EIGHT
    : ('8')
    ;

fragment NINE
    : ('9')
    ;
