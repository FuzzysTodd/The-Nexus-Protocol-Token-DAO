from _typeshed import Incomplete

class MessageFactory:
    """Factory for creating Proto2 messages from descriptors in a pool."""
    pool: Incomplete
    def __init__(self, pool: Incomplete | None = None) -> None:
        """Initializes a new factory."""
    def GetPrototype(self, descriptor):
        """Obtains a proto2 message class based on the passed in descriptor.

    Passing a descriptor with a fully qualified name matching a previous
    invocation will cause the same class to be returned.

    Args:
      descriptor: The descriptor to build from.

    Returns:
      A class describing the passed in descriptor.
    """
    def CreatePrototype(self, descriptor):
        """Builds a proto2 message class based on the passed in descriptor.

    Don't call this function directly, it always creates a new class. Call
    GetPrototype() instead. This method is meant to be overridden in subblasses
    to perform additional operations on the newly constructed class.

    Args:
      descriptor: The descriptor to build from.

    Returns:
      A class describing the passed in descriptor.
    """
    def GetMessages(self, files):
        """Gets all the messages from a specified file.

    This will find and resolve dependencies, failing if the descriptor
    pool cannot satisfy them.

    Args:
      files: The file names to extract messages from.

    Returns:
      A dictionary mapping proto names to the message classes. This will include
      any dependent messages as well as any messages defined in the same file as
      a specified message.
    """

def GetMessages(file_protos):
    """Builds a dictionary of all the messages available in a set of files.

  Args:
    file_protos: Iterable of FileDescriptorProto to build messages out of.

  Returns:
    A dictionary mapping proto names to the message classes. This will include
    any dependent messages as well as any messages defined in the same file as
    a specified message.
  """
