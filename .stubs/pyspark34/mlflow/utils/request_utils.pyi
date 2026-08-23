from _typeshed import Incomplete

def augmented_raise_for_status(response) -> None:
    """Wrap the standard `requests.response.raise_for_status()` method and return reason"""
def download_chunk(range_start, range_end, headers, download_path, http_uri) -> None: ...
def cloud_storage_http_request(method, url, max_retries: int = 5, backoff_factor: int = 2, retry_codes=..., timeout: Incomplete | None = None, **kwargs):
    """
    Performs an HTTP PUT/GET/PATCH request using Python's `requests` module with automatic retry.

    :param method: string of 'PUT' or 'GET' or 'PATCH', specify to do http PUT or GET or PATCH
    :param url: the target URL address for the HTTP request.
    :param max_retries: maximum number of retries before throwing an exception.
    :param backoff_factor: a time factor for exponential backoff. e.g. value 5 means the HTTP
      request will be retried with interval 5, 10, 20... seconds. A value of 0 turns off the
      exponential backoff.
    :param retry_codes: a list of HTTP response error codes that qualifies for retry.
    :param timeout: wait for timeout seconds for response from remote server for connect and
      read request. Default to None owing to long duration operation in read / write.
    :param kwargs: Additional keyword arguments to pass to `requests.Session.request()`

    :return requests.Response object.
    """
