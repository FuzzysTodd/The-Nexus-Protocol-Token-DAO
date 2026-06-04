from _typeshed import Incomplete
from tensorflow.python.util.tf_export import tf_export as tf_export

class Fingerprint:
    """The SavedModel fingerprint.

  Each attribute of this class is named after a field name in the
  FingerprintDef proto and contains the value of the respective field in the
  protobuf.

  Attributes:
    saved_model_checksum: A uint64 containing the `saved_model_checksum`.
    graph_def_program_hash: A uint64 containing `graph_def_program_hash`.
    signature_def_hash: A uint64 containing the `signature_def_hash`.
    saved_object_graph_hash: A uint64 containing the `saved_object_graph_hash`.
    checkpoint_hash: A uint64 containing the`checkpoint_hash`.
    version: An int32 containing the producer field of the VersionDef.
  """
    saved_model_checksum: Incomplete
    graph_def_program_hash: Incomplete
    signature_def_hash: Incomplete
    saved_object_graph_hash: Incomplete
    checkpoint_hash: Incomplete
    version: Incomplete
    def __init__(self, saved_model_checksum: Incomplete | None = None, graph_def_program_hash: Incomplete | None = None, signature_def_hash: Incomplete | None = None, saved_object_graph_hash: Incomplete | None = None, checkpoint_hash: Incomplete | None = None, version: Incomplete | None = None) -> None:
        """Initializes the instance based on values in the SavedModel fingerprint.

    Args:
      saved_model_checksum: Value of the`saved_model_checksum`.
      graph_def_program_hash: Value of the `graph_def_program_hash`.
      signature_def_hash: Value of the `signature_def_hash`.
      saved_object_graph_hash: Value of the `saved_object_graph_hash`.
      checkpoint_hash: Value of the `checkpoint_hash`.
      version: Value of the producer field of the VersionDef.
    """

def read_fingerprint(export_dir):
    """Reads the fingerprint of a SavedModel in `export_dir`.

  Returns a `tf.saved_model.experimental.Fingerprint` object that contains
  the values of the SavedModel fingerprint, which is persisted on disk in the
  `fingerprint.pb` file in the `export_dir`.
  TODO(b/265199038): Add link to TensorFlow SavedModel guide.

  Args:
    export_dir: The directory that contains the SavedModel.

  Returns:
    A `tf.saved_model.experimental.Fingerprint`.

  Raises:
    ValueError: If no or an invalid fingerprint is found.
  """
