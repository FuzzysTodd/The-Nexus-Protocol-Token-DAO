from . import Image as Image
from _typeshed import Incomplete

def register(viewer, order: int = 1) -> None:
    """
    The :py:func:`register` function is used to register additional viewers::

        from PIL import ImageShow
        ImageShow.register(MyViewer())  # MyViewer will be used as a last resort
        ImageShow.register(MySecondViewer(), 0)  # MySecondViewer will be prioritised
        ImageShow.register(ImageShow.XVViewer(), 0)  # XVViewer will be prioritised

    :param viewer: The viewer to be registered.
    :param order:
        Zero or a negative integer to prepend this viewer to the list,
        a positive integer to append it.
    """
def show(image, title: Incomplete | None = None, **options):
    """
    Display a given image.

    :param image: An image object.
    :param title: Optional title. Not all viewers can display the title.
    :param \\**options: Additional viewer options.
    :returns: ``True`` if a suitable viewer was found, ``False`` otherwise.
    """

class Viewer:
    """Base class for viewers."""
    def show(self, image, **options):
        """
        The main function for displaying an image.
        Converts the given image to the target format and displays it.
        """
    format: Incomplete
    options: Incomplete
    def get_format(self, image):
        """Return format name, or ``None`` to save as PGM/PPM."""
    def get_command(self, file, **options) -> None:
        """
        Returns the command used to display the file.
        Not implemented in the base class.
        """
    def save_image(self, image):
        """Save to temporary file and return filename."""
    def show_image(self, image, **options):
        """Display the given image."""
    def show_file(self, path, **options):
        """
        Display given file.
        """

class WindowsViewer(Viewer):
    """The default viewer on Windows is the default system application for PNG files."""
    format: str
    options: Incomplete
    def get_command(self, file, **options): ...

class MacViewer(Viewer):
    """The default viewer on macOS using ``Preview.app``."""
    format: str
    options: Incomplete
    def get_command(self, file, **options): ...
    def show_file(self, path, **options):
        """
        Display given file.
        """

class UnixViewer(Viewer):
    format: str
    options: Incomplete
    def get_command(self, file, **options): ...

class XDGViewer(UnixViewer):
    """
    The freedesktop.org ``xdg-open`` command.
    """
    def get_command_ex(self, file, **options): ...
    def show_file(self, path, **options):
        """
        Display given file.
        """

class DisplayViewer(UnixViewer):
    """
    The ImageMagick ``display`` command.
    This viewer supports the ``title`` parameter.
    """
    def get_command_ex(self, file, title: Incomplete | None = None, **options): ...
    def show_file(self, path, **options):
        """
        Display given file.
        """

class GmDisplayViewer(UnixViewer):
    """The GraphicsMagick ``gm display`` command."""
    def get_command_ex(self, file, **options): ...
    def show_file(self, path, **options):
        """
        Display given file.
        """

class EogViewer(UnixViewer):
    """The GNOME Image Viewer ``eog`` command."""
    def get_command_ex(self, file, **options): ...
    def show_file(self, path, **options):
        """
        Display given file.
        """

class XVViewer(UnixViewer):
    """
    The X Viewer ``xv`` command.
    This viewer supports the ``title`` parameter.
    """
    def get_command_ex(self, file, title: Incomplete | None = None, **options): ...
    def show_file(self, path, **options):
        """
        Display given file.
        """

class IPythonViewer(Viewer):
    """The viewer for IPython frontends."""
    def show_image(self, image, **options): ...
