from . import Image as Image, ImageFile as ImageFile

def register_handler(handler) -> None:
    """
    Install application-specific GRIB image handler.

    :param handler: Handler object.
    """

class GribStubImageFile(ImageFile.StubImageFile):
    format: str
    format_description: str
