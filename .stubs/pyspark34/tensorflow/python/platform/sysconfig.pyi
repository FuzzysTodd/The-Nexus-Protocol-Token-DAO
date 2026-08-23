from tensorflow.python.client import pywrap_tf_session as pywrap_tf_session
from tensorflow.python.platform import build_info as build_info
from tensorflow.python.util.tf_export import tf_export as tf_export

def get_include():
    """Get the directory containing the TensorFlow C++ header files.

  Returns:
    The directory as string.
  """
def get_lib():
    """Get the directory containing the TensorFlow framework library.

  Returns:
    The directory as string.
  """
def get_compile_flags():
    """Returns the compilation flags for compiling with TensorFlow.

  The returned list of arguments can be passed to the compiler for compiling
  against TensorFlow headers. The result is platform dependent.

  For example, on a typical Linux system with Python 3.7 the following command
  prints `['-I/usr/local/lib/python3.7/dist-packages/tensorflow/include',
  '-D_GLIBCXX_USE_CXX11_ABI=1', '-DEIGEN_MAX_ALIGN_BYTES=64']`

  >>> print(tf.sysconfig.get_compile_flags())

  Returns:
    A list of strings for the compiler flags.
  """
def get_link_flags():
    """Returns the linker flags for linking with TensorFlow.

  The returned list of arguments can be passed to the linker for linking against
  TensorFlow. The result is platform dependent.

  For example, on a typical Linux system with Python 3.7 the following command
  prints `['-L/usr/local/lib/python3.7/dist-packages/tensorflow',
  '-l:libtensorflow_framework.so.2']`

  >>> print(tf.sysconfig.get_link_flags())

  Returns:
    A list of strings for the linker flags.
  """
def get_build_info():
    """Get a dictionary describing TensorFlow's build environment.

  Values are generated when TensorFlow is compiled, and are static for each
  TensorFlow package. The return value is a dictionary with string keys such as:

    - cuda_version
    - cudnn_version
    - is_cuda_build
    - is_rocm_build
    - msvcp_dll_names
    - nvcuda_dll_name
    - cudart_dll_name
    - cudnn_dll_name

  Note that the actual keys and values returned by this function is subject to
  change across different versions of TensorFlow or across platforms.

  Returns:
    A Dictionary describing TensorFlow's build environment.
  """
