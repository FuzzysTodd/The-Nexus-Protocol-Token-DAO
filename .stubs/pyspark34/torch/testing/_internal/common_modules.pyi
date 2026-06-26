from _typeshed import Incomplete
from collections.abc import Generator
from torch.nn.utils.rnn import pack_padded_sequence as pack_padded_sequence
from torch.testing import make_tensor as make_tensor
from torch.testing._internal.common_cuda import TEST_CUDNN as TEST_CUDNN
from torch.testing._internal.common_device_type import _TestParametrizer, precisionOverride as precisionOverride, skipCUDAIfCudnnVersionLessThan as skipCUDAIfCudnnVersionLessThan, skipCUDAIfRocm as skipCUDAIfRocm, skipCUDAVersionIn as skipCUDAVersionIn, skipMeta as skipMeta, tol as tol, toleranceOverride as toleranceOverride
from torch.testing._internal.common_dtype import floating_and_complex_types_and as floating_and_complex_types_and, floating_types as floating_types
from torch.testing._internal.common_methods_invocations import DecorateInfo as DecorateInfo
from torch.testing._internal.common_nn import get_reduction as get_reduction, nllloss_reference as nllloss_reference
from torch.testing._internal.common_utils import GRADCHECK_NONDET_TOL as GRADCHECK_NONDET_TOL, TEST_WITH_ROCM as TEST_WITH_ROCM, freeze_rng_state as freeze_rng_state, set_single_threaded_if_parallel_tbb as set_single_threaded_if_parallel_tbb, skipIfMps as skipIfMps
from types import ModuleType
from typing import Dict, List, Set, Type

MODULE_NAMESPACES: List[ModuleType]
MODULES_TO_SKIP: Set[Type]
MODULE_CLASSES: List[Type]
MODULE_CLASS_NAMES: Dict[Type, str]
module_cls: Incomplete
namespace_name: Incomplete
TrainEvalMode: Incomplete

class modules(_TestParametrizer):
    """ PROTOTYPE: Decorator for specifying a list of modules over which to run a test. """
    module_info_list: Incomplete
    allowed_dtypes: Incomplete
    train_eval_mode: Incomplete
    def __init__(self, module_info_iterable, allowed_dtypes: Incomplete | None = None, train_eval_mode=...) -> None: ...

def get_module_common_name(module_cls): ...

class FunctionInput:
    """ Contains args and kwargs to pass as input to a function. """
    args: Incomplete
    kwargs: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...

class ModuleInput:
    """ Contains args / kwargs for module instantiation + forward pass. """
    constructor_input: Incomplete
    forward_input: Incomplete
    desc: Incomplete
    reference_fn: Incomplete
    def __init__(self, constructor_input, forward_input: Incomplete | None = None, desc: str = '', reference_fn: Incomplete | None = None) -> None: ...

class ModuleInfo:
    """ Module information to be used in testing. """
    module_cls: Incomplete
    module_inputs_func: Incomplete
    decorators: Incomplete
    dtypes: Incomplete
    supports_gradgrad: Incomplete
    gradcheck_nondet_tol: Incomplete
    module_memformat_affects_out: Incomplete
    train_and_eval_differ: Incomplete
    def __init__(self, module_cls, *, module_inputs_func, skips=(), decorators: Incomplete | None = None, dtypes=..., supports_gradgrad: bool = True, gradcheck_nondet_tol: float = 0.0, module_memformat_affects_out: bool = False, train_and_eval_differ: bool = False) -> None: ...
    def get_decorators(self, test_class, test_name, device, dtype, param_kwargs): ...
    @property
    def name(self): ...
    @property
    def formatted_name(self): ...

def module_inputs_torch_nn_Linear(module_info, device, dtype, requires_grad, training, **kwargs): ...
def module_inputs_torch_nn_Bilinear(module_info, device, dtype, requires_grad, training, **kwargs): ...
def module_inputs_torch_nn_NLLLoss(module_info, device, dtype, requires_grad, training, **kwargs): ...
def module_inputs_torch_nn_GaussianNLLLoss(module_info, device, dtype, requires_grad, training, **kwargs): ...
def no_batch_dim_reference_fn(m, p, *args, **kwargs):
    """Reference function for modules supporting no batch dimensions.

    Unbatched inputs are unsqueezed to form a
    single batch input before passing them to the module.
    The output is squeezed to compare with the
    output of unbatched input to the module.

    Currently it only supports modules which return a single Tensor as output.
    You can bind the following kwargs.
    Kwargs:
        batch_first[bool] : If True, all the Tensors in `args` while be unsqueezed at dim `0` .
                        and output will be squeezed at dim `0` else dim `1` for both.
        kwargs_to_batchify[dict] : Dictionary specifying the name of the argument and dimension to unsqueeze.
                               Useful if there are few arguments whose batch dimension are different
                               from the ones selected by `batch_first`.
        is_criterion[bool] : Specify if the module is a criterion and handle the reduction for output accordingly.
    """
def no_batch_dim_reference_mha(m, p, *args, **kwargs):
    """Reference function for MultiheadAttention supporting no batch dimensions.

    Unbatched inputs are unsqueezed to form a
    single batch input before passing them to the module.
    The output is squeezed to compare with the
    output of unbatched input to the module.
    """
def no_batch_dim_reference_rnn_gru(m, p, *args, **kwargs):
    """Reference function for RNN and GRU supporting no batch dimensions.

    Unbatched inputs are unsqueezed to form a
    single batch input before passing them to the module.
    The output is squeezed to compare with the
    output of unbatched input to the module.
    """
def no_batch_dim_reference_lstm(m, p, *args, **kwargs):
    """Reference function for LSTM supporting no batch dimensions.

    Unbatched inputs are unsqueezed to form a
    single batch input before passing them to the module.
    The output is squeezed to compare with the
    output of unbatched input to the module.
    """
def no_batch_dim_reference_lstmcell(m, p, *args, **kwargs):
    """Reference function for LSTMCell supporting no batch dimensions.

    The module is passed the input and target in batched form with a single item.
    The output is squeezed to compare with the no-batch input.
    """
def generate_regression_criterion_inputs(make_input): ...
def module_inputs_torch_nn_AvgPool1d(module_info, device, dtype, requires_grad, training, **kwargs): ...
def module_inputs_torch_nn_AdaptiveAvgPool2d(module_info, device, dtype, requires_grad, training, **kwargs): ...
def module_inputs_torch_nn_BatchNorm2d(module_info, device, dtype, requires_grad, training, **kwargs): ...
def module_inputs_torch_nn_BatchNorm3d(module_info, device, dtype, requires_grad, training, **kwargs): ...
def module_inputs_torch_nn_ConvNd(module_info, device, dtype, requires_grad, training, **kwargs): ...
def module_inputs_torch_nn_ELU(module_info, device, dtype, requires_grad, training, **kwargs): ...
def module_inputs_torch_nn_CELU(module_info, device, dtype, requires_grad, training, **kwargs): ...
def module_inputs_torch_nn_ReLU(module_info, device, dtype, requires_grad, training, **kwargs): ...
def module_inputs_torch_nn_L1Loss(module_info, device, dtype, requires_grad, training, **kwargs): ...
def module_inputs_torch_nn_CrossEntropyLoss(module_info, device, dtype, requires_grad, training, **kwargs): ...
def module_inputs_torch_nn_Hardswish(module_info, device, dtype, requires_grad, training, **kwargs): ...
def module_inputs_torch_nn_MaxPool2d(module_info, device, dtype, requires_grad, training, **kwargs): ...
def module_inputs_torch_nn_Sigmoid(module_info, device, dtype, requires_grad, training, **kwargs): ...
def module_inputs_torch_nn_TransformerEncoder(module_info, device, dtype, requires_grad, training, **kwargs) -> Generator[Incomplete, None, None]: ...
def module_inputs_torch_nn_TransformerEncoderLayer(module_info, device, dtype, requires_grad, training, **kwargs): ...
def module_inputs_torch_nn_TransformerDecoderLayer(module_info, device, dtype, requires_grad, training, **kwargs): ...
def module_inputs_torch_nn_Transformer(module_info, device, dtype, requires_grad, training, **kwargs): ...
def module_inputs_torch_nn_Embedding(module_info, device, dtype, requires_grad, training, **kwargs): ...
def module_inputs_torch_nn_MultiheadAttention(module_info, device, dtype, requires_grad, training, **kwargs): ...
def module_inputs_torch_nn_RNN_GRU_Cell(module_info, device, dtype, requires_grad, training, **kwargs): ...
def module_inputs_torch_nn_LSTMCell(module_info, device, dtype, requires_grad, training, **kwargs): ...
def make_packed_sequence(inp, batch_sizes): ...
def module_inputs_torch_nn_RNN_GRU(module_info, device, dtype, requires_grad, training, with_packed_sequence: bool = False, **kwargs): ...
def module_inputs_torch_nn_LSTM(module_info, device, dtype, requires_grad, training, **kwargs): ...

rnn_gru_lstm_module_info_decorators: Incomplete
module_db: List[ModuleInfo]
