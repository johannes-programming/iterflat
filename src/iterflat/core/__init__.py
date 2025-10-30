import operator
from typing import *

__all__ = ["iterflat"]


def iterflat(data: Any, *, depth: SupportsIndex = 1) -> Generator[Any, None, None]:
    n: int
    ans: Iterable
    n = operator.index(depth)
    if n < -1:
        yield iterflat(data, depth=n + 1)
        return
    if n == -1:
        yield data
        return
    ans = data
    while n > 0:
        ans = (item for sub in ans for item in sub)
        n -= 1
    yield from ans
