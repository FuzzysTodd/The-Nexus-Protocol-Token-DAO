from _typeshed import Incomplete
from torch.testing._internal.common_utils import TEST_WITH_ROCM as TEST_WITH_ROCM

class AutocastTestLists:
    torch_expect_builtin_promote: Incomplete
    methods_expect_builtin_promote: Incomplete
    torch_fp16: Incomplete
    torch_fp32: Incomplete
    torch_need_autocast_promote: Incomplete
    nn_fp16: Incomplete
    nn_fp32: Incomplete
    linalg_fp16: Incomplete
    methods_fp16: Incomplete
    methods_fp32: Incomplete
    banned: Incomplete
    def __init__(self, dev) -> None: ...

class AutocastCPUTestLists:
    torch_expect_builtin_promote: Incomplete
    methods_expect_builtin_promote: Incomplete
    torch_bf16: Incomplete
    torch_fp32: Incomplete
    nn_bf16: Incomplete
    nn_fp32: Incomplete
    torch_need_autocast_promote: Incomplete
    def __init__(self, dev) -> None: ...
