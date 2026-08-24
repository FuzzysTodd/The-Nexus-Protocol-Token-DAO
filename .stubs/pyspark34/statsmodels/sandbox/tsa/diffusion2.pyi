class JumpDiffusionMerton:
    """

    Example
    -------
    mu=.00     # deterministic drift
    sig=.20 # Gaussian component
    l=3.45 # Poisson process arrival rate
    a=0 # drift of log-jump
    D=.2 # st.dev of log-jump

    X = JumpDiffusionMerton().simulate(mu,sig,lambd,a,D,ts,nrepl)

    plt.figure()
    plt.plot(X.T)
    plt.title('Merton jump-diffusion')


    """
    def __init__(self) -> None: ...
    def simulate(self, m, s, lambd, a, D, ts, nrepl): ...

class JumpDiffusionKou:
    def __init__(self) -> None: ...
    def simulate(self, m, s, lambd, p, e1, e2, ts, nrepl): ...

class VG:
    """variance gamma process
    """
    def __init__(self) -> None: ...
    def simulate(self, m, s, kappa, ts, nrepl): ...

class IG:
    """inverse-Gaussian ??? used by NIG
    """
    def __init__(self) -> None: ...
    def simulate(self, l, m, nrepl): ...

class NIG:
    """normal-inverse-Gaussian
    """
    def __init__(self) -> None: ...
    def simulate(self, th, k, s, ts, nrepl): ...

class Heston:
    """Heston Stochastic Volatility
    """
    def __init__(self) -> None: ...
    def simulate(self, m, kappa, eta, lambd, r, ts, nrepl, tratio: float = 1.0): ...

class CIRSubordinatedBrownian:
    """CIR subordinated Brownian Motion
    """
    def __init__(self) -> None: ...
    def simulate(self, m, kappa, T_dot, lambd, sigma, ts, nrepl): ...

def schout2contank(a, b, d): ...
