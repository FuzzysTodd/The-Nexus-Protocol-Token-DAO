from _typeshed import Incomplete
from collections.abc import Generator
from torch.testing._internal.common_utils import IS_WINDOWS as IS_WINDOWS, TEST_NUMBA as TEST_NUMBA, TEST_WITH_ROCM as TEST_WITH_ROCM

TEST_CUDA: Incomplete
TEST_MULTIGPU: Incomplete
CUDA_DEVICE: Incomplete
TEST_CUDNN: Incomplete
TEST_CUDNN_VERSION: Incomplete
SM53OrLater: Incomplete
SM60OrLater: Incomplete
SM80OrLater: Incomplete
PLATFORM_SUPPORTS_FUSED_SDPA: bool
TEST_MAGMA = TEST_CUDA
TEST_NUMBA_CUDA: Incomplete

def initialize_cuda_context_rng() -> None: ...
def tf32_is_not_fp32(): ...
def tf32_off() -> Generator[None, None, None]: ...
def tf32_on(self, tf32_precision: float = 1e-05) -> Generator[None, None, None]: ...
def tf32_on_and_off(tf32_precision: float = 1e-05): ...
def with_tf32_off(f): ...

TEST_CUSPARSE_GENERIC: Incomplete
TEST_HIPSPARSE_GENERIC: Incomplete
