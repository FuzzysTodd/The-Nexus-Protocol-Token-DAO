from mypy import defaults as defaults
from mypy.errorcodes import error_codes as error_codes
from mypy.options import Options as Options, PER_MODULE_OPTIONS as PER_MODULE_OPTIONS
from typing import Any, Callable, Mapping, Sequence, TextIO
from typing_extensions import Final

def parse_version(v: str | float) -> tuple[int, int]: ...
def try_split(v: str | Sequence[str], split_regex: str = '[,]') -> list[str]:
    """Split and trim a str or list of str into a list of str"""
def validate_codes(codes: list[str]) -> list[str]: ...
def expand_path(path: str) -> str:
    """Expand the user home directory and any environment variables contained within
    the provided path.
    """
def str_or_array_as_list(v: str | Sequence[str]) -> list[str]: ...
def split_and_match_files_list(paths: Sequence[str]) -> list[str]:
    """Take a list of files/directories (with support for globbing through the glob library).

    Where a path/glob matches no file, we still include the raw path in the resulting list.

    Returns a list of file paths
    """
def split_and_match_files(paths: str) -> list[str]:
    """Take a string representing a list of files/directories (with support for globbing
    through the glob library).

    Where a path/glob matches no file, we still include the raw path in the resulting list.

    Returns a list of file paths
    """
def check_follow_imports(choice: str) -> str: ...
def split_commas(value: str) -> list[str]: ...

ini_config_types: Final[dict[str, _INI_PARSER_CALLABLE]]
toml_config_types: Final[dict[str, _INI_PARSER_CALLABLE]]

def parse_config_file(options: Options, set_strict_flags: Callable[[], None], filename: str | None, stdout: TextIO | None = None, stderr: TextIO | None = None) -> None:
    """Parse a config file into an Options object.

    Errors are written to stderr but are not fatal.

    If filename is None, fall back to default config files.
    """
def get_prefix(file_read: str, name: str) -> str: ...
def is_toml(filename: str) -> bool: ...
def destructure_overrides(toml_data: dict[str, Any]) -> dict[str, Any]:
    '''Take the new [[tool.mypy.overrides]] section array in the pyproject.toml file,
    and convert it back to a flatter structure that the existing config_parser can handle.

    E.g. the following pyproject.toml file:

        [[tool.mypy.overrides]]
        module = [
            "a.b",
            "b.*"
        ]
        disallow_untyped_defs = true

        [[tool.mypy.overrides]]
        module = \'c\'
        disallow_untyped_defs = false

    Would map to the following config dict that it would have gotten from parsing an equivalent
    ini file:

        {
            "mypy-a.b": {
                disallow_untyped_defs = true,
            },
            "mypy-b.*": {
                disallow_untyped_defs = true,
            },
            "mypy-c": {
                disallow_untyped_defs: false,
            },
        }
    '''
def parse_section(prefix: str, template: Options, set_strict_flags: Callable[[], None], section: Mapping[str, Any], config_types: dict[str, Any], stderr: TextIO = ...) -> tuple[dict[str, object], dict[str, str]]:
    """Parse one section of a config file.

    Returns a dict of option values encountered, and a dict of report directories.
    """
def convert_to_boolean(value: Any | None) -> bool:
    """Return a boolean value translating from other types if necessary."""
def split_directive(s: str) -> tuple[list[str], list[str]]:
    """Split s on commas, except during quoted sections.

    Returns the parts and a list of error messages."""
def mypy_comments_to_config_map(line: str, template: Options) -> tuple[dict[str, str], list[str]]:
    """Rewrite the mypy comment syntax into ini file syntax."""
def parse_mypy_comments(args: list[tuple[int, str]], template: Options) -> tuple[dict[str, object], list[tuple[int, str]]]:
    """Parse a collection of inline mypy: configuration comments.

    Returns a dictionary of options to be applied and a list of error messages
    generated.
    """
def get_config_module_names(filename: str | None, modules: list[str]) -> str: ...

class ConfigTOMLValueError(ValueError): ...
