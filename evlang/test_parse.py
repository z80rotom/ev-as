from evlang.ast import (
    Call,
    LabeledStatement,
    Literal,
    Operator,
    Program,
    SourceInfo,
    Unary,
)
from evlang.parse import parse
import orjson
from pytest import mark, fixture
from pytest_mock import MockerFixture

SI = SourceInfo(0, 0)


@fixture
def mock_sourceinfo(mocker: MockerFixture):
    mocker.patch("evlang.parse.Listener.getsrcinfo", return_value=SI)
    return mocker


@mark.parametrize(
    ("src", "expected"),
    [
        (
            "hello: world()",
            Program(
                SI,
                [
                    LabeledStatement(
                        SI,
                        "hello",
                        Call(
                            SI,
                            Literal.Identifier(SI, "world"),
                            [],
                        ),
                    )
                ],
            ),
        ),
        (
            """
            world(bar(), foo())()
            """,
            Program(
                SI,
                [
                    Call(
                        SI,
                        Call(
                            SI,
                            Literal.Identifier(SI, "world"),
                            [
                                Call(SI, Literal.Identifier(SI, "bar"), []),
                                Call(SI, Literal.Identifier(SI, "foo"), []),
                            ],
                        ),
                        [],
                    ),
                ],
            ),
        ),
        (
            """
            0x100001
            0b0001
            -2.999e-100
            +1234
            -0xFFF
            """,
            Program(
                SI,
                [
                    Literal.HexInt(SI, "0x100001"),
                    Literal.BinInt(SI, "0b0001"),
                    Unary(
                        SI, Operator(SI, "-"), Literal.DecimalFloat(SI, "2.999e-100")
                    ),
                    Unary(SI, Operator(SI, "+"), Literal.DecimalInt(SI, "1234")),
                    Unary(SI, Operator(SI, "-"), Literal.HexInt(SI, "0xFFF")),
                ],
            ),
        ),
        (
            """
            ev_z80r0101_obj00:
                _TALKMSG('dp_scenario2%00-some-locale-label') 
                _END()
            ev_z80r0101_obj01:
                _GET_POKETCH()
                _ADD_POKEMON(181, 50, 0, @247) 
            """,
            Program(
                SI,
                [
                    LabeledStatement(
                        SI,
                        "ev_z80r0101_obj00",
                        Call(
                            SI,
                            Literal.Identifier(
                                SI,
                                "_TALKMSG",
                            ),
                            [Literal.String(SI, "'dp_scenario2%00-some-locale-label'")],
                        ),
                    ),
                    Call(
                        SI,
                        Literal.Identifier(SI, "_END"),
                        [],
                    ),
                    LabeledStatement(
                        SI,
                        "ev_z80r0101_obj01",
                        Call(
                            SI,
                            Literal.Identifier(
                                SI,
                                "_GET_POKETCH",
                            ),
                            [],
                        ),
                    ),
                    Call(
                        SI,
                        Literal.Identifier(SI, "_ADD_POKEMON"),
                        [
                            Literal.DecimalInt(SI, "181"),
                            Literal.DecimalInt(SI, "50"),
                            Literal.DecimalInt(SI, "0"),
                            Unary(
                                SI,
                                Operator(SI, "@"),
                                Literal.DecimalInt(SI, "247"),
                            ),
                        ],
                    ),
                ],
            ),
        ),
    ],
)
def test_parse(mock_sourceinfo, src: str, expected: Program):
    program = parse(src)
    assert expected == program
