from transformers import ImageGPTConfig as ImageGPTConfig, ImageGPTForCausalLM as ImageGPTForCausalLM, load_tf_weights_in_imagegpt as load_tf_weights_in_imagegpt
from transformers.utils import CONFIG_NAME as CONFIG_NAME, WEIGHTS_NAME as WEIGHTS_NAME, logging as logging

def convert_imagegpt_checkpoint_to_pytorch(imagegpt_checkpoint_path, model_size, pytorch_dump_folder_path) -> None: ...
