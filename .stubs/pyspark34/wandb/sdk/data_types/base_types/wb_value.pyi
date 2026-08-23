from ...wandb_run import Run as LocalRun
from _typeshed import Incomplete
from typing import Any, List
from wandb import util as util
from wandb.sdk.artifacts.artifact import Artifact as Artifact

TypeMappingType: Incomplete

class _WBValueArtifactSource:
    artifact: Artifact
    name: str | None
    def __init__(self, artifact: Artifact, name: str | None = None) -> None: ...

class _WBValueArtifactTarget:
    artifact: Artifact
    name: str | None
    def __init__(self, artifact: Artifact, name: str | None = None) -> None: ...

class WBValue:
    """Typed objects that can be logged with `wandb.log()` and visualized by wandb.

    The objects will be serialized as JSON and always have a _type attribute that
    indicates how to interpret the other fields.
    """
    def __init__(self) -> None: ...
    def to_json(self, run_or_artifact: LocalRun | Artifact) -> dict:
        """Serialize the object into a JSON blob.

        Uses current run or artifact to store additional data.

        Args:
            run_or_artifact (wandb.Run | wandb.Artifact): the Run or Artifact for which
                this object should be generating JSON for - this is useful to to store
                additional data if needed.

        Returns:
            dict: JSON representation
        """
    @classmethod
    def from_json(cls, json_obj: dict, source_artifact: Artifact) -> WBValue:
        """Deserialize a `json_obj` into it's class representation.

        If additional resources were stored in the `run_or_artifact` artifact during the
        `to_json` call, then those resources should be in the `source_artifact`.

        Args:
            json_obj (dict): A JSON dictionary to deserialize source_artifact
            (wandb.Artifact): An artifact which will hold any additional
                resources which were stored during the `to_json` function.
        """
    @classmethod
    def with_suffix(cls, name: str, filetype: str = 'json') -> str:
        '''Get the name with the appropriate suffix.

        Args:
            name (str): the name of the file
            filetype (str, optional): the filetype to use. Defaults to "json".

        Returns:
            str: a filename which is suffixed with it\'s `_log_type` followed by the
                filetype.
        '''
    @staticmethod
    def init_from_json(json_obj: dict, source_artifact: Artifact) -> WBValue | None:
        """Initialize a `WBValue` from a JSON blob based on the class that creatd it.

        Looks through all subclasses and tries to match the json obj with the class
        which created it. It will then call that subclass' `from_json` method.
        Importantly, this function will set the return object's `source_artifact`
        attribute to the passed in source artifact. This is critical for artifact
        bookkeeping. If you choose to create a wandb.Value via it's `from_json` method,
        make sure to properly set this `artifact_source` to avoid data duplication.

        Args:
            json_obj (dict): A JSON dictionary to deserialize. It must contain a `_type`
                key. This is used to lookup the correct subclass to use.
            source_artifact (wandb.Artifact): An artifact which will hold any additional
                resources which were stored during the `to_json` function.

        Returns:
            wandb.Value: a newly created instance of a subclass of wandb.Value
        """
    @staticmethod
    def type_mapping() -> TypeMappingType:
        """Return a map from `_log_type` to subclass. Used to lookup correct types for deserialization.

        Returns:
            dict: dictionary of str:class
        """
    def __eq__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    def to_data_array(self) -> List[Any]:
        """Convert the object to a list of primitives representing the underlying data."""
