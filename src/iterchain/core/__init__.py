import operator
from typing import *

__all__ = ["iterchain"]


def iterchain(data: Any, *, depth: SupportsIndex = 1) -> Generator[Any, None, None]:
    n: int
    x: Iterable
    n = operator.index(depth)
    if n < -1:
        yield iterchain(data, depth=n + 1)
        return
    if n == -1:
        yield data
        return
    if n == 0:
        yield from data
        return
    for x in data:
        yield from iterchain(x, depth=n - 1)
