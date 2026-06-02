from __future__ import annotations
from dataclasses import dataclass
from enum import Enum
from typing import (
    List,
)


@dataclass
class SourceInfo:
    startpos: int
    endpos: int


@dataclass
class Literal:
    class Kind(Enum):
        STRING = "string"
        DECIMAL_INT = "decimal_int"
        HEX_INT = "hex_int"
        BIN_INT = "bin_int"
        DECIMAL_FLOAT = "decimal_float"
        IDENTIFIER = "identifier"

    srcinfo: SourceInfo
    kind: Kind
    text: str

    def is_int(self) -> bool:
        return self.kind in (
            Literal.Kind.DECIMAL_INT,
            Literal.Kind.HEX_INT,
            Literal.Kind.BIN_INT,
        )

    @staticmethod
    def String(srcinfo: SourceInfo, text: str) -> Literal:
        return Literal(srcinfo, Literal.Kind.STRING, text)

    @staticmethod
    def DecimalInt(srcinfo: SourceInfo, text: str) -> Literal:
        return Literal(srcinfo, Literal.Kind.DECIMAL_INT, text)

    @staticmethod
    def HexInt(srcinfo: SourceInfo, text: str) -> Literal:
        return Literal(srcinfo, Literal.Kind.HEX_INT, text)

    @staticmethod
    def BinInt(srcinfo: SourceInfo, text: str) -> Literal:
        return Literal(srcinfo, Literal.Kind.BIN_INT, text)

    @staticmethod
    def DecimalFloat(srcinfo: SourceInfo, text: str) -> Literal:
        return Literal(srcinfo, Literal.Kind.DECIMAL_FLOAT, text)

    @staticmethod
    def Identifier(srcinfo: SourceInfo, text: str) -> Literal:
        return Literal(srcinfo, Literal.Kind.IDENTIFIER, text)


@dataclass
class Operator:
    srcinfo: SourceInfo
    text: str


@dataclass
class Unary:
    srcinfo: SourceInfo
    operator: Operator
    operand: Operand


Operand = Literal | Unary


@dataclass
class Call:
    srcinfo: SourceInfo
    expression: Expression
    arguments: List[Expression]


@dataclass
class LabeledStatement:
    srcinfo: SourceInfo
    label: str
    statement: SimpleStatement


Expression = Operand | Unary | Call
SimpleStatement = Expression
Statement = SimpleStatement | LabeledStatement


@dataclass
class Program:
    srcinfo: SourceInfo
    statements: List[Statement]
