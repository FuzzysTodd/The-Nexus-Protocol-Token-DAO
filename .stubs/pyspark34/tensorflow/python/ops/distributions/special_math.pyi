__all__ = ['erfinv', 'ndtr', 'ndtri', 'log_ndtr', 'log_cdf_laplace']

def ndtr(x, name: str = 'ndtr'):
    '''Normal distribution function.

  Returns the area under the Gaussian probability density function, integrated
  from minus infinity to x:

  ```
                    1       / x
     ndtr(x)  = ----------  |    exp(-0.5 t**2) dt
                sqrt(2 pi)  /-inf

              = 0.5 (1 + erf(x / sqrt(2)))
              = 0.5 erfc(x / sqrt(2))
  ```

  Args:
    x: `Tensor` of type `float32`, `float64`.
    name: Python string. A name for the operation (default="ndtr").

  Returns:
    ndtr: `Tensor` with `dtype=x.dtype`.

  Raises:
    TypeError: if `x` is not floating-type.
  '''
def ndtri(p, name: str = 'ndtri'):
    '''The inverse of the CDF of the Normal distribution function.

  Returns x such that the area under the pdf from minus infinity to x is equal
  to p.

  A piece-wise rational approximation is done for the function.
  This is a port of the implementation in netlib.

  Args:
    p: `Tensor` of type `float32`, `float64`.
    name: Python string. A name for the operation (default="ndtri").

  Returns:
    x: `Tensor` with `dtype=p.dtype`.

  Raises:
    TypeError: if `p` is not floating-type.
  '''
def log_ndtr(x, series_order: int = 3, name: str = 'log_ndtr'):
    '''Log Normal distribution function.

  For details of the Normal distribution function see `ndtr`.

  This function calculates `(log o ndtr)(x)` by either calling `log(ndtr(x))` or
  using an asymptotic series. Specifically:
  - For `x > upper_segment`, use the approximation `-ndtr(-x)` based on
    `log(1-x) ~= -x, x << 1`.
  - For `lower_segment < x <= upper_segment`, use the existing `ndtr` technique
    and take a log.
  - For `x <= lower_segment`, we use the series approximation of erf to compute
    the log CDF directly.

  The `lower_segment` is set based on the precision of the input:

  ```
  lower_segment = { -20,  x.dtype=float64
                  { -10,  x.dtype=float32
  upper_segment = {   8,  x.dtype=float64
                  {   5,  x.dtype=float32
  ```

  When `x < lower_segment`, the `ndtr` asymptotic series approximation is:

  ```
     ndtr(x) = scale * (1 + sum) + R_N
     scale   = exp(-0.5 x**2) / (-x sqrt(2 pi))
     sum     = Sum{(-1)^n (2n-1)!! / (x**2)^n, n=1:N}
     R_N     = O(exp(-0.5 x**2) (2N+1)!! / |x|^{2N+3})
  ```

  where `(2n-1)!! = (2n-1) (2n-3) (2n-5) ...  (3) (1)` is a
  [double-factorial](https://en.wikipedia.org/wiki/Double_factorial).


  Args:
    x: `Tensor` of type `float32`, `float64`.
    series_order: Positive Python `integer`. Maximum depth to
      evaluate the asymptotic expansion. This is the `N` above.
    name: Python string. A name for the operation (default="log_ndtr").

  Returns:
    log_ndtr: `Tensor` with `dtype=x.dtype`.

  Raises:
    TypeError: if `x.dtype` is not handled.
    TypeError: if `series_order` is a not Python `integer.`
    ValueError:  if `series_order` is not in `[0, 30]`.
  '''
def erfinv(x, name: str = 'erfinv'):
    '''The inverse function for erf, the error function.

  Args:
    x: `Tensor` of type `float32`, `float64`.
    name: Python string. A name for the operation (default="erfinv").

  Returns:
    x: `Tensor` with `dtype=x.dtype`.

  Raises:
    TypeError: if `x` is not floating-type.
  '''
def log_cdf_laplace(x, name: str = 'log_cdf_laplace'):
    '''Log Laplace distribution function.

  This function calculates `Log[L(x)]`, where `L(x)` is the cumulative
  distribution function of the Laplace distribution, i.e.

  ```L(x) := 0.5 * int_{-infty}^x e^{-|t|} dt```

  For numerical accuracy, `L(x)` is computed in different ways depending on `x`,

  ```
  x <= 0:
    Log[L(x)] = Log[0.5] + x, which is exact

  0 < x:
    Log[L(x)] = Log[1 - 0.5 * e^{-x}], which is exact
  ```

  Args:
    x: `Tensor` of type `float32`, `float64`.
    name: Python string. A name for the operation (default="log_ndtr").

  Returns:
    `Tensor` with `dtype=x.dtype`.

  Raises:
    TypeError: if `x.dtype` is not handled.
  '''
