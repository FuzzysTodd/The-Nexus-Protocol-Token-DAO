from _typeshed import Incomplete
from typing import Dict, List, Set

NON_CACHE_KEY: Incomplete

def get_key(config):
    """Get a unique identifier of a configuration.

    Args:
        config (dict or list): A configuration.

    Returns:
        tuple: A unique identifier which can be used as a key for a dict.
    """
def get_config_list(api_keys: List, api_bases: List | None = None, api_type: str | None = None, api_version: str | None = None) -> List[Dict]:
    """Get a list of configs for openai api calls.

    Args:
        api_keys (list): The api keys for openai api calls.
        api_bases (list, optional): The api bases for openai api calls.
        api_type (str, optional): The api type for openai api calls.
        api_version (str, optional): The api version for openai api calls.
    """
def config_list_openai_aoai(key_file_path: str | None = '.', openai_api_key_file: str | None = 'key_openai.txt', aoai_api_key_file: str | None = 'key_aoai.txt', aoai_api_base_file: str | None = 'base_aoai.txt', exclude: str | None = None) -> List[Dict]:
    '''Get a list of configs for openai + azure openai api calls.

    Args:
        key_file_path (str, optional): The path to the key files.
        openai_api_key_file (str, optional): The file name of the openai api key.
        aoai_api_key_file (str, optional): The file name of the azure openai api key.
        aoai_api_base_file (str, optional): The file name of the azure openai api base.
        exclude (str, optional): The api type to exclude, "openai" or "aoai".

    Returns:
        list: A list of configs for openai api calls.
    '''
def config_list_from_models(key_file_path: str | None = '.', openai_api_key_file: str | None = 'key_openai.txt', aoai_api_key_file: str | None = 'key_aoai.txt', aoai_api_base_file: str | None = 'base_aoai.txt', exclude: str | None = None, model_list: list | None = None) -> List[Dict]:
    '''Get a list of configs for api calls with models in the model list.

    Args:
        key_file_path (str, optional): The path to the key files.
        openai_api_key_file (str, optional): The file name of the openai api key.
        aoai_api_key_file (str, optional): The file name of the azure openai api key.
        aoai_api_base_file (str, optional): The file name of the azure openai api base.
        exclude (str, optional): The api type to exclude, "openai" or "aoai".
        model_list (list, optional): The model list.

    Returns:
        list: A list of configs for openai api calls.
    '''
def config_list_gpt4_gpt35(key_file_path: str | None = '.', openai_api_key_file: str | None = 'key_openai.txt', aoai_api_key_file: str | None = 'key_aoai.txt', aoai_api_base_file: str | None = 'base_aoai.txt', exclude: str | None = None) -> List[Dict]:
    '''Get a list of configs for gpt-4 followed by gpt-3.5 api calls.

    Args:
        key_file_path (str, optional): The path to the key files.
        openai_api_key_file (str, optional): The file name of the openai api key.
        aoai_api_key_file (str, optional): The file name of the azure openai api key.
        aoai_api_base_file (str, optional): The file name of the azure openai api base.
        exclude (str, optional): The api type to exclude, "openai" or "aoai".

    Returns:
        list: A list of configs for openai api calls.
    '''
def filter_config(config_list, filter_dict):
    """Filter the config list by provider and model.

    Args:
        config_list (list): The config list.
        filter_dict (dict, optional): The filter dict with keys corresponding to a field in each config,
            and values corresponding to lists of acceptable values for each key.

    Returns:
        list: The filtered config list.
    """
def config_list_from_json(env_or_file: str, file_location: str | None = '', filter_dict: Dict[str, List[str | None] | Set[str | None]] | None = None) -> List[Dict]:
    '''Get a list of configs from a json parsed from an env variable or a file.

    Args:
        env_or_file (str): The env variable name or file name.
        file_location (str, optional): The file location.
        filter_dict (dict, optional): The filter dict with keys corresponding to a field in each config,
            and values corresponding to lists of acceptable values for each key.
            e.g.,
    ```python
    filter_dict = {
        "api_type": ["open_ai", None],  # None means a missing key is acceptable
        "model": ["gpt-3.5-turbo", "gpt-4"],
    }
    ```

    Returns:
        list: A list of configs for openai api calls.
    '''
