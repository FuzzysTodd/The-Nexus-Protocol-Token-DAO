from _typeshed import Incomplete
from typing import Any, Dict, List, Sequence, Tuple
from wandb.sdk.integration_utils.auto_logging import Response as Response
from wandb.sdk.lib.runid import generate_id as generate_id

logger: Incomplete

def subset_dict(original_dict: Dict[str, Any], keys_subset: Sequence[str]) -> Dict[str, Any]:
    """Create a subset of a dictionary using a subset of keys.

    :param original_dict: The original dictionary.
    :param keys_subset: The subset of keys to extract.
    :return: A dictionary containing only the specified keys.
    """
def reorder_and_convert_dict_list_to_table(data: List[Dict[str, Any]], order: List[str]) -> Tuple[List[str], List[List[Any]]]:
    """Convert a list of dictionaries to a pair of column names and corresponding values, with the option to order specific dictionaries.

    :param data: A list of dictionaries.
    :param order: A list of keys specifying the desired order for specific dictionaries. The remaining dictionaries will be ordered based on their original order.
    :return: A pair of column names and corresponding values.
    """
def flatten_dict(dictionary: Dict[str, Any], parent_key: str = '', sep: str = '-') -> Dict[str, Any]:
    """Flatten a nested dictionary, joining keys using a specified separator.

    :param dictionary: The dictionary to flatten.
    :param parent_key: The base key to prepend to each key.
    :param sep: The separator to use when joining keys.
    :return: A flattened dictionary.
    """
def collect_common_keys(list_of_dicts: List[Dict[str, Any]]) -> Dict[str, List[Any]]:
    """Collect the common keys of a list of dictionaries. For each common key, put its values into a list in the order they appear in the original dictionaries.

    :param list_of_dicts: The list of dictionaries to inspect.
    :return: A dictionary with each common key and its corresponding list of values.
    """

class CohereRequestResponseResolver:
    """Class to resolve the request/response from the Cohere API and convert it to a dictionary that can be logged."""
    def __call__(self, args: Sequence[Any], kwargs: Dict[str, Any], response: Response, start_time: float, time_elapsed: float) -> Dict[str, Any] | None:
        """Process the response from the Cohere API and convert it to a dictionary that can be logged.

        :param args: The arguments of the original function.
        :param kwargs: The keyword arguments of the original function.
        :param response: The response from the Cohere API.
        :param start_time: The start time of the request.
        :param time_elapsed: The time elapsed for the request.
        :return: A dictionary containing the parsed response and timing information.
        """
