import numpy as np
from _typeshed import Incomplete
from collections.abc import Sequence
from jax._src import compilation_cache as compilation_cache, lib as lib, monitoring as monitoring, path as path, profiler as profiler, traceback_util as traceback_util
from jax._src.config import config as config
from jax._src.lib import xla_client as xc, xla_extension_version as xla_extension_version
from jax._src.lib.mlir import ir as ir
from typing import Any

CompileOptions: Incomplete
logger: Incomplete

def get_latest_profile_version() -> int: ...
def use_detailed_logging(module: ir.Module) -> bool:
    """Returns 'true' if detailed logging should be enabled for 'module'."""
def get_compile_options(num_replicas: int, num_partitions: int, device_assignment: Incomplete | None = None, use_spmd_partitioning: bool = True, use_auto_spmd_partitioning: bool = False, auto_spmd_partitioning_mesh_shape: list[int] | None = None, auto_spmd_partitioning_mesh_ids: list[int] | None = None, env_options_overrides: dict[str, str] | None = None, fdo_profile: bytes | None = None, detailed_logging: bool = True) -> xc.CompileOptions:
    '''Returns the compile options to use, as derived from flag values.

  Args:
    num_replicas: Number of replicas for which to compile.
    num_partitions: Number of partitions for which to compile.
    device_assignment: Optional ndarray of jax devices indicating the assignment
      of logical replicas to physical devices (default inherited from
      xla_client.CompileOptions). Must be consistent with `num_replicas` and
      `num_partitions`.
    use_spmd_partitioning: boolean indicating whether to enable SPMD or MPMD
      partitioning in XLA.
    use_auto_spmd_partitioning: boolean indicating whether to automatically
      generate XLA shardings for SPMD partitioner.
    auto_spmd_partitioning_mesh_shape: device mesh shape used to create
      auto_spmd_partitioning search space.
    auto_spmd_partitioning_mesh_ids: device ids used to create
      auto_spmd_partitioning search space.
    env_options_overrides: dict of additional options parsed by the compiler
    fdo_profile: Optional profile for feedback-directed optimization passed to
      XLA.
    detailed_logging: Is this an "interesting" computation about which XLA
      would be wise to log compilation information?
  '''
def backend_compile(backend: xc.Client, module: ir.Module, options: xc.CompileOptions, host_callbacks: Sequence[Any]) -> xc.LoadedExecutable: ...
def compile_or_get_cached(backend: xc.Client, computation: ir.Module, devices: np.ndarray, compile_options: xc.CompileOptions, host_callbacks: Sequence[Any]) -> xc.LoadedExecutable: ...
