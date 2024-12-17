# LL.5 Fitting using Levenberg-Marquardt

## Overview

This package provides a Python wrapper fitting the 'LL.5' function using the **Generic Levenberg-Marquardt routine (lmmin)** C package, writte by Joachim Wuttke at Forschungszentrum Juelich GmbH, for curve fitting. The 'LL.5' function, a five-parameter log-logistic function commonly used in dose-response fits, such as in the the R package [`drc`](https://doseresponse.github.io/drc/reference/LL.5.html).

## LL5 Function

The five-parameter log-logistic function is defined as:

$$f(x) = c + \frac{d-c}{(1+\exp(b(\log(x)-\log(e))))^f}$$


## Installation

Install using pip:

Clone the repository and install:

```bash
pip install .
```

or install directly from GitHub:

```bash
pip install git+https://github.com/mockaWolke/py_lmcurve_ll5.git
```


## Usage Example
```python
from py_lmcurve_ll5.ll5 import lmcurve_ll5, LL5Params, fix_ll5

# Example data
x_data = [1, 2, 3]
y_data = [100, 95, 50]

# Perform curve fitting wit parameter d fixed to 100
params: LL5Params = lmcurve_ll5(x_data, y_data, b=None, c=None, d=100, e=None, f=None)

fitted_func = fix_ll5(params)

predictions = fitted_func(some_values)
```

`LL5Params` is a simple dataclass containing the parameters `b`, `c`, `d`, `e`, and `f`.

By setting a parameter in `lmcurve_ll5`, you freeze it, rather than just providing an initial value.


## License

This project is licensed under the FreeBSD License. See the [COPYING](COPYING) file for more details.
