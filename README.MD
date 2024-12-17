# Python Wrapper for Levenberg-Marquardt (lmmin)

A Python wrapper for the **Generic Levenberg-Marquardt routine (lmmin)**, providing fast curve fitting via a compiled C library.

## Installation

Install using pip:
```bash
pip install .
```


Usage Example
```python
from py_lmcurve_ll5.ll5 import lmcurve_ll5, LL5Params

result : LL5Params = lmcurve_ll5([1, 2, 3], [1, 2, 3], b=1, c=2, d=3, e=4, f=5)
print(result)
```