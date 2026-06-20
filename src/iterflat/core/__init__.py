import operator
from collections.abc import Generator, Iterable
from typing import Any, SupportsIndex

__all__ = ["iterflat"]


def iterflat(
    data: Any, *, depth: SupportsIndex = 1
) -> Generator[Any, None, None]:
    n: int
    x: Iterable[Any]
    n = operator.index(depth)
    if n < -1:
        yield iterflat(data, depth=n + 1)
        return
    if n == -1:
        yield data
        return
    if n == 0:
        yield from data
        return
    for x in data:
        yield from iterflat(x, depth=n - 1)
