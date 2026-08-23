from ..wandb_run import Run as LocalRun
from ._private import MEDIA_TMP as MEDIA_TMP
from .base_types.wb_value import WBValue as WBValue
from typing import Any, Generic, List, TypeVar
from wandb import util as util
from wandb.sdk.artifacts.artifact import Artifact as Artifact
from wandb.sdk.lib import runid as runid
from wandb.sdk.lib.hashutil import md5_file_hex as md5_file_hex
from wandb.sdk.lib.paths import LogicalPath as LogicalPath

DEBUG_MODE: bool
SavedModelObjType = TypeVar('SavedModelObjType')

class _SavedModel(WBValue, Generic[SavedModelObjType]):
    """Internal W&B Artifact model storage.

    _model_type_id: (str) The id of the SavedModel subclass used to serialize the model.
    """
    def __init__(self, obj_or_path: SavedModelObjType | str, **kwargs: Any) -> None: ...
    @staticmethod
    def init(obj_or_path: Any, **kwargs: Any) -> _SavedModel: ...
    @classmethod
    def from_json(cls, json_obj: dict, source_artifact: Artifact) -> _SavedModel: ...
    def to_json(self, run_or_artifact: LocalRun | Artifact) -> dict: ...
    def model_obj(self) -> SavedModelObjType:
        """Return the model object."""
PicklingSavedModelObjType = TypeVar('PicklingSavedModelObjType')

class _PicklingSavedModel(_SavedModel[SavedModelObjType]):
    def __init__(self, obj_or_path: SavedModelObjType | str, dep_py_files: List[str] | None = None) -> None: ...
    @classmethod
    def from_json(cls, json_obj: dict, source_artifact: Artifact) -> _PicklingSavedModel: ...
    def to_json(self, run_or_artifact: LocalRun | Artifact) -> dict: ...

class _PytorchSavedModel(_PicklingSavedModel['torch.nn.Module']): ...
class _SklearnSavedModel(_PicklingSavedModel['sklearn.base.BaseEstimator']): ...
class _TensorflowKerasSavedModel(_SavedModel['tensorflow.keras.Model']): ...
