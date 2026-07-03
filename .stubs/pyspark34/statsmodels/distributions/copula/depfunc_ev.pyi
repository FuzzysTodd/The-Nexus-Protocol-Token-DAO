from _typeshed import Incomplete
from statsmodels.tools.numdiff import approx_hess as approx_hess

class PickandDependence:
    def __call__(self, *args, **kwargs): ...
    def evaluate(self, t, *args) -> None: ...
    def deriv(self, t, *args):
        """First derivative of the dependence function

        implemented through numerical differentiation
        """
    def deriv2(self, t, *args):
        """Second derivative of the dependence function

        implemented through numerical differentiation
        """

class AsymLogistic(PickandDependence):
    """asymmetric logistic model of Tawn 1988

    special case: a1=a2=1 : Gumbel

    restrictions:
     - theta in (0,1]
     - a1, a2 in [0,1]
    """
    k_args: int
    def evaluate(self, t, a1, a2, theta): ...
    def deriv(self, t, a1, a2, theta): ...
    def deriv2(self, t, a1, a2, theta): ...

transform_tawn: Incomplete

class AsymNegLogistic(PickandDependence):
    """asymmetric negative logistic model of Joe 1990

    special case:  a1=a2=1 : symmetric negative logistic of Galambos 1978

    restrictions:
     - theta in (0,inf)
     - a1, a2 in (0,1]
    """
    k_args: int
    def evaluate(self, t, a1, a2, theta): ...
    def deriv(self, t, a1, a2, theta): ...
    def deriv2(self, t, a1, a2, theta): ...

transform_joe: Incomplete

class AsymMixed(PickandDependence):
    """asymmetric mixed model of Tawn 1988

    special case:  k=0, theta in [0,1] : symmetric mixed model of
        Tiago de Oliveira 1980

    restrictions:
     - theta > 0
     - theta + 3*k > 0
     - theta + k <= 1
     - theta + 2*k <= 1
    """
    k_args: int
    def evaluate(self, t, theta, k): ...
    def deriv(self, t, theta, k): ...
    def deriv2(self, t, theta, k): ...

transform_tawn2: Incomplete

class AsymBiLogistic(PickandDependence):
    """bilogistic model of Coles and Tawn 1994, Joe, Smith and Weissman 1992

    restrictions:
     - (beta, delta) in (0,1)^2 or
     - (beta, delta) in (-inf,0)^2

    not vectorized because of numerical integration
    """
    k_args: int
    def evaluate(self, t, beta, delta): ...

transform_bilogistic: Incomplete

class HR(PickandDependence):
    """model of Huesler Reiss 1989

    special case:  a1=a2=1 : symmetric negative logistic of Galambos 1978

    restrictions:
     - lambda in (0,inf)
    """
    k_args: int
    def evaluate(self, t, lamda): ...
    def deriv(self, t, lamda): ...
    def deriv2(self, t, lamda): ...

transform_hr: Incomplete

class TEV(PickandDependence):
    """t-EV model of Demarta and McNeil 2005

    restrictions:
     - rho in (-1,1)
     - x > 0
    """
    k_args: int
    def evaluate(self, t, rho, df): ...

transform_tev: Incomplete
