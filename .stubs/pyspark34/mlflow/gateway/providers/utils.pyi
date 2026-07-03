from mlflow.gateway.constants import MLFLOW_GATEWAY_ROUTE_TIMEOUT_SECONDS as MLFLOW_GATEWAY_ROUTE_TIMEOUT_SECONDS
from mlflow.utils.uri import append_to_uri_path as append_to_uri_path
from typing import Any, Dict

async def send_request(headers: Dict[str, str], base_url: str, path: str, payload: Dict[str, Any]):
    """
    Send an HTTP request to a specific URL path with given headers and payload.

    :param headers: The headers to include in the request.
    :param base_url: The base URL where the request will be sent.
    :param path: The specific path of the URL to which the request will be sent.
    :param payload: The payload (or data) to be included in the request.
    :return: The server's response as a JSON object.
    :raise: HTTPException if the HTTP request fails.
    """
def rename_payload_keys(payload: Dict[str, Any], mapping: Dict[str, str]) -> Dict[str, Any]:
    """
    Transform the keys in a dictionary based on a provided mapping.

    :param payload: The original dictionary to transform.
    :param mapping: A dictionary where each key-value pair represents a mapping from the old
                    key to the new key.
    :return: A new dictionary containing the transformed keys.
    """
