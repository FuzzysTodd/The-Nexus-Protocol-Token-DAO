from . import get_session as get_session, hf_raise_for_status as hf_raise_for_status, logging as logging
from _typeshed import Incomplete
from typing import Dict, Iterable

logger: Incomplete

def paginate(path: str, params: Dict, headers: Dict) -> Iterable:
    '''Fetch a list of models/datasets/spaces and paginate through results.

    This is using the same "Link" header format as GitHub.
    See:
    - https://requests.readthedocs.io/en/latest/api/#requests.Response.links
    - https://docs.github.com/en/rest/guides/traversing-with-pagination#link-header
    '''
