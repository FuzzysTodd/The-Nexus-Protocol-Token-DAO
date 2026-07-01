import threading
from _typeshed import Incomplete
from jax import custom_derivatives as custom_derivatives, lax as lax
from jax._src import ad_checkpoint as ad_checkpoint, api as api, compiler as compiler, config as config, core as core, dispatch as dispatch, dtypes as dtypes, sharding_impls as sharding_impls, source_info_util as source_info_util, tree_util as tree_util, util as util
from jax._src.interpreters import ad as ad, batching as batching, mlir as mlir, pxla as pxla, xla as xla
from jax._src.lib import xla_client as xla_client, xla_extension as xla_extension
from jax._src.lib.mlir.dialects import hlo as hlo
from jax.experimental import pjit as pjit
from typing import Any, Callable

logger: Incomplete
xops: Incomplete
XlaOp: Incomplete
XlaShape: Incomplete
XlaBuilder: Incomplete
XlaDevice: Incomplete
XlaLocalClient: Incomplete
DType = Any

def id_tap(tap_func, arg, *, result: Incomplete | None = None, tap_with_device: bool = False, device_index: int = 0, **kwargs):
    """Host-callback tap primitive, like identity function with a call to ``tap_func``.

  **Experimental: please give feedback, and expect changes!**

  ``id_tap`` behaves semantically like the identity function but has the
  side-effect that a user-defined Python function is called with the runtime
  value of the argument.

  Args:
    tap_func: tap function to call like ``tap_func(arg, transforms)``, with
      ``arg`` as described below and where ``transforms`` is the sequence of
      applied JAX transformations in the form ``(name, params)``. If the
      `tap_with_device` optional argument is True, then the invocation also
      includes the device from which the value is tapped as a keyword argument:
      ``tap_func(arg, transforms, device=dev)``.
    arg: the argument passed to the tap function, can be a pytree of JAX
      types.
    result: if given, specifies the return value of ``id_tap``. This value is
      not passed to the tap function, and in fact is not sent from the device to
      the host. If the ``result`` parameter is not specified then the return
      value of ``id_tap`` is ``arg``.
    tap_with_device: if True then the tap function is invoked with the
      device from which the tap originates as a keyword argument.
    device_index: specifies from which device the tap function is invoked in a
      SPMD program. Works only when using the outfeed implementation mechanism,
      i.e., does not work on CPU unless --jax_host_callback_outfeed=True.

  Returns:
    ``arg``, or ``result`` if given.

  The order of execution is by data dependency: after all the arguments and
  the value of ``result`` if present, are computed and before the returned
  value is used. At least one of the returned values of ``id_tap`` must be
  used in the rest of the computation, or else this operation has no effect.

  Tapping works even for code executed on accelerators and even for code under
  JAX transformations.

  For more details see the :mod:`jax.experimental.host_callback` module documentation.
  """
def id_print(arg, *, result: Incomplete | None = None, tap_with_device: bool = False, device_index: int = 0, output_stream: Incomplete | None = None, threshold: Incomplete | None = None, **kwargs):
    """Like :func:`id_tap` with a printing tap function.

   **Experimental: please give feedback, and expect changes!**

   On each invocation of the printing tap, the ``kwargs`` if present
   will be printed first (sorted by keys). Then arg will be printed,
   with the arrays stringified with ``numpy.array2string``.

   See the :func:`id_tap` documentation.

   Additional keyword arguments:

   * ``tap_with_device`` if True, will print also the device from which
     the value originates.
   * ``output_stream`` if given then it will be used instead of the
     built-in ``print``. The string will be passed as
     ``output_stream.write(s)``.
   * ``threshold`` is passed to ``numpy.array2string``.

  For more details see the :mod:`jax.experimental.host_callback` module documentation.
  """
def call(callback_func: Callable, arg, *, result_shape: Incomplete | None = None, call_with_device: bool = False, device_index: int = 0):
    """Make a call to the host, and expect a result.

  **Experimental: please give feedback, and expect changes!**

  Args:
    callback_func: The Python function to invoke on the host as
      ``callback_func(arg)``. If the ``call_with_device`` optional argument is True,
      then the invocation also includes the ``device`` kwarg with the device
      from which the call originates: ``callback_func(arg, device=dev)``. This function
      must return a pytree of numpy ndarrays.

    arg: the argument passed to the callback function, can be a pytree of JAX
      types.

    result_shape: a value that describes the expected shape and dtype of the
      result. This can be a numeric scalar, from which a shape and dtype are
      obtained, or an object that has ``.shape`` and ``.dtype`` attributes.
      If the result of the callback is a pytree, then ``result_shape`` should
      also be a pytree with the same structure. In particular, ``result_shape``
      can be `()` or `None` if the function does not have any results.
      The device code containing ``call`` is compiled with the expected result shape and dtype,
      and an error will be raised at runtime if the actual ``callback_func``
      invocation returns a different kind of result.

    call_with_device: if True then the callback function is invoked with the
      device from which the call originates as a keyword argument.

    device_index: specifies from which device the tap function is invoked in a
      SPMD program. Works only when using the outfeed implementation mechanism,
      i.e., does not work on CPU unless --jax_host_callback_outfeed=True.
  Returns:
    the result of the ``callback_func`` invocation.

  For more details see the :mod:`jax.experimental.host_callback` module documentation.
  """

class _CallbackWrapper:
    callback_func: Incomplete
    identity: Incomplete
    call_with_device: Incomplete
    def __init__(self, callback_func, identity, call_with_device) -> None: ...
    def __hash__(self): ...
    def __eq__(self, other): ...
    def __call__(self, arg, device, transforms): ...

outside_call_p: Incomplete
id_p: Incomplete

class CallbackException(Exception):
    """Signals that some callback function had exceptions.

  Raised by :func:`barrier_wait`. See the :mod:`jax.experimental.host_callback`
  module documentation for details.
  """
TapFunctionException = CallbackException

class _CallbackHandlerData:
    """Keep track of the outfeed receiver data."""
    receiver: Any
    initialized: bool
    on_exit: bool
    lock: threading.Lock
    last_callback_exception: tuple[Exception, str] | None
    clients: tuple[XlaLocalClient, ...]
    devices: tuple[XlaDevice, ...]
    consumer_registry: dict[Callable, int]
    consumer_registry_by_id: dict[int, Callable]
    callback_registry: Incomplete
    callback_registry_by_id: Incomplete
    keep_alives: Incomplete
    def __init__(self) -> None: ...
    def stop(self) -> None:
        """Wait for all pending outfeeds and stop the receiver."""

def barrier_wait(logging_name: str | None = None):
    """Blocks the calling thread until all current outfeed is processed.

  Waits until all callbacks from computations already running on all devices
  have been received and processed by the Python callbacks. Raises
  CallbackException if there were exceptions while processing the callbacks.

  This works by enqueueing a special tap computation to all devices to which
  we are listening for outfeed. Once all those tap computations are done, we
  return from barrier_wait.

  Note: If any of the devices are busy and cannot accept new computations,
  this will deadlock.

  Args:
    logging_name: an optional string that will be used in the logging statements
      for this invocation. See `Debugging` in the module documentation.

  For more details see the :mod:`jax.experimental.host_callback` module documentation.
  """
def stop_outfeed_receiver() -> None:
    """Stops the outfeed receiver runtime.

  This waits for all outfeeds from computations already running on all devices,
  and then stops the outfeed receiver runtime. The runtime will be restarted
  next time you use a tap function.

  It should not be necessary to use this function, unless you want to start
  using lax.outfeed directly after having used host callbacks.
  """
