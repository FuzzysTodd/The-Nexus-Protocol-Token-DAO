import abc
from sempy.fabric._client import WorkspaceClient as WorkspaceClient
from sempy.fabric._client._base_dataset_client import BaseDatasetClient as BaseDatasetClient
from sempy.fabric._token_provider import TokenProvider as TokenProvider
from sempy.fabric._utils import SparkConfigTemporarily as SparkConfigTemporarily
from uuid import UUID

class DatasetOneLakeImportClient(BaseDatasetClient, metaclass=abc.ABCMeta):
    """
    Import exported semantic models from onelake.

    See `onelake integration <https://learn.microsoft.com/en-us/power-bi/enterprise/onelake-integration-overview>`_
    """
    def __init__(self, workspace: str | WorkspaceClient, dataset: str | UUID, token_provider: TokenProvider | None = None) -> None: ...
