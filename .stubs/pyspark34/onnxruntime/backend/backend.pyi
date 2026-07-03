from _typeshed import Incomplete
from onnx import ModelProto as ModelProto
from onnx.backend.base import Backend
from onnxruntime import InferenceSession as InferenceSession, SessionOptions as SessionOptions, get_available_providers as get_available_providers, get_device as get_device
from onnxruntime.backend.backend_rep import OnnxRuntimeBackendRep as OnnxRuntimeBackendRep

class OnnxRuntimeBackend(Backend):
    """
    Implements
    `ONNX's backend API <https://github.com/onnx/onnx/blob/main/docs/ImplementingAnOnnxBackend.md>`_
    with *ONNX Runtime*.
    The backend is mostly used when you need to switch between
    multiple runtimes with the same API.
    `Importing models from ONNX to Caffe2 <https://github.com/onnx/tutorials/blob/master/tutorials/OnnxCaffe2Import.ipynb>`_
    shows how to use *caffe2* as a backend for a converted model.
    Note: This is not the official Python API.
    """
    allowReleasedOpsetsOnly: Incomplete
    @classmethod
    def is_compatible(cls, model, device: Incomplete | None = None, **kwargs):
        """
        Return whether the model is compatible with the backend.

        :param model: unused
        :param device: None to use the default device or a string (ex: `'CPU'`)
        :return: boolean
        """
    @classmethod
    def is_opset_supported(cls, model):
        """
        Return whether the opset for the model is supported by the backend.
        When By default only released onnx opsets are allowed by the backend
        To test new opsets env variable ALLOW_RELEASED_ONNX_OPSET_ONLY should be set to 0

        :param model: Model whose opsets needed to be verified.
        :return: boolean and error message if opset is not supported.
        """
    @classmethod
    def supports_device(cls, device):
        """
        Check whether the backend is compiled with particular device support.
        In particular it's used in the testing suite.
        """
    @classmethod
    def prepare(cls, model, device: Incomplete | None = None, **kwargs):
        """
        Load the model and creates a :class:`onnxruntime.InferenceSession`
        ready to be used as a backend.

        :param model: ModelProto (returned by `onnx.load`),
            string for a filename or bytes for a serialized model
        :param device: requested device for the computation,
            None means the default one which depends on
            the compilation settings
        :param kwargs: see :class:`onnxruntime.SessionOptions`
        :return: :class:`onnxruntime.InferenceSession`
        """
    @classmethod
    def run_model(cls, model, inputs, device: Incomplete | None = None, **kwargs):
        """
        Compute the prediction.

        :param model: :class:`onnxruntime.InferenceSession` returned
            by function *prepare*
        :param inputs: inputs
        :param device: requested device for the computation,
            None means the default one which depends on
            the compilation settings
        :param kwargs: see :class:`onnxruntime.RunOptions`
        :return: predictions
        """
    @classmethod
    def run_node(cls, node, inputs, device: Incomplete | None = None, outputs_info: Incomplete | None = None, **kwargs) -> None:
        """
        This method is not implemented as it is much more efficient
        to run a whole model than every node independently.
        """

is_compatible: Incomplete
prepare: Incomplete
run: Incomplete
supports_device: Incomplete
