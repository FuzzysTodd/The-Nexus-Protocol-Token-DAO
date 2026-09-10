import torch
from _typeshed import Incomplete
from enum import Enum

__all__ = ['OptState', 'GradScaler']

class _MultiDeviceReplicator:
    """
    Lazily serves copies of a tensor to requested devices.  Copies are cached per-device.
    """
    master: Incomplete
    def __init__(self, master_tensor: torch.Tensor) -> None: ...
    def get(self, device) -> torch.Tensor: ...

class OptState(Enum):
    READY: int
    UNSCALED: int
    STEPPED: int

class GradScaler:
    def __init__(self, init_scale=..., growth_factor: float = 2.0, backoff_factor: float = 0.5, growth_interval: int = 2000, enabled: bool = True) -> None: ...
    def scale(self, outputs):
        """
        Multiplies ('scales') a tensor or list of tensors by the scale factor.

        Returns scaled outputs.  If this instance of :class:`GradScaler` is not enabled, outputs are returned
        unmodified.

        Args:
            outputs (Tensor or iterable of Tensors):  Outputs to scale.
        """
    def unscale_(self, optimizer) -> None:
        '''
        Divides ("unscales") the optimizer\'s gradient tensors by the scale factor.

        :meth:`unscale_` is optional, serving cases where you need to
        :ref:`modify or inspect gradients<working-with-unscaled-gradients>`
        between the backward pass(es) and :meth:`step`.
        If :meth:`unscale_` is not called explicitly,  gradients will be unscaled  automatically during :meth:`step`.

        Simple example, using :meth:`unscale_` to enable clipping of unscaled gradients::

            ...
            scaler.scale(loss).backward()
            scaler.unscale_(optimizer)
            torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm)
            scaler.step(optimizer)
            scaler.update()

        Args:
            optimizer (torch.optim.Optimizer):  Optimizer that owns the gradients to be unscaled.

        .. note::
            :meth:`unscale_` does not incur a CPU-GPU sync.

        .. warning::
            :meth:`unscale_` should only be called once per optimizer per :meth:`step` call,
            and only after all gradients for that optimizer\'s assigned parameters have been accumulated.
            Calling :meth:`unscale_` twice for a given optimizer between each :meth:`step` triggers a RuntimeError.

        .. warning::
            :meth:`unscale_` may unscale sparse gradients out of place, replacing the ``.grad`` attribute.
        '''
    def step(self, optimizer, *args, **kwargs):
        """
        :meth:`step` carries out the following two operations:

        1.  Internally invokes ``unscale_(optimizer)`` (unless :meth:`unscale_` was explicitly called for ``optimizer``
            earlier in the iteration).  As part of the :meth:`unscale_`, gradients are checked for infs/NaNs.
        2.  If no inf/NaN gradients are found, invokes ``optimizer.step()`` using the unscaled
            gradients.  Otherwise, ``optimizer.step()`` is skipped to avoid corrupting the params.

        ``*args`` and ``**kwargs`` are forwarded to ``optimizer.step()``.

        Returns the return value of ``optimizer.step(*args, **kwargs)``.

        Args:
            optimizer (torch.optim.Optimizer):  Optimizer that applies the gradients.
            args:  Any arguments.
            kwargs:  Any keyword arguments.

        .. warning::
            Closure use is not currently supported.
        """
    def update(self, new_scale: Incomplete | None = None) -> None:
        """
        Updates the scale factor.

        If any optimizer steps were skipped the scale is multiplied by ``backoff_factor``
        to reduce it. If ``growth_interval`` unskipped iterations occurred consecutively,
        the scale is multiplied by ``growth_factor`` to increase it.

        Passing ``new_scale`` sets the new scale value manually. (``new_scale`` is not
        used directly, it's used to fill GradScaler's internal scale tensor. So if
        ``new_scale`` was a tensor, later in-place changes to that tensor will not further
        affect the scale GradScaler uses internally.)

        Args:
            new_scale (float or :class:`torch.cuda.FloatTensor`, optional, default=None):  New scale factor.

        .. warning::
            :meth:`update` should only be called at the end of the iteration, after ``scaler.step(optimizer)`` has
            been invoked for all optimizers used this iteration.
        """
    def get_scale(self):
        """
        Returns a Python float containing the current scale, or 1.0 if scaling is disabled.

        .. warning::
            :meth:`get_scale` incurs a CPU-GPU sync.
        """
    def get_growth_factor(self):
        """
        Returns a Python float containing the scale growth factor.
        """
    def set_growth_factor(self, new_factor) -> None:
        """
        Args:
            new_scale (float):  Value to use as the new scale growth factor.
        """
    def get_backoff_factor(self):
        """
        Returns a Python float containing the scale backoff factor.
        """
    def set_backoff_factor(self, new_factor) -> None:
        """
        Args:
            new_scale (float):  Value to use as the new scale backoff factor.
        """
    def get_growth_interval(self):
        """
        Returns a Python int containing the growth interval.
        """
    def set_growth_interval(self, new_interval) -> None:
        """
        Args:
            new_interval (int):  Value to use as the new growth interval.
        """
    def is_enabled(self):
        """
        Returns a bool indicating whether this instance is enabled.
        """
    def state_dict(self):
        '''
        Returns the state of the scaler as a :class:`dict`.  It contains five entries:

        * ``"scale"`` - a Python float containing the current scale
        * ``"growth_factor"`` - a Python float containing the current growth factor
        * ``"backoff_factor"`` - a Python float containing the current backoff factor
        * ``"growth_interval"`` - a Python int containing the current growth interval
        * ``"_growth_tracker"`` - a Python int containing the number of recent consecutive unskipped steps.

        If this instance is not enabled, returns an empty dict.

        .. note::
           If you wish to checkpoint the scaler\'s state after a particular iteration, :meth:`state_dict`
           should be called after :meth:`update`.
        '''
    def load_state_dict(self, state_dict) -> None:
        """
        Loads the scaler state.  If this instance is disabled, :meth:`load_state_dict` is a no-op.

        Args:
           state_dict(dict): scaler state.  Should be an object returned from a call to :meth:`state_dict`.
        """
