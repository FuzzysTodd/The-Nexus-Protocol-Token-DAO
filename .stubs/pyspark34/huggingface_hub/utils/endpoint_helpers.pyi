from ..hf_api import ModelInfo as ModelInfo
from dataclasses import dataclass
from typing import List

@dataclass
class DatasetFilter:
    '''
    A class that converts human-readable dataset search parameters into ones
    compatible with the REST API. For all parameters capitalization does not
    matter.

    Args:
        author (`str`, *optional*):
            A string or list of strings that can be used to identify datasets on
            the Hub by the original uploader (author or organization), such as
            `facebook` or `huggingface`.
        benchmark (`str` or `List`, *optional*):
            A string or list of strings that can be used to identify datasets on
            the Hub by their official benchmark.
        dataset_name (`str`, *optional*):
            A string or list of strings that can be used to identify datasets on
            the Hub by its name, such as `SQAC` or `wikineural`
        language_creators (`str` or `List`, *optional*):
            A string or list of strings that can be used to identify datasets on
            the Hub with how the data was curated, such as `crowdsourced` or
            `machine_generated`.
        language (`str` or `List`, *optional*):
            A string or list of strings representing a two-character language to
            filter datasets by on the Hub.
        multilinguality (`str` or `List`, *optional*):
            A string or list of strings representing a filter for datasets that
            contain multiple languages.
        size_categories (`str` or `List`, *optional*):
            A string or list of strings that can be used to identify datasets on
            the Hub by the size of the dataset such as `100K<n<1M` or
            `1M<n<10M`.
        task_categories (`str` or `List`, *optional*):
            A string or list of strings that can be used to identify datasets on
            the Hub by the designed task, such as `audio_classification` or
            `named_entity_recognition`.
        task_ids (`str` or `List`, *optional*):
            A string or list of strings that can be used to identify datasets on
            the Hub by the specific task such as `speech_emotion_recognition` or
            `paraphrase`.

    Examples:

    ```py
    >>> from huggingface_hub import DatasetFilter

    >>> # Using author
    >>> new_filter = DatasetFilter(author="facebook")

    >>> # Using benchmark
    >>> new_filter = DatasetFilter(benchmark="raft")

    >>> # Using dataset_name
    >>> new_filter = DatasetFilter(dataset_name="wikineural")

    >>> # Using language_creator
    >>> new_filter = DatasetFilter(language_creator="crowdsourced")

    >>> # Using language
    >>> new_filter = DatasetFilter(language="en")

    >>> # Using multilinguality
    >>> new_filter = DatasetFilter(multilinguality="multilingual")

    >>> # Using size_categories
    >>> new_filter = DatasetFilter(size_categories="100K<n<1M")

    >>> # Using task_categories
    >>> new_filter = DatasetFilter(task_categories="audio_classification")

    >>> # Using task_ids
    >>> new_filter = DatasetFilter(task_ids="paraphrase")
    ```
    '''
    author: str | None = ...
    benchmark: str | List[str] | None = ...
    dataset_name: str | None = ...
    language_creators: str | List[str] | None = ...
    language: str | List[str] | None = ...
    multilinguality: str | List[str] | None = ...
    size_categories: str | List[str] | None = ...
    task_categories: str | List[str] | None = ...
    task_ids: str | List[str] | None = ...
    def __init__(self, author, benchmark, dataset_name, language_creators, language, multilinguality, size_categories, task_categories, task_ids) -> None: ...

@dataclass
class ModelFilter:
    '''
    A class that converts human-readable model search parameters into ones
    compatible with the REST API. For all parameters capitalization does not
    matter.

    Args:
        author (`str`, *optional*):
            A string that can be used to identify models on the Hub by the
            original uploader (author or organization), such as `facebook` or
            `huggingface`.
        library (`str` or `List`, *optional*):
            A string or list of strings of foundational libraries models were
            originally trained from, such as pytorch, tensorflow, or allennlp.
        language (`str` or `List`, *optional*):
            A string or list of strings of languages, both by name and country
            code, such as "en" or "English"
        model_name (`str`, *optional*):
            A string that contain complete or partial names for models on the
            Hub, such as "bert" or "bert-base-cased"
        task (`str` or `List`, *optional*):
            A string or list of strings of tasks models were designed for, such
            as: "fill-mask" or "automatic-speech-recognition"
        tags (`str` or `List`, *optional*):
            A string tag or a list of tags to filter models on the Hub by, such
            as `text-generation` or `spacy`.
        trained_dataset (`str` or `List`, *optional*):
            A string tag or a list of string tags of the trained dataset for a
            model on the Hub.


    ```python
    >>> from huggingface_hub import ModelFilter

    >>> # For the author_or_organization
    >>> new_filter = ModelFilter(author_or_organization="facebook")

    >>> # For the library
    >>> new_filter = ModelFilter(library="pytorch")

    >>> # For the language
    >>> new_filter = ModelFilter(language="french")

    >>> # For the model_name
    >>> new_filter = ModelFilter(model_name="bert")

    >>> # For the task
    >>> new_filter = ModelFilter(task="text-classification")

    >>> # Retrieving tags using the `HfApi.get_model_tags` method
    >>> from huggingface_hub import HfApi

    >>> api = HfApi()
    # To list model tags

    >>> api.get_model_tags()
    # To list dataset tags

    >>> api.get_dataset_tags()
    >>> new_filter = ModelFilter(tags="benchmark:raft")

    >>> # Related to the dataset
    >>> new_filter = ModelFilter(trained_dataset="common_voice")
    ```
    '''
    author: str | None = ...
    library: str | List[str] | None = ...
    language: str | List[str] | None = ...
    model_name: str | None = ...
    task: str | List[str] | None = ...
    trained_dataset: str | List[str] | None = ...
    tags: str | List[str] | None = ...
    def __init__(self, author, library, language, model_name, task, trained_dataset, tags) -> None: ...

class AttributeDictionary(dict):
    '''
    `dict` subclass that also provides access to keys as attributes

    If a key starts with a number, it will exist in the dictionary but not as an
    attribute

    Example:

    ```python
    >>> d = AttributeDictionary()
    >>> d["test"] = "a"
    >>> print(d.test)  # prints "a"
    ```

    '''
    def __getattr__(self, k): ...
    def __setattr__(self, k, v) -> None: ...
    def __delattr__(self, k) -> None: ...
    def __dir__(self): ...

class GeneralTags(AttributeDictionary):
    '''
    A namespace object holding all tags, filtered by `keys` If a tag starts with
    a number, it will only exist in the dictionary

    Example:
    ```python
    >>> a.b["1a"]  # will work
    >>> a["b"]["1a"]  # will work
    >>> # a.b.1a # will not work
    ```

    Args:
        tag_dictionary (`dict`):
            A dictionary of tags returned from the /api/***-tags-by-type api
            endpoint
        keys (`list`):
            A list of keys to unpack the `tag_dictionary` with, such as
            `["library","language"]`
    '''
    def __init__(self, tag_dictionary: dict, keys: list | None = None) -> None: ...

class ModelTags(GeneralTags):
    '''
    A namespace object holding all available model tags If a tag starts with a
    number, it will only exist in the dictionary

    Example:

    ```python
    >>> a.dataset["1_5BArabicCorpus"]  # will work
    >>> a["dataset"]["1_5BArabicCorpus"]  # will work
    >>> # o.dataset.1_5BArabicCorpus # will not work
    ```

    Args:
        model_tag_dictionary (`dict`):
            A dictionary of valid model tags, returned from the
            /api/models-tags-by-type api endpoint
    '''
    def __init__(self, model_tag_dictionary: dict) -> None: ...

class DatasetTags(GeneralTags):
    '''
    A namespace object holding all available dataset tags If a tag starts with a
    number, it will only exist in the dictionary

    Example

    ```python
    >>> a.size_categories["100K<n<1M"]  # will work
    >>> a["size_categories"]["100K<n<1M"]  # will work
    >>> # o.size_categories.100K<n<1M # will not work
    ```

    Args:
        dataset_tag_dictionary (`dict`):
            A dictionary of valid dataset tags, returned from the
            /api/datasets-tags-by-type api endpoint
    '''
    def __init__(self, dataset_tag_dictionary: dict) -> None: ...
