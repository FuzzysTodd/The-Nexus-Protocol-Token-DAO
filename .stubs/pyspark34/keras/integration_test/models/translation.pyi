from _typeshed import Incomplete
from keras.integration_test.models.input_spec import InputSpec as InputSpec
from tensorflow import keras

VOCAB_SIZE: int
SEQUENCE_LENGTH: int

def get_data_spec(batch_size): ...
def get_input_preprocessor(): ...

class TransformerEncoder(keras.layers.Layer):
    embed_dim: Incomplete
    dense_dim: Incomplete
    num_heads: Incomplete
    attention: Incomplete
    dense_proj: Incomplete
    layernorm_1: Incomplete
    layernorm_2: Incomplete
    supports_masking: bool
    def __init__(self, embed_dim, dense_dim, num_heads, **kwargs) -> None: ...
    def call(self, inputs, mask: Incomplete | None = None): ...

class PositionalEmbedding(keras.layers.Layer):
    token_embeddings: Incomplete
    position_embeddings: Incomplete
    sequence_length: Incomplete
    vocab_size: Incomplete
    embed_dim: Incomplete
    def __init__(self, sequence_length, vocab_size, embed_dim, **kwargs) -> None: ...
    def call(self, inputs): ...
    def compute_mask(self, inputs, mask: Incomplete | None = None): ...

class TransformerDecoder(keras.layers.Layer):
    embed_dim: Incomplete
    latent_dim: Incomplete
    num_heads: Incomplete
    attention_1: Incomplete
    attention_2: Incomplete
    dense_proj: Incomplete
    layernorm_1: Incomplete
    layernorm_2: Incomplete
    layernorm_3: Incomplete
    supports_masking: bool
    def __init__(self, embed_dim, latent_dim, num_heads, **kwargs) -> None: ...
    def call(self, inputs, encoder_outputs, mask: Incomplete | None = None): ...
    def get_causal_attention_mask(self, inputs): ...

def get_model(build: bool = False, compile: bool = False, jit_compile: bool = False, include_preprocessing: bool = True): ...
def get_custom_objects(): ...
