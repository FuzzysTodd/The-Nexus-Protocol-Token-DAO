from mlflow.exceptions import MlflowException as MlflowException
from mlflow.utils.import_hooks import register_post_import_hook as register_post_import_hook

class ModelEvaluatorRegistry:
    """
    Scheme-based registry for model evaluator implementations
    """
    def __init__(self) -> None: ...
    def register(self, scheme, evaluator) -> None:
        """Register model evaluator provided by other packages"""
    def register_entrypoints(self) -> None: ...
    def get_evaluator(self, evaluator_name):
        """
        Get an evaluator instance from the registry based on the name of evaluator
        """

def register_evaluators(module) -> None: ...
