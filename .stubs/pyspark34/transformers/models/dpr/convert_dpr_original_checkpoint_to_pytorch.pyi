from .transformers import BertConfig as BertConfig, DPRConfig as DPRConfig, DPRContextEncoder as DPRContextEncoder, DPRQuestionEncoder as DPRQuestionEncoder, DPRReader as DPRReader
from _typeshed import Incomplete
from pathlib import Path
from typing import NamedTuple

class CheckpointState(NamedTuple):
    model_dict: Incomplete
    optimizer_dict: Incomplete
    scheduler_dict: Incomplete
    offset: Incomplete
    epoch: Incomplete
    encoder_params: Incomplete

def load_states_from_checkpoint(model_file: str) -> CheckpointState: ...

class DPRState:
    src_file: Incomplete
    def __init__(self, src_file: Path) -> None: ...
    def load_dpr_model(self) -> None: ...
    @staticmethod
    def from_type(comp_type: str, *args, **kwargs) -> DPRState: ...

class DPRContextEncoderState(DPRState):
    def load_dpr_model(self): ...

class DPRQuestionEncoderState(DPRState):
    def load_dpr_model(self): ...

class DPRReaderState(DPRState):
    def load_dpr_model(self): ...

def convert(comp_type: str, src_file: Path, dest_dir: Path): ...
