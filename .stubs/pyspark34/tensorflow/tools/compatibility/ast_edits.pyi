import ast
from _typeshed import Incomplete
from typing import NamedTuple

FIND_OPEN: Incomplete
FIND_STRING_CHARS: Incomplete
INFO: str
WARNING: str
ERROR: str

class ImportRename(NamedTuple):
    new_name: Incomplete
    excluded_prefixes: Incomplete

def full_name_node(name, ctx=...):
    """Make an Attribute or Name node for name.

  Translate a qualified name into nested Attribute nodes (and a Name node).

  Args:
    name: The name to translate to a node.
    ctx: What context this name is used in. Defaults to Load()

  Returns:
    A Name or Attribute node.
  """
def get_arg_value(node, arg_name, arg_pos: Incomplete | None = None):
    """Get the value of an argument from a ast.Call node.

  This function goes through the positional and keyword arguments to check
  whether a given argument was used, and if so, returns its value (the node
  representing its value).

  This cannot introspect *args or **args, but it safely handles *args in
  Python3.5+.

  Args:
    node: The ast.Call node to extract arg values from.
    arg_name: The name of the argument to extract.
    arg_pos: The position of the argument (in case it's passed as a positional
      argument).

  Returns:
    A tuple (arg_present, arg_value) containing a boolean indicating whether
    the argument is present, and its value in case it is.
  """
def uses_star_args_in_call(node):
    """Check if an ast.Call node uses arbitrary-length positional *args.

  This function works with the AST call node format of Python3.5+
  as well as the different AST format of earlier versions of Python.

  Args:
    node: The ast.Call node to check arg values for.

  Returns:
    True if the node uses starred variadic positional args or keyword args.
    False if it does not.
  """
def uses_star_kwargs_in_call(node):
    """Check if an ast.Call node uses arbitrary-length **kwargs.

  This function works with the AST call node format of Python3.5+
  as well as the different AST format of earlier versions of Python.

  Args:
    node: The ast.Call node to check arg values for.

  Returns:
    True if the node uses starred variadic positional args or keyword args.
    False if it does not.
  """
def uses_star_args_or_kwargs_in_call(node):
    """Check if an ast.Call node uses arbitrary-length *args or **kwargs.

  This function works with the AST call node format of Python3.5+
  as well as the different AST format of earlier versions of Python.

  Args:
    node: The ast.Call node to check arg values for.

  Returns:
    True if the node uses starred variadic positional args or keyword args.
    False if it does not.
  """
def excluded_from_module_rename(module, import_rename_spec):
    """Check if this module import should not be renamed.

  Args:
    module: (string) module name.
    import_rename_spec: ImportRename instance.

  Returns:
    True if this import should not be renamed according to the
    import_rename_spec.
  """

class APIChangeSpec:
    """This class defines the transformations that need to happen.

  This class must provide the following fields:

  * `function_keyword_renames`: maps function names to a map of old -> new
    argument names
  * `symbol_renames`: maps function names to new function names
  * `change_to_function`: a set of function names that have changed (for
    notifications)
  * `function_reorders`: maps functions whose argument order has changed to the
    list of arguments in the new order
  * `function_warnings`: maps full names of functions to warnings that will be
    printed out if the function is used. (e.g. tf.nn.convolution())
  * `function_transformers`: maps function names to custom handlers
  * `module_deprecations`: maps module names to warnings that will be printed
    if the module is still used after all other transformations have run
  * `import_renames`: maps import name (must be a short name without '.')
    to ImportRename instance.

  For an example, see `TFAPIChangeSpec`.
  """
    def preprocess(self, root_node):
        """Preprocess a parse tree. Return a preprocessed node, logs and errors."""
    def clear_preprocessing(self) -> None:
        """Restore this APIChangeSpec to before it preprocessed a file.

    This is needed if preprocessing a file changed any rewriting rules.
    """

class NoUpdateSpec(APIChangeSpec):
    """A specification of an API change which doesn't change anything."""
    function_handle: Incomplete
    function_reorders: Incomplete
    function_keyword_renames: Incomplete
    symbol_renames: Incomplete
    function_warnings: Incomplete
    change_to_function: Incomplete
    module_deprecations: Incomplete
    function_transformers: Incomplete
    import_renames: Incomplete
    def __init__(self) -> None: ...

class _PastaEditVisitor(ast.NodeVisitor):
    """AST Visitor that processes function calls.

  Updates function calls from old API version to new API version using a given
  change spec.
  """
    def __init__(self, api_change_spec) -> None: ...
    def visit(self, node) -> None: ...
    @property
    def errors(self): ...
    @property
    def warnings(self): ...
    @property
    def warnings_and_errors(self): ...
    @property
    def info(self): ...
    @property
    def log(self): ...
    def add_log(self, severity, lineno, col, msg) -> None: ...
    def add_logs(self, logs) -> None:
        """Record a log and print it.

    The log should be a tuple `(severity, lineno, col_offset, msg)`, which will
    be printed and recorded. It is part of the log available in the `self.log`
    property.

    Args:
      logs: The logs to add. Must be a list of tuples
        `(severity, lineno, col_offset, msg)`.
    """
    def visit_Call(self, node) -> None:
        """Handle visiting a call node in the AST.

    Args:
      node: Current Node
    """
    def visit_Attribute(self, node) -> None:
        """Handle bare Attributes i.e. [tf.foo, tf.bar]."""
    def visit_Import(self, node) -> None:
        """Handle visiting an import node in the AST.

    Args:
      node: Current Node
    """
    def visit_ImportFrom(self, node) -> None:
        """Handle visiting an import-from node in the AST.

    Args:
      node: Current Node
    """

class AnalysisResult:
    """This class represents an analysis result and how it should be logged.

  This class must provide the following fields:

  * `log_level`: The log level to which this detection should be logged
  * `log_message`: The message that should be logged for this detection

  For an example, see `VersionedTFImport`.
  """
class APIAnalysisSpec:
    """This class defines how `AnalysisResult`s should be generated.

  It specifies how to map imports and symbols to `AnalysisResult`s.

  This class must provide the following fields:

  * `symbols_to_detect`: maps function names to `AnalysisResult`s
  * `imports_to_detect`: maps imports represented as (full module name, alias)
    tuples to `AnalysisResult`s
    notifications)

  For an example, see `TFAPIImportAnalysisSpec`.
  """

class PastaAnalyzeVisitor(_PastaEditVisitor):
    """AST Visitor that looks for specific API usage without editing anything.

  This is used before any rewriting is done to detect if any symbols are used
  that require changing imports or disabling rewriting altogether.
  """
    def __init__(self, api_analysis_spec) -> None: ...
    @property
    def results(self): ...
    def add_result(self, analysis_result) -> None: ...
    def visit_Attribute(self, node) -> None:
        """Handle bare Attributes i.e. [tf.foo, tf.bar]."""
    def visit_Import(self, node) -> None:
        """Handle visiting an import node in the AST.

    Args:
      node: Current Node
    """
    def visit_ImportFrom(self, node) -> None:
        """Handle visiting an import-from node in the AST.

    Args:
      node: Current Node
    """

class ASTCodeUpgrader:
    """Handles upgrading a set of Python files using a given API change spec."""
    def __init__(self, api_change_spec) -> None: ...
    def process_file(self, in_filename, out_filename, no_change_to_outfile_on_error: bool = False):
        """Process the given python file for incompatible changes.

    Args:
      in_filename: filename to parse
      out_filename: output file to write to
      no_change_to_outfile_on_error: not modify the output file on errors
    Returns:
      A tuple representing number of files processed, log of actions, errors
    """
    def format_log(self, log, in_filename): ...
    def update_string_pasta(self, text, in_filename):
        """Updates a file using pasta."""
    def process_opened_file(self, in_filename, in_file, out_filename, out_file):
        """Process the given python file for incompatible changes.

    This function is split out to facilitate StringIO testing from
    tf_upgrade_test.py.

    Args:
      in_filename: filename to parse
      in_file: opened file (or StringIO)
      out_filename: output file to write to
      out_file: opened file (or StringIO)
    Returns:
      A tuple representing number of files processed, log of actions, errors
    """
    def process_tree(self, root_directory, output_root_directory, copy_other_files):
        """Processes upgrades on an entire tree of python files in place.

    Note that only Python files. If you have custom code in other languages,
    you will need to manually upgrade those.

    Args:
      root_directory: Directory to walk and process.
      output_root_directory: Directory to use as base.
      copy_other_files: Copy files that are not touched by this converter.

    Returns:
      A tuple of files processed, the report string for all files, and a dict
        mapping filenames to errors encountered in that file.
    """
    def process_tree_inplace(self, root_directory):
        """Process a directory of python files in place."""
