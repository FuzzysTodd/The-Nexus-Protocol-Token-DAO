from .._serializable import Deserializer as Deserializer, Serializable as Serializable, Serializer as Serializer
from ..utils import record_import_error as record_import_error, safe_isinstance as safe_isinstance
from _typeshed import Incomplete

class Model(Serializable):
    """ This is the superclass of all models.
    """
    inner_model: Incomplete
    output_names: Incomplete
    def __init__(self, model: Incomplete | None = None) -> None:
        """ Wrap a callable model as a SHAP Model object.
        """
    def __call__(self, *args): ...
    def save(self, out_file) -> None:
        """ Save the model to the given file stream.
        """
    @classmethod
    def load(cls, in_file, instantiate: bool = True): ...
