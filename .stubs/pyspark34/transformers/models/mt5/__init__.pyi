from ...utils.dummy_sentencepiece_objects import T5Tokenizer as T5Tokenizer
from ...utils.dummy_tokenizers_objects import T5TokenizerFast as T5TokenizerFast
from .configuration_mt5 import MT5Config as MT5Config, MT5OnnxConfig as MT5OnnxConfig
from .modeling_flax_mt5 import FlaxMT5EncoderModel as FlaxMT5EncoderModel, FlaxMT5ForConditionalGeneration as FlaxMT5ForConditionalGeneration, FlaxMT5Model as FlaxMT5Model
from .modeling_mt5 import MT5EncoderModel as MT5EncoderModel, MT5ForConditionalGeneration as MT5ForConditionalGeneration, MT5Model as MT5Model, MT5PreTrainedModel as MT5PreTrainedModel, MT5Stack as MT5Stack
from .modeling_tf_mt5 import TFMT5EncoderModel as TFMT5EncoderModel, TFMT5ForConditionalGeneration as TFMT5ForConditionalGeneration, TFMT5Model as TFMT5Model

MT5Tokenizer = T5Tokenizer
MT5TokenizerFast = T5TokenizerFast
