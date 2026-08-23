from .._serializable import Deserializer as Deserializer, Serializer as Serializer
from ._masker import Masker as Masker
from _typeshed import Incomplete

class FixedComposite(Masker):
    """ A masker that outputs both the masked data and the original data as a pair.
    """
    masker: Incomplete
    def __init__(self, masker) -> None:
        """ Creates a Composite masker from an underlying masker and returns the original args along with the masked output.

        Parameters
        ----------
        masker: object
            An object of the shap.maskers.Masker base class (eg. Text/Image masker).

        Returns
        -------
        tuple
            A tuple consisting of the masked input using the underlying masker appended with the original args in a list.
        """
    def __call__(self, mask, *args):
        """ Computes mask on the args using the masker data attribute and returns tuple containing masked input with args.
        """
    def save(self, out_file) -> None:
        """ Write a FixedComposite masker to a file stream.
        """
    @classmethod
    def load(cls, in_file, instantiate: bool = True):
        """ Load a FixedComposite masker from a file stream.
        """
