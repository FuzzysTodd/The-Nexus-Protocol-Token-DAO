import abc
import torch
import torch.distributed as dist
import torch.nn as nn
from _typeshed import Incomplete
from abc import ABC, abstractmethod
from enum import Enum
from torch.distributed.fsdp import CPUOffload as CPUOffload, FullyShardedDataParallel as FSDP
from torch.distributed.fsdp._common_utils import TrainingState as TrainingState
from torch.distributed.fsdp.fully_sharded_data_parallel import BackwardPrefetch as BackwardPrefetch, MixedPrecision as MixedPrecision, ShardingStrategy as ShardingStrategy
from torch.distributed.fsdp.sharded_grad_scaler import ShardedGradScaler as ShardedGradScaler
from torch.distributed.fsdp.wrap import ModuleWrapPolicy as ModuleWrapPolicy, always_wrap_policy as always_wrap_policy, wrap as wrap
from torch.nn import TransformerDecoderLayer as TransformerDecoderLayer, TransformerEncoderLayer as TransformerEncoderLayer
from torch.testing._internal.common_distributed import MultiProcessTestCase as MultiProcessTestCase, TEST_SKIPS as TEST_SKIPS
from torch.testing._internal.common_utils import FILE_SCHEMA as FILE_SCHEMA, get_cycles_per_ms as get_cycles_per_ms
from typing import Any, Callable, Dict, List, Tuple, Type

class FSDPInitMode(Enum):
    NO_FSDP: Incomplete
    RECURSIVE: Incomplete

class CUDAInitMode(Enum):
    CUDA_BEFORE: Incomplete
    CUDA_AFTER: Incomplete
    CUDA_NEVER: Incomplete

class FSDPTestModel(nn.Module, ABC, metaclass=abc.ABCMeta):
    """This defines the interface expected from all models used commonly for
    FSDP unit tests."""
    @abstractmethod
    def get_input(self, device) -> Tuple[torch.Tensor, ...]:
        """Returns an input for the model as as tuple."""
    @abstractmethod
    def get_loss(self, input, output) -> torch.Tensor:
        """Returns the loss given the input and output."""
    @abstractmethod
    def run_backward(self, loss) -> None:
        """Runs the backward pass (e.g. including ``loss.backward()``)."""
    @staticmethod
    @abstractmethod
    def init(group: dist.ProcessGroup, fsdp_init_mode: FSDPInitMode, *init_args: Any, cuda_init_mode: CUDAInitMode, fsdp_kwargs: Dict[str, Any] | None = None, deterministic: bool = False, **init_kwargs: Any) -> nn.Module:
        """Initializes an instance of this model."""

def subtest_name(test_name_mapping, *args): ...
def get_full_params(model: nn.Module, recurse: bool = True):
    """
    Returns the full unsharded parameters of ``model``. Any FSDP-managed
    parameters offloaded to CPU are moved to GPU in the returned list.

    Args:
        recurse (bool): If ``False``, only unshards the parameters immediate to
            ``model``; if ``True``, recurses through the module hierarchy
            rooted at ``model``.
    """

class DummyProcessGroup:
    def __init__(self, rank: int, size: int) -> None: ...
    def rank(self) -> int: ...
    def size(self) -> int: ...
    def allreduce(self, *args, **kwargs): ...

class TransformerWithSharedParams(FSDPTestModel):
    rank: Incomplete
    world_size: Incomplete
    embed_tokens: Incomplete
    transformer: Incomplete
    output_proj: Incomplete
    bs: int
    bn: Incomplete
    def __init__(self, group: dist.ProcessGroup, cuda_init_mode: CUDAInitMode, add_bn: bool, deterministic: bool) -> None: ...
    def get_input(self, device): ...
    def forward(self, src_ids, tgt_ids): ...
    def get_loss(self, input, output): ...
    def run_backward(self, loss) -> None: ...
    @staticmethod
    def init(group: dist.ProcessGroup, fsdp_init_mode: FSDPInitMode, cuda_init_mode: CUDAInitMode, fsdp_kwargs: Dict[str, Any] | None = None, deterministic: bool = False, add_bn: bool = True) -> nn.Module | FSDP:
        """
        Initializes a :class:`TransformerWithSharedParams` instance.

        Args:
            fsdp_init_mode (FSDPInitMode): If ``NO_FSDP``, then does not wrap
                any modules with FSDP. If ``RECURSIVE``, then wraps with
                top-level FSDP. By default, the top-level FSDP uses the
                ``ModuleWrapPolicy`` for encoder and decoder layers, but a
                different auto wrap policy may be specified via
                ``fsdp_kwargs``.
            cuda_init_mode (CUDAInitMode): Determines model movement to CUDA.
            fsdp_kwargs (Optional[Dict[str, Any]]): Optional keyword arguments
                forwarded to the FSDP constructor.
            deterministic (bool): Whether to make the model deterministic
                across constructions.
            add_bn (bool): Whether to include batch norm in the model.
        """
    def get_ignored_modules(self): ...

class NestedWrappedModule(FSDPTestModel):
    rank: Incomplete
    world_size: Incomplete
    module: Incomplete
    def __init__(self, group: dist.ProcessGroup, wrap_fsdp: bool, cuda_init_mode: CUDAInitMode, deterministic: bool, **fsdp_kwargs) -> None: ...
    def get_input(self, device): ...
    def forward(self, x): ...
    def get_loss(self, input, output): ...
    def run_backward(self, loss) -> None: ...
    @staticmethod
    def init(group: dist.ProcessGroup, fsdp_init_mode: FSDPInitMode, cuda_init_mode: CUDAInitMode, fsdp_kwargs: Dict[str, Any] | None = None, deterministic: bool = False) -> nn.Module:
        """
        Initializes a :class:`NestedWrappedModule` instance.

        Args:
            fsdp_init_mode (FSDPInitMode): If ``NO_FSDP``, then does not wrap
                any modules with FSDP. If ``RECURSIVE``, then wraps some nested
                modules with FSDP but not the top-level module. The model may
                later be wrapped with a top-level FSDP external to this method
                if desired.
            cuda_init_mode (CUDAInitMode): Determines model movement to CUDA.
            fsdp_kwargs (Optional[Dict[str, Any]]): Optional keyword arguments
                forwarded to the FSDP constructor.
            deterministic (bool): Whether to make the model deterministic
                across constructions.
        """

class AlwaysWrapNestedWrappedModule(NestedWrappedModule):
    @staticmethod
    def init(group: dist.ProcessGroup, fsdp_init_mode: FSDPInitMode, cuda_init_mode: CUDAInitMode, fsdp_kwargs: Dict[str, Any] | None = None, deterministic: bool = False):
        """
        Initializes a :class:`NestedWrappedModule` instance, but unlike
        :meth:`NestedWrappedModule.init`, for the ``RECURSIVE`` init mode, this
        wraps with top-level FSDP and the ``always_wrap_policy()`` auto wrap
        policy.
        """

class ModuleWithDelay(FSDPTestModel):
    """This class wraps a :class:`FSDPTestModel` to optionally add a delay
    after computing the loss and/or before the gradient reduction."""
    delay_after_loss_ms: Incomplete
    delay_before_reduction_ms: Incomplete
    module: Incomplete
    def __init__(self, module: nn.Module, delay_after_loss_ms: int, delay_before_reduction_ms: int) -> None: ...
    def get_input(self, device): ...
    def forward(self, x): ...
    def get_loss(self, input, output): ...
    def run_backward(self, loss): ...
    @staticmethod
    def init(module_class: Type[FSDPTestModel], *model_args: Any, delay_after_loss_ms: int, delay_before_reduction_ms: int, **model_kwargs: Any):
        """
        Args:
            module_class (Type[FSDPTestModel]): Wrapped module class to which
                to add delays.
            model_args: Positional arguments forwarded to the ``module_class``
                ``init()``.
            delay_after_loss_ms (int): Delay after computing the loss/before
                the optimizer step (in ms).
            delay_before_reduction_ms (int): Delay before reduce-scattering
                gradients (in ms).
            model_kwargs: Keyword arguments forwarded to the ``module_class``
                ``init()``.
        """

class NestedWrappedModuleWithDelay(ModuleWithDelay):
    @staticmethod
    def init(group: dist.ProcessGroup, fsdp_init_mode: FSDPInitMode, cuda_init_mode: CUDAInitMode = ..., fsdp_kwargs: Dict[str, Any] | None = None, deterministic: bool = False, delay_after_loss_ms: int = 0, delay_before_reduction_ms: int = 0): ...

class DummyDDP(nn.Module):
    module: Incomplete
    def __init__(self, module) -> None: ...
    def forward(self, *args, **kwargs): ...

class MixtureOfExperts(NestedWrappedModule):
    group: Incomplete
    delay_before_free_ms: Incomplete
    wrap_fsdp: Incomplete
    move_to_cuda: Incomplete
    num_expert_params: Incomplete
    module: Incomplete
    def __init__(self, group: dist.ProcessGroup, wrap_fsdp: bool, cuda_init_mode: CUDAInitMode, delay_before_free_ms: int, deterministic: bool, **fsdp_kwargs) -> None: ...
    def forward(self, x): ...
    def run_backward(self, loss) -> None: ...
    @staticmethod
    def init(group: dist.ProcessGroup, fsdp_init_mode: FSDPInitMode, cuda_init_mode: CUDAInitMode, fsdp_kwargs: Dict[str, Any] | None = None, deterministic: bool = False, delay_before_free_ms: int = 0):
        """
        Initializes a :class:`MixtureOfExperts` instance.

        Args:
            fsdp_init_mode (FSDPInitMode): If ``NO_FSDP``, then does not wrap
                any modules with FSDP. If ``RECURSIVE``, then wraps some nested
                modules with FSDP, including the expert and shared layers, but
                not the top-level module. The model may later be wrapped with a
                top-level FSDP external to this method if desired.
            cuda_init_mode (CUDAInitMode): Determines model movement to CUDA.
            fsdp_kwargs (Optional[Dict[str, Any]]): Optional keyword arguments
                forwarded to the FSDP constructor.
            deterministic (bool): Whether to make the model deterministic
                across constructions.
            delay_before_free_ms (int): Delay before resharding expert
                parameters in the forward pass (in ms).
        """

class FSDPTest(MultiProcessTestCase):
    def setUp(self) -> None: ...
    @property
    def world_size(self): ...
    @property
    def process_group(self): ...
    @property
    def init_method(self): ...
    def run_subtests(self, subtest_config: Dict[str, List[Any]], test_fn: Callable, *test_args, **test_kwargs: Any):
        """
        Runs a test function given by ``test_fn`` as a subtest according to the
        configurations specified by ``subtest_config``. This amortizes the
        costly setup overhead (including process spawn and initializing the
        process group) over the subtests.

        Args:
            subtest_config (Dict[str, List[Any]]): A mapping from subtest
                keyword argument name to a list of its possible values.
            test_fn (Callable): A callable that runs the actual test.
            test_args: Positional arguments to pass to ``test_fn``.
            test_kwargs: Keyword arguments to pass to ``test_fn``.
        """

class SkipModule(nn.Module):
    lin: Incomplete
    def __init__(self) -> None: ...
    def forward(self, x): ...

class NestedLinear(nn.Module):
    nested_linear: Incomplete
    def __init__(self, fsdp_wrap) -> None: ...
    def forward(self, x): ...

class SkipModel(nn.Module):
    linear: Incomplete
    linear_skip: Incomplete
    nested_linear: Incomplete
    def __init__(self, double_nest) -> None: ...
    def forward(self, x): ...
