from _typeshed import Incomplete
from ipykernel.jsonutil import json_clean as json_clean
from ipykernel.serialize import serialize_object as serialize_object
from traitlets.config import Configurable

class ZMQDataPublisher(Configurable):
    """A zmq data publisher."""
    topic: Incomplete
    session: Incomplete
    pub_socket: Incomplete
    parent_header: Incomplete
    def set_parent(self, parent) -> None:
        """Set the parent for outbound messages."""
    def publish_data(self, data) -> None:
        """publish a data_message on the IOPub channel

        Parameters
        ----------
        data : dict
            The data to be published. Think of it as a namespace.
        """

def publish_data(data) -> None:
    """publish a data_message on the IOPub channel

    Parameters
    ----------
    data : dict
        The data to be published. Think of it as a namespace.
    """
