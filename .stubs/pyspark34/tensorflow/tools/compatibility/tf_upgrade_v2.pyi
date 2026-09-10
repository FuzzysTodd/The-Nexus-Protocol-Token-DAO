import ast
from _typeshed import Incomplete
from tensorflow.tools.compatibility import all_renames_v2 as all_renames_v2, ast_edits as ast_edits, module_deprecations_v2 as module_deprecations_v2, reorders_v2 as reorders_v2

class UnaliasedTFImport(ast_edits.AnalysisResult):
    log_level: Incomplete
    log_message: str
    def __init__(self) -> None: ...

class VersionedTFImport(ast_edits.AnalysisResult):
    log_level: Incomplete
    log_message: Incomplete
    def __init__(self, version) -> None: ...

compat_v1_import: Incomplete
compat_v2_import: Incomplete

class TFAPIImportAnalysisSpec(ast_edits.APIAnalysisSpec):
    symbols_to_detect: Incomplete
    imports_to_detect: Incomplete
    def __init__(self) -> None: ...

class CompatV1ImportReplacer(ast.NodeVisitor):
    """AST Visitor that replaces `import tensorflow.compat.v1 as tf`.

  Converts `import tensorflow.compat.v1 as tf` to `import tensorflow as tf`
  """
    def visit_Import(self, node) -> None:
        """Handle visiting an import node in the AST.

    Args:
      node: Current Node
    """

class TFAPIChangeSpec(ast_edits.NoUpdateSpec):
    """List of maps that describe what changed in the API."""
    upgrade_compat_v1_import: Incomplete
    function_keyword_renames: Incomplete
    symbol_renames: Incomplete
    import_rename: Incomplete
    import_renames: Incomplete
    change_to_function: Incomplete
    reordered_function_names: Incomplete
    manual_function_reorders: Incomplete
    function_reorders: Incomplete
    function_warnings: Incomplete
    function_arg_warnings: Incomplete
    function_transformers: Incomplete
    module_deprecations: Incomplete
    def __init__(self, import_rename: bool = False, upgrade_compat_v1_import: bool = False) -> None: ...
    function_handle: Incomplete
    def preprocess(self, root_node, after_compat_v1_upgrade: bool = False): ...
    def clear_preprocessing(self) -> None: ...
