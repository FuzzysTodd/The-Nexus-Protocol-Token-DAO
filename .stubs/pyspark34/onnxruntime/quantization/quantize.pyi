from .calibrate import CalibrationDataReader as CalibrationDataReader, CalibrationMethod as CalibrationMethod, TensorsData as TensorsData, create_calibrator as create_calibrator
from .onnx_quantizer import ONNXQuantizer as ONNXQuantizer
from .qdq_quantizer import QDQQuantizer as QDQQuantizer
from .quant_utils import QuantFormat as QuantFormat, QuantType as QuantType, QuantizationMode as QuantizationMode, load_model_with_shape_infer as load_model_with_shape_infer, model_has_pre_process_metadata as model_has_pre_process_metadata
from .registry import IntegerOpsRegistry as IntegerOpsRegistry, QDQRegistry as QDQRegistry, QLinearOpsRegistry as QLinearOpsRegistry
from _typeshed import Incomplete
from pathlib import Path

class QuantConfig:
    op_types_to_quantize: Incomplete
    per_channel: Incomplete
    reduce_range: Incomplete
    weight_type: Incomplete
    activation_type: Incomplete
    nodes_to_quantize: Incomplete
    nodes_to_exclude: Incomplete
    use_external_data_format: Incomplete
    def __init__(self, activation_type=..., weight_type=..., op_types_to_quantize: Incomplete | None = None, nodes_to_quantize: Incomplete | None = None, nodes_to_exclude: Incomplete | None = None, per_channel: bool = False, reduce_range: bool = False, use_external_data_format: bool = False) -> None:
        """
        This is the Base class for both Static and Dynamic Quantize Configuration
        Args:
            activation_type:
                quantization data type of activation. Please refer to
                https://onnxruntime.ai/docs/performance/quantization.html for more details on data type selection
            weight_type:
                quantization data type of weight. Please refer to
                https://onnxruntime.ai/docs/performance/quantization.html for more details on data type selection
            op_types_to_quantize:
                specify the types of operators to quantize, like ['Conv'] to quantize Conv only.
                It quantizes all supported operators by default.
            nodes_to_quantize:
                List of nodes names to quantize. When this list is not None only the nodes in this list
                are quantized.
                example:
                [
                    'Conv__224',
                    'Conv__252'
                ]
            nodes_to_exclude:
                List of nodes names to exclude. The nodes in this list will be excluded from quantization
                when it is not None.
            per_channel: quantize weights per channel
            reduce_range:
                quantize weights with 7-bits. It may improve the accuracy for some models running on non-VNNI machine,
                especially for per-channel mode
            use_external_data_format: option used for large size (>2GB) model. Set to False by default.
        """

class StaticQuantConfig(QuantConfig):
    calibration_data_reader: Incomplete
    calibrate_method: Incomplete
    quant_format: Incomplete
    extra_options: Incomplete
    def __init__(self, calibration_data_reader: CalibrationDataReader, calibrate_method=..., quant_format=..., activation_type=..., weight_type=..., op_types_to_quantize: Incomplete | None = None, nodes_to_quantize: Incomplete | None = None, nodes_to_exclude: Incomplete | None = None, per_channel: bool = False, reduce_range: bool = False, use_external_data_format: bool = False, extra_options: Incomplete | None = None) -> None:
        '''
        This is the derived class for static Quantize Configuration

        Args:
            calibration_data_reader:
                a calibration data reader. It enumerates calibration data and generates inputs for the original model.
            calibrate_method:
                Current calibration methods supported are MinMax, Entropy and Percentile.
            quant_format: QuantFormat{QOperator, QDQ}.
                QOperator format quantizes the model with quantized operators directly.
                QDQ format quantize the model by inserting QuantizeLinear/DeQuantizeLinear on the tensor.
            extra_options:
                key value pair dictionary for various options in different case. Current used:
                    extra.Sigmoid.nnapi = True/False  (Default is False)
                    ActivationSymmetric = True/False: symmetrize calibration data for activations (default is False).
                    WeightSymmetric = True/False: symmetrize calibration data for weights (default is True).
                    EnableSubgraph = True/False : Default is False. If enabled, subgraph will be quantized.
                                                  Dyanmic mode currently is supported. Will support more in future.
                    ForceQuantizeNoInputCheck = True/False :
                        By default, some latent operators like maxpool, transpose, do not quantize if their input is not
                        quantized already. Setting to True to force such operator always quantize input and so generate
                        quantized output. Also the True behavior could be disabled per node using the nodes_to_exclude.
                    MatMulConstBOnly = True/False:
                        Default is False for static mode. If enabled, only MatMul with const B will be quantized.
                    AddQDQPairToWeight = True/False :
                        Default is False which quantizes floating-point weight and feeds it to solely inserted
                        DeQuantizeLinear node. If True, it remains floating-point weight and inserts both
                        QuantizeLinear/DeQuantizeLinear nodes to weight.
                    OpTypesToExcludeOutputQuantization = list of op type :
                        Default is []. If any op type is specified, it won\'t quantize the output of ops with this
                        specific op types.
                    DedicatedQDQPair = True/False :
                        Default is False. When inserting QDQ pair, multiple nodes can share a single QDQ pair as their
                        inputs. If True, it will create identical and dedicated QDQ pair for each node.
                    QDQOpTypePerChannelSupportToAxis = dictionary :
                        Default is {}. Set channel axis for specific op type, for example: {\'MatMul\': 1}, and it\'s
                        effective only when per channel quantization is supported and per_channel is True. If specific
                        op type supports per channel quantization but not explicitly specified with channel axis,
                        default channel axis will be used.
                    CalibTensorRangeSymmetric = True/False :
                        Default is False. If enabled, the final range of tensor during calibration will be explicitly
                        set to symmetric to central point "0".
                    CalibMovingAverage = True/False :
                        Default is False. If enabled, the moving average of the minimum and maximum values will be
                        computed when the calibration method selected is MinMax.
                    CalibMovingAverageConstant = float :
                        Default is 0.01. Constant smoothing factor to use when computing the moving average of the
                        minimum and maximum values. Effective only when the calibration method selected is MinMax and
                        when CalibMovingAverage is set to True.
                    QuantizeBias = True/False :
                        Default is True which quantizes floating-point biases and it solely inserts
                        a DeQuantizeLinear node. If False, it remains floating-point bias and does not insert
                        any quantization nodes associated with biases.
                        This extra option is only effective when quant_format is QuantFormat.QDQ.
                    SmoothQuant = True/False :
                        Default is False. If enabled, SmoothQuant algorithm will be applied before quantization to do
                        fake input channel quantization.
                    SmoothQuantAlpha = float :
                        Default is 0.5. It only works if SmoothQuant is True. It controls the difficulty of weight
                        and activation quantization. A larger alpha value could be used on models with more significant
                        activation outliers to migrate more quantization difficulty to weights.
                    SmoothQuantFolding = True/False :
                        Default is True. It only works if SmoothQuant is True. If enabled, inserted Mul ops during
                        SmoothQuant will be folded into the previous op if the previous op is foldable.
            execution_provider : A enum indicates the Execution Provider such as: CPU, TRT, NNAPI, SNE, etc.
        Raises:
            ValueError: Raise ValueError if execution provider is unknown
        '''

class DynamicQuantConfig(QuantConfig):
    extra_options: Incomplete
    def __init__(self, weight_type=..., op_types_to_quantize: Incomplete | None = None, nodes_to_quantize: Incomplete | None = None, nodes_to_exclude: Incomplete | None = None, per_channel: bool = False, reduce_range: bool = False, use_external_data_format: bool = False, extra_options: Incomplete | None = None) -> None:
        """
        This is a class for dynamic Quant Configuration

        Args:
            extra_options: key value pair dictionary for various options in different case. Current used:
                extra.Sigmoid.nnapi = True/False  (Default is False)
                ActivationSymmetric = True/False: symmetrize calibration data for activations (default is False).
                WeightSymmetric = True/False: symmetrize calibration data for weights (default is True).
                EnableSubgraph = True/False :
                    Default is False. If enabled, subgraph will be quantized. Dynamic mode currently is supported. Will
                    support more in the future.
                ForceQuantizeNoInputCheck = True/False :
                    By default, some latent operators like maxpool, transpose, do not quantize if their input is not
                    quantized already. Setting to True to force such operator always quantize input and so generate
                    quantized output. Also the True behavior could be disabled per node using the nodes_to_exclude.
                MatMulConstBOnly = True/False:
                    Default is True for dynamic mode. If enabled, only MatMul with const B will be quantized.
            execution_provider : A enum indicates the Execution Provider such as: CPU, TRT, NNAPI, SNE, etc.

        Raises:
            ValueError: Raise ValueError if execution provider is unknown
        """

def check_static_quant_arguments(quant_format: QuantFormat, activation_type: QuantType, weight_type: QuantType): ...
def quantize_static(model_input, model_output, calibration_data_reader: CalibrationDataReader, quant_format=..., op_types_to_quantize: Incomplete | None = None, per_channel: bool = False, reduce_range: bool = False, activation_type=..., weight_type=..., nodes_to_quantize: Incomplete | None = None, nodes_to_exclude: Incomplete | None = None, use_external_data_format: bool = False, calibrate_method=..., extra_options: Incomplete | None = None):
    '''
    Given an onnx model and calibration data reader, create a quantized onnx model and save it into a file
    It is recommended to use QuantFormat.QDQ format from 1.11 with activation_type = QuantType.QInt8 and weight_type
    = QuantType.QInt8. If model is targeted to GPU/TRT, symmetric activation and weight are required. If model is
    targeted to CPU, asymmetric activation and symmetric weight are recommended for balance of performance and
    accuracy.

    Args:

        model_input: file path of model to quantize
        model_output: file path of quantized model
        calibration_data_reader: a calibration data reader. It
            enumerates calibration data and generates inputs for the
            original model.
        quant_format: QuantFormat{QOperator, QDQ}.
            QOperator format quantizes the model with quantized operators directly.
            QDQ format quantize the model by inserting QuantizeLinear/DeQuantizeLinear on the tensor.
        activation_type:
            quantization data type of activation. Please refer to
            https://onnxruntime.ai/docs/performance/quantization.html for more details on data type selection
        calibrate_method:
            Current calibration methods supported are MinMax and Entropy.
                Please use CalibrationMethod.MinMax or CalibrationMethod.Entropy as options.
        op_types_to_quantize:
                specify the types of operators to quantize, like [\'Conv\'] to quantize Conv only.
                It quantizes all supported operators by default.
        per_channel: quantize weights per channel
        reduce_range:
            quantize weights with 7-bits. It may improve the accuracy for some models running on non-VNNI machine,
            especially for per-channel mode
        weight_type:
            quantization data type of weight. Please refer to
            https://onnxruntime.ai/docs/performance/quantization.html for more details on data type selection
        nodes_to_quantize:
            List of nodes names to quantize. When this list is not None only the nodes in this list
            are quantized.
            example:
            [
                \'Conv__224\',
                \'Conv__252\'
            ]
        nodes_to_exclude:
            List of nodes names to exclude. The nodes in this list will be excluded from quantization
            when it is not None.
        use_external_data_format: option used for large size (>2GB) model. Set to False by default.
        extra_options:
            key value pair dictionary for various options in different case. Current used:
                extra.Sigmoid.nnapi = True/False  (Default is False)
                ActivationSymmetric = True/False: symmetrize calibration data for activations (default is False).
                WeightSymmetric = True/False: symmetrize calibration data for weights (default is True).
                EnableSubgraph = True/False : Default is False. If enabled, subgraph will be quantized.
                                              Dyanmic mode currently is supported. Will support more in the future.
                ForceQuantizeNoInputCheck = True/False :
                    By default, some latent operators like maxpool, transpose, do not quantize if their input is not
                    quantized already. Setting to True to force such operator always quantize input and so generate
                    quantized output. Also, the True behavior could be disabled per node using the nodes_to_exclude.
                MatMulConstBOnly = True/False:
                    Default is False for static mode. If enabled, only MatMul with const B will be quantized.
                AddQDQPairToWeight = True/False :
                    Default is False which quantizes floating-point weight and feeds it to solely inserted
                    DeQuantizeLinear node. If True, it remains floating-point weight and inserts both
                    QuantizeLinear/DeQuantizeLinear nodes to weight.
                OpTypesToExcludeOutputQuantization = list of op type :
                    Default is []. If any op type is specified, it won\'t quantize the output of ops with this
                    specific op types.
                DedicatedQDQPair = True/False :
                    Default is False. When inserting QDQ pair, multiple nodes can share a single QDQ pair as their
                    inputs. If True, it will create identical and dedicated QDQ pair for each node.
                QDQOpTypePerChannelSupportToAxis = dictionary :
                    Default is {}. Set channel axis for specific op type, for example: {\'MatMul\': 1}, and it\'s
                    effective only when per channel quantization is supported and per_channel is True. If specific
                    op type supports per channel quantization but not explicitly specified with channel axis,
                    default channel axis will be used.
                CalibTensorRangeSymmetric = True/False :
                    Default is False. If enabled, the final range of tensor during calibration will be explicitly
                    set to symmetric to central point "0".
                CalibMovingAverage = True/False :
                    Default is False. If enabled, the moving average of the minimum and maximum values will be
                    computed when the calibration method selected is MinMax.
                CalibMovingAverageConstant = float :
                    Default is 0.01. Constant smoothing factor to use when computing the moving average of the
                    minimum and maximum values. Effective only when the calibration method selected is MinMax and
                    when CalibMovingAverage is set to True.
                SmoothQuant = True/False :
                    Default is False. If enabled, SmoothQuant algorithm will be applied before quantization to do
                    fake input channel quantization.
                SmoothQuantAlpha = float :
                    Default is 0.5. It only works if SmoothQuant is True. It controls the difficulty of weight
                    and activation quantization. A larger alpha value could be used on models with more significant
                    activation outliers to migrate more quantization difficulty to weights.
                SmoothQuantFolding = True/False :
                    Default is True. It only works if SmoothQuant is True. If enabled, inserted Mul ops during
                    SmoothQuant will be folded into the previous op if the previous op is foldable.
    '''
def quantize_dynamic(model_input: Path, model_output: Path, op_types_to_quantize: Incomplete | None = None, per_channel: bool = False, reduce_range: bool = False, weight_type=..., nodes_to_quantize: Incomplete | None = None, nodes_to_exclude: Incomplete | None = None, use_external_data_format: bool = False, extra_options: Incomplete | None = None):
    """Given an onnx model, create a quantized onnx model and save it into a file

    Args:
        model_input: file path of model to quantize
        model_output: file path of quantized model
        op_types_to_quantize:
            specify the types of operators to quantize, like ['Conv'] to quantize Conv only.
            It quantizes all supported operators by default.
        per_channel: quantize weights per channel
        reduce_range:
            quantize weights with 7-bits. It may improve the accuracy for some models running on non-VNNI machine,
            especially for per-channel mode
        weight_type:
            quantization data type of weight. Please refer to
            https://onnxruntime.ai/docs/performance/quantization.html for more details on data type selection
        nodes_to_quantize:
            List of nodes names to quantize. When this list is not None only the nodes in this list
            are quantized.
            example:
            [
                'Conv__224',
                'Conv__252'
            ]
        nodes_to_exclude:
            List of nodes names to exclude. The nodes in this list will be excluded from quantization
            when it is not None.
        use_external_data_format: option used for large size (>2GB) model. Set to False by default.
        extra_options:
            key value pair dictionary for various options in different case. Current used:
                extra.Sigmoid.nnapi = True/False  (Default is False)
                ActivationSymmetric = True/False: symmetrize calibration data for activations (default is False).
                WeightSymmetric = True/False: symmetrize calibration data for weights (default is True).
                EnableSubgraph = True/False :
                    Default is False. If enabled, subgraph will be quantized. Dynamic mode currently is supported. Will
                    support more in the future.
                ForceQuantizeNoInputCheck = True/False :
                    By default, some latent operators like maxpool, transpose, do not quantize if their input is not
                    quantized already. Setting to True to force such operator always quantize input and so generate
                    quantized output. Also the True behavior could be disabled per node using the nodes_to_exclude.
                MatMulConstBOnly = True/False:
                    Default is True for dynamic mode. If enabled, only MatMul with const B will be quantized.
    """
def quantize(model_input: Path, model_output: Path, quant_config: QuantConfig):
    """Quantize a model with QuantConfig.

    Args:
        model_input (Path): Path to the model to quantize.
        model_output (Path): Path to save the quantized model.
        quant_config (QuantConfig): Quantization Configuration.
    """
