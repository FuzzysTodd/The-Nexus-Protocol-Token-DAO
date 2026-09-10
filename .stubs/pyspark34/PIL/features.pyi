from . import Image as Image
from _typeshed import Incomplete

modules: Incomplete

def check_module(feature):
    """
    Checks if a module is available.

    :param feature: The module to check for.
    :returns: ``True`` if available, ``False`` otherwise.
    :raises ValueError: If the module is not defined in this version of Pillow.
    """
def version_module(feature):
    """
    :param feature: The module to check for.
    :returns:
        The loaded version number as a string, or ``None`` if unknown or not available.
    :raises ValueError: If the module is not defined in this version of Pillow.
    """
def get_supported_modules():
    """
    :returns: A list of all supported modules.
    """

codecs: Incomplete

def check_codec(feature):
    """
    Checks if a codec is available.

    :param feature: The codec to check for.
    :returns: ``True`` if available, ``False`` otherwise.
    :raises ValueError: If the codec is not defined in this version of Pillow.
    """
def version_codec(feature):
    """
    :param feature: The codec to check for.
    :returns:
        The version number as a string, or ``None`` if not available.
        Checked at compile time for ``jpg``, run-time otherwise.
    :raises ValueError: If the codec is not defined in this version of Pillow.
    """
def get_supported_codecs():
    """
    :returns: A list of all supported codecs.
    """

features: Incomplete

def check_feature(feature):
    """
    Checks if a feature is available.

    :param feature: The feature to check for.
    :returns: ``True`` if available, ``False`` if unavailable, ``None`` if unknown.
    :raises ValueError: If the feature is not defined in this version of Pillow.
    """
def version_feature(feature):
    """
    :param feature: The feature to check for.
    :returns: The version number as a string, or ``None`` if not available.
    :raises ValueError: If the feature is not defined in this version of Pillow.
    """
def get_supported_features():
    """
    :returns: A list of all supported features.
    """
def check(feature):
    """
    :param feature: A module, codec, or feature name.
    :returns:
        ``True`` if the module, codec, or feature is available,
        ``False`` or ``None`` otherwise.
    """
def version(feature):
    """
    :param feature:
        The module, codec, or feature to check for.
    :returns:
        The version number as a string, or ``None`` if unknown or not available.
    """
def get_supported():
    """
    :returns: A list of all supported modules, features, and codecs.
    """
def pilinfo(out: Incomplete | None = None, supported_formats: bool = True) -> None:
    """
    Prints information about this installation of Pillow.
    This function can be called with ``python3 -m PIL``.

    :param out:
        The output stream to print to. Defaults to ``sys.stdout`` if ``None``.
    :param supported_formats:
        If ``True``, a list of all supported image file formats will be printed.
    """
