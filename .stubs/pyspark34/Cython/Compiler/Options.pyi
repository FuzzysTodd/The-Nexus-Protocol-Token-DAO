from .. import Utils as Utils
from _typeshed import Incomplete

class ShouldBeFromDirective:
    known_directives: Incomplete
    options_name: Incomplete
    directive_name: Incomplete
    disallow: Incomplete
    def __init__(self, options_name, directive_name: Incomplete | None = None, disallow: bool = False) -> None: ...
    def __nonzero__(self) -> None: ...
    def __int__(self) -> int: ...

docstrings: bool
embed_pos_in_docstring: bool
pre_import: Incomplete
generate_cleanup_code: bool
clear_to_none: bool
annotate: bool
annotate_coverage_xml: Incomplete
fast_fail: bool
warning_errors: bool
error_on_unknown_names: bool
error_on_uninitialized: bool
convert_range: bool
cache_builtins: bool
gcc_branch_hints: bool
lookup_module_cpdef: bool
embed: Incomplete
old_style_globals: Incomplete
cimport_from_pyx: bool
buffer_max_dims: int
closure_freelist_size: int

def get_directive_defaults(): ...
def copy_inherited_directives(outer_directives, **new_directives): ...

extra_warnings: Incomplete

def one_of(*args): ...
def normalise_encoding_name(option_name, encoding):
    """
    >>> normalise_encoding_name('c_string_encoding', 'ascii')
    'ascii'
    >>> normalise_encoding_name('c_string_encoding', 'AsCIi')
    'ascii'
    >>> normalise_encoding_name('c_string_encoding', 'us-ascii')
    'ascii'
    >>> normalise_encoding_name('c_string_encoding', 'utF8')
    'utf8'
    >>> normalise_encoding_name('c_string_encoding', 'utF-8')
    'utf8'
    >>> normalise_encoding_name('c_string_encoding', 'deFAuLT')
    'default'
    >>> normalise_encoding_name('c_string_encoding', 'default')
    'default'
    >>> normalise_encoding_name('c_string_encoding', 'SeriousLyNoSuch--Encoding')
    'SeriousLyNoSuch--Encoding'
    """

class DEFER_ANALYSIS_OF_ARGUMENTS: ...

directive_types: Incomplete
directive_scopes: Incomplete
immediate_decorator_directives: Incomplete

def parse_directive_value(name, value, relaxed_bool: bool = False):
    """
    Parses value as an option value for the given name and returns
    the interpreted value. None is returned if the option does not exist.

    >>> print(parse_directive_value('nonexisting', 'asdf asdfd'))
    None
    >>> parse_directive_value('boundscheck', 'True')
    True
    >>> parse_directive_value('boundscheck', 'true')
    Traceback (most recent call last):
       ...
    ValueError: boundscheck directive must be set to True or False, got 'true'

    >>> parse_directive_value('c_string_encoding', 'us-ascii')
    'ascii'
    >>> parse_directive_value('c_string_type', 'str')
    'str'
    >>> parse_directive_value('c_string_type', 'bytes')
    'bytes'
    >>> parse_directive_value('c_string_type', 'bytearray')
    'bytearray'
    >>> parse_directive_value('c_string_type', 'unicode')
    'unicode'
    >>> parse_directive_value('c_string_type', 'unnicode')
    Traceback (most recent call last):
    ValueError: c_string_type directive must be one of ('bytes', 'bytearray', 'str', 'unicode'), got 'unnicode'
    """
def parse_directive_list(s, relaxed_bool: bool = False, ignore_unknown: bool = False, current_settings: Incomplete | None = None):
    '''
    Parses a comma-separated list of pragma options. Whitespace
    is not considered.

    >>> parse_directive_list(\'      \')
    {}
    >>> (parse_directive_list(\'boundscheck=True\') ==
    ... {\'boundscheck\': True})
    True
    >>> parse_directive_list(\'  asdf\')
    Traceback (most recent call last):
       ...
    ValueError: Expected "=" in option "asdf"
    >>> parse_directive_list(\'boundscheck=hey\')
    Traceback (most recent call last):
       ...
    ValueError: boundscheck directive must be set to True or False, got \'hey\'
    >>> parse_directive_list(\'unknown=True\')
    Traceback (most recent call last):
       ...
    ValueError: Unknown option: "unknown"
    >>> warnings = parse_directive_list(\'warn.all=True\')
    >>> len(warnings) > 1
    True
    >>> sum(warnings.values()) == len(warnings)  # all true.
    True
    '''
def parse_variable_value(value):
    """
    Parses value as an option value for the given name and returns
    the interpreted value.

    >>> parse_variable_value('True')
    True
    >>> parse_variable_value('true')
    'true'
    >>> parse_variable_value('us-ascii')
    'us-ascii'
    >>> parse_variable_value('str')
    'str'
    >>> parse_variable_value('123')
    123
    >>> parse_variable_value('1.23')
    1.23

    """
def parse_compile_time_env(s, current_settings: Incomplete | None = None):
    '''
    Parses a comma-separated list of pragma options. Whitespace
    is not considered.

    >>> parse_compile_time_env(\'      \')
    {}
    >>> (parse_compile_time_env(\'HAVE_OPENMP=True\') ==
    ... {\'HAVE_OPENMP\': True})
    True
    >>> parse_compile_time_env(\'  asdf\')
    Traceback (most recent call last):
       ...
    ValueError: Expected "=" in option "asdf"
    >>> parse_compile_time_env(\'NUM_THREADS=4\') == {\'NUM_THREADS\': 4}
    True
    >>> parse_compile_time_env(\'unknown=anything\') == {\'unknown\': \'anything\'}
    True
    '''

class CompilationOptions:
    """
    See default_options at the end of this module for a list of all possible
    options and CmdLine.usage and CmdLine.parse_command_line() for their
    meaning.
    """
    include_path: Incomplete
    def __init__(self, defaults: Incomplete | None = None, **kw) -> None: ...
    def configure_language_defaults(self, source_extension) -> None: ...
    def get_fingerprint(self):
        """
        Return a string that contains all the options that are relevant for cache invalidation.
        """

default_options: Incomplete
