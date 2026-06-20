from .constants import CONFIG_NAME as CONFIG_NAME
from .hf_api import HfApi as HfApi
from .utils import SoftTemporaryDirectory as SoftTemporaryDirectory, logging as logging, validate_hf_hub_args as validate_hf_hub_args
from _typeshed import Incomplete
from huggingface_hub import ModelHubMixin as ModelHubMixin, snapshot_download as snapshot_download
from huggingface_hub.utils import get_tf_version as get_tf_version, is_graphviz_available as is_graphviz_available, is_pydot_available as is_pydot_available, is_tf_available as is_tf_available, yaml_dump as yaml_dump
from pathlib import Path
from typing import Any, Dict, List

logger: Incomplete

def save_pretrained_keras(model, save_directory: str | Path, config: Dict[str, Any] | None = None, include_optimizer: bool = False, plot_model: bool = True, tags: list | str | None = None, **model_save_kwargs):
    """
    Saves a Keras model to save_directory in SavedModel format. Use this if
    you're using the Functional or Sequential APIs.

    Args:
        model (`Keras.Model`):
            The [Keras
            model](https://www.tensorflow.org/api_docs/python/tf/keras/Model)
            you'd like to save. The model must be compiled and built.
        save_directory (`str` or `Path`):
            Specify directory in which you want to save the Keras model.
        config (`dict`, *optional*):
            Configuration object to be saved alongside the model weights.
        include_optimizer(`bool`, *optional*, defaults to `False`):
            Whether or not to include optimizer in serialization.
        plot_model (`bool`, *optional*, defaults to `True`):
            Setting this to `True` will plot the model and put it in the model
            card. Requires graphviz and pydot to be installed.
        tags (Union[`str`,`list`], *optional*):
            List of tags that are related to model or string of a single tag. See example tags
            [here](https://github.com/huggingface/hub-docs/blame/main/modelcard.md).
        model_save_kwargs(`dict`, *optional*):
            model_save_kwargs will be passed to
            [`tf.keras.models.save_model()`](https://www.tensorflow.org/api_docs/python/tf/keras/models/save_model).
    """
def from_pretrained_keras(*args, **kwargs) -> KerasModelHubMixin:
    """
    Instantiate a pretrained Keras model from a pre-trained model from the Hub.
    The model is expected to be in `SavedModel` format.

    Args:
        pretrained_model_name_or_path (`str` or `os.PathLike`):
            Can be either:
                - A string, the `model id` of a pretrained model hosted inside a
                  model repo on huggingface.co. Valid model ids can be located
                  at the root-level, like `bert-base-uncased`, or namespaced
                  under a user or organization name, like
                  `dbmdz/bert-base-german-cased`.
                - You can add `revision` by appending `@` at the end of model_id
                  simply like this: `dbmdz/bert-base-german-cased@main` Revision
                  is the specific model version to use. It can be a branch name,
                  a tag name, or a commit id, since we use a git-based system
                  for storing models and other artifacts on huggingface.co, so
                  `revision` can be any identifier allowed by git.
                - A path to a `directory` containing model weights saved using
                  [`~transformers.PreTrainedModel.save_pretrained`], e.g.,
                  `./my_model_directory/`.
                - `None` if you are both providing the configuration and state
                  dictionary (resp. with keyword arguments `config` and
                  `state_dict`).
        force_download (`bool`, *optional*, defaults to `False`):
            Whether to force the (re-)download of the model weights and
            configuration files, overriding the cached versions if they exist.
        resume_download (`bool`, *optional*, defaults to `False`):
            Whether to delete incompletely received files. Will attempt to
            resume the download if such a file exists.
        proxies (`Dict[str, str]`, *optional*):
            A dictionary of proxy servers to use by protocol or endpoint, e.g.,
            `{'http': 'foo.bar:3128', 'http://hostname': 'foo.bar:4012'}`. The
            proxies are used on each request.
        token (`str` or `bool`, *optional*):
            The token to use as HTTP bearer authorization for remote files. If
            `True`, will use the token generated when running `transformers-cli
            login` (stored in `~/.huggingface`).
        cache_dir (`Union[str, os.PathLike]`, *optional*):
            Path to a directory in which a downloaded pretrained model
            configuration should be cached if the standard cache should not be
            used.
        local_files_only(`bool`, *optional*, defaults to `False`):
            Whether to only look at local files (i.e., do not try to download
            the model).
        model_kwargs (`Dict`, *optional*):
            model_kwargs will be passed to the model during initialization

    <Tip>

    Passing `token=True` is required when you want to use a private
    model.

    </Tip>
    """
def push_to_hub_keras(model, repo_id: str, *, config: dict | None = None, commit_message: str = 'Push Keras model using huggingface_hub.', private: bool = False, api_endpoint: str | None = None, token: str | None = None, branch: str | None = None, create_pr: bool | None = None, allow_patterns: List[str] | str | None = None, ignore_patterns: List[str] | str | None = None, delete_patterns: List[str] | str | None = None, log_dir: str | None = None, include_optimizer: bool = False, tags: list | str | None = None, plot_model: bool = True, **model_save_kwargs):
    '''
    Upload model checkpoint to the Hub.

    Use `allow_patterns` and `ignore_patterns` to precisely filter which files should be pushed to the hub. Use
    `delete_patterns` to delete existing remote files in the same commit. See [`upload_folder`] reference for more
    details.

    Args:
        model (`Keras.Model`):
            The [Keras model](`https://www.tensorflow.org/api_docs/python/tf/keras/Model`) you\'d like to push to the
            Hub. The model must be compiled and built.
        repo_id (`str`):
                ID of the repository to push to (example: `"username/my-model"`).
        commit_message (`str`, *optional*, defaults to "Add Keras model"):
            Message to commit while pushing.
        private (`bool`, *optional*, defaults to `False`):
            Whether the repository created should be private.
        api_endpoint (`str`, *optional*):
            The API endpoint to use when pushing the model to the hub.
        token (`str`, *optional*):
            The token to use as HTTP bearer authorization for remote files. If
            not set, will use the token set when logging in with
            `huggingface-cli login` (stored in `~/.huggingface`).
        branch (`str`, *optional*):
            The git branch on which to push the model. This defaults to
            the default branch as specified in your repository, which
            defaults to `"main"`.
        create_pr (`boolean`, *optional*):
            Whether or not to create a Pull Request from `branch` with that commit.
            Defaults to `False`.
        config (`dict`, *optional*):
            Configuration object to be saved alongside the model weights.
        allow_patterns (`List[str]` or `str`, *optional*):
            If provided, only files matching at least one pattern are pushed.
        ignore_patterns (`List[str]` or `str`, *optional*):
            If provided, files matching any of the patterns are not pushed.
        delete_patterns (`List[str]` or `str`, *optional*):
            If provided, remote files matching any of the patterns will be deleted from the repo.
        log_dir (`str`, *optional*):
            TensorBoard logging directory to be pushed. The Hub automatically
            hosts and displays a TensorBoard instance if log files are included
            in the repository.
        include_optimizer (`bool`, *optional*, defaults to `False`):
            Whether or not to include optimizer during serialization.
        tags (Union[`list`, `str`], *optional*):
            List of tags that are related to model or string of a single tag. See example tags
            [here](https://github.com/huggingface/hub-docs/blame/main/modelcard.md).
        plot_model (`bool`, *optional*, defaults to `True`):
            Setting this to `True` will plot the model and put it in the model
            card. Requires graphviz and pydot to be installed.
        model_save_kwargs(`dict`, *optional*):
            model_save_kwargs will be passed to
            [`tf.keras.models.save_model()`](https://www.tensorflow.org/api_docs/python/tf/keras/models/save_model).

    Returns:
        The url of the commit of your model in the given repository.
    '''

class KerasModelHubMixin(ModelHubMixin):
    '''
    Implementation of [`ModelHubMixin`] to provide model Hub upload/download
    capabilities to Keras models.


    ```python
    >>> import tensorflow as tf
    >>> from huggingface_hub import KerasModelHubMixin


    >>> class MyModel(tf.keras.Model, KerasModelHubMixin):
    ...     def __init__(self, **kwargs):
    ...         super().__init__()
    ...         self.config = kwargs.pop("config", None)
    ...         self.dummy_inputs = ...
    ...         self.layer = ...

    ...     def call(self, *args):
    ...         return ...


    >>> # Initialize and compile the model as you normally would
    >>> model = MyModel()
    >>> model.compile(...)
    >>> # Build the graph by training it or passing dummy inputs
    >>> _ = model(model.dummy_inputs)
    >>> # Save model weights to local directory
    >>> model.save_pretrained("my-awesome-model")
    >>> # Push model weights to the Hub
    >>> model.push_to_hub("my-awesome-model")
    >>> # Download and initialize weights from the Hub
    >>> model = MyModel.from_pretrained("username/super-cool-model")
    ```
    '''
