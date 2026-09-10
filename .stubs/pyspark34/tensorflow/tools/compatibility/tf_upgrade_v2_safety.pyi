from _typeshed import Incomplete
from tensorflow.tools.compatibility import all_renames_v2 as all_renames_v2, ast_edits as ast_edits, module_deprecations_v2 as module_deprecations_v2

class TFAPIChangeSpec(ast_edits.APIChangeSpec):
    """List of maps that describe what changed in the API."""
    function_keyword_renames: Incomplete
    symbol_renames: Incomplete
    change_to_function: Incomplete
    function_reorders: Incomplete
    function_warnings: Incomplete
    function_transformers: Incomplete
    module_deprecations: Incomplete
    import_renames: Incomplete
    max_submodule_depth: int
    def __init__(self) -> None: ...
