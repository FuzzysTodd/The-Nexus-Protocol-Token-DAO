from .. import CatBoostError as CatBoostError
from ..eval.log_config import get_eval_logger as get_eval_logger
from .utils import make_dirs_if_not_exists as make_dirs_if_not_exists

class FoldStorage:
    """
    Base class.
    """
    default_dir: str
    @staticmethod
    def remove_dir() -> None:
        """
        Remove default directory for folds if there're no files nut models. In other way it raises warning.

        Args:
            :return: Nothing.

        """
    def __init__(self, fold, storage_name, sep, column_description) -> None: ...
    def get_separator(self):
        """
        Args:
            :return: (str) Delimiter for data used when we saved fold to file.

        """
    def column_description(self):
        """
        Args:
            :return: (str) Path to the column description.

        """
    def contains_group_id(self, group_id):
        """
        Args:
            :param group_id: (int) The number of group we want to check.
            :return: True if fold contains line or lines with that group id.

        """
    def open(self) -> None: ...
    def close(self) -> None: ...
    def delete(self) -> None: ...

class _FoldFile(FoldStorage):
    """
    FoldFile is the realisation of the interface of FoldStorage. It always saves data to file before reset them.
    All files place to the special directory 'folds'.
    """
    def __init__(self, fold, storage_name, sep, column_description) -> None: ...
    def path(self): ...
    def add(self, line) -> None: ...
    def add_all(self, lines) -> None: ...
    def open(self) -> None: ...
    def is_opened(self): ...
    def close(self) -> None: ...
    def delete(self) -> None: ...
