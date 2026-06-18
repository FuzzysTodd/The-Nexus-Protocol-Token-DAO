from .. import errors as errors, utils as utils
from _typeshed import Incomplete

class SecretApiMixin:
    def create_secret(self, name, data, labels: Incomplete | None = None, driver: Incomplete | None = None):
        """
            Create a secret

            Args:
                name (string): Name of the secret
                data (bytes): Secret data to be stored
                labels (dict): A mapping of labels to assign to the secret
                driver (DriverConfig): A custom driver configuration. If
                    unspecified, the default ``internal`` driver will be used

            Returns (dict): ID of the newly created secret
        """
    def inspect_secret(self, id):
        """
            Retrieve secret metadata

            Args:
                id (string): Full ID of the secret to inspect

            Returns (dict): A dictionary of metadata

            Raises:
                :py:class:`docker.errors.NotFound`
                    if no secret with that ID exists
        """
    def remove_secret(self, id):
        """
            Remove a secret

            Args:
                id (string): Full ID of the secret to remove

            Returns (boolean): True if successful

            Raises:
                :py:class:`docker.errors.NotFound`
                    if no secret with that ID exists
        """
    def secrets(self, filters: Incomplete | None = None):
        """
            List secrets

            Args:
                filters (dict): A map of filters to process on the secrets
                list. Available filters: ``names``

            Returns (list): A list of secrets
        """
