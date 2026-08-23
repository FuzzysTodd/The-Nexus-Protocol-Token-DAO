from sentry_sdk.integrations import Integration

__all__ = ['SocketIntegration']

class SocketIntegration(Integration):
    identifier: str
    @staticmethod
    def setup_once() -> None:
        """
        patches two of the most used functions of socket: create_connection and getaddrinfo(dns resolver)
        """
