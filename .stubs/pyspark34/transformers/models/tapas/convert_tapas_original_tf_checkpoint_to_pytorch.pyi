from transformers import TapasConfig as TapasConfig, TapasForMaskedLM as TapasForMaskedLM, TapasForQuestionAnswering as TapasForQuestionAnswering, TapasForSequenceClassification as TapasForSequenceClassification, TapasModel as TapasModel, TapasTokenizer as TapasTokenizer, load_tf_weights_in_tapas as load_tf_weights_in_tapas
from transformers.utils import logging as logging

def convert_tf_checkpoint_to_pytorch(task, reset_position_index_per_cell, tf_checkpoint_path, tapas_config_file, pytorch_dump_path) -> None: ...
