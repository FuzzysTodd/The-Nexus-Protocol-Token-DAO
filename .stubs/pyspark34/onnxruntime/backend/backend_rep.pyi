from onnx.backend.base import BackendRep
from onnxruntime import RunOptions as RunOptions
from typing import Any, Tuple

class OnnxRuntimeBackendRep(BackendRep):
    """
    Computes the prediction for a pipeline converted into
    an :class:`onnxruntime.InferenceSession` node.
    """
    def __init__(self, session) -> None:
        """
        :param session: :class:`onnxruntime.InferenceSession`
        """
    def run(self, inputs: Any, **kwargs: Any) -> Tuple[Any, ...]:
        """
        Computes the prediction.
        See :meth:`onnxruntime.InferenceSession.run`.
        """
