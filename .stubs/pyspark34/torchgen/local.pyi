import threading
from typing import Iterator

class Locals(threading.local):
    use_const_ref_for_mutable_tensors: bool | None
    use_ilistref_for_tensor_lists: bool | None

def use_const_ref_for_mutable_tensors() -> bool: ...
def use_ilistref_for_tensor_lists() -> bool: ...
def parametrize(*, use_const_ref_for_mutable_tensors: bool, use_ilistref_for_tensor_lists: bool) -> Iterator[None]: ...
