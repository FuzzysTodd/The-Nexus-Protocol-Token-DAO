from sentry_sdk.integrations import Integration

__all__ = ['HttpxIntegration']

class HttpxIntegration(Integration):
    identifier: str
    @staticmethod
    def setup_once() -> None:
        """
        httpx has its own transport layer and can be customized when needed,
        so patch Client.send and AsyncClient.send to support both synchronous and async interfaces.
        """
