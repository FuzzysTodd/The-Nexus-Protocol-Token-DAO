from ...wandb_run import Run as LocalRun
from .wb_value import WBValue as WBValue
from _typeshed import Incomplete
from typing import Sequence
from wandb import util as util
from wandb.sdk.artifacts.artifact import Artifact as Artifact
from wandb.sdk.lib import filesystem as filesystem
from wandb.sdk.lib.paths import LogicalPath as LogicalPath

SYS_PLATFORM: Incomplete

class Media(WBValue):
    """A WBValue stored as a file outside JSON that can be rendered in a media panel.

    If necessary, we move or copy the file into the Run's media directory so that it
    gets uploaded.
    """
    def __init__(self, caption: str | None = None) -> None: ...
    @classmethod
    def get_media_subdir(cls) -> str: ...
    @staticmethod
    def captions(media_items: Sequence['Media']) -> bool | Sequence[str | None]: ...
    def is_bound(self) -> bool: ...
    def file_is_set(self) -> bool: ...
    def bind_to_run(self, run: LocalRun, key: int | str, step: int | str, id_: int | str | None = None, ignore_copy_err: bool | None = None) -> None:
        """Bind this object to a particular Run.

        Calling this function is necessary so that we have somewhere specific to put the
        file associated with this object, from which other Runs can refer to it.
        """
    def to_json(self, run: LocalRun | Artifact) -> dict:
        """Serialize the object into a JSON blob.

        Uses run or artifact to store additional data. If `run_or_artifact` is a
        wandb.Run then `self.bind_to_run()` must have been previously been called.

        Args:
            run_or_artifact (wandb.Run | wandb.Artifact): the Run or Artifact for which
                this object should be generating JSON for - this is useful to store
                additional data if needed.

        Returns:
            dict: JSON representation
        """
    @classmethod
    def from_json(cls, json_obj: dict, source_artifact: Artifact) -> Media:
        """Likely will need to override for any more complicated media objects."""
    def __eq__(self, other: object) -> bool:
        """Likely will need to override for any more complicated media objects."""
    @staticmethod
    def path_is_reference(path: str | None) -> bool: ...

class BatchableMedia(Media):
    """Media that is treated in batches.

    E.g. images and thumbnails. Apart from images, we just use these batches to help
    organize files by name in the media directory.
    """
    def __init__(self) -> None: ...
    @classmethod
    def seq_to_json(cls, seq: Sequence['BatchableMedia'], run: LocalRun, key: str, step: int | str) -> dict: ...
