from _typeshed import Incomplete
from transformers import FSMTConfig as FSMTConfig, FSMTForConditionalGeneration as FSMTForConditionalGeneration
from transformers.models.fsmt.tokenization_fsmt import VOCAB_FILES_NAMES as VOCAB_FILES_NAMES
from transformers.tokenization_utils_base import TOKENIZER_CONFIG_FILE as TOKENIZER_CONFIG_FILE
from transformers.utils import WEIGHTS_NAME as WEIGHTS_NAME, logging as logging

json_indent: int
best_score_hparams: Incomplete
org_names: Incomplete

def rewrite_dict_keys(d): ...
def convert_fsmt_checkpoint_to_pytorch(fsmt_checkpoint_path, pytorch_dump_folder_path) -> None: ...
