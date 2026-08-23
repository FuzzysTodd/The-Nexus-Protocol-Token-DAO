from _typeshed import Incomplete
from mlflow.environment_variables import MLFLOW_HTTP_REQUEST_BACKOFF_FACTOR as MLFLOW_HTTP_REQUEST_BACKOFF_FACTOR, MLFLOW_HTTP_REQUEST_MAX_RETRIES as MLFLOW_HTTP_REQUEST_MAX_RETRIES, MLFLOW_HTTP_REQUEST_TIMEOUT as MLFLOW_HTTP_REQUEST_TIMEOUT
from mlflow.exceptions import InvalidUrlException as InvalidUrlException, MlflowException as MlflowException, RestException as RestException, get_error_code as get_error_code
from mlflow.protos import databricks_pb2 as databricks_pb2
from mlflow.protos.databricks_pb2 import ENDPOINT_NOT_FOUND as ENDPOINT_NOT_FOUND, ErrorCode as ErrorCode, INVALID_PARAMETER_VALUE as INVALID_PARAMETER_VALUE
from mlflow.utils.proto_json_utils import parse_dict as parse_dict
from mlflow.utils.request_utils import augmented_raise_for_status as augmented_raise_for_status, cloud_storage_http_request as cloud_storage_http_request
from mlflow.utils.string_utils import strip_suffix as strip_suffix

RESOURCE_DOES_NOT_EXIST: str

def http_request(host_creds, endpoint, method, max_retries: Incomplete | None = None, backoff_factor: Incomplete | None = None, extra_headers: Incomplete | None = None, retry_codes=..., timeout: Incomplete | None = None, **kwargs):
    '''
    Makes an HTTP request with the specified method to the specified hostname/endpoint. Transient
    errors such as Rate-limited (429), service unavailable (503) and internal error (500) are
    retried with an exponential back off with backoff_factor * (1, 2, 4, ... seconds).
    The function parses the API response (assumed to be JSON) into a Python object and returns it.

    :param host_creds: A :py:class:`mlflow.rest_utils.MlflowHostCreds` object containing
        hostname and optional authentication.
    :param endpoint: a string for service endpoint, e.g. "/path/to/object".
    :param method: a string indicating the method to use, e.g. "GET", "POST", "PUT".
    :param max_retries: maximum number of retries before throwing an exception.
    :param backoff_factor: a time factor for exponential backoff. e.g. value 5 means the HTTP
      request will be retried with interval 5, 10, 20... seconds. A value of 0 turns off the
      exponential backoff.
    :param extra_headers: a dict of HTTP header name-value pairs to be included in the request.
    :param retry_codes: a list of HTTP response error codes that qualifies for retry.
    :param timeout: wait for timeout seconds for response from remote server for connect and
      read request.
    :param kwargs: Additional keyword arguments to pass to `requests.Session.request()`

    :return: requests.Response object.
    '''
def http_request_safe(host_creds, endpoint, method, **kwargs):
    """
    Wrapper around ``http_request`` that also verifies that the request succeeds with code 200.
    """
def verify_rest_response(response, endpoint):
    """Verify the return code and format, raise exception if the request was not successful."""
def extract_api_info_for_service(service, path_prefix):
    """Return a dictionary mapping each API method to a tuple (path, HTTP method)"""
def extract_all_api_info_for_service(service, path_prefix):
    """Return a dictionary mapping each API method to a list of tuples [(path, HTTP method)]"""
def call_endpoint(host_creds, endpoint, method, json_body, response_proto, extra_headers: Incomplete | None = None): ...
def call_endpoints(host_creds, endpoints, json_body, response_proto, extra_headers: Incomplete | None = None): ...

class MlflowHostCreds:
    """
    Provides a hostname and optional authentication for talking to an MLflow tracking server.
    :param host: Hostname (e.g., http://localhost:5000) to MLflow server. Required.
    :param username: Username to use with Basic authentication when talking to server.
        If this is specified, password must also be specified.
    :param password: Password to use with Basic authentication when talking to server.
        If this is specified, username must also be specified.
    :param token: Token to use with Bearer authentication when talking to server.
        If provided, user/password authentication will be ignored.
    :param aws_sigv4: If true, we will create a signature V4 to be added for any outgoing request.
        Keys for signing the request can be passed via ENV variables,
        or will be fetched via boto3 session.
    :param ignore_tls_verification: If true, we will not verify the server's hostname or TLS
        certificate. This is useful for certain testing situations, but should never be
        true in production.
        If this is set to true ``server_cert_path`` must not be set.
    :param client_cert_path: Path to ssl client cert file (.pem).
        Sets the cert param of the ``requests.request``
        function (see https://requests.readthedocs.io/en/master/api/).
    :param server_cert_path: Path to a CA bundle to use.
        Sets the verify param of the ``requests.request``
        function (see https://requests.readthedocs.io/en/master/api/).
        If this is set ``ignore_tls_verification`` must be false.
    """
    host: Incomplete
    username: Incomplete
    password: Incomplete
    token: Incomplete
    aws_sigv4: Incomplete
    ignore_tls_verification: Incomplete
    client_cert_path: Incomplete
    server_cert_path: Incomplete
    def __init__(self, host, username: Incomplete | None = None, password: Incomplete | None = None, token: Incomplete | None = None, aws_sigv4: bool = False, ignore_tls_verification: bool = False, client_cert_path: Incomplete | None = None, server_cert_path: Incomplete | None = None) -> None: ...
    def __eq__(self, other): ...
    @property
    def verify(self): ...
