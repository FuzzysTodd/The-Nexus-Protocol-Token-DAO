import enum
from _typeshed import Incomplete
from tensorflow.core.protobuf.tpu import topology_pb2 as topology_pb2
from tensorflow.python.util.tf_export import tf_export as tf_export

class HardwareFeature:
    """class holds all the feature info about the TPU."""
    tpu_hardware_feature_proto: Incomplete
    def __init__(self, tpu_hardware_feature_proto) -> None:
        """Store TPU hardware feature info.

    Args:
      tpu_hardware_feature_proto: protobuf which describe the tpu hardware
        feature.
    """
    class EmbeddingFeature(enum.Enum):
        """Embedding feature flag strings.

    UNSUPPORTED: No embedding lookup accelerator available on the tpu.
    V1: Embedding lookup accelerator V1. The embedding lookup operation can only
        be placed at the beginning of computation. Only one instance of
        embedding
        lookup layer is allowed.
    V2: Embedding lookup accelerator V2. The embedding lookup operation can be
        placed anywhere of the computation. Multiple instances of embedding
        lookup layer is allowed.
    """
        UNSUPPORTED: str
        V1: str
        V2: str
    @property
    def embedding_feature(self):
        """TPU embedding feature.

    Returns:
      An EmbeddingFeature enum.
    """
