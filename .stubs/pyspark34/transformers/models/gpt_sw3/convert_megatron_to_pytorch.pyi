from transformers import GPT2Config as GPT2Config

def recursive_print(name, val, spaces: int = 0) -> None: ...
def fix_query_key_value_ordering(param, num_splits, num_heads, hidden_size): ...
def convert_megatron_checkpoint(sd_megatron, config):
    """
    Converts a Megatron checkpoint to a HuggingFace GPT-SW3 checkpoint.
    """
def copy_config(config_hf, config_megatron):
    """Copy the config from Megatron to hf."""
def main(args) -> None: ...
