import abc
from .quant_utils import apply_plot as apply_plot, load_model_with_shape_infer as load_model_with_shape_infer, smooth_distribution as smooth_distribution
from _typeshed import Incomplete
from enum import Enum
from onnx import ModelProto as ModelProto
from pathlib import Path
from typing import Dict, Sequence, Tuple

class TensorData:
    def __init__(self, **kwargs) -> None: ...
    @property
    def range_value(self): ...
    @property
    def avg_std(self): ...

class TensorsData:
    calibration_method: Incomplete
    data: Incomplete
    def __init__(self, calibration_method, data: Dict[str, TensorData | Tuple]) -> None: ...
    def __iter__(self): ...
    def __contains__(self, key) -> bool: ...
    def __getitem__(self, key): ...
    def __setitem__(self, key, value) -> None: ...
    def values(self): ...

class CalibrationMethod(Enum):
    MinMax: int
    Entropy: int
    Percentile: int
    Distribution: int

class CalibrationDataReader(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass): ...
    @abc.abstractmethod
    def get_next(self) -> dict:
        """generate the input data dict for ONNXinferenceSession run"""
    def __iter__(self): ...
    def __next__(self): ...

class CalibraterBase:
    model: Incomplete
    op_types_to_calibrate: Incomplete
    augmented_model_path: Incomplete
    symmetric: Incomplete
    use_external_data_format: Incomplete
    augment_model: Incomplete
    infer_session: Incomplete
    execution_providers: Incomplete
    def __init__(self, model_path: str | Path, op_types_to_calibrate: Sequence[str] | None = None, augmented_model_path: str = 'augmented_model.onnx', symmetric: bool = False, use_external_data_format: bool = False) -> None:
        """
        :param model_path: ONNX model to calibrate. It should be a model file path
        :param op_types_to_calibrate: operator types to calibrate. By default, calibrate all the float32/float16 tensors.
        :param augmented_model_path: save augmented model to this path.
        :param symmetric: make range of tensor symmetric (central point is 0).
        :param use_external_data_format: use external data format to store model which size is >= 2Gb
        """
    def set_execution_providers(self, execution_providers=['CPUExecutionProvider']) -> None:
        """
        reset the execution providers to execute the collect_data. It triggers to re-creating inference session.
        """
    def create_inference_session(self) -> None:
        """
        create an OnnxRuntime InferenceSession.
        """
    def select_tensors_to_calibrate(self, model: ModelProto):
        """
        select input/output tensors of candidate nodes to calibrate.
        returns:
            tensors (set): set of tensor name.
            value_infos (dict): tensor name to value info.
        """
    def get_augment_model(self):
        """
        return: augmented onnx model. Call after calling augment_graph
        """
    def augment_graph(self) -> None:
        """
        abstract method: augment the input model to prepare for collecting data. It will:
            1. augment the model to be able to collect desired statistics data
            2. save augmented model to augmented_model_paths
        """
    def collect_data(self, data_reader: CalibrationDataReader):
        """
        abstract method: collect the tensors that will be used for range computation. It can be called multiple times.
        """
    def compute_data(self) -> TensorsData:
        """
        abstract method: compute data based on the calibration method stored in TensorsData
        """

class MinMaxCalibrater(CalibraterBase):
    intermediate_outputs: Incomplete
    calibrate_tensors_range: Incomplete
    num_model_outputs: Incomplete
    model_original_outputs: Incomplete
    moving_average: Incomplete
    averaging_constant: Incomplete
    def __init__(self, model_path: str | Path, op_types_to_calibrate: Sequence[str] | None = None, augmented_model_path: str = 'augmented_model.onnx', symmetric: bool = False, use_external_data_format: bool = False, moving_average: bool = False, averaging_constant: float = 0.01) -> None:
        """
        :param model_path: ONNX model to calibrate. It is a model path
        :param op_types_to_calibrate: operator types to calibrate. By default, calibrate all the float32/float16 tensors.
        :param augmented_model_path: save augmented model to this path.
        :param symmetric: make range of tensor symmetric (central point is 0).
        :param use_external_data_format: use external data format to store model which size is >= 2Gb
        :param moving_average: compute the moving average of the minimum and maximum values instead of the global minimum and maximum.
        :param averaging_constant: constant smoothing factor to use when computing the moving average.
        """
    def augment_graph(self) -> None:
        """
        Adds ReduceMin and ReduceMax nodes to all quantization_candidates op type nodes in
        model and ensures their outputs are stored as part of the graph output
        :return: augmented ONNX model
        """
    def clear_collected_data(self) -> None: ...
    def collect_data(self, data_reader: CalibrationDataReader): ...
    def merge_range(self, old_range, new_range): ...
    def compute_data(self) -> TensorsData:
        """
        Compute the min-max range of tensor
        :return: dictionary mapping: {added node names: (ReduceMin, ReduceMax) pairs }
        """

class HistogramCalibrater(CalibraterBase):
    intermediate_outputs: Incomplete
    calibrate_tensors_range: Incomplete
    num_model_outputs: Incomplete
    model_original_outputs: Incomplete
    collector: Incomplete
    method: Incomplete
    num_bins: Incomplete
    num_quantized_bins: Incomplete
    percentile: Incomplete
    tensors_to_calibrate: Incomplete
    scenario: Incomplete
    def __init__(self, model_path: str | Path, op_types_to_calibrate: Sequence[str] | None = None, augmented_model_path: str = 'augmented_model.onnx', use_external_data_format: bool = False, method: str = 'percentile', symmetric: bool = False, num_bins: int = 128, num_quantized_bins: int = 2048, percentile: float = 99.999, scenario: str = 'same') -> None:
        """
        :param model_path: ONNX model to calibrate. It is a model path.
        :param op_types_to_calibrate: operator types to calibrate. By default, calibrate all the float32/float16 tensors.
        :param augmented_model_path: save augmented model to this path.
        :param use_external_data_format: use external data format to store model which size is >= 2Gb
        :param method: A string. One of ['entropy', 'percentile'].
        :param symmetric: make range of tensor symmetric (central point is 0).
        :param num_bins: number of bins to create a new histogram for collecting tensor values.
        :param num_quantized_bins: number of quantized bins. Default 128.
        :param percentile: A float number between [0, 100]. Default 99.99.
        :param scenario: see :class:`DistributionCalibrater`
        """
    def augment_graph(self) -> None:
        """
        make all quantization_candidates op type nodes as part of the graph output.
        :return: augmented ONNX model
        """
    def clear_collected_data(self) -> None: ...
    def collect_data(self, data_reader: CalibrationDataReader):
        """
        Entropy Calibrator collects operators' tensors as well as generates tensor histogram for each operator.
        """
    def compute_data(self) -> TensorsData:
        """
        Compute the min-max range of tensor
        :return: dictionary mapping: {tensor name: (min value, max value)}
        """

class EntropyCalibrater(HistogramCalibrater):
    def __init__(self, model_path: str | Path, op_types_to_calibrate: Sequence[str] | None = None, augmented_model_path: str = 'augmented_model.onnx', use_external_data_format: bool = False, method: str = 'entropy', symmetric: bool = False, num_bins: int = 128, num_quantized_bins: int = 128) -> None:
        """
        :param model_path: ONNX model to calibrate. It is a model path
        :param op_types_to_calibrate: operator types to calibrate. By default, calibrate all the float32/float16 tensors.
        :param augmented_model_path: save augmented model to this path.
        :param use_external_data_format: use external data format to store model which size is >= 2Gb
        :param method: A string. One of ['entropy', 'percentile', 'distribution'].
        :param symmetric: make range of tensor symmetric (central point is 0).
        :param num_bins: number of bins to create a new histogram for collecting tensor values.
        :param num_quantized_bins: number of quantized bins. Default 128.
        """

class PercentileCalibrater(HistogramCalibrater):
    def __init__(self, model_path: str | Path, op_types_to_calibrate: Sequence[str] | None = None, augmented_model_path: str = 'augmented_model.onnx', use_external_data_format: bool = False, method: str = 'percentile', symmetric: bool = False, num_bins: int = 2048, percentile: float = 99.999) -> None:
        """
        :param model_path: ONNX model to calibrate. It is a model path
        :param op_types_to_calibrate: operator types to calibrate. By default, calibrate all the float32/float16 tensors.
        :param augmented_model_path: save augmented model to this path.
        :param use_external_data_format: use external data format to store model which size is >= 2Gb
        :param method: A string. One of ['entropy', 'percentile', 'distribution'].
        :param symmetric: make range of tensor symmetric (central point is 0).
        :param num_quantized_bins: number of quantized bins. Default 128.
        :param percentile: A float number between [0, 100]. Default 99.99.
        """

class DistributionCalibrater(HistogramCalibrater):
    def __init__(self, model_path: str | Path, op_types_to_calibrate: Sequence[str] | None = None, augmented_model_path: str = 'augmented_model.onnx', use_external_data_format: bool = False, method: str = 'distribution', num_bins: int = 128, scenario: str = 'same') -> None:
        '''
        :param model_path: ONNX model to calibrate. It is a model path
        :param op_types_to_calibrate: operator types to calibrate. By default, calibrate all the float32/float16 tensors.
        :param augmented_model_path: save augmented model to this path.
        :param use_external_data_format: use external data format to store model which size is >= 2Gb
        :param method: A string. One of [\'entropy\', \'percentile\', \'distribution\'].
        :param symmetric: make range of tensor symmetric (central point is 0).
        :param num_bins: number of bins to create a new histogram for collecting tensor values.
        :param scenario: for float 8 only, if `scenario="same"`,
            the algorithm weights and float 8 follow the same distribution,
            if `scenario="p3"`, it assumes the weights follow
            a gaussian law and float 8 ~ X^3 where X is a gaussian law
        '''

class CalibrationDataCollector(metaclass=abc.ABCMeta):
    """
    Base class for collecting data for calibration-based quantization.
    """
    @abc.abstractmethod
    def collect(self, name_to_arr):
        """
        Generate informative data based on given data.
            name_to_arr : dict
                tensor name to NDArray data
        """
    @abc.abstractmethod
    def compute_collection_result(self):
        """
        Get the optimal result among collection data.
        """

class HistogramCollector(CalibrationDataCollector):
    """
    Collecting histogram for each tensor. Percentile and Entropy method are supported.

    ref: https://github.com//apache/incubator-mxnet/blob/master/python/mxnet/contrib/quantization.py
    ref: https://docs.nvidia.com/deeplearning/tensorrt/pytorch-quantization-toolkit/docs/_modules/
                 pytorch_quantization/calib/histogram.html
    """
    histogram_dict: Incomplete
    method: Incomplete
    symmetric: Incomplete
    num_bins: Incomplete
    num_quantized_bins: Incomplete
    percentile: Incomplete
    scenario: Incomplete
    def __init__(self, method, symmetric, num_bins, num_quantized_bins, percentile, scenario) -> None: ...
    def get_histogram_dict(self): ...
    def collect(self, name_to_arr): ...
    def collect_absolute_value(self, name_to_arr) -> None:
        """
        Collect histogram on absolute value
        """
    def collect_value(self, name_to_arr) -> None:
        """
        Collect histogram on real value
        """
    def merge_histogram(self, old_histogram, data_arr, new_min, new_max, new_threshold): ...
    def compute_collection_result(self): ...
    def compute_percentile(self): ...
    def compute_entropy(self): ...
    def compute_distribution(self): ...
    def get_entropy_threshold(self, histogram, num_quantized_bins):
        """Given a dataset, find the optimal threshold for quantizing it.
        The reference distribution is `q`, and the candidate distribution is `p`.
        `q` is a truncated version of the original distribution.
        Ref: http://on-demand.gputechconf.com/gtc/2017/presentation/s7310-8-bit-inference-with-tensorrt.pdf
        """

def create_calibrator(model: str | Path, op_types_to_calibrate: Sequence[str] | None = None, augmented_model_path: str = 'augmented_model.onnx', calibrate_method=..., use_external_data_format: bool = False, extra_options={}): ...
