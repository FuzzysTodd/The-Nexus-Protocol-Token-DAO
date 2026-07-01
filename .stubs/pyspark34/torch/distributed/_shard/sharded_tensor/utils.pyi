import torch
from .metadata import ShardedTensorMetadata as ShardedTensorMetadata, TensorProperties as TensorProperties
from .shard import Shard as Shard
from torch.distributed import distributed_c10d as distributed_c10d, rpc as rpc
from torch.distributed._shard.metadata import ShardMetadata as ShardMetadata
from torch.distributed._shard.sharding_spec._internals import check_tensor as check_tensor, validate_non_overlapping_shards_metadata as validate_non_overlapping_shards_metadata
from typing import List, Sequence

def build_metadata_from_local_shards(local_shards: List[Shard], global_size: torch.Size, current_rank: int, pg: distributed_c10d.ProcessGroup) -> ShardedTensorMetadata: ...
def build_global_metadata(gathered_metadatas: Sequence[ShardedTensorMetadata | None]): ...
