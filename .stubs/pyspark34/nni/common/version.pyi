from _typeshed import Incomplete

PYTHON_VERSION: Incomplete
NUMPY_VERSION: Incomplete
TORCH_VERSION: Incomplete
PYTORCH_LIGHTNING_VERSION: Incomplete
TENSORFLOW_VERSION: Incomplete
CLOUDPICKLE_VERSION: Incomplete
JSON_TRICKS_VERSION: Incomplete
PYYAML_VERSION: Incomplete
NNI_VERSION: Incomplete

def version_dump() -> dict[str, tuple[int, int] | None]: ...
def version_check(expect: dict, raise_error: bool = False) -> None: ...
