from .settings_static import SettingsStatic as SettingsStatic
from typing import Any, Dict, List, TypedDict
from wandb.proto.wandb_internal_pb2 import ArtifactRecord as ArtifactRecord, UseArtifactRecord as UseArtifactRecord
from wandb.sdk.artifacts.artifact import Artifact as Artifact
from wandb.sdk.data_types._dtypes import TypeRegistry as TypeRegistry
from wandb.sdk.lib.filenames import DIFF_FNAME as DIFF_FNAME, METADATA_FNAME as METADATA_FNAME, REQUIREMENTS_FNAME as REQUIREMENTS_FNAME
from wandb.util import make_artifact_name_safe as make_artifact_name_safe

FROZEN_REQUIREMENTS_FNAME: str
JOB_FNAME: str
JOB_ARTIFACT_TYPE: str

class GitInfo(TypedDict):
    remote: str
    commit: str

class GitSourceDict(TypedDict):
    git: GitInfo
    entrypoint: List[str]
    notebook: bool

class ArtifactSourceDict(TypedDict):
    artifact: str
    entrypoint: List[str]
    notebook: bool

class ImageSourceDict(TypedDict):
    image: str

class JobSourceDict(TypedDict, total=False):
    source_type: str
    source: GitSourceDict | ArtifactSourceDict | ImageSourceDict
    input_types: Dict[str, Any]
    output_types: Dict[str, Any]
    runtime: str | None

class PartialJobSourceDict(TypedDict):
    job_name: str
    job_source_info: JobSourceDict

class ArtifactInfoForJob(TypedDict):
    id: str
    name: str

class JobArtifact(Artifact):
    def __init__(self, name: str, *args: Any, **kwargs: Any) -> None: ...

class JobBuilder:
    def __init__(self, settings: SettingsStatic) -> None: ...
    def set_config(self, config: Dict[str, Any]) -> None: ...
    def set_summary(self, summary: Dict[str, Any]) -> None: ...
    @property
    def disable(self) -> bool: ...
    @disable.setter
    def disable(self, val: bool) -> None: ...
    def build(self) -> Artifact | None: ...

def convert_use_artifact_to_job_source(use_artifact: UseArtifactRecord) -> PartialJobSourceDict: ...
