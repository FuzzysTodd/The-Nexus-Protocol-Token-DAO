from _typeshed import Incomplete
from transformers import BertModel as BertModel

def convert_pytorch_checkpoint_to_tf(model: BertModel, ckpt_dir: str, model_name: str):
    """
    Args:
        model: BertModel Pytorch model instance to be converted
        ckpt_dir: Tensorflow model directory
        model_name: model name

    Currently supported HF models:

        - Y BertModel
        - N BertForMaskedLM
        - N BertForPreTraining
        - N BertForMultipleChoice
        - N BertForNextSentencePrediction
        - N BertForSequenceClassification
        - N BertForQuestionAnswering
    """
def main(raw_args: Incomplete | None = None) -> None: ...
