from _typeshed import Incomplete
from tensorflow.python.ops import linalg_ops as linalg_ops, math_ops as math_ops

TRACE_MODE_PART_TENSOR: str
TRACE_MODE_FULL_TENSOR: str
TRACE_MODE_FULL_TENSOR_SUMMARY: str
TRACE_MODE_NAN_INF: str
TRACE_MODE_NORM: str
TRACE_MODE_MAX_ABS: str
TRACE_MODE_SUMMARY: str
TRACE_MODE_HISTORY: str
FLAGS_ENV_VAR: str
FLAG_NAME_ENABLE: str
FLAG_NAME_TRACE_MODE: str
FLAG_NAME_TRACE_SCALAR_OPS: str
FLAG_NAME_SUBMODE: str
FLAG_NAME_EXCLUDED_OPNAMES: str
FLAG_NAME_EXCLUDED_OPTYPES: str
FLAG_NAME_INCLUDED_OPNAMES: str
FLAG_NAME_INCLUDED_OPTYPES: str
FLAG_NAME_TRACE_LEVEL: str
FLAG_NAME_TRACE_DIR: str
FLAG_NAME_REPORT_FILE: str
FLAG_NAME_USE_TEST_UNDECLARED_OUTPUTS_DIR: str
FLAG_NAME_OP_RANGE: str
FLAG_NAME_DUMP_BEFORE_AFTER_GRAPHS: str
FLAG_NAME_SUMMARY_SIGNATURES: str
FLAG_NAME_SUMMARY_PER_CORE: str
FLAG_NAME_TEMP_CACHE_VAR: str
FLAG_NAME_INSPECT_TRACE: str
FLAG_NAME_FINGERPRINT_DIR: str
FLAG_FLUSH_SUMMARY: str
VALID_FLAG_NAMES: Incomplete
TT_SUMMARY_NORM: Incomplete
TT_SUMMARY_MAX: Incomplete
TT_SUMMARY_MAX_ABS: Incomplete
TT_SUMMARY_MIN: Incomplete
TT_SUMMARY_SPARSITY: Incomplete
TT_SUMMARY_MEAN: Incomplete
TT_SUMMARY_VAR: Incomplete
TT_SUMMARY_SIZE: Incomplete
TT_SUMMARY_SIGNATURES: Incomplete
FLAGS: Incomplete
DELTA_THRESHOLD: Incomplete
TT_CHECK_FILTER: Incomplete
TT_SINGLE_CORE_SUMMARIES: Incomplete

class TTParameters:
    """A class that handles the parameters of Tensor Tracer."""
    trace_mode: Incomplete
    submode: Incomplete
    trace_dir: Incomplete
    report_file_path: Incomplete
    op_range: Incomplete
    excluded_opname_re_list: Incomplete
    excluded_optype_re_list: Incomplete
    included_opname_re_list: Incomplete
    included_optype_re_list: Incomplete
    trace_scalar_ops: Incomplete
    use_compact_trace: Incomplete
    use_temp_cache_var: Incomplete
    inspect_trace: Incomplete
    use_fingerprint_subdir: Incomplete
    trace_level: Incomplete
    summary_signatures: Incomplete
    collect_summary_per_core: Incomplete
    flush_summaries_with_outside_compile: Incomplete
    def __init__(self, env: Incomplete | None = None) -> None: ...
    def is_brief_mode(self): ...
    @staticmethod
    def match_next_flag(tt_flags, pos):
        """Returns the match for the next TensorTracer flag.

    Args:
       tt_flags: a string that contains the flags.
       pos: where in flags to start the search.

    Returns:
       A pair where the first element is the regular-expression
       match found and the second element indicates if the match
       has a value.
    """
    def get_signature_to_agg_fn_map(self):
        """Returns a map that contains the aggregate function for each signature."""
    def get_flag_value(self, wanted_flag_name):
        """Returns the value of a TensorTracer flags.

    Args:
      wanted_flag_name: the name of the flag we are looking for.

    Returns:
      A pair where the first element indicates if the flag is
      found and the second element is the value of the flag.

    Raises:
      RuntimeError: If supposedly deadcode is reached.
    """
    def is_flag_on(self, flag_name):
        """Returns True if the given flag is on."""
    def is_enabled(self):
        """Returns True if TensorTracer is enabled."""
    def use_test_undeclared_outputs_dir(self):
        """Decides the output directory of the report and trace files.

    Args:
       None.

    Returns:
       True if the output files should be written to the
       test-undeclared-outputs-directory defined via an
       env variable.
    """
