from transformers import ElectraConfig as ElectraConfig, ElectraForMaskedLM as ElectraForMaskedLM, ElectraForPreTraining as ElectraForPreTraining, load_tf_weights_in_electra as load_tf_weights_in_electra
from transformers.utils import logging as logging

def convert_tf_checkpoint_to_pytorch(tf_checkpoint_path, config_file, pytorch_dump_path, discriminator_or_generator) -> None: ...
