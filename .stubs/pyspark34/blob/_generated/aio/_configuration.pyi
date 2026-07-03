from _typeshed import Incomplete
from azure.core.configuration import Configuration
from typing import Any

VERSION: str

class AzureBlobStorageConfiguration(Configuration):
    '''Configuration for AzureBlobStorage.

    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param url: The URL of the service account, container, or blob that is the target of the
     desired operation. Required.
    :type url: str
    :keyword version: Specifies the version of the operation to use for this request. Default value
     is "2021-12-02". Note that overriding this default value may result in unsupported behavior.
    :paramtype version: str
    '''
    url: Incomplete
    version: Incomplete
    def __init__(self, url: str, **kwargs: Any) -> None: ...
