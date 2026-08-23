from ..utils._exceptions import InvalidMaskerError as InvalidMaskerError
from ._masker import Masker as Masker
from _typeshed import Incomplete

class Composite(Masker):
    """ This merges several maskers for different inputs together into a single composite masker.

    This is not yet implemented.
    """
    maskers: Incomplete
    arg_counts: Incomplete
    total_args: int
    text_data: bool
    image_data: bool
    clustering: Incomplete
    def __init__(self, *maskers) -> None: ...
    def shape(self, *args):
        """ Compute the shape of this masker as the sum of all the sub masker shapes.
        """
    def mask_shapes(self, *args):
        """ The shape of the masks we expect.
        """
    def data_transform(self, *args):
        """ Transform the argument
        """
    def __call__(self, mask, *args): ...

def joint_clustering(self, *args):
    """ Return a joint clustering that merges the clusterings of all the submaskers.
    """
