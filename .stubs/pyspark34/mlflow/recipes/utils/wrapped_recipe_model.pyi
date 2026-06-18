from _typeshed import Incomplete
from mlflow.pyfunc import PythonModel as PythonModel
from typing import Any, Dict

class WrappedRecipeModel(PythonModel):
    predict_scores_for_all_classes: Incomplete
    predict_prefix: Incomplete
    target_column_class_labels: Incomplete
    def __init__(self, predict_scores_for_all_classes, predict_prefix, target_column_class_labels: Incomplete | None = None) -> None: ...
    def load_context(self, context) -> None: ...
    def predict(self, context, model_input, params: Dict[str, Any] | None = None):
        """
        :param context: A :class:`~PythonModelContext` instance containing artifacts that the model
                        can use to perform inference.
        :param model_input: A pyfunc-compatible input for the model to evaluate.
        :param params: Additional parameters to pass to the model for inference.

                       .. Note:: Experimental: This parameter may change or be removed in a future
                                               release without warning.

        :return: Model predictions.
        """
