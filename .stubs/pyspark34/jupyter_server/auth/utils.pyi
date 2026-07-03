from _typeshed import Incomplete

def warn_disabled_authorization() -> None:
    """DEPRECATED, does nothing"""

HTTP_METHOD_TO_AUTH_ACTION: Incomplete

def get_regex_to_resource_map():
    '''Returns a dictionary with all of Jupyter Server\'s
    request handler URL regex patterns mapped to
    their resource name.

    e.g.
    { "/api/contents/<regex_pattern>": "contents", ...}
    '''
def match_url_to_resource(url, regex_mapping: Incomplete | None = None):
    '''Finds the JupyterHandler regex pattern that would
    match the given URL and returns the resource name (str)
    of that handler.

    e.g.
    /api/contents/... returns "contents"
    '''

moons_of_jupyter: Incomplete

def get_anonymous_username() -> str:
    '''
    Get a random user-name based on the moons of Jupyter.
    This function returns names like "Anonymous Io" or "Anonymous Metis".
    '''
