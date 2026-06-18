from .utils import format_environment as format_environment

class ProxyConfig(dict):
    """
    Hold the client's proxy configuration
    """
    @property
    def http(self): ...
    @property
    def https(self): ...
    @property
    def ftp(self): ...
    @property
    def no_proxy(self): ...
    @staticmethod
    def from_dict(config):
        """
        Instantiate a new ProxyConfig from a dictionary that represents a
        client configuration, as described in `the documentation`_.

        .. _the documentation:
            https://docs.docker.com/network/proxy/#configure-the-docker-client
        """
    def get_environment(self):
        """
        Return a dictionary representing the environment variables used to
        set the proxy settings.
        """
    def inject_proxy_environment(self, environment):
        """
        Given a list of strings representing environment variables, prepend the
        environment variables corresponding to the proxy settings.
        """
