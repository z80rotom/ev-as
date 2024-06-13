from __future__ import annotations
from typing import Callable, Generic, List, Type, TypeVar, overload
from inspect import Signature

F = TypeVar("F", bound=Callable)
T = TypeVar("T")


class partial(Generic[F]):
    def __init__(self, func: F, eager: bool = True, callcount: int | None = None):
        self._sig = Signature.from_callable(func)
        self._binding = self._sig.bind_partial()
        self._emptycall = False
        self._kwonly = False
        self._func = func
        self._eager = eager
        self._callcount = callcount
        self._calls = 0

    @overload
    def __call__(self: partial[Callable[..., T]]) -> T:
        pass

    @overload
    def __call__(
        self: partial[Callable[..., T]], *args, **kwargs
    ) -> T | partial[Callable[..., T]] | None:
        pass

    def __call__(
        self: partial[Callable[..., T]], *args, **kwargs
    ) -> T | partial[Callable[..., T]] | None:
        if args and self._kwonly:
            raise TypeError("positional argument following keyword argument")
        if kwargs:
            self._kwonly = True
        if not args and not kwargs:
            if self._callcount is not None and self._calls < self._callcount:
                raise TypeError("empty call before call count reached")
            if self._emptycall:
                raise TypeError("more than one empty call")
            self._emptycall = True
            binding = self._sig.bind(*self._binding.args, **self._binding.kwargs)
            return self._func(*binding.args, **binding.kwargs)
        if self._emptycall:
            raise TypeError("cannot apply arguments after empty call")
        if self._callcount is not None and self._calls == self._callcount:
            raise TypeError("cannot apply arguments after empty call")
        self._calls += 1
        partial_binding = self._sig.bind_partial(
            *(self._binding.args + args), **({} | self._binding.kwargs | kwargs)
        )
        try:
            binding = self._sig.bind(
                *(self._binding.args + args), **({} | self._binding.kwargs | kwargs)
            )
        except TypeError:
            self._binding = partial_binding
        else:
            self._binding = binding
            if self._eager:
                raise StopIteration()
        if self._callcount is not None and self._calls == self._callcount:
            raise StopIteration()
        return self


E = TypeVar("E")


def snake(_: Type[E], capacity=None) -> partial[Callable[..., List[E]]]:
    def args(*args: E) -> List[E]:
        return list(args)

    return partial(args, eager=False, callcount=capacity)


s = snake(int)
s1 = s(1)
s1 = s()
