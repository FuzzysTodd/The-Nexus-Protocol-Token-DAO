from _typeshed import Incomplete

class FxToOnnxContext:
    '''Context manager to make PyTorch friendly to FX-to-ONNX exporter.
    This class means to collect all "patches" required by FX-to-ONNX
    exporter. If PyTorch needs to be patched, please use this class to
    manage the patch.

    This context overrides several torch functions to support symbolic
    export of large scale models.

    torch.load:
        This function is patched to record the files PyTorch stores model
        parameters and buffers. Downstream FX-to-ONNX exporter can create
        initializers from these files.
    torch._util._rebuild_tensor:
        This function is patched to avoid creating real tensors during
        model loading. FakeTensor\'s are created instead. Real tensors
        cannot be fitted into single machine\'s memory for the targeted
        model scale.
    torch.fx._symbolic_trace._wrapped_methods_to_patch:
        This list is extended with (torch.Tensor, "__getitem__") so that
        weight[x, :, y] becomes exportable with torch.fx.symbolic_trace.

    Search for FxToOnnxContext in test_fx_to_onnx_with_onnxruntime.py for
    example usage.
    '''
    paths: Incomplete
    torch_load: Incomplete
    torch__util_rebuild_tensor: Incomplete
    torch_load_wrapper: Incomplete
    torch__util_rebuild_tensor_wrapper: Incomplete
    def __init__(self) -> None: ...
    torch_fx__symbolic_trace__wrapped_methods_to_patch: Incomplete
    def __enter__(self) -> None: ...
    def __exit__(self, exc_type: type[BaseException] | None, exc_value: BaseException | None, traceback: types.TracebackType | None) -> None: ...
