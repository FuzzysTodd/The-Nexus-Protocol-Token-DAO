from _typeshed import Incomplete
from tensorflow.python.eager import backprop as backprop
from tensorflow.python.framework import constant_op as constant_op, dtypes as dtypes, test_util as test_util
from tensorflow.python.ops import nn_ops as nn_ops
from tensorflow.python.platform import test as test
from typing import NamedTuple

class LayerShapeNHWC(NamedTuple):
    batch: Incomplete
    height: Incomplete
    width: Incomplete
    channels: Incomplete

class FilterShape2D(NamedTuple):
    height: Incomplete
    width: Incomplete
    in_channels: Incomplete
    out_channels: Incomplete

class FilterShape2DTranspose(NamedTuple):
    height: Incomplete
    width: Incomplete
    out_channels: Incomplete
    in_channels: Incomplete

class LayerShapeNCDHW(NamedTuple):
    batch: Incomplete
    channels: Incomplete
    depth: Incomplete
    height: Incomplete
    width: Incomplete

class FilterShape3D(NamedTuple):
    depth: Incomplete
    height: Incomplete
    width: Incomplete
    in_channels: Incomplete
    out_channels: Incomplete

class ConvolutionTest(test.TestCase):
    """Tests for deterministic cuDNN functionality."""
    def testConvForwardDefaultAlgorithmChoice(self): ...
    def testConvForwardXLA(self): ...
    def testConvBackwardFilterGradient(self, rate: int = 1): ...
    def testConvBackwardFilterGradientWithDilations(self) -> None: ...
    def testConvBackwardInputGradient(self, rate: int = 1): ...
    def testConvBackwardInputGradientWithDilations(self) -> None: ...
    def testConvTransposeForward(self, rate: int = 1): ...
    def testConvTransposeForwardWithDilations(self) -> None: ...
    def testConvTransposeBackwardFilterGradient(self, rate: int = 1): ...
    def testConvTransposeBackwardFilterGradientWithDilations(self) -> None: ...
    def testConvTransposeBackwardInputGradient(self, rate: int = 1): ...
    def testConvTransposeBackwardInputGradientWithDilations(self) -> None: ...
