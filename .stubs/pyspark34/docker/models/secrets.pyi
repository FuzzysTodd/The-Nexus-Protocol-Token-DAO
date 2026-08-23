from ..api import APIClient as APIClient
from .resource import Collection as Collection, Model as Model

class Secret(Model):
    """A secret."""
    id_attribute: str
    @property
    def name(self): ...
    def remove(self):
        """
        Remove this secret.

        Raises:
            :py:class:`docker.errors.APIError`
                If secret failed to remove.
        """

class SecretCollection(Collection):
    """Secrets on the Docker server."""
    model = Secret
    def create(self, **kwargs): ...
    def get(self, secret_id):
        """
        Get a secret.

        Args:
            secret_id (str): Secret ID.

        Returns:
            (:py:class:`Secret`): The secret.

        Raises:
            :py:class:`docker.errors.NotFound`
                If the secret does not exist.
            :py:class:`docker.errors.APIError`
                If the server returns an error.
        """
    def list(self, **kwargs):
        """
        List secrets. Similar to the ``docker secret ls`` command.

        Args:
            filters (dict): Server-side list filtering options.

        Returns:
            (list of :py:class:`Secret`): The secrets.

        Raises:
            :py:class:`docker.errors.APIError`
                If the server returns an error.
        """
