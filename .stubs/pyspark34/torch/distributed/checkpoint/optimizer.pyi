import torch
import torch.distributed.checkpoint as dist_cp
from _typeshed import Incomplete
from torch.distributed.checkpoint.default_planner import DefaultLoadPlanner
from torch.distributed.checkpoint.metadata import Metadata, MetadataIndex, STATE_DICT_TYPE
from torch.distributed.checkpoint.planner import LoadPlan
from typing import Dict, Sequence, Tuple

__all__ = ['load_sharded_optimizer_state_dict']

STATE_DICT_2D_LAYOUT = Dict[str, Tuple[Sequence[int] | None, Sequence[int]]]

class _ReaderWithOffset(DefaultLoadPlanner):
    translation: Dict[MetadataIndex, MetadataIndex]
    state_dict: STATE_DICT_TYPE
    metadata: Metadata
    fqn_to_offset: Incomplete
    def __init__(self, fqn_to_offset: Dict[str, Sequence[int]]) -> None: ...
    def create_local_plan(self) -> LoadPlan: ...
    def lookup_tensor(self, index: MetadataIndex) -> torch.Tensor: ...

def load_sharded_optimizer_state_dict(model_state_dict: STATE_DICT_TYPE, optimizer_key: str, storage_reader: dist_cp.StorageReader) -> STATE_DICT_TYPE:
    '''
    Loads a state_dict to be used in conjuntion with FSDP sharded optimizer state.
    This is the current recommended way to checkpoint is FSDP
    >>> # xdoctest: +SKIP
    >>> import torch.distributed.checkpoint as dist_cp
    >>> # Save
    >>> model: torch.nn.Model
    >>> optim_params = model.parameters()
    >>> optim = torch.optim.SGD(optim_params, lr=0.01)
    >>>
    >>> with FSDP.state_dict_type(model, StateDictType.SHARDED_STATE_DICT):
    >>>     state_dict = {
    >>>         "optimizer": FSDP.sharded_optim_state_dict(model, optim, optim_params),
    >>>         "model": model.state_dict()
    >>>     }
    >>>     dist_cp.save_state_dict(
    >>>         state_dict=optim_state,
    >>>         storage_writer=dist_cp.FileSystemWriter("checkpoint"),
    >>>         planner=dist_cp.DefaultSavePlanner(),
    >>>     )
    >>>
    >>> # Load
    >>> with FSDP.state_dict_type(model_tp, StateDictType.SHARDED_STATE_DICT):
    >>>     model_state_dict = model_tp.state_dict()
    >>>     checkpoint = {
    >>>         "model": model_state_dict
    >>>     }
    >>>     dist_cp.load_state_dict(
    >>>         state_dict=checkpoint,
    >>>         storage_reader=dist_cp.FileSystemReader(checkpoint_file),
    >>>         planner=dist_cp.DefaultLoadPlanner(),
    >>>     )
    >>>     model.load_state_dict(checkpoint["model_state"])
    >>>
    >>>     optim_state = sp_cp.load_sharded_optimizer_state_dict(
    >>>         model_state_dict,
    >>>         optimizer_key="optimizer",
    >>>         storage_reader=dist_cp.FileSystemReader("checkpoint"),
    >>>     )
    >>>
    >>>     flattened_osd = FSDP.flatten_sharded_optim_state_dict(
    >>>        optim_state["optimizer"], model, optim
    >>>     )
    >>>
    >>>     optim.load_state_dict(flattened_osd)
    '''
