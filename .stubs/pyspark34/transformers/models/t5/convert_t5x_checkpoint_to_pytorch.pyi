from transformers import T5Config as T5Config, T5EncoderModel as T5EncoderModel, T5ForConditionalGeneration as T5ForConditionalGeneration
from transformers.utils import logging as logging

def t5x_attention_lookup(params, i, prefix, layer_name: str = 'attention'):
    """Returns the KOQV parameters of (self-)attention. Does not transpose."""
def t5x_mlp_lookup(params, i, prefix, split_mlp_wi: bool = False):
    """Returns the MLP parameters of a layer. Does not transpose."""
def t5x_layer_norm_lookup(params, i, prefix, layer_name):
    """Returns the layer norm param of a layer."""
def convert_t5x_to_pytorch(variables: dict, *, num_layers: int, is_encoder_only: bool):
    """Converts the parameters from T5X-Flax to Transformers-PyTorch."""
def make_state_dict(converted_params, is_encoder_only: bool):
    """Prepares a state dict for the PyTorch model."""
def load_t5x_weights_in_t5(model, config, t5x_checkpoint_path, is_encoder_only) -> None:
    """Replaces the params in model witht the T5X converted params."""
def convert_t5x_checkpoint_to_pytorch(t5x_checkpoint_path, config_file, pytorch_dump_path, is_encoder_only: bool = False):
    """Loads the config and model, converts the T5X checkpoint, and saves a PyTorch checkpoint."""
