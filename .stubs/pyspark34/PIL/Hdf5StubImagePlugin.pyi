from . import Image as Image, ImageFile as ImageFile

def register_handler(handler) -> None:
    """
    Install application-specific HDF5 image handler.

    :param handler: Handler object.
    """

class HDF5StubImageFile(ImageFile.StubImageFile):
    format: str
    format_description: str
