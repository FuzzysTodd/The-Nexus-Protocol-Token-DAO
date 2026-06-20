from _typeshed import Incomplete
from typing import Any

conf: dict[str, dict[str, Any]]
default_conf_dir: Incomplete
conf_dir: Incomplete

def set_conf_env(conf_dict, envdict=...) -> None:
    """Set config values from environment variables

    Looks for variables of the form ``FSSPEC_<protocol>`` and
    ``FSSPEC_<protocol>_<kwarg>``. For ``FSSPEC_<protocol>`` the value is parsed
    as a json dictionary and used to ``update`` the config of the
    corresponding protocol. For ``FSSPEC_<protocol>_<kwarg>`` there is no
    attempt to convert the string value, but the kwarg keys will be lower-cased.

    The ``FSSPEC_<protocol>_<kwarg>`` variables are applied after the
    ``FSSPEC_<protocol>`` ones.

    Parameters
    ----------
    conf_dict : dict(str, dict)
        This dict will be mutated
    envdict : dict-like(str, str)
        Source for the values - usually the real environment
    """
def set_conf_files(cdir, conf_dict) -> None:
    """Set config values from files

    Scans for INI and JSON files in the given dictionary, and uses their
    contents to set the config. In case of repeated values, later values
    win.

    In the case of INI files, all values are strings, and these will not
    be converted.

    Parameters
    ----------
    cdir : str
        Directory to search
    conf_dict : dict(str, dict)
        This dict will be mutated
    """
def apply_config(cls, kwargs, conf_dict: Incomplete | None = None):
    """Supply default values for kwargs when instantiating class

    Augments the passed kwargs, by finding entries in the config dict
    which match the classes ``.protocol`` attribute (one or more str)

    Parameters
    ----------
    cls : file system implementation
    kwargs : dict
    conf_dict : dict of dict
        Typically this is the global configuration

    Returns
    -------
    dict : the modified set of kwargs
    """
