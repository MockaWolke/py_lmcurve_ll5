import math
from dataclasses import dataclass
from typing import Optional
from .lmcurve_ll5 import lmcurve_ll5 as c_lmcurve_ll5


@dataclass
class LL5Params:
    b: Optional[float]
    c: Optional[float]
    d: Optional[float]
    e: Optional[float]
    f: Optional[float]


def lmcurve_ll5(x, y, b=None, c=None, d=None, e=None, f=None) -> LL5Params:
    """
    Wrapper around the C function 'lmcurve_ll5' for curve fitting.

    Args:
        x (list or np.ndarray): Independent variable values.
        y (list or np.ndarray): Dependent variable values.
        b, c, d, e, f (Optional[float]): Initial guesses for parameters.
                                         Use None for unknown values.

    Returns:
        LL5Params: A dataclass with the fitted parameters.
    """
    if not isinstance(x, list) or not all([isinstance(i, float) for i in x]):
        raise ValueError("x must be a list of floats")


    if not isinstance(y, list) or not all([isinstance(i, float) for i in y]):
        raise ValueError("y must be a list of floats")

    if len(x) != len(y):
        raise ValueError("x and y must be same length")

    # Convert None to NaN for compatibility with C code
    b_val = float("nan") if b is None else b
    c_val = float("nan") if c is None else c
    d_val = float("nan") if d is None else d
    e_val = float("nan") if e is None else e
    f_val = float("nan") if f is None else f

    # Call the C extension function
    result = c_lmcurve_ll5(
        x, y, b_val, c_val, d_val, e_val, f_val
    )

    # Convert back to Python types and check for NaN to return None
    return LL5Params(
        None if math.isnan(result[0]) else result[0],
        None if math.isnan(result[1]) else result[1],
        None if math.isnan(result[2]) else result[2],
        None if math.isnan(result[3]) else result[3],
        None if math.isnan(result[4]) else result[4],
    )

