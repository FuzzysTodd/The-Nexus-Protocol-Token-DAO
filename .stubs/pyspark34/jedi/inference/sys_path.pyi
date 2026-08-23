from jedi import debug as debug, settings as settings
from jedi.file_io import FileIO as FileIO
from jedi.inference.base_value import ContextualizedNode as ContextualizedNode
from jedi.inference.cache import inference_state_method_cache as inference_state_method_cache
from jedi.inference.helpers import get_str_or_none as get_str_or_none, is_string as is_string
from jedi.parser_utils import get_cached_code_lines as get_cached_code_lines

def check_sys_path_modifications(module_context):
    """
    Detect sys.path modifications within module.
    """
def discover_buildout_paths(inference_state, script_path): ...
def remove_python_path_suffix(path): ...
def transform_path_to_dotted(sys_path, module_path):
    '''
    Returns the dotted path inside a sys.path as a list of names. e.g.

    >>> transform_path_to_dotted([str(Path("/foo").absolute())], Path(\'/foo/bar/baz.py\').absolute())
    ((\'bar\', \'baz\'), False)

    Returns (None, False) if the path doesn\'t really resolve to anything.
    The second return part is if it is a package.
    '''
