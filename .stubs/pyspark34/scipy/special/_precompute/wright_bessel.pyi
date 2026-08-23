from scipy.integrate import quad as quad
from scipy.optimize import curve_fit as curve_fit, minimize_scalar as minimize_scalar

def series_small_a():
    """Tylor series expansion of Phi(a, b, x) in a=0 up to order 5.
    """
def dg_series(z, n):
    """Symbolic expansion of digamma(z) in z=0 to order n.

    See https://dlmf.nist.gov/5.7.E4 and with https://dlmf.nist.gov/5.5.E2
    """
def pg_series(k, z, n):
    """Symbolic expansion of polygamma(k, z) in z=0 to order n."""
def series_small_a_small_b():
    """Tylor series expansion of Phi(a, b, x) in a=0 and b=0 up to order 5.

    Be aware of cancellation of poles in b=0 of digamma(b)/Gamma(b) and
    polygamma functions.

    digamma(b)/Gamma(b) = -1 - 2*M_EG*b + O(b^2)
    digamma(b)^2/Gamma(b) = 1/b + 3*M_EG + b*(-5/12*PI^2+7/2*M_EG^2) + O(b^2)
    polygamma(1, b)/Gamma(b) = 1/b + M_EG + b*(1/12*PI^2 + 1/2*M_EG^2) + O(b^2)
    and so on.
    """
def asymptotic_series():
    """Asymptotic expansion for large x.

    Phi(a, b, x) ~ Z^(1/2-b) * exp((1+a)/a * Z) * sum_k (-1)^k * C_k / Z^k
    Z = (a*x)^(1/(1+a))

    Wright (1935) lists the coefficients C_0 and C_1 (he calls them a_0 and
    a_1). With slightly different notation, Paris (2017) lists coefficients
    c_k up to order k=3.
    Paris (2017) uses ZP = (1+a)/a * Z  (ZP = Z of Paris) and
    C_k = C_0 * (-a/(1+a))^k * c_k
    """
def optimal_epsilon_integral():
    """Fit optimal choice of epsilon for integral representation.

    The integrand of
        int_0^pi P(eps, a, b, x, phi) * dphi
    can exhibit oscillatory behaviour. It stems from the cosine of P and can be
    minimized by minimizing the arc length of the argument
        f(phi) = eps * sin(phi) - x * eps^(-a) * sin(a * phi) + (1 - b) * phi
    of cos(f(phi)).
    We minimize the arc length in eps for a grid of values (a, b, x) and fit a
    parametric function to it.
    """
def main(): ...
