from . import config as config, plugins as plugins, v2 as v2, v3 as v3
from .v2 import get_reader as get_reader, get_reader as read, get_writer as get_writer, get_writer as save, help as help, imwrite as imsave, imwrite as imwrite, mimread as mimread, mimwrite as mimsave, mimwrite as mimwrite, mvolread as mvolread, mvolwrite as mvolsave, mvolwrite as mvolwrite, volread as volread, volwrite as volsave, volwrite as volwrite
from .v3 import imiter as imiter, imopen as imopen
from _typeshed import Incomplete

__all__ = ['v2', 'v3', 'config', 'plugins', 'imopen', 'imread', 'imwrite', 'imiter', 'mimread', 'volread', 'mvolread', 'imwrite', 'mimwrite', 'volwrite', 'mvolwrite', 'read', 'save', 'imsave', 'mimsave', 'volsave', 'mvolsave', 'help', 'get_reader', 'get_writer', 'formats', 'show_formats']

formats: Incomplete
show_formats: Incomplete

def imread(uri, format: Incomplete | None = None, **kwargs):
    """imread(uri, format=None, **kwargs)

    Reads an image from the specified file. Returns a numpy array, which
    comes with a dict of meta data at its 'meta' attribute.

    Note that the image data is returned as-is, and may not always have
    a dtype of uint8 (and thus may differ from what e.g. PIL returns).

    Parameters
    ----------
    uri : {str, pathlib.Path, bytes, file}
        The resource to load the image from, e.g. a filename, pathlib.Path,
        http address or file object, see the docs for more info.
    format : str
        The format to use to read the file. By default imageio selects
        the appropriate for you based on the filename and its contents.
    kwargs : ...
        Further keyword arguments are passed to the reader. See :func:`.help`
        to see what arguments are available for a particular format.
    """
