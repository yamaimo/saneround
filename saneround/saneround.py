import math
import sys
from decimal import ROUND_HALF_UP, Decimal
from typing import Union

Numeric = Union[int, float]


def round(number: Numeric, ndigits: int = 0) -> float:
    if (number == 0.0) or math.isinf(number) or math.isnan(number):
        return number

    _, num_binexp = math.frexp(number)
    if __will_overflow(num_binexp, ndigits):
        return number
    if __will_underflow(num_binexp, ndigits):
        return 0.0

    if abs(ndigits) > sys.float_info.dig:
        return __decimal_round(number, ndigits)

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


def __will_overflow(num_binexp: int, ndigits: int) -> bool:
    num_exp = num_binexp / 3.322259  # log_2(10) = 3.322259
    return (num_exp + ndigits) >= sys.float_info.dig


def __will_underflow(num_binexp: int, ndigits: int) -> bool:
    num_exp = num_binexp / 3.322259  # log_2(10) = 3.322259
    return (num_exp + ndigits) < 0


def __decimal_round(number: Numeric, ndigits: int) -> float:
    decimal = Decimal(str(number))
    exp_decimal = Decimal(f"1e{-ndigits}")
    rounded = decimal.quantize(exp_decimal, rounding=ROUND_HALF_UP)
    return float(rounded)
