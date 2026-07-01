from _typeshed import Incomplete

log: Incomplete

class Serializable:
    """ This is the superclass of all serializable objects.
    """
    def save(self, out_file) -> None:
        """ Save the model to the given file stream.
        """
    @classmethod
    def load(cls, in_file, instantiate: bool = True):
        """ This is meant to be overriden by subclasses and called with super.

        We return constructor argument values when not being instantiated. Since there are no
        constructor arguments for the Serializable class we just return an empty dictionary.
        """

class Serializer:
    """ Save data items to an input stream.
    """
    out_stream: Incomplete
    block_name: Incomplete
    block_version: Incomplete
    serializer_version: int
    def __init__(self, out_stream, block_name, version) -> None: ...
    def __enter__(self): ...
    def __exit__(self, exception_type: type[BaseException] | None, exception_value: BaseException | None, traceback: types.TracebackType | None) -> None: ...
    def save(self, name, value, encoder: str = 'auto') -> None:
        """ Dump a data item to the current input stream.
        """

class Deserializer:
    """ Load data items from an input stream.
    """
    in_stream: Incomplete
    block_name: Incomplete
    block_min_version: Incomplete
    block_max_version: Incomplete
    serializer_min_version: int
    serializer_max_version: int
    def __init__(self, in_stream, block_name, min_version, max_version) -> None: ...
    def __enter__(self): ...
    def __exit__(self, exception_type: type[BaseException] | None, exception_value: BaseException | None, traceback: types.TracebackType | None) -> None: ...
    def load(self, name, decoder: Incomplete | None = None):
        """ Load a data item from the current input stream.
        """
