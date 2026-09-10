from . import base
from git.types import Literal

__all__ = ['Blob']

class Blob(base.IndexObject):
    """A Blob encapsulates a git blob object"""
    DEFAULT_MIME_TYPE: str
    type: Literal['blob']
    executable_mode: int
    file_mode: int
    link_mode: int
    @property
    def mime_type(self) -> str:
        """
        :return: String describing the mime type of this file (based on the filename)
        :note: Defaults to 'text/plain' in case the actual file type is unknown."""
