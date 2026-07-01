from .. import SentenceTransformer as SentenceTransformer, util as util
from ..evaluation import SentenceEvaluator as SentenceEvaluator
from _typeshed import Incomplete
from torch.optim import Optimizer
from torch.utils.data import DataLoader
from typing import Callable, Dict, List, Type

logger: Incomplete

class CrossEncoder:
    config: Incomplete
    model: Incomplete
    tokenizer: Incomplete
    max_length: Incomplete
    default_activation_function: Incomplete
    def __init__(self, model_name: str, num_labels: int = None, max_length: int = None, device: str = None, tokenizer_args: Dict = {}, default_activation_function: Incomplete | None = None) -> None:
        """
        A CrossEncoder takes exactly two sentences / texts as input and either predicts
        a score or label for this sentence pair. It can for example predict the similarity of the sentence pair
        on a scale of 0 ... 1.

        It does not yield a sentence embedding and does not work for individually sentences.

        :param model_name: Any model name from Huggingface Models Repository that can be loaded with AutoModel. We provide several pre-trained CrossEncoder models that can be used for common tasks
        :param num_labels: Number of labels of the classifier. If 1, the CrossEncoder is a regression model that outputs a continous score 0...1. If > 1, it output several scores that can be soft-maxed to get probability scores for the different classes.
        :param max_length: Max length for input sequences. Longer sequences will be truncated. If None, max length of the model will be used
        :param device: Device that should be used for the model. If None, it will use CUDA if available.
        :param tokenizer_args: Arguments passed to AutoTokenizer
        :param default_activation_function: Callable (like nn.Sigmoid) about the default activation function that should be used on-top of model.predict(). If None. nn.Sigmoid() will be used if num_labels=1, else nn.Identity()
        """
    def smart_batching_collate(self, batch): ...
    def smart_batching_collate_text_only(self, batch): ...
    best_score: int
    def fit(self, train_dataloader: DataLoader, evaluator: SentenceEvaluator = None, epochs: int = 1, loss_fct: Incomplete | None = None, activation_fct=..., scheduler: str = 'WarmupLinear', warmup_steps: int = 10000, optimizer_class: Type[Optimizer] = ..., optimizer_params: Dict[str, object] = {'lr': 2e-05}, weight_decay: float = 0.01, evaluation_steps: int = 0, output_path: str = None, save_best_model: bool = True, max_grad_norm: float = 1, use_amp: bool = False, callback: Callable[[float, int, int], None] = None):
        """
        Train the model with the given training objective
        Each training objective is sampled in turn for one batch.
        We sample only as many batches from each objective as there are in the smallest one
        to make sure of equal training with each dataset.

        :param train_dataloader: DataLoader with training InputExamples
        :param evaluator: An evaluator (sentence_transformers.evaluation) evaluates the model performance during training on held-out dev data. It is used to determine the best model that is saved to disc.
        :param epochs: Number of epochs for training
        :param loss_fct: Which loss function to use for training. If None, will use nn.BCEWithLogitsLoss() if self.config.num_labels == 1 else nn.CrossEntropyLoss()
        :param activation_fct: Activation function applied on top of logits output of model.
        :param scheduler: Learning rate scheduler. Available schedulers: constantlr, warmupconstant, warmuplinear, warmupcosine, warmupcosinewithhardrestarts
        :param warmup_steps: Behavior depends on the scheduler. For WarmupLinear (default), the learning rate is increased from o up to the maximal learning rate. After these many training steps, the learning rate is decreased linearly back to zero.
        :param optimizer_class: Optimizer
        :param optimizer_params: Optimizer parameters
        :param weight_decay: Weight decay for model parameters
        :param evaluation_steps: If > 0, evaluate the model using evaluator after each number of training steps
        :param output_path: Storage path for the model and evaluation files
        :param save_best_model: If true, the best model (according to evaluator) is stored at output_path
        :param max_grad_norm: Used for gradient normalization.
        :param use_amp: Use Automatic Mixed Precision (AMP). Only for Pytorch >= 1.6.0
        :param callback: Callback function that is invoked after each evaluation.
                It must accept the following three parameters in this order:
                `score`, `epoch`, `steps`
        """
    def predict(self, sentences: List[List[str]], batch_size: int = 32, show_progress_bar: bool = None, num_workers: int = 0, activation_fct: Incomplete | None = None, apply_softmax: bool = False, convert_to_numpy: bool = True, convert_to_tensor: bool = False):
        """
        Performs predicts with the CrossEncoder on the given sentence pairs.

        :param sentences: A list of sentence pairs [[Sent1, Sent2], [Sent3, Sent4]]
        :param batch_size: Batch size for encoding
        :param show_progress_bar: Output progress bar
        :param num_workers: Number of workers for tokenization
        :param activation_fct: Activation function applied on the logits output of the CrossEncoder. If None, nn.Sigmoid() will be used if num_labels=1, else nn.Identity
        :param convert_to_numpy: Convert the output to a numpy matrix.
        :param apply_softmax: If there are more than 2 dimensions and apply_softmax=True, applies softmax on the logits output
        :param convert_to_tensor:  Conver the output to a tensor.
        :return: Predictions for the passed sentence pairs
        """
    def save(self, path) -> None:
        """
        Saves all model and tokenizer to path
        """
    def save_pretrained(self, path):
        """
        Same function as save
        """
