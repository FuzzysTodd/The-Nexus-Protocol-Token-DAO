import pytorch_lightning as pl
from _typeshed import Incomplete
from transformers import LongformerForQuestionAnswering as LongformerForQuestionAnswering, LongformerModel as LongformerModel

class LightningModel(pl.LightningModule):
    model: Incomplete
    num_labels: int
    qa_outputs: Incomplete
    def __init__(self, model) -> None: ...
    def forward(self) -> None: ...

def convert_longformer_qa_checkpoint_to_pytorch(longformer_model: str, longformer_question_answering_ckpt_path: str, pytorch_dump_folder_path: str): ...
