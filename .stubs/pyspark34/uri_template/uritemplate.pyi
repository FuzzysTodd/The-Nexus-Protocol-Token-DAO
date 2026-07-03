from .expansions import CommaExpansion as CommaExpansion, Expansion as Expansion, FormStyleQueryContinuation as FormStyleQueryContinuation, FormStyleQueryExpansion as FormStyleQueryExpansion, FragmentExpansion as FragmentExpansion, LabelExpansion as LabelExpansion, Literal as Literal, PathExpansion as PathExpansion, PathStyleExpansion as PathStyleExpansion, ReservedCommaExpansion as ReservedCommaExpansion, ReservedExpansion as ReservedExpansion, SimpleExpansion as SimpleExpansion
from .variable import Variable as Variable
from collections.abc import Iterable

class ExpansionReservedError(Exception):
    """Exception thrown for reserved but unsupported expansions."""
    expansion: str
    def __init__(self, expansion: str) -> None: ...

class ExpansionInvalidError(Exception):
    """Exception thrown for unknown expansions."""
    expansion: str
    def __init__(self, expansion: str) -> None: ...

class URITemplate:
    """
    URI Template object.

    Constructor may raise ExpansionReservedError, ExpansionInvalidError, or VariableInvalidError.
    """
    expansions: list[Expansion]
    def __init__(self, template: str) -> None: ...
    @property
    def variables(self) -> Iterable[Variable]:
        """Get all variables in template."""
    @property
    def variable_names(self) -> Iterable[str]:
        """Get names of all variables in template."""
    def expand(self, **kwargs) -> str:
        """
        Expand the template.

        May raise ExpansionFailed if a composite value is passed to a variable with a prefix modifier.
        """
    def partial(self, **kwargs) -> URITemplate:
        """
        Expand the template, preserving expansions for missing variables.

        May raise ExpansionFailed if a composite value is passed to a variable with a prefix modifier.
        """
    @property
    def expanded(self) -> bool:
        """Determine if template is fully expanded."""
