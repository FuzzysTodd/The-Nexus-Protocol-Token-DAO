from ..api import APIClient as APIClient
from .resource import Collection as Collection, Model as Model
from _typeshed import Incomplete

class Volume(Model):
    """A volume."""
    id_attribute: str
    @property
    def name(self):
        """The name of the volume."""
    def remove(self, force: bool = False):
        """
        Remove this volume.

        Args:
            force (bool): Force removal of volumes that were already removed
                out of band by the volume driver plugin.
        Raises:
            :py:class:`docker.errors.APIError`
                If volume failed to remove.
        """

class VolumeCollection(Collection):
    """Volumes on the Docker server."""
    model = Volume
    def create(self, name: Incomplete | None = None, **kwargs):
        '''
        Create a volume.

        Args:
            name (str): Name of the volume.  If not specified, the engine
                generates a name.
            driver (str): Name of the driver used to create the volume
            driver_opts (dict): Driver options as a key-value dictionary
            labels (dict): Labels to set on the volume

        Returns:
            (:py:class:`Volume`): The volume created.

        Raises:
            :py:class:`docker.errors.APIError`
                If the server returns an error.

        Example:

            >>> volume = client.volumes.create(name=\'foobar\', driver=\'local\',
                    driver_opts={\'foo\': \'bar\', \'baz\': \'false\'},
                    labels={"key": "value"})

        '''
    def get(self, volume_id):
        """
        Get a volume.

        Args:
            volume_id (str): Volume name.

        Returns:
            (:py:class:`Volume`): The volume.

        Raises:
            :py:class:`docker.errors.NotFound`
                If the volume does not exist.
            :py:class:`docker.errors.APIError`
                If the server returns an error.
        """
    def list(self, **kwargs):
        """
        List volumes. Similar to the ``docker volume ls`` command.

        Args:
            filters (dict): Server-side list filtering options.

        Returns:
            (list of :py:class:`Volume`): The volumes.

        Raises:
            :py:class:`docker.errors.APIError`
                If the server returns an error.
        """
    def prune(self, filters: Incomplete | None = None): ...
