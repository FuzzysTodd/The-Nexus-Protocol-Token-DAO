import torch
from typing import Any, Iterable, List, Tuple

__all__ = ['checkpoint', 'checkpoint_sequential', 'CheckpointFunction', 'check_backward_validity', 'detach_variable', 'get_device_states', 'set_device_states']

def detach_variable(inputs: Tuple[Any, ...]) -> Tuple[torch.Tensor, ...]: ...
def check_backward_validity(inputs: Iterable[Any]) -> None: ...
def get_device_states(*args) -> Tuple[List[int], List[torch.Tensor]]: ...
def set_device_states(devices, states) -> None: ...

class CheckpointFunction(torch.autograd.Function):
    @staticmethod
    def forward(ctx, run_function, preserve_rng_state, *args): ...
    @staticmethod
    def backward(ctx, *args): ...

def checkpoint(function, *args, use_reentrant: bool = True, **kwargs):
    """Checkpoint a model or part of the model

    Checkpointing works by trading compute for memory. Rather than storing all
    intermediate activations of the entire computation graph for computing
    backward, the checkpointed part does **not** save intermediate activations,
    and instead recomputes them in backward pass. It can be applied on any part
    of a model.

    Specifically, in the forward pass, :attr:`function` will run in
    :func:`torch.no_grad` manner, i.e., not storing the intermediate
    activations. Instead, the forward pass saves the inputs tuple and the
    :attr:`function` parameter. In the backwards pass, the saved inputs and
    :attr:`function` is retrieved, and the forward pass is computed on
    :attr:`function` again, now tracking the intermediate activations, and then
    the gradients are calculated using these activation values.

    The output of :attr:`function` can contain non-Tensor values and gradient
    recording is only performed for the Tensor values. Note that if the output
    consists of nested structures (ex: custom objects, lists, dicts etc.)
    consisting of Tensors, these Tensors nested in custom structures will not
    be considered as part of autograd.


    .. warning::
        If :attr:`function` invocation during backward does anything different
        than the one during forward, e.g., due to some global variable, the
        checkpointed version won't be equivalent, and unfortunately it can't be
        detected.

    .. warning::
        If ``use_reentrant=True`` is specified, then if the checkpointed segment
        contains tensors detached from the computational graph by `detach()` or
        `torch.no_grad()`, the backward pass will raise an error. This is
        because `checkpoint` makes all the outputs require gradients which
        causes issues when a tensor is defined to have no gradient in the model.
        To circumvent this, detach the tensors outside of the `checkpoint`
        function. Note that the checkpointed segment can contain tensors
        detached from the computational graph if ``use_reentrant=False`` is
        specified.

    .. warning::
        If ``use_reentrant=True`` is specified, at least one of the inputs needs
        to have :code:`requires_grad=True` if grads are needed for model inputs,
        otherwise the checkpointed part of the model won't have gradients. At
        least one of the outputs needs to have :code:`requires_grad=True` as
        well. Note that this does not apply if ``use_reentrant=False`` is
        specified.

    .. warning::
        If ``use_reentrant=True`` is specified, checkpointing currently only
        supports :func:`torch.autograd.backward` and only if its `inputs`
        argument is not passed. :func:`torch.autograd.grad`
        is not supported. If ``use_reentrant=False`` is specified, checkpointing
        will work with :func:`torch.autograd.grad`.

    Args:
        function: describes what to run in the forward pass of the model or
            part of the model. It should also know how to handle the inputs
            passed as the tuple. For example, in LSTM, if user passes
            ``(activation, hidden)``, :attr:`function` should correctly use the
            first input as ``activation`` and the second input as ``hidden``
        preserve_rng_state(bool, optional):  Omit stashing and restoring
            the RNG state during each checkpoint.
            Default: ``True``
        use_reentrant(bool, optional): Use checkpointing
            implementation that requires re-entrant autograd.
            If ``use_reentrant=False`` is specified, ``checkpoint`` will use an
            implementation that does not require re-entrant autograd. This
            allows ``checkpoint`` to support additional functionality, such as
            working as expected with ``torch.autograd.grad`` and support for
            keyword arguments input into the checkpointed function. Note that future
            versions of PyTorch will default to ``use_reentrant=False``.
            Default: ``True``
        args: tuple containing inputs to the :attr:`function`

    Returns:
        Output of running :attr:`function` on :attr:`*args`
    """
def checkpoint_sequential(functions, segments, input, use_reentrant: bool = True, **kwargs):
    '''A helper function for checkpointing sequential models.

    Sequential models execute a list of modules/functions in order
    (sequentially). Therefore, we can divide such a model in various segments
    and checkpoint each segment. All segments except the last will run in
    :func:`torch.no_grad` manner, i.e., not storing the intermediate
    activations. The inputs of each checkpointed segment will be saved for
    re-running the segment in the backward pass.

    See :func:`~torch.utils.checkpoint.checkpoint` on how checkpointing works.

    .. warning::
        Checkpointing currently only supports :func:`torch.autograd.backward`
        and only if its `inputs` argument is not passed. :func:`torch.autograd.grad`
        is not supported.

    .. warning:
        At least one of the inputs needs to have :code:`requires_grad=True` if
        grads are needed for model inputs, otherwise the checkpointed part of the
        model won\'t have gradients.

    .. warning:
        Since PyTorch 1.4, it allows only one Tensor as the input and
        intermediate outputs, just like :class:`torch.nn.Sequential`.

    Args:
        functions: A :class:`torch.nn.Sequential` or the list of modules or
            functions (comprising the model) to run sequentially.
        segments: Number of chunks to create in the model
        input: A Tensor that is input to :attr:`functions`
        preserve_rng_state(bool, optional):  Omit stashing and restoring
            the RNG state during each checkpoint.
            Default: ``True``
        use_reentrant(bool, optional): Use checkpointing
            implementation that requires re-entrant autograd.
            If ``use_reentrant=False`` is specified, ``checkpoint`` will use an
            implementation that does not require re-entrant autograd. This
            allows ``checkpoint`` to support additional functionality, such as
            working as expected with ``torch.autograd.grad`` and support for
            keyword arguments input into the checkpointed function.
            Default: ``True``

    Returns:
        Output of running :attr:`functions` sequentially on :attr:`*inputs`

    Example:
        >>> # xdoctest: +SKIP("stub")
        >>> model = nn.Sequential(...)
        >>> input_var = checkpoint_sequential(model, chunks, input_var)
    '''
