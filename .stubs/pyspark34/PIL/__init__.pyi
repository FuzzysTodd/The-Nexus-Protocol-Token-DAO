from _typeshed import Incomplete

__version__: Incomplete

class UnidentifiedImageError(OSError):
    """
    Raised in :py:meth:`PIL.Image.open` if an image cannot be opened and identified.

    If a PNG image raises this error, setting :data:`.ImageFile.LOAD_TRUNCATED_IMAGES`
    to true may allow the image to be opened after all. The setting will ignore missing
    data and checksum failures.
    """
