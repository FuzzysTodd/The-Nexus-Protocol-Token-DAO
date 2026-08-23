from _typeshed import Incomplete

class UserException(Exception):
    """ An exception capturing user friendly information. """
    text: Incomplete
    detail: Incomplete
    def __init__(self, text, *, detail: Incomplete | None = None) -> None:
        """ Initialise the exception with its user friendly text and the
        optional detail.
        """

class UserFileException(UserException):
    """ An exception related to a specific file. """
    def __init__(self, filename, text, *, detail: Incomplete | None = None) -> None:
        """ Initialise the exception. """

class UserParseException(UserFileException):
    """ An exception related to the parsing of a specific file. """
    def __init__(self, filename, *, detail: Incomplete | None = None) -> None:
        """ Initialise the exception. """

def handle_exception(e) -> None:
    """ Tell the user about an exception. """
