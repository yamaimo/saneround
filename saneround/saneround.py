import builtins # for insane round
from typing import Union

Numeric = Union[int, float]

def round(number: Numeric, ndigits: int = 0) -> float:
    # FIXME: insane round...
    return builtins.round(number, ndigits)
