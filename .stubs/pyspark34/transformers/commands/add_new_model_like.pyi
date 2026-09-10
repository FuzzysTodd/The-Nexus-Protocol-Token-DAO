import os
from . import BaseTransformersCLICommand as BaseTransformersCLICommand
from ..utils import is_flax_available as is_flax_available, is_tf_available as is_tf_available, is_torch_available as is_torch_available, logging as logging
from _typeshed import Incomplete
from argparse import ArgumentParser, Namespace
from dataclasses import dataclass
from pathlib import Path
from transformers.models.auto.configuration_auto import model_type_to_module_name as model_type_to_module_name
from typing import Any, Callable, Dict, List, Optional, Pattern, Tuple, Union

logger: Incomplete
CURRENT_YEAR: Incomplete
TRANSFORMERS_PATH: Incomplete
REPO_PATH: Incomplete

@dataclass
class ModelPatterns:
    '''
    Holds the basic information about a new model for the add-new-model-like command.

    Args:
        model_name (`str`): The model name.
        checkpoint (`str`): The checkpoint to use for doc examples.
        model_type (`str`, *optional*):
            The model type, the identifier used internally in the library like `bert` or `xlm-roberta`. Will default to
            `model_name` lowercased with spaces replaced with minuses (-).
        model_lower_cased (`str`, *optional*):
            The lowercased version of the model name, to use for the module name or function names. Will default to
            `model_name` lowercased with spaces and minuses replaced with underscores.
        model_camel_cased (`str`, *optional*):
            The camel-cased version of the model name, to use for the class names. Will default to `model_name`
            camel-cased (with spaces and minuses both considered as word separators.
        model_upper_cased (`str`, *optional*):
            The uppercased version of the model name, to use for the constant names. Will default to `model_name`
            uppercased with spaces and minuses replaced with underscores.
        config_class (`str`, *optional*):
            The tokenizer class associated with this model. Will default to `"{model_camel_cased}Config"`.
        tokenizer_class (`str`, *optional*):
            The tokenizer class associated with this model (leave to `None` for models that don\'t use a tokenizer).
        image_processor_class (`str`, *optional*):
            The image processor class associated with this model (leave to `None` for models that don\'t use an image
            processor).
        feature_extractor_class (`str`, *optional*):
            The feature extractor class associated with this model (leave to `None` for models that don\'t use a feature
            extractor).
        processor_class (`str`, *optional*):
            The processor class associated with this model (leave to `None` for models that don\'t use a processor).
    '''
    model_name: str
    checkpoint: str
    model_type: Optional[str] = ...
    model_lower_cased: Optional[str] = ...
    model_camel_cased: Optional[str] = ...
    model_upper_cased: Optional[str] = ...
    config_class: Optional[str] = ...
    tokenizer_class: Optional[str] = ...
    image_processor_class: Optional[str] = ...
    feature_extractor_class: Optional[str] = ...
    processor_class: Optional[str] = ...
    def __post_init__(self) -> None: ...
    def __init__(self, model_name, checkpoint, model_type, model_lower_cased, model_camel_cased, model_upper_cased, config_class, tokenizer_class, image_processor_class, feature_extractor_class, processor_class) -> None: ...

ATTRIBUTE_TO_PLACEHOLDER: Incomplete

def is_empty_line(line: str) -> bool:
    """
    Determines whether a line is empty or not.
    """
def find_indent(line: str) -> int:
    """
    Returns the number of spaces that start a line indent.
    """
def parse_module_content(content: str) -> List[str]:
    """
    Parse the content of a module in the list of objects it defines.

    Args:
        content (`str`): The content to parse

    Returns:
        `List[str]`: The list of objects defined in the module.
    """
def add_content_to_text(text: str, content: str, add_after: Optional[Union[str, Pattern]] = None, add_before: Optional[Union[str, Pattern]] = None, exact_match: bool = False) -> str:
    """
    A utility to add some content inside a given text.

    Args:
       text (`str`): The text in which we want to insert some content.
       content (`str`): The content to add.
       add_after (`str` or `Pattern`):
           The pattern to test on a line of `text`, the new content is added after the first instance matching it.
       add_before (`str` or `Pattern`):
           The pattern to test on a line of `text`, the new content is added before the first instance matching it.
       exact_match (`bool`, *optional*, defaults to `False`):
           A line is considered a match with `add_after` or `add_before` if it matches exactly when `exact_match=True`,
           otherwise, if `add_after`/`add_before` is present in the line.

    <Tip warning={true}>

    The arguments `add_after` and `add_before` are mutually exclusive, and one exactly needs to be provided.

    </Tip>

    Returns:
        `str`: The text with the new content added if a match was found.
    """
def add_content_to_file(file_name: Union[str, os.PathLike], content: str, add_after: Optional[Union[str, Pattern]] = None, add_before: Optional[Union[str, Pattern]] = None, exact_match: bool = False):
    """
    A utility to add some content inside a given file.

    Args:
       file_name (`str` or `os.PathLike`): The name of the file in which we want to insert some content.
       content (`str`): The content to add.
       add_after (`str` or `Pattern`):
           The pattern to test on a line of `text`, the new content is added after the first instance matching it.
       add_before (`str` or `Pattern`):
           The pattern to test on a line of `text`, the new content is added before the first instance matching it.
       exact_match (`bool`, *optional*, defaults to `False`):
           A line is considered a match with `add_after` or `add_before` if it matches exactly when `exact_match=True`,
           otherwise, if `add_after`/`add_before` is present in the line.

    <Tip warning={true}>

    The arguments `add_after` and `add_before` are mutually exclusive, and one exactly needs to be provided.

    </Tip>
    """
def replace_model_patterns(text: str, old_model_patterns: ModelPatterns, new_model_patterns: ModelPatterns) -> Tuple[str, str]:
    """
    Replace all patterns present in a given text.

    Args:
        text (`str`): The text to treat.
        old_model_patterns (`ModelPatterns`): The patterns for the old model.
        new_model_patterns (`ModelPatterns`): The patterns for the new model.

    Returns:
        `Tuple(str, str)`: A tuple of with the treated text and the replacement actually done in it.
    """
def simplify_replacements(replacements):
    '''
    Simplify a list of replacement patterns to make sure there are no needless ones.

    For instance in the sequence "Bert->BertNew, BertConfig->BertNewConfig, bert->bert_new", the replacement
    "BertConfig->BertNewConfig" is implied by "Bert->BertNew" so not needed.

    Args:
        replacements (`List[Tuple[str, str]]`): List of patterns (old, new)

    Returns:
        `List[Tuple[str, str]]`: The list of patterns simplified.
    '''
def get_module_from_file(module_file: Union[str, os.PathLike]) -> str:
    """
    Returns the module name corresponding to a module file.
    """

SPECIAL_PATTERNS: Incomplete

def duplicate_module(module_file: Union[str, os.PathLike], old_model_patterns: ModelPatterns, new_model_patterns: ModelPatterns, dest_file: Optional[str] = None, add_copied_from: bool = True):
    """
    Create a new module from an existing one and adapting all function and classes names from old patterns to new ones.

    Args:
        module_file (`str` or `os.PathLike`): Path to the module to duplicate.
        old_model_patterns (`ModelPatterns`): The patterns for the old model.
        new_model_patterns (`ModelPatterns`): The patterns for the new model.
        dest_file (`str` or `os.PathLike`, *optional*): Path to the new module.
        add_copied_from (`bool`, *optional*, defaults to `True`):
            Whether or not to add `# Copied from` statements in the duplicated module.
    """
def filter_framework_files(files: List[Union[str, os.PathLike]], frameworks: Optional[List[str]] = None) -> List[Union[str, os.PathLike]]:
    """
    Filter a list of files to only keep the ones corresponding to a list of frameworks.

    Args:
        files (`List[Union[str, os.PathLike]]`): The list of files to filter.
        frameworks (`List[str]`, *optional*): The list of allowed frameworks.

    Returns:
        `List[Union[str, os.PathLike]]`: The list of filtered files.
    """
def get_model_files(model_type: str, frameworks: Optional[List[str]] = None) -> Dict[str, Union[Path, List[Path]]]:
    '''
    Retrieves all the files associated to a model.

    Args:
        model_type (`str`): A valid model type (like "bert" or "gpt2")
        frameworks (`List[str]`, *optional*):
            If passed, will only keep the model files corresponding to the passed frameworks.

    Returns:
        `Dict[str, Union[Path, List[Path]]]`: A dictionary with the following keys:
        - **doc_file** -- The documentation file for the model.
        - **model_files** -- All the files in the model module.
        - **test_files** -- The test files for the model.
    '''
def find_base_model_checkpoint(model_type: str, model_files: Optional[Dict[str, Union[Path, List[Path]]]] = None) -> str:
    '''
    Finds the model checkpoint used in the docstrings for a given model.

    Args:
        model_type (`str`): A valid model type (like "bert" or "gpt2")
        model_files (`Dict[str, Union[Path, List[Path]]`, *optional*):
            The files associated to `model_type`. Can be passed to speed up the function, otherwise will be computed.

    Returns:
        `str`: The checkpoint used.
    '''
def get_default_frameworks():
    """
    Returns the list of frameworks (PyTorch, TensorFlow, Flax) that are installed in the environment.
    """
def retrieve_model_classes(model_type: str, frameworks: Optional[List[str]] = None) -> Dict[str, List[str]]:
    '''
    Retrieve the model classes associated to a given model.

    Args:
        model_type (`str`): A valid model type (like "bert" or "gpt2")
        frameworks (`List[str]`, *optional*):
            The frameworks to look for. Will default to `["pt", "tf", "flax"]`, passing a smaller list will restrict
            the classes returned.

    Returns:
        `Dict[str, List[str]]`: A dictionary with one key per framework and the list of model classes associated to
        that framework as values.
    '''
def retrieve_info_for_model(model_type, frameworks: Optional[List[str]] = None):
    '''
    Retrieves all the information from a given model_type.

    Args:
        model_type (`str`): A valid model type (like "bert" or "gpt2")
        frameworks (`List[str]`, *optional*):
            If passed, will only keep the info corresponding to the passed frameworks.

    Returns:
        `Dict`: A dictionary with the following keys:
        - **frameworks** (`List[str]`): The list of frameworks that back this model type.
        - **model_classes** (`Dict[str, List[str]]`): The model classes implemented for that model type.
        - **model_files** (`Dict[str, Union[Path, List[Path]]]`): The files associated with that model type.
        - **model_patterns** (`ModelPatterns`): The various patterns for the model.
    '''
def clean_frameworks_in_init(init_file: Union[str, os.PathLike], frameworks: Optional[List[str]] = None, keep_processing: bool = True):
    """
    Removes all the import lines that don't belong to a given list of frameworks or concern tokenizers/feature
    extractors/image processors/processors in an init.

    Args:
        init_file (`str` or `os.PathLike`): The path to the init to treat.
        frameworks (`List[str]`, *optional*):
           If passed, this will remove all imports that are subject to a framework not in frameworks
        keep_processing (`bool`, *optional*, defaults to `True`):
            Whether or not to keep the preprocessing (tokenizer, feature extractor, image processor, processor) imports
            in the init.
    """
def add_model_to_main_init(old_model_patterns: ModelPatterns, new_model_patterns: ModelPatterns, frameworks: Optional[List[str]] = None, with_processing: bool = True):
    """
    Add a model to the main init of Transformers.

    Args:
        old_model_patterns (`ModelPatterns`): The patterns for the old model.
        new_model_patterns (`ModelPatterns`): The patterns for the new model.
        frameworks (`List[str]`, *optional*):
            If specified, only the models implemented in those frameworks will be added.
        with_processsing (`bool`, *optional*, defaults to `True`):
            Whether the tokenizer/feature extractor/processor of the model should also be added to the init or not.
    """
def insert_tokenizer_in_auto_module(old_model_patterns: ModelPatterns, new_model_patterns: ModelPatterns):
    """
    Add a tokenizer to the relevant mappings in the auto module.

    Args:
        old_model_patterns (`ModelPatterns`): The patterns for the old model.
        new_model_patterns (`ModelPatterns`): The patterns for the new model.
    """

AUTO_CLASSES_PATTERNS: Incomplete

def add_model_to_auto_classes(old_model_patterns: ModelPatterns, new_model_patterns: ModelPatterns, model_classes: Dict[str, List[str]]):
    """
    Add a model to the relevant mappings in the auto module.

    Args:
        old_model_patterns (`ModelPatterns`): The patterns for the old model.
        new_model_patterns (`ModelPatterns`): The patterns for the new model.
        model_classes (`Dict[str, List[str]]`): A dictionary framework to list of model classes implemented.
    """

DOC_OVERVIEW_TEMPLATE: str

def duplicate_doc_file(doc_file: Union[str, os.PathLike], old_model_patterns: ModelPatterns, new_model_patterns: ModelPatterns, dest_file: Optional[Union[str, os.PathLike]] = None, frameworks: Optional[List[str]] = None):
    """
    Duplicate a documentation file and adapts it for a new model.

    Args:
        module_file (`str` or `os.PathLike`): Path to the doc file to duplicate.
        old_model_patterns (`ModelPatterns`): The patterns for the old model.
        new_model_patterns (`ModelPatterns`): The patterns for the new model.
        dest_file (`str` or `os.PathLike`, *optional*): Path to the new doc file.
            Will default to the a file named `{new_model_patterns.model_type}.mdx` in the same folder as `module_file`.
        frameworks (`List[str]`, *optional*):
            If passed, will only keep the model classes corresponding to this list of frameworks in the new doc file.
    """
def create_new_model_like(model_type: str, new_model_patterns: ModelPatterns, add_copied_from: bool = True, frameworks: Optional[List[str]] = None, old_checkpoint: Optional[str] = None):
    '''
    Creates a new model module like a given model of the Transformers library.

    Args:
        model_type (`str`): The model type to duplicate (like "bert" or "gpt2")
        new_model_patterns (`ModelPatterns`): The patterns for the new model.
        add_copied_from (`bool`, *optional*, defaults to `True`):
            Whether or not to add "Copied from" statements to all classes in the new model modeling files.
        frameworks (`List[str]`, *optional*):
            If passed, will limit the duplicate to the frameworks specified.
        old_checkpoint (`str`, *optional*):
            The name of the base checkpoint for the old model. Should be passed along when it can\'t be automatically
            recovered from the `model_type`.
    '''
def add_new_model_like_command_factory(args: Namespace): ...

class AddNewModelLikeCommand(BaseTransformersCLICommand):
    @staticmethod
    def register_subcommand(parser: ArgumentParser): ...
    old_model_type: Incomplete
    model_patterns: Incomplete
    add_copied_from: Incomplete
    frameworks: Incomplete
    old_checkpoint: Incomplete
    path_to_repo: Incomplete
    def __init__(self, config_file: Incomplete | None = None, path_to_repo: Incomplete | None = None, *args) -> None: ...
    def run(self) -> None: ...

def get_user_field(question: str, default_value: Optional[str] = None, is_valid_answer: Optional[Callable] = None, convert_to: Optional[Callable] = None, fallback_message: Optional[str] = None) -> Any:
    """
    A utility function that asks a question to the user to get an answer, potentially looping until it gets a valid
    answer.

    Args:
        question (`str`): The question to ask the user.
        default_value (`str`, *optional*): A potential default value that will be used when the answer is empty.
        is_valid_answer (`Callable`, *optional*):
            If set, the question will be asked until this function returns `True` on the provided answer.
        convert_to (`Callable`, *optional*):
            If set, the answer will be passed to this function. If this function raises an error on the procided
            answer, the question will be asked again.
        fallback_message (`str`, *optional*):
            A message that will be displayed each time the question is asked again to the user.

    Returns:
        `Any`: The answer provided by the user (or the default), passed through the potential conversion function.
    """
def convert_to_bool(x: str) -> bool:
    """
    Converts a string to a bool.
    """
def get_user_input():
    """
    Ask the user for the necessary inputs to add the new model.
    """
