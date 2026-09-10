from _typeshed import Incomplete
from abc import ABCMeta
from py4j.java_gateway import JavaObject as JavaObject
from synapse.ml.onnx._ONNXModel import _ONNXModel
from typing import List, Mapping

basestring = str

class NodeInfo:
    name: Incomplete
    value_info: Incomplete
    def __init__(self, name: str, value_info: JavaObject) -> None: ...

class ONNXModel(_ONNXModel):
    """

    Args:
        SparkSession (SparkSession): The SparkSession that will be used to find the model
        location (str): The location of the model, either on local or HDFS
    """
    def setModelLocation(self, location): ...
    def setMiniBatchSize(self, n): ...
    def getModelInputs(self): ...
    def getModelOutputs(self) -> Mapping[str, NodeInfo]: ...

class ValueInfo(metaclass=ABCMeta):
    @classmethod
    def from_java(cls, java_value_info: JavaObject) -> ValueInfo: ...

class TensorInfo(ValueInfo):
    shape: Incomplete
    type: Incomplete
    def __init__(self, shape: List[int], type: str) -> None: ...
    @classmethod
    def from_java(cls, java_tensor_info: JavaObject) -> TensorInfo: ...

class MapInfo(ValueInfo):
    key_type: Incomplete
    value_type: Incomplete
    size: Incomplete
    def __init__(self, key_type: str, value_type: str, size: int = -1) -> None: ...
    @classmethod
    def from_java(cls, java_map_info: JavaObject) -> MapInfo: ...

class SequenceInfo(ValueInfo):
    length: Incomplete
    sequence_of_maps: Incomplete
    map_info: Incomplete
    sequence_type: Incomplete
    def __init__(self, length: int, sequence_of_maps: bool, map_info: MapInfo, sequence_type: str) -> None: ...
    @classmethod
    def from_java(cls, java_sequence_info: JavaObject) -> SequenceInfo: ...
