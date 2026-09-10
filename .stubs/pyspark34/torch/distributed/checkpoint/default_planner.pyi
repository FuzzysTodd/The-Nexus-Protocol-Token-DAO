import io
import torch
from _typeshed import Incomplete
from torch.distributed.checkpoint._nested_dict import FLATTEN_MAPPING
from torch.distributed.checkpoint.metadata import Metadata, MetadataIndex, STATE_DICT_TYPE
from torch.distributed.checkpoint.planner import LoadPlan, LoadPlanner, ReadItem, SavePlan, SavePlanner, WriteItem
from typing import Any, Dict, List, Tuple

__all__ = ['DefaultSavePlanner', 'DefaultLoadPlanner', 'create_default_local_load_plan', 'create_default_global_load_plan', 'create_default_local_save_plan', 'create_default_global_save_plan']

class DefaultSavePlanner(SavePlanner):
    mappings: FLATTEN_MAPPING
    flatten_state_dict: Incomplete
    flatten_sharded_tensors: Incomplete
    dedup_replicated_tensors: Incomplete
    def __init__(self, flatten_state_dict: bool = True, flatten_sharded_tensors: bool = True, dedup_replicated_tensors: bool = True) -> None: ...
    state_dict: Incomplete
    is_coordinator: Incomplete
    def set_up_planner(self, state_dict: STATE_DICT_TYPE, is_coordinator: bool) -> None: ...
    plan: Incomplete
    def create_local_plan(self) -> SavePlan: ...
    global_plan: Incomplete
    metadata: Incomplete
    def create_global_plan(self, all_plans: List[SavePlan]) -> Tuple[List[SavePlan], Metadata]: ...
    def finish_plan(self, new_plan: SavePlan) -> SavePlan: ...
    def resolve_data(self, write_item: WriteItem) -> torch.Tensor | io.BytesIO: ...
    def lookup_object(self, index: MetadataIndex) -> Any:
        """
        This is an extension from the planner interface to make it easy to extend the default planner
        """
    def transform_object(self, write_item: WriteItem, object: Any):
        """
        This is an extension from the planner interface to make it easy to extend the default planner
        """

class DefaultLoadPlanner(LoadPlanner):
    """
    DefaultLoadPlanner that adds multiple features on top of LoadPlanner.

    In particular it adds the following:

    flatten_state_dict: Handle state_dict with nested dicts
    flatten_sharded_tensors: For FSDP in 2D parallel mode
    """
    original_state_dict: STATE_DICT_TYPE
    mappings: FLATTEN_MAPPING
    flatten_state_dict: Incomplete
    flatten_sharded_tensors: Incomplete
    def __init__(self, flatten_state_dict: bool = True, flatten_sharded_tensors: bool = True) -> None: ...
    state_dict: Incomplete
    metadata: Incomplete
    is_coordinator: Incomplete
    def set_up_planner(self, state_dict: STATE_DICT_TYPE, metadata: Metadata, is_coordinator: bool) -> None: ...
    def create_local_plan(self) -> LoadPlan: ...
    def create_global_plan(self, global_plan: List[LoadPlan]) -> List[LoadPlan]: ...
    def finish_plan(self, new_plan: LoadPlan) -> LoadPlan: ...
    def load_bytes(self, read_item: ReadItem, value: io.BytesIO) -> None: ...
    def resolve_tensor(self, read_item: ReadItem): ...
    def commit_tensor(self, read_item: ReadItem, tensor: torch.Tensor) -> None: ...
    def lookup_tensor(self, index: MetadataIndex) -> torch.Tensor:
        """
        This is an extension from the planner interface to make it easy to extend the default planner
        """
    def transform_tensor(self, read_item: ReadItem, tensor: torch.Tensor):
        """
        This is an extension from the planner interface to make it easy to extend the default planner
        """

def create_default_local_load_plan(state_dict: Dict[str, Any], metadata: Metadata) -> LoadPlan: ...
def create_default_global_load_plan(all_plans: List[LoadPlan]) -> List[LoadPlan]:
    """
    Create global load plan used by DefaultLoadPlanner.

    The default load behavior involved no global coordination and this function
    currently doesn't change the local plans.
    """
def create_default_local_save_plan(state_dict: Dict[str, Any], is_coordinator: bool) -> SavePlan:
    """
    Create the ``SavePlan`` used by DefaultSavePlanner.

    On non-coordinator ranks, this function ignores tensors and non-tensor objects,
    only producing writes for ShardedTensor objects.

    On the coordinator rank, produce writes for all values.
    """
def create_default_global_save_plan(all_plans: List[SavePlan]) -> Tuple[List[SavePlan], Metadata]:
    """
    Create the global plan and metadata used by DefaultSavePlanner.

    Metadata is produced by concatenating the metadata of all ``WriteItem`` from the supplied plans.

    The only global planning change is to update index hints in all ``MetadataIndex`` objects.
    """
