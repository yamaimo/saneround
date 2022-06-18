import math
from typing import Union

Numeric = Union[int, float]

def round(number: Numeric, ndigits: int = 0) -> float:
    if number in [math.inf, -math.inf, math.nan, 0.0]:
        return number

    shift_amount = math.pow(10, ndigits)

    if number > 0:
        shifted = math.floor(number * shift_amount)
        bound = (shifted + 0.5) / shift_amount
        if number >= bound:
            shifted += 1
    else:
        shifted = math.ceil(number * shift_amount)
        bound = (shifted - 0.5) / shift_amount
        if number <= bound:
            shifted -= 1

    return shifted / shift_amount
