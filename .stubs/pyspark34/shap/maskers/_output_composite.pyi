from .._serializable import Deserializer as Deserializer, Serializer as Serializer
from ._masker import Masker as Masker
from _typeshed import Incomplete

class OutputComposite(Masker):
    """ A masker that is a combination of a masker and a model and outputs both masked args and the model's output.
    """
    masker: Incomplete
    model: Incomplete
    def __init__(self, masker, model) -> None:
        """ Creates a masker from an underlying masker and and model.

        This masker returns the masked input along with the model output for the passed args.

        Parameters
        ----------
        masker: object
            An object of the shap.maskers.Masker base class (eg. Text/Image masker).

        model: object
            An object shap.models.Model base class used to generate output.

        Returns
        -------
        tuple
            A tuple consisting of the masked input using the underlying masker appended with the model output for passed args.
        """
    def __call__(self, mask, *args):
        """ Mask the args using the masker and return a tuple containing the masked input and the model output on the args.
        """
    def save(self, out_file) -> None:
        """ Write a OutputComposite masker to a file stream.
        """
    @classmethod
    def load(cls, in_file, instantiate: bool = True):
        """ Load a OutputComposite masker from a file stream.
        """
