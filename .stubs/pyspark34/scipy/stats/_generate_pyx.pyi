def isNPY_OLD():
    """
    A new random C API was added in 1.18 and became stable in 1.19.
    Prefer the new random C API when building with recent numpy.
    """
def make_biasedurn(outdir) -> None:
    """Substitute True/False values for NPY_OLD Cython build variable."""
def make_unuran(srcdir, outdir) -> None:
    """Substitute True/False values for NPY_OLD Cython build variable."""
def make_boost(outdir, distutils_build: bool = False) -> None: ...
