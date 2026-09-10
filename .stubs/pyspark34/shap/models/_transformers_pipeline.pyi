from ._model import Model as Model
from _typeshed import Incomplete

class TransformersPipeline(Model):
    """ This wraps a transformers pipeline object for easy explanations.

    By default transformers pipeline object output lists of dictionaries, not standard
    tensors as expected by SHAP. This class wraps pipelines to make them output nice
    tensor formats.
    """
    rescale_to_logits: Incomplete
    label2id: Incomplete
    id2label: Incomplete
    output_shape: Incomplete
    output_names: Incomplete
    def __init__(self, pipeline, rescale_to_logits: bool = False) -> None:
        """ Build a new model by wrapping the given pipeline object.
        """
    def __call__(self, strings): ...
