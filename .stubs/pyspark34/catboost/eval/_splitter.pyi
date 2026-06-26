from ._fold_storage import FoldStorage as FoldStorage
from _typeshed import Incomplete
from collections.abc import Generator

class _Splitter:
    '''
     Splitter needs providing some parameters to create folds and some "reader",
     that can read source.
    '''
    def __init__(self, line_reader, column_description, seed, min_folds_count) -> None: ...
    def create_fold_sets(self, fold_size, folds_count):
        """Create all folds for all permutations."""
    def fold_groups_files_generator(self, folds_groups, fold_offset) -> Generator[Incomplete, None, None]:
        """Create folds storages for all folds in folds_groups. Generator."""
    def create_fold(self, fold_set, name, id): ...
    def clean_folds(self) -> None: ...
    def clean(self) -> None: ...
    @staticmethod
    def create_name_from_id(name, id, offset: Incomplete | None = None, max_count_digits: int = 4): ...
