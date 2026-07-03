from .utils.logging import get_logger as get_logger
from _typeshed import Incomplete
from dataclasses import dataclass
from huggingface_hub.utils import yaml_dump as yaml_dump
from typing import Any, Dict, List, Tuple

logger: Incomplete

@dataclass
class EvalResult:
    '''
    Flattened representation of individual evaluation results found in model-index of Model Cards.

    For more information on the model-index spec, see https://github.com/huggingface/hub-docs/blob/main/modelcard.md?plain=1.

    Args:
        task_type (`str`):
            The task identifier. Example: "image-classification".
        dataset_type (`str`):
            The dataset identifier. Example: "common_voice". Use dataset id from https://hf.co/datasets.
        dataset_name (`str`):
            A pretty name for the dataset. Example: "Common Voice (French)".
        metric_type (`str`):
            The metric identifier. Example: "wer". Use metric id from https://hf.co/metrics.
        metric_value (`Any`):
            The metric value. Example: 0.9 or "20.0 ± 1.2".
        task_name (`str`, *optional*):
            A pretty name for the task. Example: "Speech Recognition".
        dataset_config (`str`, *optional*):
            The name of the dataset configuration used in `load_dataset()`.
            Example: fr in `load_dataset("common_voice", "fr")`. See the `datasets` docs for more info:
            https://hf.co/docs/datasets/package_reference/loading_methods#datasets.load_dataset.name
        dataset_split (`str`, *optional*):
            The split used in `load_dataset()`. Example: "test".
        dataset_revision (`str`, *optional*):
            The revision (AKA Git Sha) of the dataset used in `load_dataset()`.
            Example: 5503434ddd753f426f4b38109466949a1217c2bb
        dataset_args (`Dict[str, Any]`, *optional*):
            The arguments passed during `Metric.compute()`. Example for `bleu`: `{"max_order": 4}`
        metric_name (`str`, *optional*):
            A pretty name for the metric. Example: "Test WER".
        metric_config (`str`, *optional*):
            The name of the metric configuration used in `load_metric()`.
            Example: bleurt-large-512 in `load_metric("bleurt", "bleurt-large-512")`.
            See the `datasets` docs for more info: https://huggingface.co/docs/datasets/v2.1.0/en/loading#load-configurations
        metric_args (`Dict[str, Any]`, *optional*):
            The arguments passed during `Metric.compute()`. Example for `bleu`: max_order: 4
        verified (`bool`, *optional*):
            Indicates whether the metrics originate from Hugging Face\'s [evaluation service](https://huggingface.co/spaces/autoevaluate/model-evaluator) or not. Automatically computed by Hugging Face, do not set.
        verify_token (`str`, *optional*):
            A JSON Web Token that is used to verify whether the metrics originate from Hugging Face\'s [evaluation service](https://huggingface.co/spaces/autoevaluate/model-evaluator) or not.
    '''
    task_type: str
    dataset_type: str
    dataset_name: str
    metric_type: str
    metric_value: Any
    task_name: str | None = ...
    dataset_config: str | None = ...
    dataset_split: str | None = ...
    dataset_revision: str | None = ...
    dataset_args: Dict[str, Any] | None = ...
    metric_name: str | None = ...
    metric_config: str | None = ...
    metric_args: Dict[str, Any] | None = ...
    verified: bool | None = ...
    verify_token: str | None = ...
    @property
    def unique_identifier(self) -> tuple:
        """Returns a tuple that uniquely identifies this evaluation."""
    def is_equal_except_value(self, other: EvalResult) -> bool:
        """
        Return True if `self` and `other` describe exactly the same metric but with a
        different value.
        """
    def __init__(self, task_type, dataset_type, dataset_name, metric_type, metric_value, task_name, dataset_config, dataset_split, dataset_revision, dataset_args, metric_name, metric_config, metric_args, verified, verify_token) -> None: ...

@dataclass
class CardData:
    """Structure containing metadata from a RepoCard.

    [`CardData`] is the parent class of [`ModelCardData`] and [`DatasetCardData`].

    Metadata can be exported as a dictionary or YAML. Export can be customized to alter the representation of the data
    (example: flatten evaluation results). `CardData` behaves as a dictionary (can get, pop, set values) but do not
    inherit from `dict` to allow this export step.
    """
    def __init__(self, ignore_metadata_errors: bool = False, **kwargs) -> None: ...
    def to_dict(self) -> Dict[str, Any]:
        """Converts CardData to a dict.

        Returns:
            `dict`: CardData represented as a dictionary ready to be dumped to a YAML
            block for inclusion in a README.md file.
        """
    def to_yaml(self, line_break: Incomplete | None = None) -> str:
        """Dumps CardData to a YAML block for inclusion in a README.md file.

        Args:
            line_break (str, *optional*):
                The line break to use when dumping to yaml.

        Returns:
            `str`: CardData represented as a YAML block.
        """
    def get(self, key: str, default: Any = None) -> Any:
        """Get value for a given metadata key."""
    def pop(self, key: str, default: Any = None) -> Any:
        """Pop value for a given metadata key."""
    def __getitem__(self, key: str) -> Any:
        """Get value for a given metadata key."""
    def __setitem__(self, key: str, value: Any) -> None:
        """Set value for a given metadata key."""
    def __contains__(self, key: str) -> bool:
        """Check if a given metadata key is set."""

class ModelCardData(CardData):
    '''Model Card Metadata that is used by Hugging Face Hub when included at the top of your README.md

    Args:
        language (`Union[str, List[str]]`, *optional*):
            Language of model\'s training data or metadata. It must be an ISO 639-1, 639-2 or
            639-3 code (two/three letters), or a special value like "code", "multilingual". Defaults to `None`.
        license (`str`, *optional*):
            License of this model. Example: apache-2.0 or any license from
            https://huggingface.co/docs/hub/repositories-licenses. Defaults to None.
        library_name (`str`, *optional*):
            Name of library used by this model. Example: keras or any library from
            https://github.com/huggingface/hub-docs/blob/main/js/src/lib/interfaces/Libraries.ts.
            Defaults to None.
        tags (`List[str]`, *optional*):
            List of tags to add to your model that can be used when filtering on the Hugging
            Face Hub. Defaults to None.
        datasets (`List[str]`, *optional*):
            List of datasets that were used to train this model. Should be a dataset ID
            found on https://hf.co/datasets. Defaults to None.
        metrics (`List[str]`, *optional*):
            List of metrics used to evaluate this model. Should be a metric name that can be found
            at https://hf.co/metrics. Example: \'accuracy\'. Defaults to None.
        eval_results (`Union[List[EvalResult], EvalResult]`, *optional*):
            List of `huggingface_hub.EvalResult` that define evaluation results of the model. If provided,
            `model_name` is used to as a name on PapersWithCode\'s leaderboards. Defaults to `None`.
        model_name (`str`, *optional*):
            A name for this model. It is used along with
            `eval_results` to construct the `model-index` within the card\'s metadata. The name
            you supply here is what will be used on PapersWithCode\'s leaderboards. If None is provided
            then the repo name is used as a default. Defaults to None.
        ignore_metadata_errors (`str`):
            If True, errors while parsing the metadata section will be ignored. Some information might be lost during
            the process. Use it at your own risk.
        kwargs (`dict`, *optional*):
            Additional metadata that will be added to the model card. Defaults to None.

    Example:
        ```python
        >>> from huggingface_hub import ModelCardData
        >>> card_data = ModelCardData(
        ...     language="en",
        ...     license="mit",
        ...     library_name="timm",
        ...     tags=[\'image-classification\', \'resnet\'],
        ... )
        >>> card_data.to_dict()
        {\'language\': \'en\', \'license\': \'mit\', \'library_name\': \'timm\', \'tags\': [\'image-classification\', \'resnet\']}

        ```
    '''
    language: Incomplete
    license: Incomplete
    library_name: Incomplete
    tags: Incomplete
    datasets: Incomplete
    metrics: Incomplete
    eval_results: Incomplete
    model_name: Incomplete
    def __init__(self, *, language: str | List[str] | None = None, license: str | None = None, library_name: str | None = None, tags: List[str] | None = None, datasets: List[str] | None = None, metrics: List[str] | None = None, eval_results: List[EvalResult] | None = None, model_name: str | None = None, ignore_metadata_errors: bool = False, **kwargs) -> None: ...

class DatasetCardData(CardData):
    '''Dataset Card Metadata that is used by Hugging Face Hub when included at the top of your README.md

    Args:
        language (`List[str]`, *optional*):
            Language of dataset\'s data or metadata. It must be an ISO 639-1, 639-2 or
            639-3 code (two/three letters), or a special value like "code", "multilingual".
        license (`Union[str, List[str]]`, *optional*):
            License(s) of this dataset. Example: apache-2.0 or any license from
            https://huggingface.co/docs/hub/repositories-licenses.
        annotations_creators (`Union[str, List[str]]`, *optional*):
            How the annotations for the dataset were created.
            Options are: \'found\', \'crowdsourced\', \'expert-generated\', \'machine-generated\', \'no-annotation\', \'other\'.
        language_creators (`Union[str, List[str]]`, *optional*):
            How the text-based data in the dataset was created.
            Options are: \'found\', \'crowdsourced\', \'expert-generated\', \'machine-generated\', \'other\'
        multilinguality (`Union[str, List[str]]`, *optional*):
            Whether the dataset is multilingual.
            Options are: \'monolingual\', \'multilingual\', \'translation\', \'other\'.
        size_categories (`Union[str, List[str]]`, *optional*):
            The number of examples in the dataset. Options are: \'n<1K\', \'1K<n<10K\', \'10K<n<100K\',
            \'100K<n<1M\', \'1M<n<10M\', \'10M<n<100M\', \'100M<n<1B\', \'1B<n<10B\', \'10B<n<100B\', \'100B<n<1T\', \'n>1T\', and \'other\'.
        source_datasets (`List[str]]`, *optional*):
            Indicates whether the dataset is an original dataset or extended from another existing dataset.
            Options are: \'original\' and \'extended\'.
        task_categories (`Union[str, List[str]]`, *optional*):
            What categories of task does the dataset support?
        task_ids (`Union[str, List[str]]`, *optional*):
            What specific tasks does the dataset support?
        paperswithcode_id (`str`, *optional*):
            ID of the dataset on PapersWithCode.
        pretty_name (`str`, *optional*):
            A more human-readable name for the dataset. (ex. "Cats vs. Dogs")
        train_eval_index (`Dict`, *optional*):
            A dictionary that describes the necessary spec for doing evaluation on the Hub.
            If not provided, it will be gathered from the \'train-eval-index\' key of the kwargs.
        config_names (`Union[str, List[str]]`, *optional*):
            A list of the available dataset configs for the dataset.
    '''
    annotations_creators: Incomplete
    language_creators: Incomplete
    language: Incomplete
    license: Incomplete
    multilinguality: Incomplete
    size_categories: Incomplete
    source_datasets: Incomplete
    task_categories: Incomplete
    task_ids: Incomplete
    paperswithcode_id: Incomplete
    pretty_name: Incomplete
    config_names: Incomplete
    train_eval_index: Incomplete
    def __init__(self, *, language: str | List[str] | None = None, license: str | List[str] | None = None, annotations_creators: str | List[str] | None = None, language_creators: str | List[str] | None = None, multilinguality: str | List[str] | None = None, size_categories: str | List[str] | None = None, source_datasets: List[str] | None = None, task_categories: str | List[str] | None = None, task_ids: str | List[str] | None = None, paperswithcode_id: str | None = None, pretty_name: str | None = None, train_eval_index: Dict | None = None, config_names: str | List[str] | None = None, ignore_metadata_errors: bool = False, **kwargs) -> None: ...

class SpaceCardData(CardData):
    '''Space Card Metadata that is used by Hugging Face Hub when included at the top of your README.md

    To get an exhaustive reference of Spaces configuration, please visit https://huggingface.co/docs/hub/spaces-config-reference#spaces-configuration-reference.

    Args:
        title (`str`, *optional*)
            Title of the Space.
        sdk (`str`, *optional*)
            SDK of the Space (one of `gradio`, `streamlit`, `docker`, or `static`).
        sdk_version (`str`, *optional*)
            Version of the used SDK (if Gradio/Streamlit sdk).
        python_version (`str`, *optional*)
            Python version used in the Space (if Gradio/Streamlit sdk).
        app_file (`str`, *optional*)
            Path to your main application file (which contains either gradio or streamlit Python code, or static html code).
            Path is relative to the root of the repository.
        app_port (`str`, *optional*)
            Port on which your application is running. Used only if sdk is `docker`.
        license (`str`, *optional*)
            License of this model. Example: apache-2.0 or any license from
            https://huggingface.co/docs/hub/repositories-licenses.
        duplicated_from (`str`, *optional*)
            ID of the original Space if this is a duplicated Space.
        models (List[`str`], *optional*)
            List of models related to this Space. Should be a dataset ID found on https://hf.co/models.
        datasets (`List[str]`, *optional*)
            List of datasets related to this Space. Should be a dataset ID found on https://hf.co/datasets.
        tags (`List[str]`, *optional*)
            List of tags to add to your Space that can be used when filtering on the Hub.
        ignore_metadata_errors (`str`):
            If True, errors while parsing the metadata section will be ignored. Some information might be lost during
            the process. Use it at your own risk.
        kwargs (`dict`, *optional*):
            Additional metadata that will be added to the space card.

    Example:
        ```python
        >>> from huggingface_hub import SpaceCardData
        >>> card_data = SpaceCardData(
        ...     title="Dreambooth Training",
        ...     license="mit",
        ...     sdk="gradio",
        ...     duplicated_from="multimodalart/dreambooth-training"
        ... )
        >>> card_data.to_dict()
        {\'title\': \'Dreambooth Training\', \'sdk\': \'gradio\', \'license\': \'mit\', \'duplicated_from\': \'multimodalart/dreambooth-training\'}
        ```
    '''
    title: Incomplete
    sdk: Incomplete
    sdk_version: Incomplete
    python_version: Incomplete
    app_file: Incomplete
    app_port: Incomplete
    license: Incomplete
    duplicated_from: Incomplete
    models: Incomplete
    datasets: Incomplete
    tags: Incomplete
    def __init__(self, *, title: str | None = None, sdk: str | None = None, sdk_version: str | None = None, python_version: str | None = None, app_file: str | None = None, app_port: int | None = None, license: str | None = None, duplicated_from: str | None = None, models: List[str] | None = None, datasets: List[str] | None = None, tags: List[str] | None = None, ignore_metadata_errors: bool = False, **kwargs) -> None: ...

def model_index_to_eval_results(model_index: List[Dict[str, Any]]) -> Tuple[str, List[EvalResult]]:
    '''Takes in a model index and returns the model name and a list of `huggingface_hub.EvalResult` objects.

    A detailed spec of the model index can be found here:
    https://github.com/huggingface/hub-docs/blob/main/modelcard.md?plain=1

    Args:
        model_index (`List[Dict[str, Any]]`):
            A model index data structure, likely coming from a README.md file on the
            Hugging Face Hub.

    Returns:
        model_name (`str`):
            The name of the model as found in the model index. This is used as the
            identifier for the model on leaderboards like PapersWithCode.
        eval_results (`List[EvalResult]`):
            A list of `huggingface_hub.EvalResult` objects containing the metrics
            reported in the provided model_index.

    Example:
        ```python
        >>> from huggingface_hub.repocard_data import model_index_to_eval_results
        >>> # Define a minimal model index
        >>> model_index = [
        ...     {
        ...         "name": "my-cool-model",
        ...         "results": [
        ...             {
        ...                 "task": {
        ...                     "type": "image-classification"
        ...                 },
        ...                 "dataset": {
        ...                     "type": "beans",
        ...                     "name": "Beans"
        ...                 },
        ...                 "metrics": [
        ...                     {
        ...                         "type": "accuracy",
        ...                         "value": 0.9
        ...                     }
        ...                 ]
        ...             }
        ...         ]
        ...     }
        ... ]
        >>> model_name, eval_results = model_index_to_eval_results(model_index)
        >>> model_name
        \'my-cool-model\'
        >>> eval_results[0].task_type
        \'image-classification\'
        >>> eval_results[0].metric_type
        \'accuracy\'

        ```
    '''
def eval_results_to_model_index(model_name: str, eval_results: List[EvalResult]) -> List[Dict[str, Any]]:
    '''Takes in given model name and list of `huggingface_hub.EvalResult` and returns a
    valid model-index that will be compatible with the format expected by the
    Hugging Face Hub.

    Args:
        model_name (`str`):
            Name of the model (ex. "my-cool-model"). This is used as the identifier
            for the model on leaderboards like PapersWithCode.
        eval_results (`List[EvalResult]`):
            List of `huggingface_hub.EvalResult` objects containing the metrics to be
            reported in the model-index.

    Returns:
        model_index (`List[Dict[str, Any]]`): The eval_results converted to a model-index.

    Example:
        ```python
        >>> from huggingface_hub.repocard_data import eval_results_to_model_index, EvalResult
        >>> # Define minimal eval_results
        >>> eval_results = [
        ...     EvalResult(
        ...         task_type="image-classification",  # Required
        ...         dataset_type="beans",  # Required
        ...         dataset_name="Beans",  # Required
        ...         metric_type="accuracy",  # Required
        ...         metric_value=0.9,  # Required
        ...     )
        ... ]
        >>> eval_results_to_model_index("my-cool-model", eval_results)
        [{\'name\': \'my-cool-model\', \'results\': [{\'task\': {\'type\': \'image-classification\'}, \'dataset\': {\'name\': \'Beans\', \'type\': \'beans\'}, \'metrics\': [{\'type\': \'accuracy\', \'value\': 0.9}]}]}]

        ```
    '''
