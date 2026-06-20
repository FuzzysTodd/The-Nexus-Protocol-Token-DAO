from .functions import defun as defun

class RSCache:
    def __init__(ctx) -> None: ...

def coef(ctx, J, eps): ...
def aux_M_Fp(ctx, xA, xeps4, a, xB1, xL): ...
def aux_J_needed(ctx, xA, xeps4, a, xB1, xM): ...
def Rzeta_simul(ctx, s, der: int = 0): ...
def Rzeta_set(ctx, s, derivatives=[0]):
    """
    Computes several derivatives of the auxiliary function of Riemann `R(s)`.

    **Definition**

    The function is defined by

    .. math ::

        \\begin{equation}
        {\\mathop{\\mathcal R }\\nolimits}(s)=
        \\int_{0\\swarrow1}\\frac{x^{-s} e^{\\pi i x^2}}{e^{\\pi i x}-
        e^{-\\pi i x}}\\,dx
        \\end{equation}

    To this function we apply the Riemann-Siegel expansion.
    """
def z_half(ctx, t, der: int = 0):
    """
    z_half(t,der=0) Computes Z^(der)(t)
    """
def zeta_half(ctx, s, k: int = 0):
    """
    zeta_half(s,k=0) Computes zeta^(k)(s) when Re s = 0.5
    """
def zeta_offline(ctx, s, k: int = 0):
    """
    Computes zeta^(k)(s) off the line
    """
def z_offline(ctx, w, k: int = 0):
    """
    Computes Z(w) and its derivatives off the line
    """
def rs_zeta(ctx, s, derivative: int = 0, **kwargs): ...
def rs_z(ctx, w, derivative: int = 0): ...
