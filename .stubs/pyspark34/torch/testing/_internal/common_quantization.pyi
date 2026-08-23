import torch
import torch.nn as nn
from _typeshed import Incomplete
from torch.ao.ns.fx.ns_types import NSSingleResultValuesType as NSSingleResultValuesType, NSSubgraph as NSSubgraph
from torch.ao.quantization import DeQuantStub as DeQuantStub, PerChannelMinMaxObserver as PerChannelMinMaxObserver, QConfig as QConfig, QuantStub as QuantStub, QuantType as QuantType, QuantWrapper as QuantWrapper, convert as convert, default_dynamic_qat_qconfig as default_dynamic_qat_qconfig, default_dynamic_qconfig as default_dynamic_qconfig, default_dynamic_quant_observer as default_dynamic_quant_observer, default_embedding_qat_qconfig as default_embedding_qat_qconfig, default_observer as default_observer, default_per_channel_qconfig as default_per_channel_qconfig, default_qconfig as default_qconfig, default_symmetric_qnnpack_qat_qconfig as default_symmetric_qnnpack_qat_qconfig, default_weight_observer as default_weight_observer, float_qparams_weight_only_qconfig as float_qparams_weight_only_qconfig, get_default_qat_qconfig as get_default_qat_qconfig, get_default_qconfig as get_default_qconfig, propagate_qconfig_ as propagate_qconfig_, quantize as quantize, quantize_dynamic_jit as quantize_dynamic_jit, quantize_jit as quantize_jit
from torch.ao.quantization.quantization_mappings import get_default_dynamic_quant_module_mappings as get_default_dynamic_quant_module_mappings, get_default_qat_module_mappings as get_default_qat_module_mappings, get_default_qconfig_propagation_list as get_default_qconfig_propagation_list
from torch.ao.quantization.quantize_fx import convert_fx as convert_fx, convert_to_reference_fx as convert_to_reference_fx, prepare_fx as prepare_fx, prepare_qat_fx as prepare_qat_fx
from torch.fx import GraphModule as GraphModule
from torch.fx.graph import Node as Node
from torch.testing import FileCheck as FileCheck
from torch.testing._internal.common_quantized import override_quantized_engine as override_quantized_engine
from torch.testing._internal.common_utils import TEST_WITH_ROCM as TEST_WITH_ROCM, TestCase as TestCase
from typing import Any, Callable, Dict, Tuple

HAS_FX: bool

class NodeSpec:
    """ Used for checking GraphModule Node
    """
    op: Incomplete
    target: Incomplete
    def __init__(self, op, target) -> None:
        """
        op: call_function | call_module
        target:
          for call_function, target would be a function
          for call_module, target would be the type of PyTorch module
        """
    @classmethod
    def call_function(cls, target): ...
    @classmethod
    def call_method(cls, target): ...
    @classmethod
    def call_module(cls, target): ...
    def __hash__(self): ...
    def __eq__(self, other): ...

def get_supported_device_types(): ...
def test_only_eval_fn(model, calib_data) -> None:
    """
    Default evaluation function takes a torch.utils.data.Dataset or a list of
    input Tensors and run the model on the dataset
    """
def test_only_train_fn(model, train_data, loss_fn=...):
    """
    Default train function takes a torch.utils.data.Dataset and train the model
    on the dataset
    """

class AverageMeter:
    """Computes and stores the average and current value"""
    name: Incomplete
    fmt: Incomplete
    def __init__(self, name, fmt: str = ':f') -> None: ...
    val: int
    avg: int
    sum: int
    count: int
    def reset(self) -> None: ...
    def update(self, val, n: int = 1) -> None: ...

def accuracy(output, target, topk=(1,)):
    """Computes the accuracy over the k top predictions for the specified values of k"""
def train_one_epoch(model, criterion, optimizer, data_loader, device, ntrain_batches) -> None: ...
def ddp_setup(rank, world_size) -> None: ...
def ddp_cleanup() -> None: ...
def run_ddp(rank, world_size, prepared) -> None: ...
def convert_dynamic(module) -> None: ...
def prepare_dynamic(model, qconfig_dict: Incomplete | None = None) -> None: ...
def skipIfNoFBGEMM(fn): ...
def skipIfNoQNNPACK(fn): ...
def withQNNPACKBackend(fn): ...
def skipIfNoONEDNN(fn): ...

HAS_TORCHVISION: bool
skip_if_no_torchvision: Incomplete

def get_script_module(model, tracing, data): ...
def lengths_to_offsets(t, offset_type=..., use_begin_offset: bool = True):
    """
    Convert lengths to offsets for embedding_bag
    """

class QuantizationTestCase(TestCase):
    calib_data: Incomplete
    train_data: Incomplete
    img_data_1d: Incomplete
    img_data_2d: Incomplete
    img_data_3d: Incomplete
    img_data_1d_train: Incomplete
    img_data_2d_train: Incomplete
    img_data_3d_train: Incomplete
    img_data_dict: Incomplete
    static_quant_types: Incomplete
    all_quant_types: Incomplete
    def setUp(self) -> None: ...
    def checkNoPrepModules(self, module) -> None:
        """Checks the module does not contain child
            modules for quantization prepration, e.g.
            quant, dequant and observer
        """
    def checkNoQconfig(self, module) -> None:
        """Checks the module does not contain qconfig
        """
    def checkHasPrepModules(self, module) -> None:
        """Checks the module contains child
            modules for quantization prepration, e.g.
            quant, dequant and observer
        """
    def checkObservers(self, module, propagate_qconfig_list: Incomplete | None = None, prepare_custom_config_dict: Incomplete | None = None):
        """Checks the module or module's leaf descendants
            have observers in preperation for quantization
        """
    def checkQuantDequant(self, mod) -> None:
        """Checks that mod has nn.Quantize and
            nn.DeQuantize submodules inserted
        """
    def checkWrappedQuantizedLinear(self, mod) -> None:
        """Checks that mod has been swapped for an nnq.Linear
            module, the bias is qint32, and that the module
            has Quantize and DeQuantize submodules
        """
    def checkQuantizedLinear(self, mod) -> None: ...
    def checkDynamicQuantizedLinear(self, mod, dtype) -> None:
        """Checks that mod has been swapped for an nnqd.Linear
            module, the bias is float.
        """
    def checkDynamicQuantizedLinearRelu(self, mod, dtype) -> None:
        """Checks that mod has been swapped for an nnqd.Linear
            module, the bias is float.
        """
    def check_eager_serialization(self, ref_model, loaded_model, x) -> None: ...
    def check_weight_bias_api(self, ref_model, weight_keys, bias_keys) -> None: ...
    def checkDynamicQuantizedLSTM(self, mod, reference_module_type, dtype) -> None:
        """Checks that mod has been swapped for an nnqd.LSTM type
            module, the bias is float.
        """
    def checkLinear(self, mod) -> None: ...
    def checkDynamicQuantizedModule(self, mod, reference_module_type, dtype) -> None:
        """Checks that mod has been swapped for an nnqd.Linear
            module, the bias is float.
        """
    def checkScriptable(self, orig_mod, calib_data, check_save_load: bool = False) -> None: ...
    def checkGraphModeOp(self, module, inputs, quantized_op, tracing: bool = False, debug: bool = False, check: bool = True, eval_mode: bool = True, dynamic: bool = False, qconfig: Incomplete | None = None): ...
    def checkGraphModuleNodes(self, graph_module, expected_node: Incomplete | None = None, expected_node_occurrence: Incomplete | None = None, expected_node_list: Incomplete | None = None) -> None:
        """ Check if GraphModule contains the target node
        Args:
            graph_module: the GraphModule instance we want to check
            expected_node, expected_node_occurrence, expected_node_list:
               see docs for checkGraphModeFxOp
        """
    def printGraphModule(self, graph_module, print_str: bool = True): ...
    def assert_types_for_matched_subgraph_pairs(self, matched_subgraph_pairs: Dict[str, Tuple[NSSubgraph, NSSubgraph]], expected_types: Dict[str, Tuple[Tuple[Callable, Callable], Tuple[Callable, Callable]]], gm_a: GraphModule, gm_b: GraphModule) -> None:
        """
            Verifies that the types specified in expected_types match
            the underlying objects pointed to by the nodes in matched_subgraph_pairs.

            An example successful test case:

              matched_subgraph_pairs = {'x0': (graph_a_conv_0_node, graph_b_conv_0_node)}
              expected_types = {'x0': (nn.Conv2d, nnq.Conv2d)}

            The function tests for key equivalence, and verifies types with
            instance checks.
            """
    def assert_ns_compare_dict_valid(self, act_compare_dict: Dict[str, Dict[str, Dict[str, Any]]]) -> None:
        """
            Verifies that the act_compare_dict (output of Numeric Suite APIs) is valid:
            1. for each layer, results are recorded for two models
            2. number of seen tensors match
            3. shapes of each pair of seen tensors match
            """
    def checkGraphModeFxOp(self, model, inputs, quant_type, expected_node: Incomplete | None = None, expected_node_occurrence: Incomplete | None = None, expected_node_list: Incomplete | None = None, is_reference: bool = False, print_debug_info: bool = False, custom_qconfig_dict: Incomplete | None = None, prepare_expected_node: Incomplete | None = None, prepare_expected_node_occurrence: Incomplete | None = None, prepare_expected_node_list: Incomplete | None = None, prepare_custom_config: Incomplete | None = None, backend_config: Incomplete | None = None):
        ''' Quantizes model with graph mode quantization on fx and check if the
                quantized model contains the quantized_node

                Args:
                    model: floating point torch.nn.Module
                    inputs: one positional sample input arguments for model
                    expected_node: NodeSpec
                        e.g. NodeSpec.call_function(torch.quantize_per_tensor)
                    expected_node_occurrence: a dict from NodeSpec to
                        expected number of occurences (int)
                        e.g. {NodeSpec.call_function(torch.quantize_per_tensor) : 1,
                                NodeSpec.call_method(\'dequantize\'): 1}
                    expected_node_list: a list of NodeSpec, used to check the order
                        of the occurrence of Node
                        e.g. [NodeSpec.call_function(torch.quantize_per_tensor),
                                NodeSpec.call_module(nnq.Conv2d),
                                NodeSpec.call_function(F.hardtanh_),
                                NodeSpec.call_method(\'dequantize\')]
                    is_reference: if True, enables reference mode
                    print_debug_info: if True, prints debug info
                    custom_qconfig_dict: overrides default qconfig_dict
                    prepare_expected_node: same as expected_node, but for prepare
                    prepare_expected_node_occurrence: same as
                        expected_node_occurrence, but for prepare
                    prepare_expected_node_list: same as expected_node_list, but
                        for prepare

                Returns:
                    A dictionary with the following structure:
                   {
                       "prepared": ...,  # the prepared model
                       "quantized": ...,  # the quantized non-reference model
                       "quantized_reference": ...,  # the quantized reference model
                       "result": ...,  # the result for either quantized or
                                       # quantized_reference model depending on the
                                       # is_reference arguemnt
                   }
            '''
    def checkEmbeddingSerialization(self, qemb, num_embeddings, embedding_dim, indices, offsets, set_qconfig, is_emb_bag, dtype=...) -> None: ...

class QuantizationLiteTestCase(QuantizationTestCase): ...

class SingleLayerLinearModel(torch.nn.Module):
    fc1: Incomplete
    def __init__(self) -> None: ...
    def forward(self, x): ...
    def get_example_inputs(self) -> Tuple[Any, ...]: ...

class AnnotatedSingleLayerLinearModel(torch.nn.Module):
    qconfig: Incomplete
    fc1: Incomplete
    def __init__(self, qengine: str = 'fbgemm') -> None: ...
    def forward(self, x): ...
    def get_example_inputs(self) -> Tuple[Any, ...]: ...

class SingleLayerLinearDynamicModel(torch.nn.Module):
    qconfig: Incomplete
    fc1: Incomplete
    def __init__(self, qengine: str = 'fbgemm') -> None: ...
    def forward(self, x): ...
    def get_example_inputs(self) -> Tuple[Any, ...]: ...

class LinearAddModel(nn.Module):
    fc1: Incomplete
    fc2: Incomplete
    def __init__(self) -> None: ...
    def forward(self, x): ...
    def get_example_inputs(self) -> Tuple[Any, ...]: ...

class RNNDynamicModel(torch.nn.Module):
    qconfig: Incomplete
    mod: Incomplete
    def __init__(self, mod_type) -> None: ...
    def forward(self, x): ...

class RNNCellDynamicModel(torch.nn.Module):
    qconfig: Incomplete
    mod: Incomplete
    def __init__(self, mod_type) -> None: ...
    def forward(self, x): ...

class LSTMwithHiddenDynamicModel(torch.nn.Module):
    qconfig: Incomplete
    lstm: Incomplete
    def __init__(self, qengine: str = 'fbgemm') -> None: ...
    def forward(self, x, hid): ...

class ConvModel(torch.nn.Module):
    conv: Incomplete
    def __init__(self) -> None: ...
    def forward(self, x): ...
    def get_example_inputs(self) -> Tuple[Any, ...]: ...

class ConvTransposeModel(torch.nn.Module):
    conv: Incomplete
    def __init__(self) -> None: ...
    def forward(self, x): ...
    def get_example_inputs(self) -> Tuple[Any, ...]: ...

class AnnotatedConvModel(torch.nn.Module):
    qconfig: Incomplete
    conv: Incomplete
    quant: Incomplete
    dequant: Incomplete
    def __init__(self, qengine) -> None: ...
    def forward(self, x): ...
    def get_example_inputs(self) -> Tuple[Any, ...]: ...

class AnnotatedConvTransposeModel(torch.nn.Module):
    qconfig: Incomplete
    conv: Incomplete
    quant: Incomplete
    dequant: Incomplete
    def __init__(self, qengine) -> None: ...
    def forward(self, x): ...
    def get_example_inputs(self) -> Tuple[Any, ...]: ...

class ConvBnModel(torch.nn.Module):
    conv: Incomplete
    bn: Incomplete
    def __init__(self) -> None: ...
    def forward(self, x): ...
    def get_example_inputs(self) -> Tuple[Any, ...]: ...

class AnnotatedConvBnModel(torch.nn.Module):
    qconfig: Incomplete
    conv: Incomplete
    bn: Incomplete
    quant: Incomplete
    dequant: Incomplete
    def __init__(self) -> None: ...
    def forward(self, x): ...
    def get_example_inputs(self) -> Tuple[Any, ...]: ...

class ConvBnReLUModel(torch.nn.Module):
    conv: Incomplete
    bn: Incomplete
    relu: Incomplete
    def __init__(self) -> None: ...
    def forward(self, x): ...
    def get_example_inputs(self) -> Tuple[Any, ...]: ...

class AnnotatedConvBnReLUModel(torch.nn.Module):
    qconfig: Incomplete
    conv: Incomplete
    bn: Incomplete
    relu: Incomplete
    quant: Incomplete
    dequant: Incomplete
    def __init__(self, qengine: str = 'fbgemm') -> None: ...
    def forward(self, x): ...
    def fuse_model(self) -> None: ...
    def get_example_inputs(self) -> Tuple[Any, ...]: ...

class TwoLayerConvModel(torch.nn.Module):
    conv1: Incomplete
    conv2: Incomplete
    def __init__(self) -> None: ...
    def forward(self, x): ...
    def get_example_inputs(self) -> Tuple[Any, ...]: ...

class TwoLayerLinearModel(torch.nn.Module):
    fc1: Incomplete
    fc2: Incomplete
    def __init__(self) -> None: ...
    def forward(self, x): ...
    def get_example_inputs(self) -> Tuple[Any, ...]: ...

class LinearModelWithSubmodule(nn.Module):
    subm: Incomplete
    fc: Incomplete
    def __init__(self) -> None: ...
    def forward(self, x): ...
    def get_example_inputs(self) -> Tuple[Any, ...]: ...

class AnnotatedTwoLayerLinearModel(torch.nn.Module):
    fc1: Incomplete
    fc2: Incomplete
    def __init__(self) -> None: ...
    def forward(self, x): ...
    def get_example_inputs(self) -> Tuple[Any, ...]: ...

class ActivationsTestModel(torch.nn.Module):
    qconfig: Incomplete
    quant: Incomplete
    hardswish: Incomplete
    elu: Incomplete
    dequant: Incomplete
    def __init__(self) -> None: ...
    def forward(self, x): ...

class LinearReluModel(torch.nn.Module):
    fc: Incomplete
    relu: Incomplete
    def __init__(self) -> None: ...
    def forward(self, x): ...
    def get_example_inputs(self) -> Tuple[Any, ...]: ...

class LinearReluLinearModel(torch.nn.Module):
    fc1: Incomplete
    relu: Incomplete
    fc2: Incomplete
    def __init__(self) -> None: ...
    def forward(self, x): ...
    def get_example_inputs(self) -> Tuple[Any, ...]: ...

class LinearReluAddModel(torch.nn.Module):
    fc1: Incomplete
    relu: Incomplete
    fc2: Incomplete
    def __init__(self) -> None: ...
    def forward(self, x): ...
    def get_example_inputs(self) -> Tuple[Any, ...]: ...

class LinearBnLeakyReluModel(torch.nn.Module):
    linear: Incomplete
    bn1d: Incomplete
    leaky_relu: Incomplete
    with_bn: Incomplete
    def __init__(self, with_bn: bool = True) -> None: ...
    def forward(self, x): ...
    def get_example_inputs(self) -> Tuple[Any, ...]: ...

class LinearTanhModel(torch.nn.Module):
    linear: Incomplete
    tanh: Incomplete
    def __init__(self) -> None: ...
    def forward(self, x): ...
    def get_example_inputs(self) -> Tuple[Any, ...]: ...

class ConvBnAddReluModel(torch.nn.Module):
    conv: Incomplete
    conv2: Incomplete
    bn: Incomplete
    relu: Incomplete
    with_bn: Incomplete
    with_relu: Incomplete
    two_conv: Incomplete
    left_conv: Incomplete
    use_torch_add: Incomplete
    def __init__(self, with_bn: bool = True, with_relu: bool = True, left_conv: bool = True, two_conv: bool = True, use_torch_add: bool = True) -> None: ...
    def forward(self, x1, x2): ...
    def get_example_inputs(self) -> Tuple[Any, ...]: ...

class ConvReluModel(torch.nn.Module):
    fc: Incomplete
    relu: Incomplete
    def __init__(self) -> None: ...
    def forward(self, x): ...
    def get_example_inputs(self) -> Tuple[Any, ...]: ...

class ConvReluConvModel(torch.nn.Module):
    fc1: Incomplete
    relu: Incomplete
    fc2: Incomplete
    def __init__(self) -> None: ...
    def forward(self, x): ...
    def get_example_inputs(self) -> Tuple[Any, ...]: ...

class ConvReluAddModel(torch.nn.Module):
    fc1: Incomplete
    relu: Incomplete
    fc2: Incomplete
    def __init__(self) -> None: ...
    def forward(self, x): ...
    def get_example_inputs(self) -> Tuple[Any, ...]: ...

class NormalizationTestModel(torch.nn.Module):
    quant: Incomplete
    fc1: Incomplete
    layer_norm: Incomplete
    group_norm: Incomplete
    instance_norm1d: Incomplete
    instance_norm2d: Incomplete
    instance_norm3d: Incomplete
    def __init__(self) -> None: ...
    def forward(self, x): ...

class NestedModel(torch.nn.Module):
    sub1: Incomplete
    sub2: Incomplete
    fc3: Incomplete
    def __init__(self) -> None: ...
    def forward(self, x): ...

class AnnotatedNestedModel(torch.nn.Module):
    sub1: Incomplete
    sub2: Incomplete
    fc3: Incomplete
    def __init__(self, qengine) -> None: ...
    def forward(self, x): ...

class AnnotatedSubNestedModel(torch.nn.Module):
    sub1: Incomplete
    sub2: Incomplete
    fc3: Incomplete
    def __init__(self) -> None: ...
    def forward(self, x): ...

class AnnotatedCustomConfigNestedModel(torch.nn.Module):
    sub1: Incomplete
    sub2: Incomplete
    fc3: Incomplete
    def __init__(self) -> None: ...
    def forward(self, x): ...

class QuantSubModel(torch.nn.Module):
    sub1: Incomplete
    sub2: Incomplete
    fc3: Incomplete
    def __init__(self) -> None: ...
    def forward(self, x): ...

class InnerModule(torch.nn.Module):
    fc1: Incomplete
    relu1: Incomplete
    fc2: Incomplete
    relu2: Incomplete
    def __init__(self) -> None: ...
    def forward(self, x): ...
    def fuse_modules(self) -> None: ...

class FunctionalLinear(torch.nn.Module):
    weight: Incomplete
    bias: Incomplete
    def __init__(self) -> None: ...
    def forward(self, x): ...
    def get_example_inputs(self) -> Tuple[Any, ...]: ...

class SingleLayerFunctionalLinearModel(torch.nn.Module):
    linear1: Incomplete
    def __init__(self) -> None: ...
    def forward(self, x): ...
    def get_example_inputs(self) -> Tuple[Any, ...]: ...

class TwoLayerFunctionalLinearModel(torch.nn.Module):
    linear1: Incomplete
    linear2: Incomplete
    def __init__(self) -> None: ...
    def forward(self, x): ...
    def get_example_inputs(self) -> Tuple[Any, ...]: ...

class FunctionalLinearAddModel(torch.nn.Module):
    linear1: Incomplete
    linear2: Incomplete
    def __init__(self) -> None: ...
    def forward(self, x): ...
    def get_example_inputs(self) -> Tuple[Any, ...]: ...

class FunctionalLinearReluModel(nn.Module):
    linear: Incomplete
    def __init__(self) -> None: ...
    def forward(self, x): ...
    def get_example_inputs(self) -> Tuple[Any, ...]: ...

class FunctionalLinearReluLinearModel(nn.Module):
    linear1: Incomplete
    relu: Incomplete
    linear2: Incomplete
    def __init__(self) -> None: ...
    def forward(self, x): ...
    def get_example_inputs(self) -> Tuple[Any, ...]: ...

class FunctionalConv2d(torch.nn.Module):
    weight: Incomplete
    bias: Incomplete
    stride: Incomplete
    padding: Incomplete
    dilation: Incomplete
    groups: int
    def __init__(self) -> None: ...
    def forward(self, x): ...
    def get_example_inputs(self) -> Tuple[Any, ...]: ...

class SingleLayerFunctionalConvModel(torch.nn.Module):
    conv1: Incomplete
    def __init__(self) -> None: ...
    def forward(self, x): ...
    def get_example_inputs(self) -> Tuple[Any, ...]: ...

class TwoLayerFunctionalConvModel(torch.nn.Module):
    conv1: Incomplete
    conv2: Incomplete
    def __init__(self) -> None: ...
    def forward(self, x): ...
    def get_example_inputs(self) -> Tuple[Any, ...]: ...

class FunctionalConvReluModel(nn.Module):
    conv: Incomplete
    def __init__(self) -> None: ...
    def forward(self, x): ...
    def get_example_inputs(self) -> Tuple[Any, ...]: ...

class FunctionalConvReluConvModel(nn.Module):
    conv1: Incomplete
    relu: Incomplete
    conv2: Incomplete
    def __init__(self) -> None: ...
    def forward(self, x): ...
    def get_example_inputs(self) -> Tuple[Any, ...]: ...

class SkipQuantModel(torch.nn.Module):
    """We can skip quantization by explicitly
    setting qconfig of a submodule to None
    """
    sub: Incomplete
    fc: Incomplete
    def __init__(self) -> None: ...
    def forward(self, x): ...
    def fuse_modules(self) -> None: ...

class AnnotatedSkipQuantModel(torch.nn.Module):
    """We can skip quantization by explicitly
    setting qconfig of a submodule to None
    """
    qconfig: Incomplete
    sub: Incomplete
    fc: Incomplete
    def __init__(self, qengine) -> None: ...
    def forward(self, x): ...
    def fuse_modules(self) -> None: ...

class QuantStubModel(torch.nn.Module):
    """A Module with manually inserted `QuantStub` and `DeQuantStub`
    """
    qconfig: Incomplete
    quant: Incomplete
    dequant: Incomplete
    fc: Incomplete
    def __init__(self) -> None: ...
    def forward(self, x): ...

class ManualLinearQATModel(torch.nn.Module):
    """A Module with manually inserted `QuantStub` and `DeQuantStub`
    """
    qconfig: Incomplete
    quant: Incomplete
    dequant: Incomplete
    fc1: Incomplete
    fc2: Incomplete
    def __init__(self, qengine) -> None: ...
    def forward(self, x): ...

class ManualDropoutQATModel(torch.nn.Module):
    """A Module with manually inserted `QuantStub` and `DeQuantStub`
    """
    qconfig: Incomplete
    quant: Incomplete
    dequant: Incomplete
    fc1: Incomplete
    dropout: Incomplete
    def __init__(self, qengine) -> None: ...
    def forward(self, x): ...

class ManualLinearDynamicQATModel(torch.nn.Module):
    """A Module that uses a dynamic QAT by default.
    """
    qconfig: Incomplete
    fc1: Incomplete
    fc2: Incomplete
    def __init__(self, qconfig: Incomplete | None = None) -> None: ...
    def forward(self, x): ...

class ManualConvLinearQATModel(torch.nn.Module):
    """A module with manually inserted `QuantStub` and `DeQuantStub`
    and contains both linear and conv modules
    """
    qconfig: Incomplete
    quant: Incomplete
    dequant: Incomplete
    conv: Incomplete
    fc1: Incomplete
    fc2: Incomplete
    def __init__(self, qconfig: Incomplete | None = None) -> None: ...
    def forward(self, x): ...

class ManualConvLinearSymmQATModel(ManualConvLinearQATModel):
    """Same as ManualConvLinearQATModule but with Symmetric Quantization.
    Supported only with qnnpack.
    """
    def __init__(self) -> None: ...

class ManualEmbeddingBagLinear(nn.Module):
    emb: Incomplete
    quant: Incomplete
    dequant: Incomplete
    linear: Incomplete
    qconfig: Incomplete
    def __init__(self) -> None: ...
    def forward(self, input: torch.Tensor, offsets: torch.Tensor | None = None, per_sample_weights: torch.Tensor | None = None): ...

class DeFusedEmbeddingBagLinear(nn.Module):
    """A module to simulate QAT embedding bag with a linear layer,
    this module uses a separate embedding and bagging op, similar
    to that which is described in the EmbeddingBag documentation.

    https://pytorch.org/docs/stable/generated/torch.nn.EmbeddingBag.html
    """
    emb: Incomplete
    bagging_op: Incomplete
    quant: Incomplete
    dequant: Incomplete
    linear: Incomplete
    qconfig: Incomplete
    def __init__(self) -> None: ...
    def forward(self, input: torch.Tensor) -> torch.Tensor: ...

class SubModelForFusion(nn.Module):
    conv: Incomplete
    bn: Incomplete
    def __init__(self) -> None: ...
    def forward(self, x): ...

class SubModelWithoutFusion(nn.Module):
    conv: Incomplete
    relu: Incomplete
    def __init__(self) -> None: ...
    def forward(self, x): ...

class ModelForFusion(nn.Module):
    conv1: Incomplete
    bn1: Incomplete
    relu1: Incomplete
    sub1: Incomplete
    sub2: Incomplete
    fc: Incomplete
    quant: Incomplete
    dequant: Incomplete
    qconfig: Incomplete
    conv2: Incomplete
    relu2: Incomplete
    bn2: Incomplete
    relu3: Incomplete
    conv3: Incomplete
    bn3: Incomplete
    relu4: Incomplete
    def __init__(self, qconfig) -> None: ...
    def forward(self, x): ...

class ConvBNReLU(nn.Sequential):
    def __init__(self) -> None: ...

class ModelWithSequentialFusion(nn.Module):
    conv1: Incomplete
    relu1: Incomplete
    features: Incomplete
    classifier: Incomplete
    seq: Incomplete
    quant: Incomplete
    dequant: Incomplete
    def __init__(self) -> None: ...
    def forward(self, x): ...

class ModelForFusionWithBias(nn.Module):
    conv1: Incomplete
    bn1: Incomplete
    relu1: Incomplete
    conv2: Incomplete
    bn2: Incomplete
    quant: Incomplete
    dequant: Incomplete
    def __init__(self) -> None: ...
    def forward(self, x): ...

class ModelForLinearBNFusion(nn.Module):
    fc: Incomplete
    bn: Incomplete
    def __init__(self) -> None: ...
    def forward(self, x): ...

class DummyObserver(torch.nn.Module):
    def calculate_qparams(self): ...
    def forward(self, x): ...

class ModelForConvTransposeBNFusion(nn.Module):
    conv1: Incomplete
    bn1: Incomplete
    conv2: Incomplete
    bn2: Incomplete
    conv3: Incomplete
    bn3: Incomplete
    def __init__(self) -> None: ...
    def forward(self, x): ...

class ModelWithFunctionals(torch.nn.Module):
    mycat: Incomplete
    myadd: Incomplete
    myadd_relu: Incomplete
    def __init__(self) -> None: ...
    def forward(self, x): ...

class ResNetBase(torch.nn.Module):
    conv1: Incomplete
    bn1: Incomplete
    relu1: Incomplete
    relu2: Incomplete
    downsample: Incomplete
    myop: Incomplete
    avgpool: Incomplete
    fc: Incomplete
    def __init__(self) -> None: ...
    def forward(self, x): ...
    def fuse_model(self) -> None: ...

class ModelMultipleOps(torch.nn.Module):
    conv1: Incomplete
    conv2: Incomplete
    bn1: Incomplete
    relu1: Incomplete
    relu2: Incomplete
    downsample: Incomplete
    skip_add: Incomplete
    cat: Incomplete
    avgpool: Incomplete
    fc: Incomplete
    def __init__(self) -> None: ...
    def forward(self, x): ...

class ModelMultipleOpsNoAvgPool(torch.nn.Module):
    conv1: Incomplete
    conv2: Incomplete
    bn1: Incomplete
    relu1: Incomplete
    relu2: Incomplete
    skip_add: Incomplete
    cat: Incomplete
    maxpool: Incomplete
    fc: Incomplete
    def __init__(self) -> None: ...
    def forward(self, x): ...

class EmbeddingBagModule(torch.nn.Module):
    emb: Incomplete
    def __init__(self) -> None: ...
    def forward(self, indices, offsets, per_sample_weights): ...

class EmbeddingModule(torch.nn.Module):
    emb: Incomplete
    def __init__(self) -> None: ...
    def forward(self, indices): ...

class EmbeddingWithStaticLinear(torch.nn.Module):
    emb: Incomplete
    fc: Incomplete
    qconfig: Incomplete
    quant: Incomplete
    dequant: Incomplete
    def __init__(self) -> None: ...
    def forward(self, indices, offsets, linear_in): ...

class DenseTopMLP(nn.Module):
    dense_mlp: Incomplete
    top_mlp: Incomplete
    def __init__(self, dense_dim, dense_out, embedding_dim, top_out_in, top_out_out) -> None: ...
    def forward(self, sparse_feature: torch.Tensor, dense: torch.Tensor) -> torch.Tensor: ...

class EmbBagWrapper(nn.Module):
    emb_bag: Incomplete
    def __init__(self, num_embeddings, embedding_dim) -> None: ...
    def forward(self, indices, offsets): ...

class SparseNNModel(nn.Module):
    model_sparse: Incomplete
    dense_top: Incomplete
    def __init__(self) -> None: ...
    def forward(self, sparse_indices: torch.Tensor, sparse_offsets: torch.Tensor, dense: torch.Tensor) -> torch.Tensor: ...
