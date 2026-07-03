from _typeshed import Incomplete
from pip._internal.models.format_control import FormatControl as FormatControl

class SelectionPreferences:
    """
    Encapsulates the candidate selection preferences for downloading
    and installing files.
    """
    allow_yanked: Incomplete
    allow_all_prereleases: Incomplete
    format_control: Incomplete
    prefer_binary: Incomplete
    ignore_requires_python: Incomplete
    def __init__(self, allow_yanked: bool, allow_all_prereleases: bool = False, format_control: FormatControl | None = None, prefer_binary: bool = False, ignore_requires_python: bool | None = None) -> None:
        '''Create a SelectionPreferences object.

        :param allow_yanked: Whether files marked as yanked (in the sense
            of PEP 592) are permitted to be candidates for install.
        :param format_control: A FormatControl object or None. Used to control
            the selection of source packages / binary packages when consulting
            the index and links.
        :param prefer_binary: Whether to prefer an old, but valid, binary
            dist over a new source dist.
        :param ignore_requires_python: Whether to ignore incompatible
            "Requires-Python" values in links. Defaults to False.
        '''
