from transformers import OpenAIGPTConfig as OpenAIGPTConfig, OpenAIGPTModel as OpenAIGPTModel, load_tf_weights_in_openai_gpt as load_tf_weights_in_openai_gpt
from transformers.utils import CONFIG_NAME as CONFIG_NAME, WEIGHTS_NAME as WEIGHTS_NAME, logging as logging

def convert_openai_checkpoint_to_pytorch(openai_checkpoint_folder_path, openai_config_file, pytorch_dump_folder_path) -> None: ...
