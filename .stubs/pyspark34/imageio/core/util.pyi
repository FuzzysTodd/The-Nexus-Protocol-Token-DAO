import numpy as np
from _typeshed import Incomplete
from collections import OrderedDict

logger: Incomplete
IS_PYPY: Incomplete
THIS_DIR: Incomplete

def urlopen(*args, **kwargs):
    """Compatibility function for the urlopen function. Raises an
    RuntimeError if urlopen could not be imported (which can occur in
    frozen applications.
    """
def image_as_uint(im, bitdepth: Incomplete | None = None):
    """Convert the given image to uint (default: uint8)

    If the dtype already matches the desired format, it is returned
    as-is. If the image is float, and all values are between 0 and 1,
    the values are multiplied by np.power(2.0, bitdepth). In all other
    situations, the values are scaled such that the minimum value
    becomes 0 and the maximum value becomes np.power(2.0, bitdepth)-1
    (255 for 8-bit and 65535 for 16-bit).
    """

class Array(np.ndarray):
    """Array(array, meta=None)

    A subclass of np.ndarray that has a meta attribute. Get the dictionary
    that contains the meta data using ``im.meta``. Convert to a plain numpy
    array using ``np.asarray(im)``.

    """
    def __new__(cls, array, meta: Incomplete | None = None): ...
    @property
    def meta(self):
        """The dict with the meta data of this image."""
    def __array_finalize__(self, ob) -> None:
        """So the meta info is maintained when doing calculations with
        the array.
        """
    def __array_wrap__(self, out, context: Incomplete | None = None):
        """So that we return a native numpy array (or scalar) when a
        reducting ufunc is applied (such as sum(), std(), etc.)
        """
Image = Array

def asarray(a):
    """Pypy-safe version of np.asarray. Pypy's np.asarray consumes a
    *lot* of memory if the given array is an ndarray subclass. This
    function does not.
    """

class Dict(OrderedDict):
    """A dict in which the keys can be get and set as if they were
    attributes. Very convenient in combination with autocompletion.

    This Dict still behaves as much as possible as a normal dict, and
    keys can be anything that are otherwise valid keys. However,
    keys that are not valid identifiers or that are names of the dict
    class (such as 'items' and 'copy') cannot be get/set as attributes.
    """
    __reserved_names__: Incomplete
    __pure_names__: Incomplete
    def __getattribute__(self, key): ...
    def __setattr__(self, key, val): ...
    def __dir__(self): ...

class BaseProgressIndicator:
    """BaseProgressIndicator(name)

    A progress indicator helps display the progres of a task to the
    user. Progress can be pending, running, finished or failed.

    Each task has:
      * a name - a short description of what needs to be done.
      * an action - the current action in performing the task (e.g. a subtask)
      * progress - how far the task is completed
      * max - max number of progress units. If 0, the progress is indefinite
      * unit - the units in which the progress is counted
      * status - 0: pending, 1: in progress, 2: finished, 3: failed

    This class defines an abstract interface. Subclasses should implement
    _start, _stop, _update_progress(progressText), _write(message).
    """
    def __init__(self, name) -> None: ...
    def start(self, action: str = '', unit: str = '', max: int = 0) -> None:
        """start(action='', unit='', max=0)

        Start the progress. Optionally specify an action, a unit,
        and a maxium progress value.
        """
    def status(self):
        """status()

        Get the status of the progress - 0: pending, 1: in progress,
        2: finished, 3: failed
        """
    def set_progress(self, progress: int = 0, force: bool = False) -> None:
        """set_progress(progress=0, force=False)

        Set the current progress. To avoid unnecessary progress updates
        this will only have a visual effect if the time since the last
        update is > 0.1 seconds, or if force is True.
        """
    def increase_progress(self, extra_progress) -> None:
        """increase_progress(extra_progress)

        Increase the progress by a certain amount.
        """
    def finish(self, message: Incomplete | None = None) -> None:
        """finish(message=None)

        Finish the progress, optionally specifying a message. This will
        not set the progress to the maximum.
        """
    def fail(self, message: Incomplete | None = None) -> None:
        """fail(message=None)

        Stop the progress with a failure, optionally specifying a message.
        """
    def write(self, message):
        """write(message)

        Write a message during progress (such as a warning).
        """

class StdoutProgressIndicator(BaseProgressIndicator):
    """StdoutProgressIndicator(name)

    A progress indicator that shows the progress in stdout. It
    assumes that the tty can appropriately deal with backspace
    characters.
    """

def appdata_dir(appname: Incomplete | None = None, roaming: bool = False):
    """appdata_dir(appname=None, roaming=False)

    Get the path to the application directory, where applications are allowed
    to write user specific files (e.g. configurations). For non-user specific
    data, consider using common_appdata_dir().
    If appname is given, a subdir is appended (and created if necessary).
    If roaming is True, will prefer a roaming directory (Windows Vista/7).
    """
def resource_dirs():
    '''resource_dirs()

    Get a list of directories where imageio resources may be located.
    The first directory in this list is the "resources" directory in
    the package itself. The second directory is the appdata directory
    (~/.imageio on Linux). The list further contains the application
    directory (for frozen apps), and may include additional directories
    in the future.
    '''
def resource_package_dir():
    """package_dir

    Get the resources directory in the imageio package installation
    directory.

    Notes
    -----
    This is a convenience method that is used by `resource_dirs` and
    imageio entry point scripts.
    """
def get_platform():
    """get_platform()

    Get a string that specifies the platform more specific than
    sys.platform does. The result can be: linux32, linux64, win32,
    win64, osx32, osx64. Other platforms may be added in the future.
    """
def has_module(module_name):
    """Check to see if a python module is available."""
