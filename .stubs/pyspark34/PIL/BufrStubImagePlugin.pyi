from . import Image as Image, ImageFile as ImageFile

def register_handler(handler) -> None:
    """
    Install application-specific BUFR image handler.

    :param handler: Handler object.
    """

class BufrStubImageFile(ImageFile.StubImageFile):
    format: str
    format_description: str
