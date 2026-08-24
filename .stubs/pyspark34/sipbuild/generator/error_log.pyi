from ..exceptions import UserException as UserException
from _typeshed import Incomplete

class ErrorLog:
    """ This object logs errors and raises a corresponding exception when
    requested.
    """
    def __init__(self) -> None:
        """ Initialise the error log. """
    def log(self, text, source_location: Incomplete | None = None) -> None:
        """ Log an error with an optional source location. """
    def as_exception(self) -> None:
        """ Raise a UserException for any logged errors. """
