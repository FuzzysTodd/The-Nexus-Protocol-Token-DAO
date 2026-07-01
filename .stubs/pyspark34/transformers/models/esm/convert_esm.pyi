from _typeshed import Incomplete
from transformers.models.esm.configuration_esm import EsmConfig as EsmConfig, EsmFoldConfig as EsmFoldConfig
from transformers.models.esm.modeling_esm import EsmForMaskedLM as EsmForMaskedLM, EsmForSequenceClassification as EsmForSequenceClassification, EsmIntermediate as EsmIntermediate, EsmLayer as EsmLayer, EsmOutput as EsmOutput, EsmSelfAttention as EsmSelfAttention, EsmSelfOutput as EsmSelfOutput
from transformers.models.esm.modeling_esmfold import EsmForProteinFolding as EsmForProteinFolding
from transformers.models.esm.tokenization_esm import EsmTokenizer as EsmTokenizer
from transformers.utils import logging as logging

logger: Incomplete
SAMPLE_DATA: Incomplete
MODEL_MAPPING: Incomplete
restypes: Incomplete
restypes_with_x: Incomplete
restypes_with_extras: Incomplete

def get_esmfold_tokenizer(): ...
def transfer_and_check_weights(original_module, our_module) -> None: ...
def convert_esm_checkpoint_to_pytorch(model: str, pytorch_dump_folder_path: str, classification_head: bool, push_to_repo: str, auth_token: str):
    """
    Copy/paste/tweak esm's weights to our BERT structure.
    """
