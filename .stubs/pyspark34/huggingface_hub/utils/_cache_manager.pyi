from . import logging as logging
from ..constants import HUGGINGFACE_HUB_CACHE as HUGGINGFACE_HUB_CACHE
from _typeshed import Incomplete
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, FrozenSet, List

logger: Incomplete
REPO_TYPE_T: Incomplete

class CacheNotFound(Exception):
    """Exception thrown when the Huggingface cache is not found."""
    cache_dir: str | Path
    def __init__(self, msg: str, cache_dir: str | Path, *args, **kwargs) -> None: ...

class CorruptedCacheException(Exception):
    """Exception for any unexpected structure in the Huggingface cache-system."""

@dataclass(frozen=True)
class CachedFileInfo:
    """Frozen data structure holding information about a single cached file.

    Args:
        file_name (`str`):
            Name of the file. Example: `config.json`.
        file_path (`Path`):
            Path of the file in the `snapshots` directory. The file path is a symlink
            referring to a blob in the `blobs` folder.
        blob_path (`Path`):
            Path of the blob file. This is equivalent to `file_path.resolve()`.
        size_on_disk (`int`):
            Size of the blob file in bytes.
        blob_last_accessed (`float`):
            Timestamp of the last time the blob file has been accessed (from any
            revision).
        blob_last_modified (`float`):
            Timestamp of the last time the blob file has been modified/created.

    <Tip warning={true}>

    `blob_last_accessed` and `blob_last_modified` reliability can depend on the OS you
    are using. See [python documentation](https://docs.python.org/3/library/os.html#os.stat_result)
    for more details.

    </Tip>
    """
    file_name: str
    file_path: Path
    blob_path: Path
    size_on_disk: int
    blob_last_accessed: float
    blob_last_modified: float
    @property
    def blob_last_accessed_str(self) -> str:
        '''
        (property) Timestamp of the last time the blob file has been accessed (from any
        revision), returned as a human-readable string.

        Example: "2 weeks ago".
        '''
    @property
    def blob_last_modified_str(self) -> str:
        '''
        (property) Timestamp of the last time the blob file has been modified, returned
        as a human-readable string.

        Example: "2 weeks ago".
        '''
    @property
    def size_on_disk_str(self) -> str:
        '''
        (property) Size of the blob file as a human-readable string.

        Example: "42.2K".
        '''
    def __init__(self, file_name, file_path, blob_path, size_on_disk, blob_last_accessed, blob_last_modified) -> None: ...

@dataclass(frozen=True)
class CachedRevisionInfo:
    '''Frozen data structure holding information about a revision.

    A revision correspond to a folder in the `snapshots` folder and is populated with
    the exact tree structure as the repo on the Hub but contains only symlinks. A
    revision can be either referenced by 1 or more `refs` or be "detached" (no refs).

    Args:
        commit_hash (`str`):
            Hash of the revision (unique).
            Example: `"9338f7b671827df886678df2bdd7cc7b4f36dffd"`.
        snapshot_path (`Path`):
            Path to the revision directory in the `snapshots` folder. It contains the
            exact tree structure as the repo on the Hub.
        files: (`FrozenSet[CachedFileInfo]`):
            Set of [`~CachedFileInfo`] describing all files contained in the snapshot.
        refs (`FrozenSet[str]`):
            Set of `refs` pointing to this revision. If the revision has no `refs`, it
            is considered detached.
            Example: `{"main", "2.4.0"}` or `{"refs/pr/1"}`.
        size_on_disk (`int`):
            Sum of the blob file sizes that are symlink-ed by the revision.
        last_modified (`float`):
            Timestamp of the last time the revision has been created/modified.

    <Tip warning={true}>

    `last_accessed` cannot be determined correctly on a single revision as blob files
    are shared across revisions.

    </Tip>

    <Tip warning={true}>

    `size_on_disk` is not necessarily the sum of all file sizes because of possible
    duplicated files. Besides, only blobs are taken into account, not the (negligible)
    size of folders and symlinks.

    </Tip>
    '''
    commit_hash: str
    snapshot_path: Path
    size_on_disk: int
    files: FrozenSet[CachedFileInfo]
    refs: FrozenSet[str]
    last_modified: float
    @property
    def last_modified_str(self) -> str:
        '''
        (property) Timestamp of the last time the revision has been modified, returned
        as a human-readable string.

        Example: "2 weeks ago".
        '''
    @property
    def size_on_disk_str(self) -> str:
        '''
        (property) Sum of the blob file sizes as a human-readable string.

        Example: "42.2K".
        '''
    @property
    def nb_files(self) -> int:
        """
        (property) Total number of files in the revision.
        """
    def __init__(self, commit_hash, snapshot_path, size_on_disk, files, refs, last_modified) -> None: ...

@dataclass(frozen=True)
class CachedRepoInfo:
    '''Frozen data structure holding information about a cached repository.

    Args:
        repo_id (`str`):
            Repo id of the repo on the Hub. Example: `"google/fleurs"`.
        repo_type (`Literal["dataset", "model", "space"]`):
            Type of the cached repo.
        repo_path (`Path`):
            Local path to the cached repo.
        size_on_disk (`int`):
            Sum of the blob file sizes in the cached repo.
        nb_files (`int`):
            Total number of blob files in the cached repo.
        revisions (`FrozenSet[CachedRevisionInfo]`):
            Set of [`~CachedRevisionInfo`] describing all revisions cached in the repo.
        last_accessed (`float`):
            Timestamp of the last time a blob file of the repo has been accessed.
        last_modified (`float`):
            Timestamp of the last time a blob file of the repo has been modified/created.

    <Tip warning={true}>

    `size_on_disk` is not necessarily the sum of all revisions sizes because of
    duplicated files. Besides, only blobs are taken into account, not the (negligible)
    size of folders and symlinks.

    </Tip>

    <Tip warning={true}>

    `last_accessed` and `last_modified` reliability can depend on the OS you are using.
    See [python documentation](https://docs.python.org/3/library/os.html#os.stat_result)
    for more details.

    </Tip>
    '''
    repo_id: str
    repo_type: REPO_TYPE_T
    repo_path: Path
    size_on_disk: int
    nb_files: int
    revisions: FrozenSet[CachedRevisionInfo]
    last_accessed: float
    last_modified: float
    @property
    def last_accessed_str(self) -> str:
        '''
        (property) Last time a blob file of the repo has been accessed, returned as a
        human-readable string.

        Example: "2 weeks ago".
        '''
    @property
    def last_modified_str(self) -> str:
        '''
        (property) Last time a blob file of the repo has been modified, returned as a
        human-readable string.

        Example: "2 weeks ago".
        '''
    @property
    def size_on_disk_str(self) -> str:
        '''
        (property) Sum of the blob file sizes as a human-readable string.

        Example: "42.2K".
        '''
    @property
    def refs(self) -> Dict[str, CachedRevisionInfo]:
        """
        (property) Mapping between `refs` and revision data structures.
        """
    def __init__(self, repo_id, repo_type, repo_path, size_on_disk, nb_files, revisions, last_accessed, last_modified) -> None: ...

@dataclass(frozen=True)
class DeleteCacheStrategy:
    """Frozen data structure holding the strategy to delete cached revisions.

    This object is not meant to be instantiated programmatically but to be returned by
    [`~utils.HFCacheInfo.delete_revisions`]. See documentation for usage example.

    Args:
        expected_freed_size (`float`):
            Expected freed size once strategy is executed.
        blobs (`FrozenSet[Path]`):
            Set of blob file paths to be deleted.
        refs (`FrozenSet[Path]`):
            Set of reference file paths to be deleted.
        repos (`FrozenSet[Path]`):
            Set of entire repo paths to be deleted.
        snapshots (`FrozenSet[Path]`):
            Set of snapshots to be deleted (directory of symlinks).
    """
    expected_freed_size: int
    blobs: FrozenSet[Path]
    refs: FrozenSet[Path]
    repos: FrozenSet[Path]
    snapshots: FrozenSet[Path]
    @property
    def expected_freed_size_str(self) -> str:
        '''
        (property) Expected size that will be freed as a human-readable string.

        Example: "42.2K".
        '''
    def execute(self) -> None:
        """Execute the defined strategy.

        <Tip warning={true}>

        If this method is interrupted, the cache might get corrupted. Deletion order is
        implemented so that references and symlinks are deleted before the actual blob
        files.

        </Tip>

        <Tip warning={true}>

        This method is irreversible. If executed, cached files are erased and must be
        downloaded again.

        </Tip>
        """
    def __init__(self, expected_freed_size, blobs, refs, repos, snapshots) -> None: ...

@dataclass(frozen=True)
class HFCacheInfo:
    """Frozen data structure holding information about the entire cache-system.

    This data structure is returned by [`scan_cache_dir`] and is immutable.

    Args:
        size_on_disk (`int`):
            Sum of all valid repo sizes in the cache-system.
        repos (`FrozenSet[CachedRepoInfo]`):
            Set of [`~CachedRepoInfo`] describing all valid cached repos found on the
            cache-system while scanning.
        warnings (`List[CorruptedCacheException]`):
            List of [`~CorruptedCacheException`] that occurred while scanning the cache.
            Those exceptions are captured so that the scan can continue. Corrupted repos
            are skipped from the scan.

    <Tip warning={true}>

    Here `size_on_disk` is equal to the sum of all repo sizes (only blobs). However if
    some cached repos are corrupted, their sizes are not taken into account.

    </Tip>
    """
    size_on_disk: int
    repos: FrozenSet[CachedRepoInfo]
    warnings: List[CorruptedCacheException]
    @property
    def size_on_disk_str(self) -> str:
        '''
        (property) Sum of all valid repo sizes in the cache-system as a human-readable
        string.

        Example: "42.2K".
        '''
    def delete_revisions(self, *revisions: str) -> DeleteCacheStrategy:
        '''Prepare the strategy to delete one or more revisions cached locally.

        Input revisions can be any revision hash. If a revision hash is not found in the
        local cache, a warning is thrown but no error is raised. Revisions can be from
        different cached repos since hashes are unique across repos,

        Examples:
        ```py
        >>> from huggingface_hub import scan_cache_dir
        >>> cache_info = scan_cache_dir()
        >>> delete_strategy = cache_info.delete_revisions(
        ...     "81fd1d6e7847c99f5862c9fb81387956d99ec7aa"
        ... )
        >>> print(f"Will free {delete_strategy.expected_freed_size_str}.")
        Will free 7.9K.
        >>> delete_strategy.execute()
        Cache deletion done. Saved 7.9K.
        ```

        ```py
        >>> from huggingface_hub import scan_cache_dir
        >>> scan_cache_dir().delete_revisions(
        ...     "81fd1d6e7847c99f5862c9fb81387956d99ec7aa",
        ...     "e2983b237dccf3ab4937c97fa717319a9ca1a96d",
        ...     "6c0e6080953db56375760c0471a8c5f2929baf11",
        ... ).execute()
        Cache deletion done. Saved 8.6G.
        ```

        <Tip warning={true}>

        `delete_revisions` returns a [`~utils.DeleteCacheStrategy`] object that needs to
        be executed. The [`~utils.DeleteCacheStrategy`] is not meant to be modified but
        allows having a dry run before actually executing the deletion.

        </Tip>
        '''
    def __init__(self, size_on_disk, repos, warnings) -> None: ...

def scan_cache_dir(cache_dir: str | Path | None = None) -> HFCacheInfo:
    '''Scan the entire HF cache-system and return a [`~HFCacheInfo`] structure.

    Use `scan_cache_dir` in order to programmatically scan your cache-system. The cache
    will be scanned repo by repo. If a repo is corrupted, a [`~CorruptedCacheException`]
    will be thrown internally but captured and returned in the [`~HFCacheInfo`]
    structure. Only valid repos get a proper report.

    ```py
    >>> from huggingface_hub import scan_cache_dir

    >>> hf_cache_info = scan_cache_dir()
    HFCacheInfo(
        size_on_disk=3398085269,
        repos=frozenset({
            CachedRepoInfo(
                repo_id=\'t5-small\',
                repo_type=\'model\',
                repo_path=PosixPath(...),
                size_on_disk=970726914,
                nb_files=11,
                revisions=frozenset({
                    CachedRevisionInfo(
                        commit_hash=\'d78aea13fa7ecd06c29e3e46195d6341255065d5\',
                        size_on_disk=970726339,
                        snapshot_path=PosixPath(...),
                        files=frozenset({
                            CachedFileInfo(
                                file_name=\'config.json\',
                                size_on_disk=1197
                                file_path=PosixPath(...),
                                blob_path=PosixPath(...),
                            ),
                            CachedFileInfo(...),
                            ...
                        }),
                    ),
                    CachedRevisionInfo(...),
                    ...
                }),
            ),
            CachedRepoInfo(...),
            ...
        }),
        warnings=[
            CorruptedCacheException("Snapshots dir doesn\'t exist in cached repo: ..."),
            CorruptedCacheException(...),
            ...
        ],
    )
    ```

    You can also print a detailed report directly from the `huggingface-cli` using:
    ```text
    > huggingface-cli scan-cache
    REPO ID                     REPO TYPE SIZE ON DISK NB FILES REFS                LOCAL PATH
    --------------------------- --------- ------------ -------- ------------------- -------------------------------------------------------------------------
    glue                        dataset         116.3K       15 1.17.0, main, 2.4.0 /Users/lucain/.cache/huggingface/hub/datasets--glue
    google/fleurs               dataset          64.9M        6 main, refs/pr/1     /Users/lucain/.cache/huggingface/hub/datasets--google--fleurs
    Jean-Baptiste/camembert-ner model           441.0M        7 main                /Users/lucain/.cache/huggingface/hub/models--Jean-Baptiste--camembert-ner
    bert-base-cased             model             1.9G       13 main                /Users/lucain/.cache/huggingface/hub/models--bert-base-cased
    t5-base                     model            10.1K        3 main                /Users/lucain/.cache/huggingface/hub/models--t5-base
    t5-small                    model           970.7M       11 refs/pr/1, main     /Users/lucain/.cache/huggingface/hub/models--t5-small

    Done in 0.0s. Scanned 6 repo(s) for a total of 3.4G.
    Got 1 warning(s) while scanning. Use -vvv to print details.
    ```

    Args:
        cache_dir (`str` or `Path`, `optional`):
            Cache directory to cache. Defaults to the default HF cache directory.

    <Tip warning={true}>

    Raises:

        `CacheNotFound`
          If the cache directory does not exist.

        [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError)
          If the cache directory is a file, instead of a directory.

    </Tip>

    Returns: a [`~HFCacheInfo`] object.
    '''
