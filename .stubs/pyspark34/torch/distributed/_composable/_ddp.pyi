from _typeshed import Incomplete
from collections.abc import Generator
from dataclasses import dataclass
from enum import Enum
from torch.autograd import Function
from torch.nn.modules import Module
from typing import Any, Callable

__all__ = ['DistributedDataParallel']

class _BufferCommHookLocation(Enum):
    PRE_FORWARD: Incomplete
    POST_FORWARD: Incomplete

@dataclass
class _BufferCommHook:
    buffer_comm_hook: Callable
    buffer_comm_hook_state: Any
    buffer_comm_hook_location: _BufferCommHookLocation
    def __init__(self, buffer_comm_hook, buffer_comm_hook_state, buffer_comm_hook_location) -> None: ...

class _DDPSink(Function):
    @staticmethod
    def forward(ctx, reducer, state_dict, *inputs): ...
    @staticmethod
    def backward(ctx, *grad_outputs): ...

class DistributedDataParallel(Module):
    logger: Incomplete
    is_multi_device_module: Incomplete
    device_type: Incomplete
    device_ids: Incomplete
    output_device: Incomplete
    process_group: Incomplete
    static_graph: bool
    dim: Incomplete
    module: Incomplete
    device: Incomplete
    broadcast_buffers: Incomplete
    find_unused_parameters: Incomplete
    require_backward_grad_sync: bool
    require_forward_param_sync: bool
    gradient_as_bucket_view: Incomplete
    parameters_to_ignore: Incomplete
    broadcast_bucket_size: Incomplete
    bucket_bytes_cap: Incomplete
    use_side_stream_for_tensor_copies: Incomplete
    def __init__(self, module, device_ids: Incomplete | None = None, output_device: Incomplete | None = None, dim: int = 0, broadcast_buffers: bool = True, process_group: Incomplete | None = None, bucket_cap_mb: int = 25, find_unused_parameters: bool = False, gradient_as_bucket_view: bool = False, static_graph: bool = False) -> None: ...
    def no_sync(self) -> Generator[None, None, None]:
        '''
        A context manager to disable gradient synchronizations across DDP
        processes. Within this context, gradients will be accumulated on module
        variables, which will later be synchronized in the first
        forward-backward pass exiting the context.

        Example::

            >>> # xdoctest: +SKIP("undefined variables")
            >>> ddp = torch.nn.parallel.DistributedDataParallel(model, pg)
            >>> with ddp.no_sync():
            >>>   for input in inputs:
            >>>     ddp(input).backward()  # no synchronization, accumulate grads
            >>> ddp(another_input).backward()  # synchronize grads
        '''
    def pre_forward(self) -> None: ...
    def post_forward(self, output): ...
    def forward(self, *inputs, **kwargs): ...
    def scatter(self, inputs, kwargs, device_ids): ...
    def to_kwargs(self, inputs, kwargs, device_id): ...
    def gather(self, outputs, output_device): ...
    def train(self, mode: bool = True): ...
    def register_comm_hook(self, state: object, hook: Callable):
        """
        Registers a communication hook which is an enhancement that provides a
        flexible hook to users where they can specify how DDP aggregates gradients
        across multiple workers.

        This hook would be very useful for researchers to try out new ideas. For
        example, this hook can be used to implement several algorithms like GossipGrad
        and gradient compression which involve different communication strategies for
        parameter syncs while running Distributed DataParallel training.

        Args:
            state (object): Passed to the hook to maintain any state information during the training process.
                            Examples include error feedback in gradient compression,
                            peers to communicate with next in GossipGrad, etc.

                            It is locally stored by each worker
                            and shared by all the gradient tensors on the worker.
            hook (Callable): Callable with the following signature:
                             ``hook(state: object, bucket: dist.GradBucket) -> torch.futures.Future[torch.Tensor]``:

                             This function is called once the bucket is ready. The
                             hook can perform whatever processing is needed and return
                             a Future indicating completion of any async work (ex: allreduce).
                             If the hook doesn't perform any communication, it still
                             must return a completed Future. The Future should hold the
                             new value of grad bucket's tensors. Once a bucket is ready,
                             c10d reducer would call this hook and use the tensors returned
                             by the Future and copy grads to individual parameters.
                             Note that the future's return type must be a single tensor.

                             We also provide an API called ``get_future`` to retrieve a
                             Future associated with the completion of ``c10d.ProcessGroup.Work``.
                             ``get_future`` is currently supported for NCCL and also supported for most
                             operations on GLOO and MPI, except for peer to peer operations (send/recv).

        .. warning ::
            Grad bucket's tensors will not be predivided by world_size. User is responsible
            to divide by the world_size in case of operations like allreduce.

        .. warning ::
            DDP communication hook can only be registered once and should be registered
            before calling backward.

        .. warning ::
            The Future object that hook returns should contain a single tensor
            that has the same shape with the tensors inside grad bucket.

        .. warning ::
            ``get_future`` API supports NCCL, and partially GLOO and MPI backends (no support
            for peer-to-peer operations like send/recv) and will return a ``torch.futures.Future``.

        Example::
            Below is an example of a noop hook that returns the same tensor.

            >>> # xdoctest: +REQUIRES(module:torch._C._distributed_c10d)
            >>> def noop(state: object, bucket: dist.GradBucket) -> torch.futures.Future[torch.Tensor]:
            >>>     fut = torch.futures.Future()
            >>>     fut.set_result(bucket.buffer())
            >>>     return fut

            >>> # xdoctest: +SKIP('undefined name')
            >>> ddp.register_comm_hook(state=None, hook=noop)

        Example::
            Below is an example of a Parallel SGD algorithm where gradients are encoded before
            allreduce, and then decoded after allreduce.

            >>> # xdoctest: +REQUIRES(module:torch._C._distributed_c10d)
            >>> def encode_and_decode(state: object, bucket: dist.GradBucket) -> torch.futures.Future[torch.Tensor]:
            >>>     encoded_tensor = encode(bucket.buffer()) # encode gradients
            >>>     fut = torch.distributed.all_reduce(encoded_tensor).get_future()
            >>>     # Define the then callback to decode.
            >>>     def decode(fut):
            >>>         decoded_tensor = decode(fut.value()[0]) # decode gradients
            >>>         return decoded_tensor
            >>>     return fut.then(decode)

            >>> # xdoctest: +SKIP('undefined name')
            >>> ddp.register_comm_hook(state=None, hook=encode_and_decode)
        """
    def will_sync_module_buffers(self): ...
