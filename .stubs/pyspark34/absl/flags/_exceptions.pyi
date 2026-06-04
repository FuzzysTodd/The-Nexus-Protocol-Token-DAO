from _typeshed import Incomplete

class Error(Exception):
    """The base class for all flags errors."""
class CantOpenFlagFileError(Error):
    """Raised when flagfile fails to open.

  E.g. the file doesn't exist, or has wrong permissions.
  """

class DuplicateFlagError(Error):
    """Raised if there is a flag naming conflict."""
    @classmethod
    def from_flag(cls, flagname, flag_values, other_flag_values: Incomplete | None = None):
        """Creates a DuplicateFlagError by providing flag name and values.

    Args:
      flagname: str, the name of the flag being redefined.
      flag_values: :class:`FlagValues`, the FlagValues instance containing the
        first definition of flagname.
      other_flag_values: :class:`FlagValues`, if it is not None, it should be
        the FlagValues object where the second definition of flagname occurs.
        If it is None, we assume that we're being called when attempting to
        create the flag a second time, and we use the module calling this one
        as the source of the second definition.

    Returns:
      An instance of DuplicateFlagError.
    """

class IllegalFlagValueError(Error):
    """Raised when the flag command line argument is illegal."""

class UnrecognizedFlagError(Error):
    """Raised when a flag is unrecognized.

  Attributes:
    flagname: str, the name of the unrecognized flag.
    flagvalue: The value of the flag, empty if the flag is not defined.
  """
    flagname: Incomplete
    flagvalue: Incomplete
    def __init__(self, flagname, flagvalue: str = '', suggestions: Incomplete | None = None) -> None: ...

class UnparsedFlagAccessError(Error):
    """Raised when accessing the flag value from unparsed :class:`FlagValues`."""
class ValidationError(Error):
    """Raised when flag validator constraint is not satisfied."""
class FlagNameConflictsWithMethodError(Error):
    """Raised when a flag name conflicts with :class:`FlagValues` methods."""
