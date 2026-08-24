import pathlib
import typing

def path_match_suffix_ignore_case(path: pathlib.Path | str, suffix: str) -> bool:
    """
    Returns whether `path` ends in `suffix`, ignoring case.
    """
def files_from_file_or_dir(file_or_dir_path: pathlib.Path | str, predicate: typing.Callable[[pathlib.Path], bool] = ...) -> typing.List[pathlib.Path]:
    """
    Gets the files in `file_or_dir_path` satisfying `predicate`.
    If `file_or_dir_path` is a file, the single file is considered. Otherwise, all files in the directory are
    considered.
    :param file_or_dir_path: Path to a file or directory.
    :param predicate: Predicate to determine if a file is included.
    :return: A list of files.
    """
