from _typeshed import Incomplete
from transformers import XLNetConfig as XLNetConfig, XLNetForQuestionAnswering as XLNetForQuestionAnswering, XLNetForSequenceClassification as XLNetForSequenceClassification, XLNetLMHeadModel as XLNetLMHeadModel, load_tf_weights_in_xlnet as load_tf_weights_in_xlnet
from transformers.utils import CONFIG_NAME as CONFIG_NAME, WEIGHTS_NAME as WEIGHTS_NAME, logging as logging

GLUE_TASKS_NUM_LABELS: Incomplete

def convert_xlnet_checkpoint_to_pytorch(tf_checkpoint_path, bert_config_file, pytorch_dump_folder_path, finetuning_task: Incomplete | None = None) -> None: ...
