from .. import config as config
from ..codecache import cache_dir as cache_dir
from ..ir import ReductionHint as ReductionHint, TileHint as TileHint
from ..utils import conditional_product as conditional_product, has_triton as has_triton
from .conv_perf_model import estimate_conv_time as estimate_conv_time
from _typeshed import Incomplete
from torch._dynamo.utils import dynamo_timed as dynamo_timed
from triton import Config
from triton.runtime.jit import KernelInterface
from typing import List

log: Incomplete
Config = object
KernelInterface = object

class CachingAutotuner(KernelInterface):
    """
    Simplified version of Triton autotuner that has no invalidation
    key and caches the best config to disk to improve cold start times.
    Unlike the main triton Autotuner, this version can precompile all
    configs, and does not rely on the Triton JIT.
    """
    fn: Incomplete
    meta: Incomplete
    save_cache_hook: Incomplete
    mutated_arg_names: Incomplete
    configs: Incomplete
    launchers: Incomplete
    lock: Incomplete
    def __init__(self, fn, meta, configs, save_cache_hook, mutated_arg_names) -> None: ...
    def precompile(self, warm_cache_only_with_cc: Incomplete | None = None) -> None: ...
    def bench(self, launcher, *args, grid):
        """Measure the performance of a given launcher"""
    def autotune_to_one_config(self, *args, **kwargs) -> None:
        """Do the actual autotuning"""
    def run(self, *args, grid, stream): ...

def hash_configs(configs: List[Config]):
    """
    Hash used to check for changes in configurations
    """
def load_cached_autotuning(cache_filename: str, configs_hash: str, configs: List[Config]):
    """
    Read a cached autotuning result from disk
    """
def cached_autotune(configs: List[Config], meta, filename: Incomplete | None = None):
    """
    A copy of triton.autotune that calls our subclass.  Our subclass
    has additional debugging, error handling, and on-disk caching.
    """
def unique_configs(configs: List[Config]):
    """Remove duplicate configurations"""
def triton_config(size_hints, x, y: Incomplete | None = None, z: Incomplete | None = None, num_stages: int = 1) -> Config:
    """
    Construct a pointwise triton config with some adjustment heuristics
    based on size_hints. Size_hints is a tuple of numels in each tile
    dimension and will be rounded up to the nearest power of 2.
    """
def triton_config_reduction(size_hints, x, r, num_stages: int = 2) -> Config:
    """
    Construct a reduction triton config with some adjustment heuristics
    based on size_hints. Size_hints is a tuple of numels in each tile
    dimension and will be rounded up to the nearest power of 2.
    """
def triton_config_tiled_reduction(size_hints, x, y, r, num_stages: int = 2):
    """
    Construct a tile reduction triton config with some adjustment
    heuristics based on size_hints. Size_hints is a tuple of numels in
    each tile dimension and will be rounded up to the nearest power of 2.
    """
def pointwise(size_hints, meta, tile_hint: Incomplete | None = None, filename: Incomplete | None = None):
    """
    Construct @triton.heuristics() based on size_hints.
    """
def reduction(size_hints, reduction_hint: bool = False, meta: Incomplete | None = None, filename: Incomplete | None = None):
    """args to @triton.heuristics()"""
def persistent_reduction(size_hints, reduction_hint: bool = False, meta: Incomplete | None = None, filename: Incomplete | None = None): ...
def template(num_stages, num_warps, meta, filename: Incomplete | None = None):
    """
    Compile a triton template
    """
def conv_heuristics(): ...
def grid(xnumel, ynumel: Incomplete | None = None, znumel: Incomplete | None = None):
    """Helper function to compute triton grids"""
