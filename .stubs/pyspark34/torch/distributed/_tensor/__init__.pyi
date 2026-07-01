from torch.distributed._tensor.api import DTensor as DTensor, distribute_module as distribute_module, distribute_tensor as distribute_tensor
from torch.distributed._tensor.device_mesh import DeviceMesh as DeviceMesh
from torch.distributed._tensor.placement_types import Replicate as Replicate, Shard as Shard

__all__ = ['DTensor', 'DeviceMesh', 'distribute_tensor', 'distribute_module', 'Shard', 'Replicate']
