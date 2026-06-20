from _typeshed import Incomplete

def c2c(forward, x, n: Incomplete | None = None, axis: int = -1, norm: Incomplete | None = None, overwrite_x: bool = False, workers: Incomplete | None = None, *, plan: Incomplete | None = None):
    """ Return discrete Fourier transform of real or complex sequence. """

fft: Incomplete
ifft: Incomplete

def r2c(forward, x, n: Incomplete | None = None, axis: int = -1, norm: Incomplete | None = None, overwrite_x: bool = False, workers: Incomplete | None = None, *, plan: Incomplete | None = None):
    """
    Discrete Fourier transform of a real sequence.
    """

rfft: Incomplete
ihfft: Incomplete

def c2r(forward, x, n: Incomplete | None = None, axis: int = -1, norm: Incomplete | None = None, overwrite_x: bool = False, workers: Incomplete | None = None, *, plan: Incomplete | None = None):
    """
    Return inverse discrete Fourier transform of real sequence x.
    """

hfft: Incomplete
irfft: Incomplete

def fft2(x, s: Incomplete | None = None, axes=(-2, -1), norm: Incomplete | None = None, overwrite_x: bool = False, workers: Incomplete | None = None, *, plan: Incomplete | None = None):
    """
    2-D discrete Fourier transform.
    """
def ifft2(x, s: Incomplete | None = None, axes=(-2, -1), norm: Incomplete | None = None, overwrite_x: bool = False, workers: Incomplete | None = None, *, plan: Incomplete | None = None):
    """
    2-D discrete inverse Fourier transform of real or complex sequence.
    """
def rfft2(x, s: Incomplete | None = None, axes=(-2, -1), norm: Incomplete | None = None, overwrite_x: bool = False, workers: Incomplete | None = None, *, plan: Incomplete | None = None):
    """
    2-D discrete Fourier transform of a real sequence
    """
def irfft2(x, s: Incomplete | None = None, axes=(-2, -1), norm: Incomplete | None = None, overwrite_x: bool = False, workers: Incomplete | None = None, *, plan: Incomplete | None = None):
    """
    2-D discrete inverse Fourier transform of a real sequence
    """
def hfft2(x, s: Incomplete | None = None, axes=(-2, -1), norm: Incomplete | None = None, overwrite_x: bool = False, workers: Incomplete | None = None, *, plan: Incomplete | None = None):
    """
    2-D discrete Fourier transform of a Hermitian sequence
    """
def ihfft2(x, s: Incomplete | None = None, axes=(-2, -1), norm: Incomplete | None = None, overwrite_x: bool = False, workers: Incomplete | None = None, *, plan: Incomplete | None = None):
    """
    2-D discrete inverse Fourier transform of a Hermitian sequence
    """
def c2cn(forward, x, s: Incomplete | None = None, axes: Incomplete | None = None, norm: Incomplete | None = None, overwrite_x: bool = False, workers: Incomplete | None = None, *, plan: Incomplete | None = None):
    """
    Return multidimensional discrete Fourier transform.
    """

fftn: Incomplete
ifftn: Incomplete

def r2cn(forward, x, s: Incomplete | None = None, axes: Incomplete | None = None, norm: Incomplete | None = None, overwrite_x: bool = False, workers: Incomplete | None = None, *, plan: Incomplete | None = None):
    """Return multidimensional discrete Fourier transform of real input"""

rfftn: Incomplete
ihfftn: Incomplete

def c2rn(forward, x, s: Incomplete | None = None, axes: Incomplete | None = None, norm: Incomplete | None = None, overwrite_x: bool = False, workers: Incomplete | None = None, *, plan: Incomplete | None = None):
    """Multidimensional inverse discrete fourier transform with real output"""

hfftn: Incomplete
irfftn: Incomplete

def r2r_fftpack(forward, x, n: Incomplete | None = None, axis: int = -1, norm: Incomplete | None = None, overwrite_x: bool = False):
    """FFT of a real sequence, returning fftpack half complex format"""

rfft_fftpack: Incomplete
irfft_fftpack: Incomplete
