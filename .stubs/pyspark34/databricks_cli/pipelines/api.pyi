from _typeshed import Incomplete
from databricks_cli.dbfs.api import DbfsApi as DbfsApi
from databricks_cli.dbfs.dbfs_path import DbfsPath as DbfsPath
from databricks_cli.sdk import DeltaPipelinesService as DeltaPipelinesService

BUFFER_SIZE: Incomplete
base_pipelines_dir: str

class PipelinesApi:
    client: Incomplete
    dbfs_client: Incomplete
    def __init__(self, api_client) -> None: ...
    def create(self, settings, settings_dir, allow_duplicate_names, headers: Incomplete | None = None): ...
    def edit(self, settings, settings_dir, allow_duplicate_names, headers: Incomplete | None = None) -> None: ...
    def delete(self, pipeline_id, headers: Incomplete | None = None) -> None: ...
    def get(self, pipeline_id, headers: Incomplete | None = None): ...
    def list(self, headers: Incomplete | None = None): ...
    def start_update(self, pipeline_id, full_refresh: Incomplete | None = None, headers: Incomplete | None = None): ...
    def stop(self, pipeline_id, headers: Incomplete | None = None) -> None: ...

class LibraryObject:
    path: Incomplete
    lib_type: Incomplete
    def __init__(self, lib_type, lib_path) -> None: ...
    @classmethod
    def from_json(cls, libraries):
        """
        Serialize Libraries into LibraryObjects
        :param libraries: List[Dictionary{String, String}]
        :return: List[LibraryObject]
        """
    @classmethod
    def to_json(cls, lib_objects):
        """
        Deserialize LibraryObjects
        :param lib_objects: List[LibraryObject]
        :return: List[Dictionary{String, String}]
        """
    def __eq__(self, other): ...
