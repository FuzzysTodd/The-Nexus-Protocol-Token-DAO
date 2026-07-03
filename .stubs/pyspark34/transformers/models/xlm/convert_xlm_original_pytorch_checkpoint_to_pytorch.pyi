from transformers.models.xlm.tokenization_xlm import VOCAB_FILES_NAMES as VOCAB_FILES_NAMES
from transformers.utils import CONFIG_NAME as CONFIG_NAME, WEIGHTS_NAME as WEIGHTS_NAME, logging as logging

def convert_xlm_checkpoint_to_pytorch(xlm_checkpoint_path, pytorch_dump_folder_path) -> None: ...
