from transformers import TransfoXLConfig as TransfoXLConfig, TransfoXLLMHeadModel as TransfoXLLMHeadModel, load_tf_weights_in_transfo_xl as load_tf_weights_in_transfo_xl
from transformers.models.transfo_xl.tokenization_transfo_xl import CORPUS_NAME as CORPUS_NAME, VOCAB_FILES_NAMES as VOCAB_FILES_NAMES
from transformers.utils import CONFIG_NAME as CONFIG_NAME, WEIGHTS_NAME as WEIGHTS_NAME, logging as logging

def convert_transfo_xl_checkpoint_to_pytorch(tf_checkpoint_path, transfo_xl_config_file, pytorch_dump_folder_path, transfo_xl_dataset_file) -> None: ...
