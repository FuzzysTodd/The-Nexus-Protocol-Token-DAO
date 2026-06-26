from .._dynamo.config_utils import install_config_module as install_config_module
from _typeshed import Incomplete

debug: bool
disable_progress: bool
verbose_progress: bool
cpp_wrapper: bool
dce: bool
static_weight_shapes: bool
size_asserts: bool
pick_loop_orders: bool
inplace_buffers: bool
benchmark_harness: bool
epilogue_fusion: bool
epilogue_fusion_first: bool
pattern_matcher: bool
reordering: bool
max_autotune: Incomplete
realize_reads_threshold: int
realize_bytes_threshold: int
realize_acc_reads_threshold: int
fallback_random: bool
implicit_fallbacks: bool
tune_layout: bool
aggressive_fusion: bool
max_fusion_size: int
unroll_reductions_threshold: int
comment_origin: bool

def is_fbcode(): ...

developer_warnings: Incomplete
compile_threads: Incomplete
kernel_name_max_ops: int
shape_padding: Incomplete
permute_fusion: Incomplete
profiler_mark_wrapper_call: bool

class cpp:
    threads: int
    dynamic_threads: bool
    simdlen: Incomplete
    min_chunk_size: int
    cxx: Incomplete
    enable_kernel_profile: bool
    weight_prepack: bool

class triton:
    cudagraphs: bool
    debug_sync_graph: bool
    debug_sync_kernel: bool
    dense_indexing: bool
    max_tiles: int
    autotune_pointwise: bool
    tiling_prevents_pointwise_fusion: bool
    tiling_prevents_reduction_fusion: bool
    ordered_kernel_names: bool
    descriptive_kernel_names: bool
    persistent_reductions: bool

class trace:
    enabled: Incomplete
    debug_log: bool
    info_log: bool
    fx_graph: bool
    fx_graph_transformed: bool
    ir_pre_fusion: bool
    ir_post_fusion: bool
    output_code: bool
    graph_diagram: bool
    compile_profile: bool
    upload_tar: Incomplete
