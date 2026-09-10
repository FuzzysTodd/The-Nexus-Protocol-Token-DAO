from ..fuser_method_mappings import fuse_conv_bn as fuse_conv_bn, fuse_conv_bn_relu as fuse_conv_bn_relu, fuse_convtranspose_bn as fuse_convtranspose_bn, fuse_linear_bn as fuse_linear_bn
from .backend_config import BackendPatternConfig as BackendPatternConfig, DTypeConfig as DTypeConfig, DTypeWithConstraints as DTypeWithConstraints, ObservationType as ObservationType
from _typeshed import Incomplete
from typing import NamedTuple

class _ConvMetadata(NamedTuple):
    root: Incomplete
    transpose: Incomplete
    bn: Incomplete
    reference: Incomplete
    transpose_reference: Incomplete
    fused_conv_relu: Incomplete
    fused_conv_bn: Incomplete
    fused_conv_bn_relu: Incomplete
    qat: Incomplete
    relu_qat: Incomplete
    bn_qat: Incomplete
    bn_relu_qat: Incomplete
    func: Incomplete
