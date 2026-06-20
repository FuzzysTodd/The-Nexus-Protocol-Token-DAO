from _typeshed import Incomplete
from torch.utils.data.datapipes.datapipe import IterDataPipe
from typing import Iterator, List, Sequence

__all__ = ['FileListerIterDataPipe']

class FileListerIterDataPipe(IterDataPipe[str]):
    '''
    Given path(s) to the root directory, yields file pathname(s) (path + filename) of files within the root directory.
    Multiple root directories can be provided (functional name: ``list_files``).

    Args:
        root: Root directory or a sequence of root directories
        masks: Unix style filter string or string list for filtering file name(s)
        recursive: Whether to return pathname from nested directories or not
        abspath: Whether to return relative pathname or absolute pathname
        non_deterministic: Whether to return pathname in sorted order or not.
            If ``False``, the results yielded from each root directory will be sorted
        length: Nominal length of the datapipe

    Example:
        >>> # xdoctest: +SKIP
        >>> from torchdata.datapipes.iter import FileLister
        >>> dp = FileLister(root=".", recursive=True)
        >>> list(dp)
        [\'example.py\', \'./data/data.tar\']
    '''
    datapipe: Incomplete
    masks: Incomplete
    recursive: Incomplete
    abspath: Incomplete
    non_deterministic: Incomplete
    length: Incomplete
    def __init__(self, root: str | Sequence[str] | IterDataPipe = '.', masks: str | List[str] = '', *, recursive: bool = False, abspath: bool = False, non_deterministic: bool = False, length: int = -1) -> None: ...
    def __iter__(self) -> Iterator[str]: ...
    def __len__(self) -> int: ...
