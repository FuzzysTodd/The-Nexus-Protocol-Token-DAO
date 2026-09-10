from _typeshed import Incomplete

class Iterator:
    """
    This class implements an iterator object that can be used to loop
    over an image sequence.

    You can use the ``[]`` operator to access elements by index. This operator
    will raise an :py:exc:`IndexError` if you try to access a nonexistent
    frame.

    :param im: An image object.
    """
    im: Incomplete
    position: Incomplete
    def __init__(self, im) -> None: ...
    def __getitem__(self, ix): ...
    def __iter__(self): ...
    def __next__(self): ...

def all_frames(im, func: Incomplete | None = None):
    """
    Applies a given function to all frames in an image or a list of images.
    The frames are returned as a list of separate images.

    :param im: An image, or a list of images.
    :param func: The function to apply to all of the image frames.
    :returns: A list of images.
    """
