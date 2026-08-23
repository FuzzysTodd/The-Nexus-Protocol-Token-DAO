from _typeshed import Incomplete

class IconCache:
    """Maintain a cache of icons.  If an icon is used more than once by a GUI
    then ensure that only one copy is created.
    """
    def __init__(self, object_factory, qtgui_module) -> None:
        """Initialise the cache."""
    def set_base_dir(self, base_dir) -> None:
        """ Set the base directory to be used for all relative filenames. """
    def get_icon(self, iconset):
        """Return an icon described by the given iconset tag."""

class _IconSet:
    """An icon set, ie. the mode and state and the pixmap used for each."""
    icon: Incomplete
    def __init__(self, iconset, base_dir) -> None:
        """Initialise the icon set from an XML tag."""
    def set_icon(self, icon, qtgui_module) -> None:
        """Save the icon and set its attributes."""
    def __eq__(self, other):
        """Compare two icon sets for equality."""
