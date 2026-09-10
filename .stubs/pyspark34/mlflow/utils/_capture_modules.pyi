from _typeshed import Incomplete
from mlflow.models.model import MLMODEL_FILE_NAME as MLMODEL_FILE_NAME, Model as Model
from mlflow.pyfunc import MAIN as MAIN
from mlflow.utils.file_utils import write_to as write_to
from mlflow.utils.requirements_utils import DATABRICKS_MODULES_TO_PACKAGES as DATABRICKS_MODULES_TO_PACKAGES

class _CaptureImportedModules:
    """
    A context manager to capture imported modules by temporarily applying a patch to
    `builtins.__import__` and `importlib.import_module`.
    """
    imported_modules: Incomplete
    original_import: Incomplete
    original_import_module: Incomplete
    def __init__(self) -> None: ...
    def __enter__(self): ...
    def __exit__(self, *_, **__) -> None: ...

def parse_args(): ...
def store_imported_modules(cap_cm, model_path, flavor, output_file): ...
def main() -> None: ...
