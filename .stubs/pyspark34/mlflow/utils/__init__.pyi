from _typeshed import Incomplete
from collections.abc import Generator

PYTHON_VERSION: Incomplete

def get_major_minor_py_version(py_version): ...
def get_unique_resource_id(max_length: Incomplete | None = None):
    """
    Obtains a unique id that can be included in a resource name. This unique id is a valid
    DNS subname.

    :param max_length: The maximum length of the identifier
    :return: A unique identifier that can be appended to a user-readable resource name to avoid
             naming collisions.
    """
def reraise(tp, value, tb: Incomplete | None = None) -> None: ...
def chunk_list(l, chunk_size) -> Generator[Incomplete, None, None]: ...
def merge_dicts(dict_a, dict_b, raise_on_duplicates: bool = True):
    """
    This function takes two dictionaries and returns one singular merged dictionary.

    :param dict_a: The first dictionary.
    :param dict_b: The second dictonary.
    :param raise_on_duplicates: If True, the function raises ValueError if there are duplicate keys.
                                Otherwise, duplicate keys in `dict_b` will override the ones in
                                `dict_a`.
    :return: A merged dictionary.
    """
def find_free_port():
    """
    Find free socket port on local machine.
    """
def check_port_connectivity(): ...
def is_iterator(obj):
    """
    :param obj: any object.
    :return: boolean representing whether or not 'obj' is an iterator.
    """
def get_results_from_paginated_fn(paginated_fn, max_results_per_page, max_results: Incomplete | None = None):
    """
    Gets results by calling the ``paginated_fn`` until either no more results remain or
    the specified ``max_results`` threshold has been reached.

    :param paginated_fn:
    :type paginated_fn: This function is expected to take in the number of results to retrieve
        per page and a pagination token, and return a PagedList object
    :param max_results_per_page:
    :type max_results_per_page: The maximum number of results to retrieve per page
    :param max_results:
    :type max_results: The maximum number of results to retrieve overall. If unspecified,
                       all results will be retrieved.
    :return: Returns a list of entities, as determined by the paginated_fn parameter, with no more
        entities than specified by max_results
    :rtype: list[object]
    """
