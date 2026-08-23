from mypy.errors import Errors as Errors
from mypy.nodes import MypyFile as MypyFile
from mypy.options import Options as Options

def parse(source: str | bytes, fnam: str, module: str | None, errors: Errors | None, options: Options) -> MypyFile:
    """Parse a source file, without doing any semantic analysis.

    Return the parse tree. If errors is not provided, raise ParseError
    on failure. Otherwise, use the errors object to report parse errors.

    The python_version (major, minor) option determines the Python syntax variant.
    """
