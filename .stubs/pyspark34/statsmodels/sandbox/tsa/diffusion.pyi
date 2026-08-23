from _typeshed import Incomplete

class Diffusion:
    """Wiener Process, Brownian Motion with mu=0 and sigma=1
    """
    def __init__(self) -> None: ...
    dW: Incomplete
    def simulateW(self, nobs: int = 100, T: int = 1, dt: Incomplete | None = None, nrepl: int = 1):
        """generate sample of Wiener Process
        """
    def expectedsim(self, func, nobs: int = 100, T: int = 1, dt: Incomplete | None = None, nrepl: int = 1):
        """get expectation of a function of a Wiener Process by simulation

        initially test example from
        """

class AffineDiffusion(Diffusion):
    """

    differential equation:

    :math::
    dx_t = f(t,x)dt + \\sigma(t,x)dW_t

    integral:

    :math::
    x_T = x_0 + \\int_{0}^{T}f(t,S)dt + \\int_0^T  \\sigma(t,S)dW_t

    TODO: check definition, affine, what about jump diffusion?

    """
    def __init__(self) -> None: ...
    def sim(self, nobs: int = 100, T: int = 1, dt: Incomplete | None = None, nrepl: int = 1): ...
    def simEM(self, xzero: Incomplete | None = None, nobs: int = 100, T: int = 1, dt: Incomplete | None = None, nrepl: int = 1, Tratio: int = 4):
        """

        from Higham 2001

        TODO: reverse parameterization to start with final nobs and DT
        TODO: check if I can skip the loop using my way from exactprocess
              problem might be Winc (reshape into 3d and sum)
        TODO: (later) check memory efficiency for large simulations
        """

class ExactDiffusion(AffineDiffusion):
    """Diffusion that has an exact integral representation

    this is currently mainly for geometric, log processes

    """
    def __init__(self) -> None: ...
    def exactprocess(self, xzero, nobs, ddt: float = 1.0, nrepl: int = 2):
        """ddt : discrete delta t



        should be the same as an AR(1)
        not tested yet
        """
    def exactdist(self, xzero, t): ...

class ArithmeticBrownian(AffineDiffusion):
    """
    :math::
    dx_t &= \\mu dt + \\sigma dW_t
    """
    xzero: Incomplete
    mu: Incomplete
    sigma: Incomplete
    def __init__(self, xzero, mu, sigma) -> None: ...
    def exactprocess(self, nobs, xzero: Incomplete | None = None, ddt: float = 1.0, nrepl: int = 2):
        """ddt : discrete delta t

        not tested yet
        """
    def exactdist(self, xzero, t): ...

class GeometricBrownian(AffineDiffusion):
    """Geometric Brownian Motion

    :math::
    dx_t &= \\mu x_t dt + \\sigma x_t dW_t

    $x_t $ stochastic process of Geometric Brownian motion,
    $\\mu $ is the drift,
    $\\sigma $ is the Volatility,
    $W$ is the Wiener process (Brownian motion).

    """
    xzero: Incomplete
    mu: Incomplete
    sigma: Incomplete
    def __init__(self, xzero, mu, sigma) -> None: ...

class OUprocess(AffineDiffusion):
    """Ornstein-Uhlenbeck

    :math::
      dx_t&=\\lambda(\\mu - x_t)dt+\\sigma dW_t

    mean reverting process



    TODO: move exact higher up in class hierarchy
    """
    xzero: Incomplete
    lambd: Incomplete
    mu: Incomplete
    sigma: Incomplete
    def __init__(self, xzero, mu, lambd, sigma) -> None: ...
    def exact(self, xzero, t, normrvs): ...
    def exactprocess(self, xzero, nobs, ddt: float = 1.0, nrepl: int = 2):
        """ddt : discrete delta t

        should be the same as an AR(1)
        not tested yet
        # after writing this I saw the same use of lfilter in sitmo
        """
    def exactdist(self, xzero, t): ...
    def fitls(self, data, dt):
        """assumes data is 1d, univariate time series
        formula from sitmo
        """

class SchwartzOne(ExactDiffusion):
    """the Schwartz type 1 stochastic process

    :math::
    dx_t = \\kappa (\\mu - \\ln x_t) x_t dt + \\sigma x_tdW \\\n
    The Schwartz type 1 process is a log of the Ornstein-Uhlenbeck stochastic
    process.

    """
    xzero: Incomplete
    mu: Incomplete
    kappa: Incomplete
    lambd: Incomplete
    sigma: Incomplete
    def __init__(self, xzero, mu, kappa, sigma) -> None: ...
    def exactprocess(self, xzero, nobs, ddt: float = 1.0, nrepl: int = 2):
        """uses exact solution for log of process
        """
    def exactdist(self, xzero, t): ...
    def fitls(self, data, dt):
        """assumes data is 1d, univariate time series
        formula from sitmo
        """

class BrownianBridge:
    def __init__(self) -> None: ...
    def simulate(self, x0, x1, nobs, nrepl: int = 1, ddt: float = 1.0, sigma: float = 1.0): ...

class CompoundPoisson:
    """nobs iid compound poisson distributions, not a process in time
    """
    nobj: Incomplete
    randfn: Incomplete
    lambd: Incomplete
    def __init__(self, lambd, randfn=...) -> None: ...
    def simulate(self, nobs, nrepl: int = 1): ...
