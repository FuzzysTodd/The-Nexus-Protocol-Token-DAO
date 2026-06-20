from ..provider import AutoVisualizeProvider as AutoVisualizeProvider, DashProvider as DashProvider, PreserveProvider as PreserveProvider
from _typeshed import Incomplete

def get_visualize_provider():
    """Gets visualization provider for show() related calls.

    Returns:
        Visualization provider.
    """
def set_visualize_provider(provider) -> None:
    '''Sets visualization provider for show() related calls.

    Args:
        provider: Visualization provider found in "interpret.provider.visualize".
    '''
def set_show_addr(addr) -> None:
    """Set a (ip, port) for inline visualizations and dashboard. Has side effects stated below.
    Side effect: restarts the app runner for 'show' method.

    Args:
        addr: (ip, port) tuple as address to assign show method to.
    Returns:
        None.
    """
def get_show_addr():
    """Returns (ip, port) used for show method.

    Returns:
        Address tuple (ip, port).
    """
def shutdown_show_server():
    """This is a hard shutdown method for the show method's backing server.

    Returns:
        True if show server has stopped.
    """
def status_show_server():
    """Returns status and associated information of show method's backing server.

    Returns:
        Status and associated information as a dictionary.
    """
def init_show_server(addr: Incomplete | None = None, base_url: Incomplete | None = None, use_relative_links: bool = False) -> None:
    """Initializes show method's backing server.

    Args:
        addr: (ip, port) tuple as address to assign show method to.
        base_url: Base url path as string. Used mostly when server is running behind a proxy.
        use_relative_links: Use relative links for what's returned to client. Otherwise have absolute links.

    Returns:
        None.
    """
def show(explanation, key: int = -1, **kwargs) -> None:
    """Provides an interactive visualization for a given explanation(s).

    By default, visualization provided is not preserved when the notebook exits.

    Args:
        explanation: Either a scalar Explanation or list of Explanations to render as visualization.
        key: Specific index of explanation to visualize.
        **kwargs: Kwargs passed down to provider's render() call.

    Returns:
        None.
    """
def show_link(explanation, share_tables: Incomplete | None = None):
    """Provides the backing URL link behind the associated 'show' call for explanation.

    Args:
        explanation: Either a scalar Explanation or list of Explanations
                     that would be provided to 'show'.
        share_tables: Boolean or dictionary that dictates if Explanations
                      should all use the same selector as provided to 'show'.
                      (table used for selecting in the Dashboard).

    Returns:
        URL as a string.
    """
def preserve(explanation, selector_key: Incomplete | None = None, file_name: Incomplete | None = None, **kwargs) -> None:
    """Preserves an explanation's visualization for Jupyter cell, or file.

    If file_name is not None the following occurs:
    - For Plotly figures, saves to HTML using `plot`.
    - For dataframes, saves to HTML using `to_html`.
    - For strings (html), saves to HTML.
    - For Dash components, fails with exception. This is currently not supported.

    Args:
        explanation: An explanation.
        selector_key: If integer, treat as index for explanation. Otherwise, looks up value in first column, gets index.
        file_name: If assigned, will save the visualization to this filename.
        **kwargs: Kwargs which are passed to the underlying render/export call.

    Returns:
        None.
    """
