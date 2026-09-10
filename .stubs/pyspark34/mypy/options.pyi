from _typeshed import Incomplete
from mypy import defaults as defaults
from mypy.errorcodes import ErrorCode as ErrorCode, error_codes as error_codes
from mypy.util import get_class_descriptors as get_class_descriptors, replace_object_state as replace_object_state
from typing import Mapping, Pattern
from typing_extensions import Final

class BuildType:
    STANDARD: Final[int]
    MODULE: Final[int]
    PROGRAM_TEXT: Final[int]

PER_MODULE_OPTIONS: Final[Incomplete]
OPTIONS_AFFECTING_CACHE: Final[Incomplete]
TYPE_VAR_TUPLE: Final[str]
UNPACK: Final[str]
INCOMPLETE_FEATURES: Final[Incomplete]

class Options:
    """Options collected from flags."""
    build_type: Incomplete
    python_version: Incomplete
    python_executable: Incomplete
    platform: Incomplete
    custom_typing_module: Incomplete
    custom_typeshed_dir: Incomplete
    abs_custom_typeshed_dir: Incomplete
    mypy_path: Incomplete
    report_dirs: Incomplete
    no_silence_site_packages: bool
    no_site_packages: bool
    ignore_missing_imports: bool
    ignore_missing_imports_per_module: bool
    follow_imports: str
    follow_imports_for_stubs: bool
    namespace_packages: bool
    explicit_package_bases: bool
    exclude: Incomplete
    disallow_any_generics: bool
    disallow_any_unimported: bool
    disallow_any_expr: bool
    disallow_any_decorated: bool
    disallow_any_explicit: bool
    disallow_untyped_calls: bool
    disallow_untyped_defs: bool
    disallow_incomplete_defs: bool
    check_untyped_defs: bool
    disallow_untyped_decorators: bool
    disallow_subclassing_any: bool
    warn_incomplete_stub: bool
    warn_redundant_casts: bool
    warn_no_return: bool
    warn_return_any: bool
    warn_unused_ignores: bool
    warn_unused_configs: bool
    ignore_errors: bool
    strict_optional: bool
    show_error_context: bool
    color_output: bool
    error_summary: bool
    implicit_optional: bool
    implicit_reexport: bool
    allow_untyped_globals: bool
    allow_redefinition: bool
    strict_equality: bool
    strict_concatenate: bool
    warn_unreachable: bool
    always_true: Incomplete
    always_false: Incomplete
    disable_error_code: Incomplete
    disabled_error_codes: Incomplete
    enable_error_code: Incomplete
    enabled_error_codes: Incomplete
    scripts_are_modules: bool
    config_file: Incomplete
    quickstart_file: Incomplete
    files: Incomplete
    packages: Incomplete
    modules: Incomplete
    junit_xml: Incomplete
    incremental: bool
    cache_dir: Incomplete
    sqlite_cache: bool
    debug_cache: bool
    skip_version_check: bool
    skip_cache_mtime_checks: bool
    fine_grained_incremental: bool
    cache_fine_grained: bool
    use_fine_grained_cache: bool
    debug_serialize: bool
    mypyc: bool
    inspections: bool
    preserve_asts: bool
    plugins: Incomplete
    per_module_options: Incomplete
    unused_configs: Incomplete
    verbosity: int
    pdb: bool
    show_traceback: bool
    raise_exceptions: bool
    dump_type_stats: bool
    dump_inference_stats: bool
    dump_build_stats: bool
    enable_incomplete_features: bool
    enable_incomplete_feature: Incomplete
    timing_stats: Incomplete
    line_checking_stats: Incomplete
    semantic_analysis_only: bool
    use_builtins_fixtures: bool
    shadow_file: Incomplete
    show_column_numbers: bool
    show_error_end: bool
    hide_error_codes: bool
    pretty: bool
    dump_graph: bool
    dump_deps: bool
    logical_deps: bool
    local_partial_types: bool
    bazel: bool
    export_types: bool
    package_root: Incomplete
    cache_map: Incomplete
    fast_exit: bool
    fast_module_lookup: bool
    allow_empty_bodies: bool
    transform_source: Incomplete
    show_absolute_path: bool
    install_types: bool
    non_interactive: bool
    many_errors_threshold: Incomplete
    disable_recursive_aliases: bool
    enable_recursive_aliases: bool
    export_ref_info: bool
    disable_bytearray_promotion: bool
    disable_memoryview_promotion: bool
    force_uppercase_builtins: bool
    force_union_syntax: bool
    def __init__(self) -> None: ...
    def use_lowercase_names(self) -> bool: ...
    def use_or_syntax(self) -> bool: ...
    @property
    def new_semantic_analyzer(self) -> bool: ...
    def snapshot(self) -> object:
        """Produce a comparable snapshot of this Option"""
    def apply_changes(self, changes: dict[str, object]) -> Options: ...
    def build_per_module_cache(self) -> None: ...
    def clone_for_module(self, module: str) -> Options:
        """Create an Options object that incorporates per-module options.

        NOTE: Once this method is called all Options objects should be
        considered read-only, else the caching might be incorrect.
        """
    def compile_glob(self, s: str) -> Pattern[str]: ...
    def select_options_affecting_cache(self) -> Mapping[str, object]: ...
