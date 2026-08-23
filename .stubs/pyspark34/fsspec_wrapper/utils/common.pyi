from _typeshed import Incomplete

class SynapseCredential:
    """
    Custom credential class implementation.
    More info: https://github.com/Azure/azure-sdk-for-python/issues/9075#issuecomment-564171752
    """
    token: Incomplete
    def __init__(self, token, **kwargs) -> None: ...
    async def get_token(self, *scopes, **kwargs): ...

IS_PYTHON_RUNTIME: Incomplete
