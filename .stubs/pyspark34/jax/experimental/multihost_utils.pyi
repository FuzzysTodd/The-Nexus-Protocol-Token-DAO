import jax
from _typeshed import Incomplete
from jax._src import array as array, core as core, distributed as distributed, sharding_impls as sharding_impls
from jax._src.interpreters import ad as ad, batching as batching, mlir as mlir, pxla as pxla
from jax._src.util import safe_zip as safe_zip
from jax.experimental.pjit import pjit as pjit
from jax.interpreters import xla as xla
from jax.tree_util import tree_flatten as tree_flatten, tree_map as tree_map, tree_unflatten as tree_unflatten
from typing import Any

def broadcast_one_to_all(in_tree: Any, is_source: bool | None = None) -> Any:
    """Broadcast data from a source host (host 0 by default) to all other hosts.

  Args:
    in_tree: pytree of arrays - each array *must* have the same shape across the
      hosts.
    is_source: optional bool denoting whether the caller is the source. Only
      'source host' will contribute the data for the broadcast. If None, then
      host 0 is used.

  Returns:
    A pytree matching in_tree where the leaves now all contain the data from the
    first host.
  """
def sync_global_devices(name: str):
    """Creates a barrier across all hosts/devices."""
def process_allgather(in_tree: Any, tiled: bool = False) -> Any:
    """Gather data from across processes.

  Args:
    in_tree: pytree of arrays - each array _must_ have the same shape across the
      hosts.
    tiled: Whether to stack or concat the output. Defaults to False i.e. stack
      into a new positional axis at index 0.

  Returns:
    Pytrees of numpy arrays.
      * If the input is a non-fully addressable jax.Array, then the data is
        fully replicated.
      * If the input is numpy array or fully addressable jax.Array, then the
        output shape is dependent on the `tiled` argument.
        If its False, then the output will be stacked else concatenated.
      * If the input is a scalar, then the output will be stacked.
  """
def assert_equal(in_tree, fail_message: str = ''):
    """Verifies that all the hosts have the same tree of values."""
def reached_preemption_sync_point(step_id: int) -> bool:
    """Determine whether all hosts have reached a preemption sync step.

  When any host receive a preemption notice, the notice will be propagated to
  all hosts and trigger a synchronization protocol in background. The
  synchronization protocol calculates the maximum step ids from all hosts, and
  uses the next step id (i.e., max + 1) as the safe step to save a checkpoint.
  All hosts should continue training more steps until this method returns True,
  indicating that the `step_id` is equal to the safe step and the hosts should
  start saving a checkpoint.

  To use this API, all hosts must start training from the same step and call at
  every training step. Example usage:

  ```
  def should_save(step_id: int) -> bool:

    # Should save an on-demand checkpoint for preemption
    if multihost_utils.reached_preemption_sync_point(step_id):
      return True

    # Should save a regular checkpoint
    return step_id - last_saved_checkpoint_step >= save_interval_steps
  ```

  Preemption notice is provided by the cluster scheduler to notify the
  application in advance before it gets evicted. By default, we use SIGTERM as
  the signal for preemption notice.

  TODO(b/230630494): Add instructions for customized preemption notice.

  Returns:
    A boolean indicating whether all hosts have reached a synchronization step
    after some hosts are preempted.

  Raises:
    RuntimeError: if preemption sync manager has not been inititialized.
  """
def host_local_array_to_global_array_impl(arr: Any, *, global_mesh: jax.sharding.Mesh, pspec: Any): ...
def host_local_array_to_global_array(local_inputs: Any, global_mesh: jax.sharding.Mesh, pspecs: Any):
    """Converts a host local value to a globally sharded jax.Array.

  You can use this function to transition to jax.Array. Using jax.Array with
  pjit has the same semantics of using GDA with pjit i.e. all jax.Array
  inputs to pjit should be globally shaped.

  If you are currently passing host local values to pjit, you can use this
  function to convert your host local values to global Arrays and then pass that
  to pjit. Example usage.

  >>> from jax.experimental import multihost_utils # doctest: +SKIP
  >>>
  >>> global_inputs = multihost_utils.host_local_array_to_global_array(host_local_inputs, global_mesh, in_pspecs) # doctest: +SKIP
  >>>
  >>> with mesh: # doctest: +SKIP
  >>>   global_out = pjitted_fun(global_inputs) # doctest: +SKIP
  >>>
  >>> host_local_output = multihost_utils.global_array_to_host_local_array(global_out, mesh, out_pspecs) # doctest: +SKIP

  Args:
    local_inputs: A Pytree of host local values.
    global_mesh: A jax.sharding.Mesh object.
    pspecs: A Pytree of jax.sharding.PartitionSpec's.
  """

host_local_array_to_global_array_p: Incomplete

def ltg_abstract_eval(arr, *, global_mesh, pspec): ...
def ltg_batcher(insert_axis, spmd_axis_name, axis_size, axis_name, main_type, vals_in, dims_in, global_mesh, pspec): ...
def global_array_to_host_local_array_impl(arr: Any, *, global_mesh: jax.sharding.Mesh, pspec: Any): ...
def global_array_to_host_local_array(global_inputs: Any, global_mesh: jax.sharding.Mesh, pspecs: Any):
    """Converts a global `jax.Array` to a host local `jax.Array`.

  You can use this function to transition to `jax.Array`. Using `jax.Array` with
  pjit has the same semantics of using GDA with pjit i.e. all `jax.Array`
  inputs to pjit should be globally shaped and the output from pjit will also
  be globally shaped jax.Array's

  You can use this function to convert the globally shaped `jax.Array` output
  from pjit to host local values again so that the transition to jax.Array can
  be a mechanical change. Example usage

  >> from jax.experimental import multihost_utils # doctest: +SKIP
  >>
  >> global_inputs = multihost_utils.host_local_array_to_global_array(host_local_inputs, global_mesh, in_pspecs) # doctest: +SKIP
  >>
  >> with mesh: # doctest: +SKIP
  >>   global_out = pjitted_fun(global_inputs) # doctest: +SKIP
  >>
  >> host_local_output = multihost_utils.global_array_to_host_local_array(global_out, mesh, out_pspecs) # doctest: +SKIP

  Args:
    global_inputs: A Pytree of global jax.Array's.
    global_mesh: A jax.sharding.Mesh object.
    pspecs: A Pytree of jax.sharding.PartitionSpec's.
  """

global_array_to_host_local_array_p: Incomplete

def gtl_abstract_eval(arr, *, global_mesh, pspec): ...
