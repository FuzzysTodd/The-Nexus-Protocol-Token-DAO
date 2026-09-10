from _typeshed import Incomplete

__all__ = ['needs_g77_abi_wrapper', 'get_g77_abi_wrappers', 'gfortran_legacy_flag_hook', 'blas_ilp64_pre_build_hook', 'get_f2py_int64_options', 'generic_pre_build_hook', 'write_file_content', 'ilp64_pre_build_hook']

def needs_g77_abi_wrapper(info):
    """Returns True if g77 ABI wrapper must be used."""
def get_g77_abi_wrappers(info):
    """
    Returns file names of source files containing Fortran ABI wrapper
    routines.
    """
def gfortran_legacy_flag_hook(cmd, ext) -> None:
    """
    Pre-build hook to add dd gfortran legacy flag -fallow-argument-mismatch
    """
def get_f2py_int64_options(): ...
def ilp64_pre_build_hook(cmd, ext):
    """
    Pre-build hook for adding Fortran compiler flags that change
    default integer size to 64-bit.
    """
def blas_ilp64_pre_build_hook(blas_info):
    """
    Pre-build hook for adding ILP64 BLAS compilation flags, and
    mangling Fortran source files to rename BLAS/LAPACK symbols when
    there are symbol suffixes.

    Examples
    --------
    ::

        from scipy._build_utils import blas_ilp64_pre_build_hook
        ext = config.add_extension(...)
        ext._pre_build_hook = blas_ilp64_pre_build_hook(blas_info)

    """
def generic_pre_build_hook(cmd, ext, fcompiler_flags, patch_source_func: Incomplete | None = None, source_fnpart: Incomplete | None = None) -> None:
    """
    Pre-build hook for adding compiler flags and patching sources.

    Parameters
    ----------
    cmd : distutils.core.Command
        Hook input. Current distutils command (build_clib or build_ext).
    ext : dict or numpy.distutils.extension.Extension
        Hook input. Configuration information for library (dict, build_clib)
        or extension (numpy.distutils.extension.Extension, build_ext).
    fcompiler_flags : dict
        Dictionary of ``{'compiler_name': ['-flag1', ...]}`` containing
        compiler flags to set.
    patch_source_func : callable, optional
        Function patching sources, see `_generic_patch_sources` below.
    source_fnpart : str, optional
        String to append to the modified file basename before extension.

    """
def write_file_content(filename, content) -> None:
    """
    Write content to file, but only if it differs from the current one.
    """
