import adlfs
from .utils.common import SynapseCredential as SynapseCredential
from _typeshed import Incomplete

tokenExpiryCushion: int
token_default_exp: Incomplete

class AzureBlobFileSystem(adlfs.AzureBlobFileSystem):
    original_kwargs: Incomplete
    token_exp: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...
    def __getattribute__(self, attr):
        """
        Overloads the __getattribute__ method.
        Returns the requested attribute.
        """
    def walk(self, path, maxdepth: Incomplete | None = None, **kwargs):
        """
        Overwrite the walk method to invalidate cache.
        """
