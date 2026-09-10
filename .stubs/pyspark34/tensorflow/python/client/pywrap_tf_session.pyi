from tensorflow.python.client._pywrap_tf_session import *
from _typeshed import Incomplete
from tensorflow.python import pywrap_tensorflow as pywrap_tensorflow
from tensorflow.python.util import tf_stack as tf_stack

__version__: Incomplete
__git_version__: Incomplete
__compiler_version__: Incomplete
__cxx11_abi_flag__: Incomplete
__cxx_version__: Incomplete
__monolithic_build__: Incomplete
GRAPH_DEF_VERSION: Incomplete
GRAPH_DEF_VERSION_MIN_CONSUMER: Incomplete
GRAPH_DEF_VERSION_MIN_PRODUCER: Incomplete
TENSOR_HANDLE_KEY: Incomplete

def TF_NewSessionOptions(target: Incomplete | None = None, config: Incomplete | None = None): ...
def TF_Reset(target, containers: Incomplete | None = None, config: Incomplete | None = None) -> None: ...
