import abc
from openpyxl.compat.abc import ABC as ABC

class ISerialisableFile(ABC, metaclass=abc.ABCMeta):
    """
    Interface for Serialisable classes that represent files in the archive
    """
    @property
    @abc.abstractmethod
    def id(self):
        """
        Object id making it unique
        """
