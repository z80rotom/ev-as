from pytest import raises, mark
from evlang.partial import snake, partial
from evlang.ast import Literal, SourceInfo


@mark.parametrize(
    ("stack", "f", "expected"),
    [
        (
            partial(Literal),
            lambda lit: lit(SourceInfo(0, 0))(Literal.Kind.STRING)("foo"),
            Literal(SourceInfo(0, 0), Literal.Kind.STRING, "foo"),
        ),
        (
            partial(Literal),
            lambda lit: lit(text="foo")(srcinfo=SourceInfo(0, 0))(
                kind=Literal.Kind.STRING
            ),
            Literal(SourceInfo(0, 0), Literal.Kind.STRING, "foo"),
        ),
        (
            partial(Literal),
            lambda lit: lit(text="foo")(text="foo")(srcinfo=SourceInfo(0, 0))(
                kind=Literal.Kind.STRING
            ),
            Literal(SourceInfo(0, 0), Literal.Kind.STRING, "foo"),
        ),
        (snake(int, 3), lambda snek: snek(1)(2)(3), [1, 2, 3]),
    ],
)
def test_stacks(stack, f, expected):
    with raises(StopIteration):
        f(stack)
    assert expected == stack()


@mark.parametrize(
    ("stack", "f", "ecls"),
    [
        (
            partial(Literal),
            lambda lit: lit(SourceInfo(0, 0))(kind=Literal.Kind.STRING)("foo"),
            TypeError,
        ),
        (
            partial(Literal),
            lambda lit: lit(),
            TypeError,
        ),
        (snake(int, capacity=3), lambda snek: snek(1)(), TypeError),
    ],
)
def test_stacks_raises(stack, f, ecls):
    with raises(ecls):
        f(stack)
