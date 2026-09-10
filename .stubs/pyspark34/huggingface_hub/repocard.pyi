from .constants import REPOCARD_NAME as REPOCARD_NAME
from .utils import EntryNotFoundError as EntryNotFoundError, SoftTemporaryDirectory as SoftTemporaryDirectory, validate_hf_hub_args as validate_hf_hub_args
from .utils.logging import get_logger as get_logger
from _typeshed import Incomplete
from huggingface_hub.file_download import hf_hub_download as hf_hub_download
from huggingface_hub.hf_api import upload_file as upload_file
from huggingface_hub.repocard_data import CardData as CardData, DatasetCardData as DatasetCardData, EvalResult as EvalResult, ModelCardData as ModelCardData, SpaceCardData as SpaceCardData, eval_results_to_model_index as eval_results_to_model_index, model_index_to_eval_results as model_index_to_eval_results
from huggingface_hub.utils import get_session as get_session, is_jinja_available as is_jinja_available, yaml_dump as yaml_dump
from pathlib import Path
from typing import Any, Dict

TEMPLATE_MODELCARD_PATH: Incomplete
TEMPLATE_DATASETCARD_PATH: Incomplete
REGEX_YAML_BLOCK: Incomplete
logger: Incomplete

class RepoCard:
    card_data_class = CardData
    default_template_path = TEMPLATE_MODELCARD_PATH
    repo_type: str
    ignore_metadata_errors: Incomplete
    def __init__(self, content: str, ignore_metadata_errors: bool = False) -> None:
        """Initialize a RepoCard from string content. The content should be a
        Markdown file with a YAML block at the beginning and a Markdown body.

        Args:
            content (`str`): The content of the Markdown file.

        Example:
            ```python
            >>> from huggingface_hub.repocard import RepoCard
            >>> text = '''
            ... ---
            ... language: en
            ... license: mit
            ... ---
            ...
            ... # My repo
            ... '''
            >>> card = RepoCard(text)
            >>> card.data.to_dict()
            {'language': 'en', 'license': 'mit'}
            >>> card.text
            '\\n# My repo\\n'

            ```
        <Tip>
        Raises the following error:

            - [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError)
              when the content of the repo card metadata is not a dictionary.

        </Tip>
        """
    @property
    def content(self):
        """The content of the RepoCard, including the YAML block and the Markdown body."""
    text: Incomplete
    data: Incomplete
    @content.setter
    def content(self, content: str):
        """Set the content of the RepoCard."""
    def save(self, filepath: Path | str):
        '''Save a RepoCard to a file.

        Args:
            filepath (`Union[Path, str]`): Filepath to the markdown file to save.

        Example:
            ```python
            >>> from huggingface_hub.repocard import RepoCard
            >>> card = RepoCard("---\\nlanguage: en\\n---\\n# This is a test repo card")
            >>> card.save("/tmp/test.md")

            ```
        '''
    @classmethod
    def load(cls, repo_id_or_path: str | Path, repo_type: str | None = None, token: str | None = None, ignore_metadata_errors: bool = False):
        '''Initialize a RepoCard from a Hugging Face Hub repo\'s README.md or a local filepath.

        Args:
            repo_id_or_path (`Union[str, Path]`):
                The repo ID associated with a Hugging Face Hub repo or a local filepath.
            repo_type (`str`, *optional*):
                The type of Hugging Face repo to push to. Defaults to None, which will use use "model". Other options
                are "dataset" and "space". Not used when loading from a local filepath. If this is called from a child
                class, the default value will be the child class\'s `repo_type`.
            token (`str`, *optional*):
                Authentication token, obtained with `huggingface_hub.HfApi.login` method. Will default to the stored token.
            ignore_metadata_errors (`str`):
                If True, errors while parsing the metadata section will be ignored. Some information might be lost during
                the process. Use it at your own risk.

        Returns:
            [`huggingface_hub.repocard.RepoCard`]: The RepoCard (or subclass) initialized from the repo\'s
                README.md file or filepath.

        Example:
            ```python
            >>> from huggingface_hub.repocard import RepoCard
            >>> card = RepoCard.load("nateraw/food")
            >>> assert card.data.tags == ["generated_from_trainer", "image-classification", "pytorch"]

            ```
        '''
    def validate(self, repo_type: str | None = None):
        '''Validates card against Hugging Face Hub\'s card validation logic.
        Using this function requires access to the internet, so it is only called
        internally by [`huggingface_hub.repocard.RepoCard.push_to_hub`].

        Args:
            repo_type (`str`, *optional*, defaults to "model"):
                The type of Hugging Face repo to push to. Options are "model", "dataset", and "space".
                If this function is called from a child class, the default will be the child class\'s `repo_type`.

        <Tip>
        Raises the following errors:

            - [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError)
              if the card fails validation checks.
            - [`HTTPError`](https://requests.readthedocs.io/en/latest/api/#requests.HTTPError)
              if the request to the Hub API fails for any other reason.

        </Tip>
        '''
    def push_to_hub(self, repo_id: str, token: str | None = None, repo_type: str | None = None, commit_message: str | None = None, commit_description: str | None = None, revision: str | None = None, create_pr: bool | None = None, parent_commit: str | None = None):
        '''Push a RepoCard to a Hugging Face Hub repo.

        Args:
            repo_id (`str`):
                The repo ID of the Hugging Face Hub repo to push to. Example: "nateraw/food".
            token (`str`, *optional*):
                Authentication token, obtained with `huggingface_hub.HfApi.login` method. Will default to
                the stored token.
            repo_type (`str`, *optional*, defaults to "model"):
                The type of Hugging Face repo to push to. Options are "model", "dataset", and "space". If this
                function is called by a child class, it will default to the child class\'s `repo_type`.
            commit_message (`str`, *optional*):
                The summary / title / first line of the generated commit.
            commit_description (`str`, *optional*)
                The description of the generated commit.
            revision (`str`, *optional*):
                The git revision to commit from. Defaults to the head of the `"main"` branch.
            create_pr (`bool`, *optional*):
                Whether or not to create a Pull Request with this commit. Defaults to `False`.
            parent_commit (`str`, *optional*):
                The OID / SHA of the parent commit, as a hexadecimal string. Shorthands (7 first characters) are also supported.
                If specified and `create_pr` is `False`, the commit will fail if `revision` does not point to `parent_commit`.
                If specified and `create_pr` is `True`, the pull request will be created from `parent_commit`.
                Specifying `parent_commit` ensures the repo has not changed before committing the changes, and can be
                especially useful if the repo is updated / committed to concurrently.
        Returns:
            `str`: URL of the commit which updated the card metadata.
        '''
    @classmethod
    def from_template(cls, card_data: CardData, template_path: str | None = None, **template_kwargs):
        """Initialize a RepoCard from a template. By default, it uses the default template.

        Templates are Jinja2 templates that can be customized by passing keyword arguments.

        Args:
            card_data (`huggingface_hub.CardData`):
                A huggingface_hub.CardData instance containing the metadata you want to include in the YAML
                header of the repo card on the Hugging Face Hub.
            template_path (`str`, *optional*):
                A path to a markdown file with optional Jinja template variables that can be filled
                in with `template_kwargs`. Defaults to the default template.

        Returns:
            [`huggingface_hub.repocard.RepoCard`]: A RepoCard instance with the specified card data and content from the
            template.
        """

class ModelCard(RepoCard):
    card_data_class = ModelCardData
    default_template_path = TEMPLATE_MODELCARD_PATH
    repo_type: str
    @classmethod
    def from_template(cls, card_data: ModelCardData, template_path: str | None = None, **template_kwargs):
        """Initialize a ModelCard from a template. By default, it uses the default template, which can be found here:
        https://github.com/huggingface/huggingface_hub/blob/main/src/huggingface_hub/templates/modelcard_template.md

        Templates are Jinja2 templates that can be customized by passing keyword arguments.

        Args:
            card_data (`huggingface_hub.ModelCardData`):
                A huggingface_hub.ModelCardData instance containing the metadata you want to include in the YAML
                header of the model card on the Hugging Face Hub.
            template_path (`str`, *optional*):
                A path to a markdown file with optional Jinja template variables that can be filled
                in with `template_kwargs`. Defaults to the default template.

        Returns:
            [`huggingface_hub.ModelCard`]: A ModelCard instance with the specified card data and content from the
            template.

        Example:
            ```python
            >>> from huggingface_hub import ModelCard, ModelCardData, EvalResult

            >>> # Using the Default Template
            >>> card_data = ModelCardData(
            ...     language='en',
            ...     license='mit',
            ...     library_name='timm',
            ...     tags=['image-classification', 'resnet'],
            ...     datasets=['beans'],
            ...     metrics=['accuracy'],
            ... )
            >>> card = ModelCard.from_template(
            ...     card_data,
            ...     model_description='This model does x + y...'
            ... )

            >>> # Including Evaluation Results
            >>> card_data = ModelCardData(
            ...     language='en',
            ...     tags=['image-classification', 'resnet'],
            ...     eval_results=[
            ...         EvalResult(
            ...             task_type='image-classification',
            ...             dataset_type='beans',
            ...             dataset_name='Beans',
            ...             metric_type='accuracy',
            ...             metric_value=0.9,
            ...         ),
            ...     ],
            ...     model_name='my-cool-model',
            ... )
            >>> card = ModelCard.from_template(card_data)

            >>> # Using a Custom Template
            >>> card_data = ModelCardData(
            ...     language='en',
            ...     tags=['image-classification', 'resnet']
            ... )
            >>> card = ModelCard.from_template(
            ...     card_data=card_data,
            ...     template_path='./src/huggingface_hub/templates/modelcard_template.md',
            ...     custom_template_var='custom value',  # will be replaced in template if it exists
            ... )

            ```
        """

class DatasetCard(RepoCard):
    card_data_class = DatasetCardData
    default_template_path = TEMPLATE_DATASETCARD_PATH
    repo_type: str
    @classmethod
    def from_template(cls, card_data: DatasetCardData, template_path: str | None = None, **template_kwargs):
        """Initialize a DatasetCard from a template. By default, it uses the default template, which can be found here:
        https://github.com/huggingface/huggingface_hub/blob/main/src/huggingface_hub/templates/datasetcard_template.md

        Templates are Jinja2 templates that can be customized by passing keyword arguments.

        Args:
            card_data (`huggingface_hub.DatasetCardData`):
                A huggingface_hub.DatasetCardData instance containing the metadata you want to include in the YAML
                header of the dataset card on the Hugging Face Hub.
            template_path (`str`, *optional*):
                A path to a markdown file with optional Jinja template variables that can be filled
                in with `template_kwargs`. Defaults to the default template.

        Returns:
            [`huggingface_hub.DatasetCard`]: A DatasetCard instance with the specified card data and content from the
            template.

        Example:
            ```python
            >>> from huggingface_hub import DatasetCard, DatasetCardData

            >>> # Using the Default Template
            >>> card_data = DatasetCardData(
            ...     language='en',
            ...     license='mit',
            ...     annotations_creators='crowdsourced',
            ...     task_categories=['text-classification'],
            ...     task_ids=['sentiment-classification', 'text-scoring'],
            ...     multilinguality='monolingual',
            ...     pretty_name='My Text Classification Dataset',
            ... )
            >>> card = DatasetCard.from_template(
            ...     card_data,
            ...     pretty_name=card_data.pretty_name,
            ... )

            >>> # Using a Custom Template
            >>> card_data = DatasetCardData(
            ...     language='en',
            ...     license='mit',
            ... )
            >>> card = DatasetCard.from_template(
            ...     card_data=card_data,
            ...     template_path='./src/huggingface_hub/templates/datasetcard_template.md',
            ...     custom_template_var='custom value',  # will be replaced in template if it exists
            ... )

            ```
        """

class SpaceCard(RepoCard):
    card_data_class = SpaceCardData
    default_template_path = TEMPLATE_MODELCARD_PATH
    repo_type: str

def metadata_load(local_path: str | Path) -> Dict | None: ...
def metadata_save(local_path: str | Path, data: Dict) -> None:
    '''
    Save the metadata dict in the upper YAML part Trying to preserve newlines as
    in the existing file. Docs about open() with newline="" parameter:
    https://docs.python.org/3/library/functions.html?highlight=open#open Does
    not work with "^M" linebreaks, which are replaced by 

    '''
def metadata_eval_result(*, model_pretty_name: str, task_pretty_name: str, task_id: str, metrics_pretty_name: str, metrics_id: str, metrics_value: Any, dataset_pretty_name: str, dataset_id: str, metrics_config: str | None = None, metrics_verified: bool = False, dataset_config: str | None = None, dataset_split: str | None = None, dataset_revision: str | None = None, metrics_verification_token: str | None = None) -> Dict:
    '''
    Creates a metadata dict with the result from a model evaluated on a dataset.

    Args:
        model_pretty_name (`str`):
            The name of the model in natural language.
        task_pretty_name (`str`):
            The name of a task in natural language.
        task_id (`str`):
            Example: automatic-speech-recognition. A task id.
        metrics_pretty_name (`str`):
            A name for the metric in natural language. Example: Test WER.
        metrics_id (`str`):
            Example: wer. A metric id from https://hf.co/metrics.
        metrics_value (`Any`):
            The value from the metric. Example: 20.0 or "20.0 ± 1.2".
        dataset_pretty_name (`str`):
            The name of the dataset in natural language.
        dataset_id (`str`):
            Example: common_voice. A dataset id from https://hf.co/datasets.
        metrics_config (`str`, *optional*):
            The name of the metric configuration used in `load_metric()`.
            Example: bleurt-large-512 in `load_metric("bleurt", "bleurt-large-512")`.
        metrics_verified (`bool`, *optional*, defaults to `False`):
            Indicates whether the metrics originate from Hugging Face\'s [evaluation service](https://huggingface.co/spaces/autoevaluate/model-evaluator) or not. Automatically computed by Hugging Face, do not set.
        dataset_config (`str`, *optional*):
            Example: fr. The name of the dataset configuration used in `load_dataset()`.
        dataset_split (`str`, *optional*):
            Example: test. The name of the dataset split used in `load_dataset()`.
        dataset_revision (`str`, *optional*):
            Example: 5503434ddd753f426f4b38109466949a1217c2bb. The name of the dataset dataset revision
            used in `load_dataset()`.
        metrics_verification_token (`bool`, *optional*):
            A JSON Web Token that is used to verify whether the metrics originate from Hugging Face\'s [evaluation service](https://huggingface.co/spaces/autoevaluate/model-evaluator) or not.

    Returns:
        `dict`: a metadata dict with the result from a model evaluated on a dataset.

    Example:
        ```python
        >>> from huggingface_hub import metadata_eval_result
        >>> results = metadata_eval_result(
        ...         model_pretty_name="RoBERTa fine-tuned on ReactionGIF",
        ...         task_pretty_name="Text Classification",
        ...         task_id="text-classification",
        ...         metrics_pretty_name="Accuracy",
        ...         metrics_id="accuracy",
        ...         metrics_value=0.2662102282047272,
        ...         dataset_pretty_name="ReactionJPEG",
        ...         dataset_id="julien-c/reactionjpeg",
        ...         dataset_config="default",
        ...         dataset_split="test",
        ... )
        >>> results == {
        ...     \'model-index\': [
        ...         {
        ...             \'name\': \'RoBERTa fine-tuned on ReactionGIF\',
        ...             \'results\': [
        ...                 {
        ...                     \'task\': {
        ...                         \'type\': \'text-classification\',
        ...                         \'name\': \'Text Classification\'
        ...                     },
        ...                     \'dataset\': {
        ...                         \'name\': \'ReactionJPEG\',
        ...                         \'type\': \'julien-c/reactionjpeg\',
        ...                         \'config\': \'default\',
        ...                         \'split\': \'test\'
        ...                     },
        ...                     \'metrics\': [
        ...                         {
        ...                             \'type\': \'accuracy\',
        ...                             \'value\': 0.2662102282047272,
        ...                             \'name\': \'Accuracy\',
        ...                             \'verified\': False
        ...                         }
        ...                     ]
        ...                 }
        ...             ]
        ...         }
        ...     ]
        ... }
        True

        ```
    '''
def metadata_update(repo_id: str, metadata: Dict, *, repo_type: str | None = None, overwrite: bool = False, token: str | None = None, commit_message: str | None = None, commit_description: str | None = None, revision: str | None = None, create_pr: bool = False, parent_commit: str | None = None) -> str:
    '''
    Updates the metadata in the README.md of a repository on the Hugging Face Hub.
    If the README.md file doesn\'t exist yet, a new one is created with metadata and an
    the default ModelCard or DatasetCard template. For `space` repo, an error is thrown
    as a Space cannot exist without a `README.md` file.

    Args:
        repo_id (`str`):
            The name of the repository.
        metadata (`dict`):
            A dictionary containing the metadata to be updated.
        repo_type (`str`, *optional*):
            Set to `"dataset"` or `"space"` if updating to a dataset or space,
            `None` or `"model"` if updating to a model. Default is `None`.
        overwrite (`bool`, *optional*, defaults to `False`):
            If set to `True` an existing field can be overwritten, otherwise
            attempting to overwrite an existing field will cause an error.
        token (`str`, *optional*):
            The Hugging Face authentication token.
        commit_message (`str`, *optional*):
            The summary / title / first line of the generated commit. Defaults to
            `f"Update metadata with huggingface_hub"`
        commit_description (`str` *optional*)
            The description of the generated commit
        revision (`str`, *optional*):
            The git revision to commit from. Defaults to the head of the
            `"main"` branch.
        create_pr (`boolean`, *optional*):
            Whether or not to create a Pull Request from `revision` with that commit.
            Defaults to `False`.
        parent_commit (`str`, *optional*):
            The OID / SHA of the parent commit, as a hexadecimal string. Shorthands (7 first characters) are also supported.
            If specified and `create_pr` is `False`, the commit will fail if `revision` does not point to `parent_commit`.
            If specified and `create_pr` is `True`, the pull request will be created from `parent_commit`.
            Specifying `parent_commit` ensures the repo has not changed before committing the changes, and can be
            especially useful if the repo is updated / committed to concurrently.
    Returns:
        `str`: URL of the commit which updated the card metadata.

    Example:
        ```python
        >>> from huggingface_hub import metadata_update
        >>> metadata = {\'model-index\': [{\'name\': \'RoBERTa fine-tuned on ReactionGIF\',
        ...             \'results\': [{\'dataset\': {\'name\': \'ReactionGIF\',
        ...                                      \'type\': \'julien-c/reactiongif\'},
        ...                           \'metrics\': [{\'name\': \'Recall\',
        ...                                        \'type\': \'recall\',
        ...                                        \'value\': 0.7762102282047272}],
        ...                          \'task\': {\'name\': \'Text Classification\',
        ...                                   \'type\': \'text-classification\'}}]}]}
        >>> url = metadata_update("hf-internal-testing/reactiongif-roberta-card", metadata)

        ```
    '''
