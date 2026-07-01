from .domwidget import DOMWidget as DOMWidget
from .trait_types import CByteMemoryView as CByteMemoryView
from .valuewidget import ValueWidget as ValueWidget
from .widget import register as register
from .widget_core import CoreWidget as CoreWidget
from _typeshed import Incomplete

class _Media(DOMWidget, ValueWidget, CoreWidget):
    '''Base class for Image, Audio and Video widgets.

    The `value` of this widget accepts a byte string.  The byte string is the
    raw data that you want the browser to display.

    If you pass `"url"` to the `"format"` trait, `value` will be interpreted
    as a URL as bytes encoded in UTF-8.
    '''
    value: Incomplete
    @classmethod
    def from_url(cls, url, **kwargs):
        """
        Create an :class:`Media` from a URL.

        :code:`Media.from_url(url)` is equivalent to:

        .. code-block: python

            med = Media(value=url, format='url')

        But both unicode and bytes arguments are allowed for ``url``.

        Parameters
        ----------
        url: [str, bytes]
            The location of a URL to load.
        """
    def set_value_from_file(self, filename) -> None:
        """
        Convenience method for reading a file into `value`.

        Parameters
        ----------
        filename: str
            The location of a file to read into value from disk.
        """

class Image(_Media):
    '''Displays an image as a widget.

    The `value` of this widget accepts a byte string.  The byte string is the
    raw image data that you want the browser to display.  You can explicitly
    define the format of the byte string using the `format` trait (which
    defaults to "png").

    If you pass `"url"` to the `"format"` trait, `value` will be interpreted
    as a URL as bytes encoded in UTF-8.
    '''
    format: Incomplete
    width: Incomplete
    height: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...
    @classmethod
    def from_file(cls, filename, **kwargs): ...

class Video(_Media):
    '''Displays a video as a widget.

    The `value` of this widget accepts a byte string.  The byte string is the
    raw video data that you want the browser to display.  You can explicitly
    define the format of the byte string using the `format` trait (which
    defaults to "mp4").

    If you pass `"url"` to the `"format"` trait, `value` will be interpreted
    as a URL as bytes encoded in UTF-8.
    '''
    format: Incomplete
    width: Incomplete
    height: Incomplete
    autoplay: Incomplete
    loop: Incomplete
    controls: Incomplete
    @classmethod
    def from_file(cls, filename, **kwargs): ...

class Audio(_Media):
    '''Displays a audio as a widget.

    The `value` of this widget accepts a byte string.  The byte string is the
    raw audio data that you want the browser to display.  You can explicitly
    define the format of the byte string using the `format` trait (which
    defaults to "mp3").

    If you pass `"url"` to the `"format"` trait, `value` will be interpreted
    as a URL as bytes encoded in UTF-8.
    '''
    format: Incomplete
    autoplay: Incomplete
    loop: Incomplete
    controls: Incomplete
    @classmethod
    def from_file(cls, filename, **kwargs): ...
