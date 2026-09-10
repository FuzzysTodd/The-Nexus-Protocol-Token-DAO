from .._serializable import Serializable as Serializable

class Masker(Serializable):
    """ This is the superclass of all maskers.
    """
    def __call__(self, mask, *args) -> None:
        """ Maskers are callable objects that accept the same inputs as the model plus a binary mask.
        """
