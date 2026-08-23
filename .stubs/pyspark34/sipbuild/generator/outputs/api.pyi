from ..specification import AccessSpecifier as AccessSpecifier
from .formatters import ClassFormatter as ClassFormatter, EnumFormatter as EnumFormatter, OverloadFormatter as OverloadFormatter, SignatureFormatter as SignatureFormatter, VariableFormatter as VariableFormatter
from enum import IntEnum

class IconNumber(IntEnum):
    """ The numbers of the different icons.  The values are those used by the
    eric IDE.
    """
    CLASS: int
    METHOD: int
    VARIABLE: int
    ENUM: int

def output_api(spec, api_filename) -> None:
    """ Output a QScintilla API file. """
