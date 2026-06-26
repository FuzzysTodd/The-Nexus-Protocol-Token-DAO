from openai.datalib.pandas_helper import assert_has_pandas as assert_has_pandas
from typing import Any, Callable, NamedTuple

class Remediation(NamedTuple):
    name: str
    immediate_msg: str | None = ...
    necessary_msg: str | None = ...
    necessary_fn: Callable[[Any], Any] | None = ...
    optional_msg: str | None = ...
    optional_fn: Callable[[Any], Any] | None = ...
    error_msg: str | None = ...

def num_examples_validator(df):
    """
    This validator will only print out the number of examples and recommend to the user to increase the number of examples if less than 100.
    """
def necessary_column_validator(df, necessary_column):
    """
    This validator will ensure that the necessary column is present in the dataframe.
    """
def additional_column_validator(df, fields=['prompt', 'completion']):
    """
    This validator will remove additional columns from the dataframe.
    """
def non_empty_field_validator(df, field: str = 'completion'):
    """
    This validator will ensure that no completion is empty.
    """
def duplicated_rows_validator(df, fields=['prompt', 'completion']):
    """
    This validator will suggest to the user to remove duplicate rows if they exist.
    """
def long_examples_validator(df):
    """
    This validator will suggest to the user to remove examples that are too long.
    """
def common_prompt_suffix_validator(df):
    """
    This validator will suggest to add a common suffix to the prompt if one doesn't already exist in case of classification or conditional generation.
    """
def common_prompt_prefix_validator(df):
    """
    This validator will suggest to remove a common prefix from the prompt if a long one exist.
    """
def common_completion_prefix_validator(df):
    """
    This validator will suggest to remove a common prefix from the completion if a long one exist.
    """
def common_completion_suffix_validator(df):
    """
    This validator will suggest to add a common suffix to the completion if one doesn't already exist in case of classification or conditional generation.
    """
def completions_space_start_validator(df):
    """
    This validator will suggest to add a space at the start of the completion if it doesn't already exist. This helps with tokenization.
    """
def lower_case_validator(df, column):
    """
    This validator will suggest to lowercase the column values, if more than a third of letters are uppercase.
    """
def read_any_format(fname, fields=['prompt', 'completion']):
    """
    This function will read a file saved in .csv, .json, .txt, .xlsx or .tsv format using pandas.
     - for .xlsx it will read the first sheet
     - for .txt it will assume completions and split on newline
    """
def format_inferrer_validator(df):
    """
    This validator will infer the likely fine-tuning format of the data, and display it to the user if it is classification.
    It will also suggest to use ada and explain train/validation split benefits.
    """
def apply_necessary_remediation(df, remediation):
    """
    This function will apply a necessary remediation to a dataframe, or print an error message if one exists.
    """
def accept_suggestion(input_text, auto_accept): ...
def apply_optional_remediation(df, remediation, auto_accept):
    """
    This function will apply an optional remediation to a dataframe, based on the user input.
    """
def estimate_fine_tuning_time(df):
    """
    Estimate the time it'll take to fine-tune the dataset
    """
def get_outfnames(fname, split): ...
def get_classification_hyperparams(df): ...
def write_out_file(df, fname, any_remediations, auto_accept) -> None:
    """
    This function will write out a dataframe to a file, if the user would like to proceed, and also offer a fine-tuning command with the newly created file.
    For classification it will optionally ask the user if they would like to split the data into train/valid files, and modify the suggested command to include the valid set.
    """
def infer_task_type(df):
    """
    Infer the likely fine-tuning task type from the data
    """
def get_common_xfix(series, xfix: str = 'suffix'):
    """
    Finds the longest common suffix or prefix of all the values in a series
    """
def get_validators(): ...
def apply_validators(df, fname, remediation, validators, auto_accept, write_out_file_func) -> None: ...
