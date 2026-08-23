from . import __MODEL_HUB_ORGANIZATION__ as __MODEL_HUB_ORGANIZATION__, __version__ as __version__
from .evaluation import SentenceEvaluator as SentenceEvaluator
from .model_card_templates import ModelCardTemplate as ModelCardTemplate
from .models import Dense as Dense, Pooling as Pooling, Transformer as Transformer
from .util import batch_to_device as batch_to_device, fullname as fullname, import_from_string as import_from_string, snapshot_download as snapshot_download
from _typeshed import Incomplete
from huggingface_hub import cached_download as cached_download, hf_hub_url as hf_hub_url
from numpy import ndarray
from torch import Tensor as Tensor, device, nn
from torch.optim import Optimizer
from torch.utils.data import DataLoader as DataLoader
from typing import Callable, Dict, Iterable, List, Tuple, Type

logger: Incomplete

class SentenceTransformer(nn.Sequential):
    """
    Loads or create a SentenceTransformer model, that can be used to map sentences / text to embeddings.

    :param model_name_or_path: If it is a filepath on disc, it loads the model from that path. If it is not a path, it first tries to download a pre-trained SentenceTransformer model. If that fails, tries to construct a model from Huggingface models repository with that name.
    :param modules: This parameter can be used to create custom SentenceTransformer models from scratch.
    :param device: Device (like 'cuda' / 'cpu') that should be used for computation. If None, checks if a GPU can be used.
    :param cache_folder: Path to store models
    """
    def __init__(self, model_name_or_path: str | None = None, modules: Iterable[nn.Module] | None = None, device: str | None = None, cache_folder: str | None = None) -> None: ...
    def encode(self, sentences: str | List[str] | List[int], batch_size: int = 32, show_progress_bar: bool = None, output_value: str = 'sentence_embedding', convert_to_numpy: bool = True, convert_to_tensor: bool = False, device: str = None, normalize_embeddings: bool = False) -> List[Tensor] | ndarray | Tensor:
        """
        Computes sentence embeddings

        :param sentences: the sentences to embed
        :param batch_size: the batch size used for the computation
        :param show_progress_bar: Output a progress bar when encode sentences
        :param output_value:  Default sentence_embedding, to get sentence embeddings. Can be set to token_embeddings to get wordpiece token embeddings.
        :param convert_to_numpy: If true, the output is a list of numpy vectors. Else, it is a list of pytorch tensors.
        :param convert_to_tensor: If true, you get one large tensor as return. Overwrites any setting from convert_to_numpy
        :param device: Which torch.device to use for the computation
        :param normalize_embeddings: If set to true, returned vectors will have length 1. In that case, the faster dot-product (util.dot_score) instead of cosine similarity can be used.

        :return:
           By default, a list of tensors is returned. If convert_to_tensor, a stacked tensor is returned. If convert_to_numpy, a numpy matrix is returned.
        """
    def start_multi_process_pool(self, target_devices: List[str] = None):
        """
        Starts multi process to process the encoding with several, independent processes.
        This method is recommended if you want to encode on multiple GPUs. It is advised
        to start only one process per GPU. This method works together with encode_multi_process

        :param target_devices: PyTorch target devices, e.g. cuda:0, cuda:1... If None, all available CUDA devices will be used
        :return: Returns a dict with the target processes, an input queue and and output queue.
        """
    @staticmethod
    def stop_multi_process_pool(pool) -> None:
        """
        Stops all processes started with start_multi_process_pool
        """
    def encode_multi_process(self, sentences: List[str], pool: Dict[str, object], batch_size: int = 32, chunk_size: int = None):
        """
        This method allows to run encode() on multiple GPUs. The sentences are chunked into smaller packages
        and sent to individual processes, which encode these on the different GPUs. This method is only suitable
        for encoding large sets of sentences

        :param sentences: List of sentences
        :param pool: A pool of workers started with SentenceTransformer.start_multi_process_pool
        :param batch_size: Encode sentences with batch size
        :param chunk_size: Sentences are chunked and sent to the individual processes. If none, it determine a sensible size.
        :return: Numpy matrix with all embeddings
        """
    def get_max_seq_length(self):
        """
        Returns the maximal sequence length for input the model accepts. Longer inputs will be truncated
        """
    def tokenize(self, texts: List[str] | List[Dict] | List[Tuple[str, str]]):
        """
        Tokenizes the texts
        """
    def get_sentence_features(self, *features): ...
    def get_sentence_embedding_dimension(self): ...
    def save(self, path: str, model_name: str | None = None, create_model_card: bool = True):
        """
        Saves all elements for this seq. sentence embedder into different sub-folders
        :param path: Path on disc
        :param model_name: Optional model name
        :param create_model_card: If True, create a README.md with basic information about this model
        """
    def save_to_hub(self, repo_name: str, organization: str | None = None, private: bool | None = None, commit_message: str = 'Add new SentenceTransformer model.', local_model_path: str | None = None, exist_ok: bool = False, replace_model_card: bool = False):
        """
        Uploads all elements of this Sentence Transformer to a new HuggingFace Hub repository.

        :param repo_name: Repository name for your model in the Hub.
        :param organization:  Organization in which you want to push your model or tokenizer (you must be a member of this organization).
        :param private: Set to true, for hosting a prive model
        :param commit_message: Message to commit while pushing.
        :param local_model_path: Path of the model locally. If set, this file path will be uploaded. Otherwise, the current model will be uploaded
        :param exist_ok: If true, saving to an existing repository is OK. If false, saving only to a new repository is possible
        :param replace_model_card: If true, replace an existing model card in the hub with the automatically created model card
        :return: The url of the commit of your model in the given repository.
        """
    def smart_batching_collate(self, batch):
        """
        Transforms a batch from a SmartBatchingDataset to a batch of tensors for the model
        Here, batch is a list of tuples: [(tokens, label), ...]

        :param batch:
            a batch from a SmartBatchingDataset
        :return:
            a batch of tensors for the model
        """
    best_score: int
    def fit(self, train_objectives: Iterable[Tuple[DataLoader, nn.Module]], evaluator: SentenceEvaluator = None, epochs: int = 1, steps_per_epoch: Incomplete | None = None, scheduler: str = 'WarmupLinear', warmup_steps: int = 10000, optimizer_class: Type[Optimizer] = ..., optimizer_params: Dict[str, object] = {'lr': 2e-05}, weight_decay: float = 0.01, evaluation_steps: int = 0, output_path: str = None, save_best_model: bool = True, max_grad_norm: float = 1, use_amp: bool = False, callback: Callable[[float, int, int], None] = None, show_progress_bar: bool = True, checkpoint_path: str = None, checkpoint_save_steps: int = 500, checkpoint_save_total_limit: int = 0):
        """
        Train the model with the given training objective
        Each training objective is sampled in turn for one batch.
        We sample only as many batches from each objective as there are in the smallest one
        to make sure of equal training with each dataset.

        :param train_objectives: Tuples of (DataLoader, LossFunction). Pass more than one for multi-task learning
        :param evaluator: An evaluator (sentence_transformers.evaluation) evaluates the model performance during training on held-out dev data. It is used to determine the best model that is saved to disc.
        :param epochs: Number of epochs for training
        :param steps_per_epoch: Number of training steps per epoch. If set to None (default), one epoch is equal the DataLoader size from train_objectives.
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
        :param show_progress_bar: If True, output a tqdm progress bar
        :param checkpoint_path: Folder to save checkpoints during training
        :param checkpoint_save_steps: Will save a checkpoint after so many steps
        :param checkpoint_save_total_limit: Total number of checkpoints to store
        """
    def evaluate(self, evaluator: SentenceEvaluator, output_path: str = None):
        """
        Evaluate the model

        :param evaluator:
            the evaluator
        :param output_path:
            the evaluator can write the results to this path
        """
    @property
    def device(self) -> device:
        """
        Get torch.device from module, assuming that the whole module has one device.
        """
    @property
    def tokenizer(self):
        """
        Property to get the tokenizer that is used by this model
        """
    @tokenizer.setter
    def tokenizer(self, value) -> None:
        """
        Property to set the tokenizer that is should used by this model
        """
    @property
    def max_seq_length(self):
        """
        Property to get the maximal input sequence length for the model. Longer inputs will be truncated.
        """
    @max_seq_length.setter
    def max_seq_length(self, value) -> None:
        """
        Property to set the maximal input sequence length for the model. Longer inputs will be truncated.
        """
