from _typeshed import Incomplete

OPT_NAME_V1_TO_V2: Incomplete
HP_IN_CKPT: Incomplete
OPT_VAR_NAME_V1_TO_V2: Incomplete
HP_IN_GRAPH: Incomplete
OPT_V2_INSTANCE: Incomplete

def convert_checkpoint(estimator_type, source_checkpoint, source_graph, target_checkpoint) -> None:
    """Converts checkpoint from TF 1.x to TF 2.0 for CannedEstimator.

  Args:
    estimator_type: The type of estimator to be converted. So far, the allowed
      args include 'dnn', 'linear', and 'combined'.
    source_checkpoint: Path to the source checkpoint file to be read in.
    source_graph: Path to the source graph file to be read in.
    target_checkpoint: Path to the target checkpoint to be written out.
  """
def main(_) -> None: ...
