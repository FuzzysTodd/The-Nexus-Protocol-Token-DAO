from .error import UsageError as UsageError
from _typeshed import Incomplete
from traitlets.config.configurable import Configurable

shell_line_split: Incomplete

def default_aliases():
    """Return list of shell aliases to auto-define.
    """

class AliasError(Exception): ...
class InvalidAliasError(AliasError): ...

class Alias:
    """Callable object storing the details of one alias.

    Instances are registered as magic functions to allow use of aliases.
    """
    blacklist: Incomplete
    shell: Incomplete
    name: Incomplete
    cmd: Incomplete
    __doc__: Incomplete
    nargs: Incomplete
    def __init__(self, shell, name, cmd) -> None: ...
    def validate(self):
        """Validate the alias, and return the number of arguments."""
    def __call__(self, rest: str = '') -> None: ...

class AliasManager(Configurable):
    default_aliases: Incomplete
    user_aliases: Incomplete
    shell: Incomplete
    linemagics: Incomplete
    def __init__(self, shell: Incomplete | None = None, **kwargs) -> None: ...
    def init_aliases(self) -> None: ...
    @property
    def aliases(self): ...
    def soft_define_alias(self, name, cmd) -> None:
        """Define an alias, but don't raise on an AliasError."""
    def define_alias(self, name, cmd) -> None:
        """Define a new alias after validating it.

        This will raise an :exc:`AliasError` if there are validation
        problems.
        """
    def get_alias(self, name):
        """Return an alias, or None if no alias by that name exists."""
    def is_alias(self, name):
        """Return whether or not a given name has been defined as an alias"""
    def undefine_alias(self, name) -> None: ...
    def clear_aliases(self) -> None: ...
    def retrieve_alias(self, name):
        """Retrieve the command to which an alias expands."""
