from ..core import Format as Format

class BaseGrabFormat(Format):
    """Base format for grab formats."""
    def __init__(self, *args, **kwargs) -> None: ...
    class Reader(Format.Reader): ...

class ScreenGrabFormat(BaseGrabFormat):
    '''The ScreenGrabFormat provided a means to grab screenshots using
    the uri of "<screen>".

    This functionality is provided via Pillow. Note that "<screen>" is
    only supported on Windows and OS X.

    Parameters for reading
    ----------------------
    No parameters.
    '''
class ClipboardGrabFormat(BaseGrabFormat):
    '''The ClipboardGrabFormat provided a means to grab image data from
    the clipboard, using the uri "<clipboard>"

    This functionality is provided via Pillow. Note that "<clipboard>" is
    only supported on Windows.

    Parameters for reading
    ----------------------
    No parameters.
    '''
