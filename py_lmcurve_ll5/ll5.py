import math
from dataclasses import dataclass
from typing import Optional, Callable
from functools import partial
from .lmcurve_ll5 import lmcurve_ll5 as c_lmcurve_ll5

def ll5(conc : float, b : float, c : float, d : float, e : float, f: float) -> float:
    return c + (d - c) / (1 + (conc / e) ** b) ** f

@dataclass
class LL5Params:
    b: Optional[float]
    c: Optional[float]
    d: Optional[float]
    e: Optional[float]
    f: Optional[float]

def fix_ll5(params: LL5Params) -> Callable:
    return partial(ll5, b=params.b, c=params.c, d=params.d, e=params.e, f=params.f)
    


def lmcurve_ll5(x, y, b=None, c=None, d=None, e=None, f=None) -> LL5Params:
    """
    Wrapper around the C function 'lmcurve_ll5' for curve fitting.

    Args:
        x (list or np.ndarray): Independent variable values.
        y (list or np.ndarray): Dependent variable values.
        b, c, d, e, f (Optional[float]): Fixing for parameters.

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
    result = c_lmcurve_ll5(x, y, b_val, c_val, d_val, e_val, f_val)

    if b is not None and result[0] != b:
        raise ValueError("Fitted parameter 'b' does not match the provided fixed value")
    if c is not None and result[1] != c:
        raise ValueError("Fitted parameter 'c' does not match the provided fixed value")
    if d is not None and result[2] != d:
        raise ValueError("Fitted parameter 'd' does not match the provided fixed value")
    if e is not None and result[3] != e:
        raise ValueError("Fitted parameter 'e' does not match the provided fixed value")
    if f is not None and result[4] != f:
        raise ValueError("Fitted parameter 'f' does not match the provided fixed value")
    
    # Convert back to Python types and check for NaN to return None
    return LL5Params(
        None if math.isnan(result[0]) else result[0],
        None if math.isnan(result[1]) else result[1],
        None if math.isnan(result[2]) else result[2],
        None if math.isnan(result[3]) else result[3],
        None if math.isnan(result[4]) else result[4],
    )
