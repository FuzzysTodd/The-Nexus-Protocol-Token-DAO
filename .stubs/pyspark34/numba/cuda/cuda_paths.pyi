from _typeshed import Incomplete
from numba.core.config import IS_WIN32 as IS_WIN32
from numba.misc.findlib import find_file as find_file, find_lib as find_lib
from typing import NamedTuple

class _env_path_tuple(NamedTuple):
    by: Incomplete
    info: Incomplete

def get_system_ctk(*subdirs):
    """Return path to system-wide cudatoolkit; or, None if it doesn't exist.
    """
def get_conda_ctk():
    """Return path to directory containing the shared libraries of cudatoolkit.
    """
def get_nvidia_nvvm_ctk():
    """Return path to directory containing the NVVM shared library.
    """
def get_nvidia_libdevice_ctk():
    """Return path to directory containing the libdevice library.
    """
def get_nvidia_cudalib_ctk():
    """Return path to directory containing the shared libraries of cudatoolkit.
    """
def get_nvidia_static_cudalib_ctk():
    """Return path to directory containing the static libraries of cudatoolkit.
    """
def get_cuda_home(*subdirs):
    """Get paths of CUDA_HOME.
    If *subdirs* are the subdirectory name to be appended in the resulting
    path.
    """
def get_cuda_paths():
    '''Returns a dictionary mapping component names to a 2-tuple
    of (source_variable, info).

    The returned dictionary will have the following keys and infos:
    - "nvvm": file_path
    - "libdevice": List[Tuple[arch, file_path]]
    - "cudalib_dir": directory_path

    Note: The result of the function is cached.
    '''
def get_debian_pkg_libdevice():
    """
    Return the Debian NVIDIA Maintainers-packaged libdevice location, if it
    exists.
    """
