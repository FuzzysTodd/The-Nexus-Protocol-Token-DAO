from _typeshed import Incomplete
from typing import NamedTuple

class DistributeConfig(NamedTuple('DistributeConfig', [('train_distribute', Incomplete), ('eval_distribute', Incomplete), ('remote_cluster', Incomplete)])):
    """A config tuple for distribution strategies.

  Attributes:
    train_distribute: a `DistributionStrategy` object for training.
    eval_distribute: an optional `DistributionStrategy` object for
      evaluation.
    remote_cluster: a dict, `ClusterDef` or `ClusterSpec` object specifying
      the cluster configurations. If this is given, the `train_and_evaluate`
      method will be running as a standalone client which connects to the
      cluster for training.
  """
    def __new__(cls, train_distribute: Incomplete | None = None, eval_distribute: Incomplete | None = None, remote_cluster: Incomplete | None = None): ...
