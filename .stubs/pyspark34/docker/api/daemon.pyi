from .. import auth as auth, types as types, utils as utils
from _typeshed import Incomplete

class DaemonApiMixin:
    def df(self):
        """
        Get data usage information.

        Returns:
            (dict): A dictionary representing different resource categories
            and their respective data usage.

        Raises:
            :py:class:`docker.errors.APIError`
                If the server returns an error.
        """
    def events(self, since: Incomplete | None = None, until: Incomplete | None = None, filters: Incomplete | None = None, decode: Incomplete | None = None):
        """
        Get real-time events from the server. Similar to the ``docker events``
        command.

        Args:
            since (UTC datetime or int): Get events from this point
            until (UTC datetime or int): Get events until this point
            filters (dict): Filter the events by event time, container or image
            decode (bool): If set to true, stream will be decoded into dicts on
                the fly. False by default.

        Returns:
            A :py:class:`docker.types.daemon.CancellableStream` generator

        Raises:
            :py:class:`docker.errors.APIError`
                If the server returns an error.

        Example:

            >>> for event in client.events(decode=True)
            ...   print(event)
            {u'from': u'image/with:tag',
             u'id': u'container-id',
             u'status': u'start',
             u'time': 1423339459}
            ...

            or

            >>> events = client.events()
            >>> for event in events:
            ...   print(event)
            >>> # and cancel from another thread
            >>> events.close()
        """
    def info(self):
        """
        Display system-wide information. Identical to the ``docker info``
        command.

        Returns:
            (dict): The info as a dict

        Raises:
            :py:class:`docker.errors.APIError`
                If the server returns an error.
        """
    def login(self, username, password: Incomplete | None = None, email: Incomplete | None = None, registry: Incomplete | None = None, reauth: bool = False, dockercfg_path: Incomplete | None = None):
        """
        Authenticate with a registry. Similar to the ``docker login`` command.

        Args:
            username (str): The registry username
            password (str): The plaintext password
            email (str): The email for the registry account
            registry (str): URL to the registry.  E.g.
                ``https://index.docker.io/v1/``
            reauth (bool): Whether or not to refresh existing authentication on
                the Docker server.
            dockercfg_path (str): Use a custom path for the Docker config file
                (default ``$HOME/.docker/config.json`` if present,
                otherwise ``$HOME/.dockercfg``)

        Returns:
            (dict): The response from the login request

        Raises:
            :py:class:`docker.errors.APIError`
                If the server returns an error.
        """
    def ping(self):
        """
        Checks the server is responsive. An exception will be raised if it
        isn't responding.

        Returns:
            (bool) The response from the server.

        Raises:
            :py:class:`docker.errors.APIError`
                If the server returns an error.
        """
    def version(self, api_version: bool = True):
        """
        Returns version information from the server. Similar to the ``docker
        version`` command.

        Returns:
            (dict): The server version information

        Raises:
            :py:class:`docker.errors.APIError`
                If the server returns an error.
        """
