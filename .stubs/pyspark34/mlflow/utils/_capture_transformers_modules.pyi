from _typeshed import Incomplete
from mlflow.exceptions import MlflowException as MlflowException
from mlflow.utils._capture_modules import _CaptureImportedModules, parse_args as parse_args, store_imported_modules as store_imported_modules

class _CaptureImportedModulesForHF(_CaptureImportedModules):
    """
    A context manager to capture imported modules by temporarily applying a patch to
    `builtins.__import__` and `importlib.import_module`.
    Used for 'transformers' flavor only.
    """
    module_to_throw: Incomplete
    def __init__(self, module_to_throw) -> None: ...
    def __enter__(self): ...

def main() -> None: ...
