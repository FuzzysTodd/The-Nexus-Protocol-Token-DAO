import numpy as np
import tensorflow as tf
from . import DataCollatorWithPadding as DataCollatorWithPadding, DefaultDataCollator as DefaultDataCollator, PreTrainedTokenizerBase as PreTrainedTokenizerBase
from .activations_tf import get_tf_activation as get_tf_activation
from .configuration_utils import PretrainedConfig as PretrainedConfig
from .dynamic_module_utils import custom_object_save as custom_object_save
from .generation import GenerationConfig as GenerationConfig, TFGenerationMixin as TFGenerationMixin
from .tf_utils import shape_list as shape_list
from .utils import DUMMY_INPUTS as DUMMY_INPUTS, ModelOutput as ModelOutput, PushToHubMixin as PushToHubMixin, SAFE_WEIGHTS_INDEX_NAME as SAFE_WEIGHTS_INDEX_NAME, SAFE_WEIGHTS_NAME as SAFE_WEIGHTS_NAME, TF2_WEIGHTS_INDEX_NAME as TF2_WEIGHTS_INDEX_NAME, TF2_WEIGHTS_NAME as TF2_WEIGHTS_NAME, TF_WEIGHTS_NAME as TF_WEIGHTS_NAME, WEIGHTS_INDEX_NAME as WEIGHTS_INDEX_NAME, WEIGHTS_NAME as WEIGHTS_NAME, cached_file as cached_file, download_url as download_url, find_labels as find_labels, has_file as has_file, is_offline_mode as is_offline_mode, is_remote_url as is_remote_url, is_safetensors_available as is_safetensors_available, logging as logging, requires_backends as requires_backends, working_or_temp_dir as working_or_temp_dir
from _typeshed import Incomplete
from tensorflow.python.keras.engine.keras_tensor import KerasTensor
from transformers.utils.hub import convert_file_size_to_int as convert_file_size_to_int, get_checkpoint_shard_files as get_checkpoint_shard_files
from typing import Any, Callable, Dict, List, Optional, Union

logger: Incomplete
tf_logger: Incomplete
TFModelInputType = Union[List[tf.Tensor], List[np.ndarray], List[KerasTensor], Dict[str, tf.Tensor], Dict[str, np.ndarray], Dict[str, KerasTensor], tf.Tensor, np.ndarray, KerasTensor]

def dummy_loss(y_true, y_pred): ...

class TFModelUtilsMixin:
    """
    A few utilities for `tf.keras.Model`, to be used as a mixin.
    """
    def num_parameters(self, only_trainable: bool = False) -> int:
        """
        Get the number of (optionally, trainable) parameters in the model.

        Args:
            only_trainable (`bool`, *optional*, defaults to `False`):
                Whether or not to return only the number of trainable parameters

        Returns:
            `int`: The number of parameters.
        """

def keras_serializable(cls):
    """
    Decorate a Keras Layer class to support Keras serialization.

    This is done by:

    1. Adding a `transformers_config` dict to the Keras config dictionary in `get_config` (called by Keras at
       serialization time.
    2. Wrapping `__init__` to accept that `transformers_config` dict (passed by Keras at deserialization time) and
       convert it to a config object for the actual layer initializer.
    3. Registering the class as a custom object in Keras (if the Tensorflow version supports this), so that it does not
       need to be supplied in `custom_objects` in the call to `tf.keras.models.load_model`.

    Args:
        cls (a `tf.keras.layers.Layers subclass`):
            Typically a `TF.MainLayer` class in this project, in general must accept a `config` argument to its
            initializer.

    Returns:
        The same class object, with modifications for Keras deserialization.
    """

class TFCausalLanguageModelingLoss:
    """
    Loss function suitable for causal language modeling (CLM), that is, the task of guessing the next token.

    <Tip>

    Any label of -100 will be ignored (along with the corresponding logits) in the loss computation.

    </Tip>
    """
    def hf_compute_loss(self, labels, logits): ...

class TFQuestionAnsweringLoss:
    """
    Loss function suitable for question answering.
    """
    def hf_compute_loss(self, labels, logits): ...

class TFTokenClassificationLoss:
    """
    Loss function suitable for token classification.

    <Tip>

    Any label of -100 will be ignored (along with the corresponding logits) in the loss computation.

    </Tip>
    """
    def hf_compute_loss(self, labels, logits): ...

class TFSequenceClassificationLoss:
    """
    Loss function suitable for sequence classification.
    """
    def hf_compute_loss(self, labels, logits): ...

class TFMultipleChoiceLoss:
    """Loss function suitable for multiple choice tasks."""
    def hf_compute_loss(self, labels, logits): ...

class TFMaskedLanguageModelingLoss(TFCausalLanguageModelingLoss):
    """
    Loss function suitable for masked language modeling (MLM), that is, the task of guessing the masked tokens.

    <Tip>

    Any label of -100 will be ignored (along with the corresponding logits) in the loss computation.

    </Tip>
    """

class TFNextSentencePredictionLoss:
    """
    Loss function suitable for next sentence prediction (NSP), that is, the task of guessing the next sentence.

    <Tip>

    Any label of -100 will be ignored (along with the corresponding logits) in the loss computation.

    </Tip>
    """
    def hf_compute_loss(self, labels, logits): ...

def booleans_processing(config, **kwargs):
    """
    Process the input booleans of each model.

    Args:
        config ([`PretrainedConfig`]):
            The config of the running model.
        **kwargs:
            The boolean parameters

    Returns:
        A dictionary with the proper values for each boolean
    """
def unpack_inputs(func):
    """
    Decorator that processes the inputs to a Keras layer, passing them to the layer as keyword arguments. This enables
    downstream use of the inputs by their variable name, even if they arrive packed as a dictionary in the first input
    (common case in Keras).

    Args:
        func (`callable`):
            The callable function of the TensorFlow model.

    Returns:
        A callable that wraps the original `func` with the behavior described above.
    """
def input_processing(func, config, **kwargs):
    '''
    Process the input of each TensorFlow model including the booleans. In case of a list of symbolic inputs, each input
    has to be named accordingly to the parameters name, i.e. `input_ids = tf.keras.Input(shape=(128,), dtype=\'int32\',
    name="input_ids")` otherwise the order of the tensors will not be guaranteed during the training.

    Args:
        func (`callable`):
            The callable function of the TensorFlow model.
        config ([`PretrainedConfig`]):
            The config of the running model.
        **kwargs:
            The inputs of the model.

    Returns:
        Two lists, one for the missing layers, and another one for the unexpected layers.
    '''
def dtype_byte_size(dtype):
    """
    Returns the size (in bytes) occupied by one parameter of type `dtype`.

    Example:

    ```py
    >>> dtype_byte_size(tf.float32)
    4
    ```
    """
def format_weight_name(name, _prefix: Incomplete | None = None): ...
def tf_shard_checkpoint(weights, max_shard_size: str = '10GB'):
    '''
    Splits a model state dictionary in sub-checkpoints so that the final size of each sub-checkpoint does not exceed a
    given size.

    The sub-checkpoints are determined by iterating through the `state_dict` in the order of its keys, so there is no
    optimization made to make each sub-checkpoint as close as possible to the maximum size passed. For example, if the
    limit is 10GB and we have weights of sizes [6GB, 6GB, 2GB, 6GB, 2GB, 2GB] they will get sharded as [6GB], [6+2GB],
    [6+2+2GB] and not [6+2+2GB], [6+2GB], [6GB].

    <Tip warning={true}>

    If one of the model\'s weight is bigger that `max_shard_size`, it will end up in its own sub-checkpoint which will
    have a size greater than `max_shard_size`.

    </Tip>

    Args:
        weights (`Dict[str, tf.RessourceVariable]`): The list of tf.RessourceVariable of a model to save.
        max_shard_size (`int` or `str`, *optional*, defaults to `"10GB"`):
            The maximum size of each sub-checkpoint. If expressed as a string, needs to be digits followed by a unit
            (like `"5MB"`).
    '''
def load_tf_sharded_weights(model, shard_files, ignore_mismatched_sizes: bool = False, strict: bool = True):
    """
    This is the same as `load_tf_weights` but for a sharded checkpoint. Detect missing and unexpected layers and load
    the TF weights from the shard file accordingly to their names and shapes.

    This load is performed efficiently: each checkpoint shard is loaded one by one in RAM and deleted after being
    loaded in the model.

    Args:
        model (`tf.keras.models.Model`): The model in which to load the checkpoint.
        shard_files (`str` or `os.PathLike`): A list containing the sharded checkpoint names.
        ignore_mismatched_sizes`bool`, *optional`, defaults to `True`):
            Whether or not to ignore the mismatch between the sizes
        strict (`bool`, *optional*, defaults to `True`):
            Whether to strictly enforce that the keys in the model state dict match the keys in the sharded checkpoint.

    Returns:
        Three lists, one for the missing layers, another one for the unexpected layers, and a last one for the
        mismatched layers.
    """
def load_tf_shard(model, model_layer_map, resolved_archive_file, ignore_mismatched_sizes: bool = False):
    """
    Loads a shard from a sharded checkpoint file. Handles the missing keys and unexpected keys.

    Args:
        model (`tf.keras.models.Model`): Model in which the weights are loaded
        model_layer_map (`Dict`): A dictionary mapping the layer name to the index of the layer in the model.
        resolved_archive_file (`str`): Path to the checkpoint file from which the weights will be loaded
        ignore_mismatched_sizes (`bool`, *optional*, defaults to `False`): Whether to ignore the mismatched keys

    Returns:
        `tf.keras.models.Model`: Three lists, one for the layers that were found and succesfully restored (from the
        shard file), one for the missmatched layers, and another one for the unexpected layers.
    """
def load_tf_weights(model, resolved_archive_file, ignore_mismatched_sizes: bool = False, _prefix: Incomplete | None = None):
    """
    Detect missing and unexpected layers and load the TF weights from the shard file accordingly to their names and
    shapes.

    Args:
        model (`tf.keras.models.Model`):
            The model to load the weights into.
        resolved_archive_file (`str`):
            The location of the H5 file.
        ignore_mismatched_sizes (`bool`, *optional*, defaults to `False`):
            Whether or not to ignore weights with shapes that don't match between the checkpoint of the model.

    Returns:
        Three lists, one for the missing layers, another one for the unexpected layers, and a last one for the
        mismatched layers.
    """
def load_tf_weights_from_h5(model, resolved_archive_file, ignore_mismatched_sizes: bool = False, _prefix: Incomplete | None = None): ...
def load_tf_weights_from_safetensors(model, resolved_archive_file, ignore_mismatched_sizes: bool = False, _prefix: Incomplete | None = None): ...
def init_copy_embeddings(old_embeddings, new_num_tokens):
    """
    This function aims to reduce the embeddings in case new_num_tokens < old_num_tokens or to pad with -1 in case
    new_num_tokens > old_num_tokens. A mask is also computed in order to know which weight in the embeddings should be
    kept or not. Example:

        - if new_num_tokens=5 and old_num_tokens=4 and old_embeddings=[w1,w2,w3,w4]

            -  mask=[True,True,True,True,False] and current_weights=[w1,w2,w3,w4,-1]
        - if new_num_tokens=4 and old_num_tokens=5 and old_embeddings=[w1,w2,w3,w4,w5]

            - mask=[True,True,True,True] and current_weights=[w1,w2,w3,w4]
    """

class TFPreTrainedModel(tf.keras.Model, TFModelUtilsMixin, TFGenerationMixin, PushToHubMixin):
    """
    Base class for all TF models.

    [`TFPreTrainedModel`] takes care of storing the configuration of the models and handles methods for loading,
    downloading and saving models as well as a few methods common to all models to:

        - resize the input embeddings,
        - prune heads in the self-attention heads.

    Class attributes (overridden by derived classes):

        - **config_class** ([`PretrainedConfig`]) -- A subclass of [`PretrainedConfig`] to use as configuration class
          for this model architecture.
        - **base_model_prefix** (`str`) -- A string indicating the attribute associated to the base model in derived
          classes of the same architecture adding modules on top of the base model.
        - **main_input_name** (`str`) -- The name of the principal input to the model (often `input_ids` for NLP
          models, `pixel_values` for vision models and `input_values` for speech models).
    """
    config_class: Incomplete
    base_model_prefix: str
    main_input_name: str
    @property
    def dummy_inputs(self) -> Dict[str, tf.Tensor]:
        """
        Dummy inputs to build the network.

        Returns:
            `Dict[str, tf.Tensor]`: The dummy inputs.
        """
    @property
    def framework(self) -> str:
        """
        :str: Identifies that this is a TensorFlow model.
        """
    config: Incomplete
    name_or_path: Incomplete
    generation_config: Incomplete
    def __init__(self, config, *inputs, **kwargs) -> None: ...
    def get_config(self): ...
    @classmethod
    def from_config(cls, config, **kwargs): ...
    def eager_serving(self, inputs):
        """
        Method used for serving the model. Intended not to be compiled with a tf.function decorator so that we can use
        it to generate multiple signatures later.

        Args:
            inputs (`Dict[str, tf.Tensor]`):
                The input of the saved model as a dictionary of tensors.
        """
    def serving(self, inputs):
        """
        Method used for serving the model.

        Args:
            inputs (`Dict[str, tf.Tensor]`):
                The input of the saved model as a dictionary of tensors.
        """
    def serving_output(self, output) -> None:
        """
        Prepare the output of the saved model. Each model must implement this function.

        Args:
            output ([`TFBaseModelOutput`]):
                The output returned by the model.
        """
    def can_generate(self) -> bool:
        """
        Returns whether this model can generate sequences with `.generate()`.

        Returns:
            `bool`: Whether this model can generate sequences with `.generate()`.
        """
    def get_input_embeddings(self) -> tf.keras.layers.Layer:
        """
        Returns the model's input embeddings layer.

        Returns:
            `tf.Variable`: The embeddings layer mapping vocabulary to hidden states.
        """
    def load_repo_checkpoint(self, repo_path_or_name):
        '''
        Loads a saved checkpoint (model weights and optimizer state) from a repo. Returns the current epoch count when
        the checkpoint was made.

        Args:
            repo_path_or_name (`str`):
                Can either be a repository name for your {object} in the Hub or a path to a local folder (in which case
                the repository will have the name of that local folder).

        Returns:
            `dict`: A dictionary of extra metadata from the checkpoint, most commonly an "epoch" count.
        '''
    def prepare_tf_dataset(self, dataset: datasets.Dataset, batch_size: int = 8, shuffle: bool = True, tokenizer: Optional['PreTrainedTokenizerBase'] = None, collate_fn: Optional[Callable] = None, collate_fn_args: Optional[Dict[str, Any]] = None, drop_remainder: Optional[bool] = None, prefetch: bool = True):
        '''
        Wraps a HuggingFace [`~datasets.Dataset`] as a `tf.data.Dataset` with collation and batching. This method is
        designed to create a "ready-to-use" dataset that can be passed directly to Keras methods like `fit()` without
        further modification. The method will drop columns from the dataset if they don\'t match input names for the
        model. If you want to specify the column names to return rather than using the names that match this model, we
        recommend using `Dataset.to_tf_dataset()` instead.

        Args:
            dataset (`Any`):
                A [~`datasets.Dataset`] to be wrapped as a `tf.data.Dataset`.
            batch_size (`int`, defaults to 8):
                The size of batches to return.
            shuffle (`bool`, defaults to `True`):
                Whether to return samples from the dataset in random order. Usually `True` for training datasets and
                `False` for validation/test datasets.
            tokenizer ([`PreTrainedTokenizerBase`], *optional*):
                A `PreTrainedTokenizer` that will be used to pad samples to create batches. Has no effect if a specific
                `collate_fn` is passed instead.
            collate_fn (`Callable`, *optional*):
                A function that collates samples from the dataset into a single batch. Defaults to
                `DefaultDataCollator` if no `tokenizer` is supplied or `DataCollatorWithPadding` if a `tokenizer` is
                passed.
            collate_fn_args (`Dict[str, Any]`, *optional*):
                A dict of arguments to pass to the `collate_fn` alongside the list of samples.
            drop_remainder (`bool`, *optional*):
                Whether to drop the final batch, if the batch_size does not evenly divide the dataset length. Defaults
                to the same setting as `shuffle`.
            prefetch (`bool`, defaults to `True`):
                Whether to add prefetching to the end of the `tf.data` pipeline. This is almost always beneficial for
                performance, but can be disabled in edge cases.


        Returns:
            `Dataset`: A `tf.data.Dataset` which is ready to pass to the Keras API.
        '''
    def compile(self, optimizer: str = 'rmsprop', loss: str = 'passthrough', metrics: Incomplete | None = None, loss_weights: Incomplete | None = None, weighted_metrics: Incomplete | None = None, run_eagerly: Incomplete | None = None, steps_per_execution: Incomplete | None = None, **kwargs) -> None:
        """
        This is a thin wrapper that sets the model's loss output head as the loss if the user does not specify a loss
        function themselves.
        """
    def compute_loss(self, *args, **kwargs): ...
    def get_label_to_output_name_mapping(self): ...
    def train_step(self, data):
        """
        A modification of Keras's default `train_step` that correctly handles matching outputs to labels for our models
        and supports directly training on the loss output head. In addition, it ensures input keys are copied to the
        labels where appropriate. It will also copy label keys into the input dict when using the dummy loss, to ensure
        that they are available to the model during the forward pass.
        """
    def test_step(self, data):
        """
        A modification of Keras's default `train_step` that correctly handles matching outputs to labels for our models
        and supports directly training on the loss output head. In addition, it ensures input keys are copied to the
        labels where appropriate. It will also copy label keys into the input dict when using the dummy loss, to ensure
        that they are available to the model during the forward pass.
        """
    def create_model_card(self, output_dir, model_name: str, language: Optional[str] = None, license: Optional[str] = None, tags: Optional[str] = None, finetuned_from: Optional[str] = None, tasks: Optional[str] = None, dataset_tags: Optional[Union[str, List[str]]] = None, dataset: Optional[Union[str, List[str]]] = None, dataset_args: Optional[Union[str, List[str]]] = None):
        """
        Creates a draft of a model card using the information available to the `Trainer`.

        Args:
            output_dir (`str` or `os.PathLike`):
                The folder in which to create the model card.
            model_name (`str`, *optional*):
                The name of the model.
            language (`str`, *optional*):
                The language of the model (if applicable)
            license (`str`, *optional*):
                The license of the model. Will default to the license of the pretrained model used, if the original
                model given to the `Trainer` comes from a repo on the Hub.
            tags (`str` or `List[str]`, *optional*):
                Some tags to be included in the metadata of the model card.
            finetuned_from (`str`, *optional*):
                The name of the model used to fine-tune this one (if applicable). Will default to the name of the repo
                of the original model given to the `Trainer` (if it comes from the Hub).
            tasks (`str` or `List[str]`, *optional*):
                One or several task identifiers, to be included in the metadata of the model card.
            dataset_tags (`str` or `List[str]`, *optional*):
                One or several dataset tags, to be included in the metadata of the model card.
            dataset (`str` or `List[str]`, *optional*):
                One or several dataset identifiers, to be included in the metadata of the model card.
            dataset_args (`str` or `List[str]`, *optional*):
               One or several dataset arguments, to be included in the metadata of the model card.
        """
    def set_input_embeddings(self, value) -> None:
        """
        Set model's input embeddings

        Args:
            value (`tf.Variable`):
                The new weights mapping hidden states to vocabulary.
        """
    def get_output_embeddings(self) -> Union[None, tf.keras.layers.Layer]:
        """
        Returns the model's output embeddings

        Returns:
            `tf.Variable`: The new weights mapping vocabulary to hidden states.
        """
    def set_output_embeddings(self, value) -> None:
        """
        Set model's output embeddings

        Args:
            value (`tf.Variable`):
                The new weights mapping hidden states to vocabulary.
        """
    def get_output_layer_with_bias(self) -> Union[None, tf.keras.layers.Layer]:
        """
        Get the layer that handles a bias attribute in case the model has an LM head with weights tied to the
        embeddings

        Return:
            `tf.keras.layers.Layer`: The layer that handles the bias, None if not an LM model.
        """
    def get_prefix_bias_name(self) -> Union[None, str]:
        """
        Get the concatenated _prefix name of the bias from the model name to the parent layer

        Return:
            `str`: The _prefix name of the bias.
        """
    def get_bias(self) -> Union[None, Dict[str, tf.Variable]]:
        """
        Dict of bias attached to an LM head. The key represents the name of the bias attribute.

        Return:
            `tf.Variable`: The weights representing the bias, None if not an LM model.
        """
    def set_bias(self, value) -> None:
        """
        Set all the bias in the LM head.

        Args:
            value (`Dict[tf.Variable]`):
                All the new bias attached to an LM head.
        """
    def get_lm_head(self) -> tf.keras.layers.Layer:
        """
        The LM Head layer. This method must be overwritten by all the models that have a lm head.

        Return:
            `tf.keras.layers.Layer`: The LM head layer if the model has one, None if not.
        """
    def resize_token_embeddings(self, new_num_tokens: Optional[int] = None) -> Union[tf.keras.layers.Embedding, tf.Variable]:
        """
        Resizes input token embeddings matrix of the model if `new_num_tokens != config.vocab_size`.

        Takes care of tying weights embeddings afterwards if the model class has a `tie_weights()` method.

        Arguments:
            new_num_tokens (`int`, *optional*):
                The number of new tokens in the embedding matrix. Increasing the size will add newly initialized
                vectors at the end. Reducing the size will remove vectors from the end. If not provided or `None`, just
                returns a pointer to the input tokens without doing anything.

        Return:
            `tf.Variable` or `tf.keras.layers.Embedding`: Pointer to the input tokens of the model.
        """
    def prune_heads(self, heads_to_prune) -> None:
        """
        Prunes heads of the base model.

        Arguments:
            heads_to_prune (`Dict[int, List[int]]`):
                Dictionary with keys being selected layer indices (`int`) and associated values being the list of heads
                to prune in said layer (list of `int`). For instance {1: [0, 2], 2: [2, 3]} will prune heads 0 and 2 on
                layer 1 and heads 2 and 3 on layer 2.
        """
    def save_pretrained(self, save_directory, saved_model: bool = False, version: int = 1, push_to_hub: bool = False, signatures: Incomplete | None = None, max_shard_size: Union[int, str] = '10GB', create_pr: bool = False, safe_serialization: bool = False, **kwargs):
        '''
        Save a model and its configuration file to a directory, so that it can be re-loaded using the
        [`~TFPreTrainedModel.from_pretrained`] class method.

        Arguments:
            save_directory (`str`):
                Directory to which to save. Will be created if it doesn\'t exist.
            saved_model (`bool`, *optional*, defaults to `False`):
                If the model has to be saved in saved model format as well or not.
            version (`int`, *optional*, defaults to 1):
                The version of the saved model. A saved model needs to be versioned in order to be properly loaded by
                TensorFlow Serving as detailed in the official documentation
                https://www.tensorflow.org/tfx/serving/serving_basic
            push_to_hub (`bool`, *optional*, defaults to `False`):
                Whether or not to push your model to the Hugging Face model hub after saving it. You can specify the
                repository you want to push to with `repo_id` (will default to the name of `save_directory` in your
                namespace).
            signatures (`dict` or `tf.function`, *optional*):
                Model\'s signature used for serving. This will be passed to the `signatures` argument of model.save().
            max_shard_size (`int` or `str`, *optional*, defaults to `"10GB"`):
                The maximum size for a checkpoint before being sharded. Checkpoints shard will then be each of size
                lower than this size. If expressed as a string, needs to be digits followed by a unit (like `"5MB"`).

                <Tip warning={true}>

                If a single weight of the model is bigger than `max_shard_size`, it will be in its own checkpoint shard
                which will be bigger than `max_shard_size`.

                </Tip>

            create_pr (`bool`, *optional*, defaults to `False`):
                Whether or not to create a PR with the uploaded files or directly commit.
            safe_serialization (`bool`, *optional*, defaults to `False`):
                Whether to save the model using `safetensors` or the traditional PyTorch way (that uses `pickle`).

            kwargs:
                Additional key word arguments passed along to the [`~utils.PushToHubMixin.push_to_hub`] method.
        '''
    @classmethod
    def from_pretrained(cls, pretrained_model_name_or_path, *model_args, **kwargs):
        '''
        Instantiate a pretrained TF 2.0 model from a pre-trained model configuration.

        The warning *Weights from XXX not initialized from pretrained model* means that the weights of XXX do not come
        pretrained with the rest of the model. It is up to you to train those weights with a downstream fine-tuning
        task.

        The warning *Weights from XXX not used in YYY* means that the layer XXX is not used by YYY, therefore those
        weights are discarded.

        Parameters:
            pretrained_model_name_or_path (`str`, *optional*):
                Can be either:

                    - A string, the *model id* of a pretrained model hosted inside a model repo on huggingface.co.
                      Valid model ids can be located at the root-level, like `bert-base-uncased`, or namespaced under a
                      user or organization name, like `dbmdz/bert-base-german-cased`.
                    - A path to a *directory* containing model weights saved using
                      [`~TFPreTrainedModel.save_pretrained`], e.g., `./my_model_directory/`.
                    - A path or url to a *PyTorch state_dict save file* (e.g, `./pt_model/pytorch_model.bin`). In this
                      case, `from_pt` should be set to `True` and a configuration object should be provided as `config`
                      argument. This loading path is slower than converting the PyTorch model in a TensorFlow model
                      using the provided conversion scripts and loading the TensorFlow model afterwards.
                    - `None` if you are both providing the configuration and state dictionary (resp. with keyword
                      arguments `config` and `state_dict`).
            model_args (sequence of positional arguments, *optional*):
                All remaining positional arguments will be passed to the underlying model\'s `__init__` method.
            config (`Union[PretrainedConfig, str]`, *optional*):
                Can be either:

                    - an instance of a class derived from [`PretrainedConfig`],
                    - a string valid as input to [`~PretrainedConfig.from_pretrained`].

                Configuration for the model to use instead of an automatically loaded configuration. Configuration can
                be automatically loaded when:

                    - The model is a model provided by the library (loaded with the *model id* string of a pretrained
                      model).
                    - The model was saved using [`~TFPreTrainedModel.save_pretrained`] and is reloaded by supplying the
                      save directory.
                    - The model is loaded by supplying a local directory as `pretrained_model_name_or_path` and a
                      configuration JSON file named *config.json* is found in the directory.
            from_pt (`bool`, *optional*, defaults to `False`):
                Load the model weights from a PyTorch state_dict save file (see docstring of
                `pretrained_model_name_or_path` argument).
            ignore_mismatched_sizes (`bool`, *optional*, defaults to `False`):
                Whether or not to raise an error if some of the weights from the checkpoint do not have the same size
                as the weights of the model (if for instance, you are instantiating a model with 10 labels from a
                checkpoint with 3 labels).
            cache_dir (`str`, *optional*):
                Path to a directory in which a downloaded pretrained model configuration should be cached if the
                standard cache should not be used.
            force_download (`bool`, *optional*, defaults to `False`):
                Whether or not to force the (re-)download of the model weights and configuration files, overriding the
                cached versions if they exist.
            resume_download (`bool`, *optional*, defaults to `False`):
                Whether or not to delete incompletely received files. Will attempt to resume the download if such a
                file exists.
            proxies:
                (`Dict[str, str], `optional`): A dictionary of proxy servers to use by protocol or endpoint, e.g.,
                `{\'http\': \'foo.bar:3128\', \'http://hostname\': \'foo.bar:4012\'}`. The proxies are used on each request.
                output_loading_info(`bool`, *optional*, defaults to `False`): Whether ot not to also return a
                dictionary containing missing keys, unexpected keys and error messages.
            local_files_only(`bool`, *optional*, defaults to `False`):
                Whether or not to only look at local files (e.g., not try doanloading the model).
            use_auth_token (`str` or `bool`, *optional*):
                The token to use as HTTP bearer authorization for remote files. If `True`, or not specified, will use
                the token generated when running `huggingface-cli login` (stored in `~/.huggingface`).
            revision (`str`, *optional*, defaults to `"main"`):
                The specific model version to use. It can be a branch name, a tag name, or a commit id, since we use a
                git-based system for storing models and other artifacts on huggingface.co, so `revision` can be any
                identifier allowed by git.


                <Tip>

                To test a pull request you made on the Hub, you can pass `revision="refs/pr/<pr_number>".

                </Tip>

            mirror (`str`, *optional*):
                Mirror source to accelerate downloads in China. If you are from China and have an accessibility
                problem, you can set this option to resolve it. Note that we do not guarantee the timeliness or safety.
                Please refer to the mirror site for more information.
            subfolder (`str`, *optional*, defaults to `""`):
                In case the relevant files are located inside a subfolder of the model repo on huggingface.co, you can
                specify the folder name here.
            kwargs (remaining dictionary of keyword arguments, *optional*):
                Can be used to update the configuration object (after it being loaded) and initiate the model (e.g.,
                `output_attentions=True`). Behaves differently depending on whether a `config` is provided or
                automatically loaded:

                    - If a configuration is provided with `config`, `**kwargs` will be directly passed to the
                      underlying model\'s `__init__` method (we assume all relevant updates to the configuration have
                      already been done)
                    - If a configuration is not provided, `kwargs` will be first passed to the configuration class
                      initialization function ([`~PretrainedConfig.from_pretrained`]). Each key of `kwargs` that
                      corresponds to a configuration attribute will be used to override said attribute with the
                      supplied `kwargs` value. Remaining keys that do not correspond to any configuration attribute
                      will be passed to the underlying model\'s `__init__` function.

        Examples:

        ```python
        >>> from transformers import BertConfig, TFBertModel

        >>> # Download model and configuration from huggingface.co and cache.
        >>> model = TFBertModel.from_pretrained("bert-base-uncased")
        >>> # Model was saved using *save_pretrained(\'./test/saved_model/\')* (for example purposes, not runnable).
        >>> model = TFBertModel.from_pretrained("./test/saved_model/")
        >>> # Update configuration during loading.
        >>> model = TFBertModel.from_pretrained("bert-base-uncased", output_attentions=True)
        >>> assert model.config.output_attentions == True
        >>> # Loading from a Pytorch model file instead of a TensorFlow checkpoint (slower, for example purposes, not runnable).
        >>> config = BertConfig.from_json_file("./pt_model/my_pt_model_config.json")
        >>> model = TFBertModel.from_pretrained("./pt_model/my_pytorch_model.bin", from_pt=True, config=config)
        ```'''
    def push_to_hub(self, repo_id: str, use_temp_dir: Optional[bool] = None, commit_message: Optional[str] = None, private: Optional[bool] = None, use_auth_token: Optional[Union[bool, str]] = None, max_shard_size: Optional[Union[int, str]] = '10GB', **model_card_kwargs) -> str:
        '''
        Upload the model files to the 🤗 Model Hub while synchronizing a local clone of the repo in `repo_path_or_name`.

        Parameters:
            repo_id (`str`):
                The name of the repository you want to push your model to. It should contain your organization name
                when pushing to a given organization.
            use_temp_dir (`bool`, *optional*):
                Whether or not to use a temporary directory to store the files saved before they are pushed to the Hub.
                Will default to `True` if there is no directory named like `repo_id`, `False` otherwise.
            commit_message (`str`, *optional*):
                Message to commit while pushing. Will default to `"Upload model"`.
            private (`bool`, *optional*):
                Whether or not the repository created should be private.
            use_auth_token (`bool` or `str`, *optional*):
                The token to use as HTTP bearer authorization for remote files. If `True`, will use the token generated
                when running `huggingface-cli login` (stored in `~/.huggingface`). Will default to `True` if `repo_url`
                is not specified.
            max_shard_size (`int` or `str`, *optional*, defaults to `"10GB"`):
                Only applicable for models. The maximum size for a checkpoint before being sharded. Checkpoints shard
                will then be each of size lower than this size. If expressed as a string, needs to be digits followed
                by a unit (like `"5MB"`).
            model_card_kwargs:
                Additional keyword arguments passed along to the [`~TFPreTrainedModel.create_model_card`] method.

        Examples:

        ```python
        from transformers import TFAutoModel

        model = TFAutoModel.from_pretrained("bert-base-cased")

        # Push the model to your namespace with the name "my-finetuned-bert".
        model.push_to_hub("my-finetuned-bert")

        # Push the model to an organization with the name "my-finetuned-bert".
        model.push_to_hub("huggingface/my-finetuned-bert")
        ```
        '''
    @classmethod
    def register_for_auto_class(cls, auto_class: str = 'TFAutoModel') -> None:
        '''
        Register this class with a given auto class. This should only be used for custom models as the ones in the
        library are already mapped with an auto class.

        <Tip warning={true}>

        This API is experimental and may have some slight breaking changes in the next releases.

        </Tip>

        Args:
            auto_class (`str` or `type`, *optional*, defaults to `"TFAutoModel"`):
                The auto class to register this new model with.
        '''

class TFConv1D(tf.keras.layers.Layer):
    """
    1D-convolutional layer as defined by Radford et al. for OpenAI GPT (and also used in GPT-2).

    Basically works like a linear layer but the weights are transposed.

    Args:
        nf (`int`):
            The number of output features.
        nx (`int`):
            The number of input features.
        initializer_range (`float`, *optional*, defaults to 0.02):
            The standard deviation to use to initialize the weights.
        kwargs:
            Additional keyword arguments passed along to the `__init__` of `tf.keras.layers.Layer`.
    """
    nf: Incomplete
    nx: Incomplete
    initializer_range: Incomplete
    def __init__(self, nf, nx, initializer_range: float = 0.02, **kwargs) -> None: ...
    weight: Incomplete
    bias: Incomplete
    def build(self, input_shape) -> None: ...
    def call(self, x): ...

class TFSharedEmbeddings(tf.keras.layers.Layer):
    """
    Construct shared token embeddings.

    The weights of the embedding layer is usually shared with the weights of the linear decoder when doing language
    modeling.

    Args:
        vocab_size (`int`):
            The size of the vocabulary, e.g., the number of unique tokens.
        hidden_size (`int`):
            The size of the embedding vectors.
        initializer_range (`float`, *optional*):
            The standard deviation to use when initializing the weights. If no value is provided, it will default to
            \\\\(1/\\sqrt{hidden\\_size}\\\\).
        kwargs:
            Additional keyword arguments passed along to the `__init__` of `tf.keras.layers.Layer`.
    """
    vocab_size: Incomplete
    hidden_size: Incomplete
    initializer_range: Incomplete
    def __init__(self, vocab_size: int, hidden_size: int, initializer_range: Optional[float] = None, **kwargs) -> None: ...
    weight: Incomplete
    def build(self, input_shape) -> None:
        """
        Build shared token embedding layer Shared weights logic adapted from
        https://github.com/tensorflow/models/blob/a009f4fb9d2fc4949e32192a944688925ef78659/official/transformer/v2/embedding_layer.py#L24
        """
    def get_config(self): ...
    def call(self, inputs: tf.Tensor, mode: str = 'embedding') -> tf.Tensor:
        '''
        Get token embeddings of inputs or decode final hidden state.

        Args:
            inputs (`tf.Tensor`):
                In embedding mode, should be an int64 tensor with shape `[batch_size, length]`.

                In linear mode, should be a float tensor with shape `[batch_size, length, hidden_size]`.
            mode (`str`, defaults to `"embedding"`):
               A valid value is either `"embedding"` or `"linear"`, the first one indicates that the layer should be
               used as an embedding layer, the second one that the layer should be used as a linear decoder.

        Returns:
            `tf.Tensor`: In embedding mode, the output is a float32 embedding tensor, with shape `[batch_size, length,
            embedding_size]`.

            In linear mode, the output is a float32 with shape `[batch_size, length, vocab_size]`.

        Raises:
            ValueError: if `mode` is not valid.

        Shared weights logic is adapted from
        [here](https://github.com/tensorflow/models/blob/a009f4fb9d2fc4949e32192a944688925ef78659/official/transformer/v2/embedding_layer.py#L24).
        '''

class TFSequenceSummary(tf.keras.layers.Layer):
    '''
    Compute a single vector summary of a sequence hidden states.

    Args:
        config ([`PretrainedConfig`]):
            The config used by the model. Relevant arguments in the config class of the model are (refer to the actual
            config class of your model for the default values it uses):

            - **summary_type** (`str`) -- The method to use to make this summary. Accepted values are:

                - `"last"` -- Take the last token hidden state (like XLNet)
                - `"first"` -- Take the first token hidden state (like Bert)
                - `"mean"` -- Take the mean of all tokens hidden states
                - `"cls_index"` -- Supply a Tensor of classification token position (GPT/GPT-2)
                - `"attn"` -- Not implemented now, use multi-head attention

            - **summary_use_proj** (`bool`) -- Add a projection after the vector extraction.
            - **summary_proj_to_labels** (`bool`) -- If `True`, the projection outputs to `config.num_labels` classes
              (otherwise to `config.hidden_size`).
            - **summary_activation** (`Optional[str]`) -- Set to `"tanh"` to add a tanh activation to the output,
              another string or `None` will add no activation.
            - **summary_first_dropout** (`float`) -- Optional dropout probability before the projection and activation.
            - **summary_last_dropout** (`float`)-- Optional dropout probability after the projection and activation.

        initializer_range (`float`, defaults to 0.02): The standard deviation to use to initialize the weights.
        kwargs:
            Additional keyword arguments passed along to the `__init__` of `tf.keras.layers.Layer`.
    '''
    summary_type: Incomplete
    has_summary: Incomplete
    summary: Incomplete
    has_activation: bool
    activation: Incomplete
    has_first_dropout: Incomplete
    first_dropout: Incomplete
    has_last_dropout: Incomplete
    last_dropout: Incomplete
    def __init__(self, config: PretrainedConfig, initializer_range: float = 0.02, **kwargs) -> None: ...
    def call(self, inputs, cls_index: Incomplete | None = None, training: bool = False): ...

def get_initializer(initializer_range: float = 0.02) -> tf.initializers.TruncatedNormal:
    """
    Creates a `tf.initializers.TruncatedNormal` with the given range.

    Args:
        initializer_range (*float*, defaults to 0.02): Standard deviation of the initializer range.

    Returns:
        `tf.initializers.TruncatedNormal`: The truncated normal initializer.
    """
