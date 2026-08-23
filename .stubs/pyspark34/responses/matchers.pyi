from typing import Any, Callable, Dict, List

def urlencoded_params_matcher(params: Dict[str, str] | None, *, allow_blank: bool = False) -> Callable[..., Any]:
    """
    Matches URL encoded data

    :param params: (dict) data provided to 'data' arg of request
    :return: (func) matcher
    """
def json_params_matcher(params: Dict[str, Any] | List[Any] | None, *, strict_match: bool = True) -> Callable[..., Any]:
    """Matches JSON encoded data of request body.

    Parameters
    ----------
    params : dict or list
        JSON object provided to 'json' arg of request or a part of it if used in
        conjunction with ``strict_match=False``.
    strict_match : bool, default=True
        Applied only when JSON object is a dictionary.
        If set to ``True``, validates that all keys of JSON object match.
        If set to ``False``, original request may contain additional keys.


    Returns
    -------
    Callable
        Matcher function.

    """
def fragment_identifier_matcher(identifier: str | None) -> Callable[..., Any]: ...
def query_param_matcher(params: Dict[str, Any] | None, *, strict_match: bool = True) -> Callable[..., Any]:
    """Matcher to match 'params' argument in request.

    Parameters
    ----------
    params : dict
        The same as provided to request or a part of it if used in
        conjunction with ``strict_match=False``.
    strict_match : bool, default=True
        If set to ``True``, validates that all parameters match.
        If set to ``False``, original request may contain additional parameters.


    Returns
    -------
    Callable
        Matcher function.

    """
def query_string_matcher(query: str | None) -> Callable[..., Any]:
    """
    Matcher to match query string part of request

    :param query: (str), same as constructed by request
    :return: (func) matcher
    """
def request_kwargs_matcher(kwargs: Dict[str, Any] | None) -> Callable[..., Any]:
    """
    Matcher to match keyword arguments provided to request

    :param kwargs: (dict), keyword arguments, same as provided to request
    :return: (func) matcher
    """
def multipart_matcher(files: Dict[str, Any], data: Dict[str, str] | None = None) -> Callable[..., Any]:
    """
    Matcher to match 'multipart/form-data' content-type.
    This function constructs request body and headers from provided 'data' and 'files'
    arguments and compares to actual request

    :param files: (dict), same as provided to request
    :param data: (dict), same as provided to request
    :return: (func) matcher
    """
def header_matcher(headers: Dict[str, str], strict_match: bool = False) -> Callable[..., Any]:
    """
    Matcher to match 'headers' argument in request using the responses library.

    Because ``requests`` will send several standard headers in addition to what
    was specified by your code, request headers that are additional to the ones
    passed to the matcher are ignored by default. You can change this behaviour
    by passing ``strict_match=True``.

    :param headers: (dict), same as provided to request
    :param strict_match: (bool), whether headers in addition to those specified
                         in the matcher should cause the match to fail.
    :return: (func) matcher
    """
