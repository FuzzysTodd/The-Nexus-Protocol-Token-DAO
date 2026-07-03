from _typeshed import Incomplete
from jedi import debug as debug, settings as settings
from jedi.file_io import FileIO as FileIO
from jedi.inference import helpers as helpers, imports as imports, recursion as recursion
from jedi.inference.base_value import ContextualizedNode as ContextualizedNode, ValueSet as ValueSet, iterate_values as iterate_values
from jedi.inference.cache import inference_state_function_cache as inference_state_function_cache
from jedi.inference.imports import follow_error_node_imports_if_possible as follow_error_node_imports_if_possible
from jedi.inference.names import TreeNameDefinition as TreeNameDefinition
from jedi.inference.syntax_tree import check_tuple_assignments as check_tuple_assignments, infer_expr_stmt as infer_expr_stmt, tree_name_to_values as tree_name_to_values
from jedi.inference.value import ClassValue as ClassValue, FunctionValue as FunctionValue
from jedi.plugins import plugin_manager as plugin_manager

class InferenceState:
    environment: Incomplete
    script_path: Incomplete
    compiled_subprocess: Incomplete
    grammar: Incomplete
    latest_grammar: Incomplete
    memoize_cache: Incomplete
    module_cache: Incomplete
    stub_module_cache: Incomplete
    compiled_cache: Incomplete
    inferred_element_counts: Incomplete
    mixed_cache: Incomplete
    analysis: Incomplete
    dynamic_params_depth: int
    do_dynamic_params_search: Incomplete
    is_analysis: bool
    project: Incomplete
    access_cache: Incomplete
    allow_unsafe_executions: bool
    flow_analysis_enabled: bool
    def __init__(self, project, environment: Incomplete | None = None, script_path: Incomplete | None = None) -> None: ...
    def import_module(self, import_names, sys_path: Incomplete | None = None, prefer_stubs: bool = True): ...
    @staticmethod
    def execute(value, arguments): ...
    @property
    def builtins_module(self): ...
    @property
    def typing_module(self): ...
    recursion_detector: Incomplete
    execution_recursion_detector: Incomplete
    def reset_recursion_limitations(self) -> None: ...
    def get_sys_path(self, **kwargs):
        """Convenience function"""
    def infer(self, context, name): ...
    def parse_and_get_code(self, code: Incomplete | None = None, path: Incomplete | None = None, use_latest_grammar: bool = False, file_io: Incomplete | None = None, **kwargs): ...
    def parse(self, *args, **kwargs): ...
