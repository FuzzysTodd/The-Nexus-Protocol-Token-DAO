import dash
from _typeshed import Incomplete

MAX_NUM_PANES: int

class UDash(dash.Dash):
    ctx: Incomplete
    ctx_item: Incomplete
    options: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...

DATA_TABLE_DEFAULTS: Incomplete

def generate_app_mini(ctx_item, url_base_pathname: Incomplete | None = None, requests_pathname_prefix: Incomplete | None = None, routes_pathname_prefix: Incomplete | None = None):
    """Generates the mini Dash application including callbacks..

    Returns:
        The dash app itself.
    """
def gen_overall_plot(exp, model_idx): ...
def gen_plot(exp, picker, model_idx, counter): ...
def generate_app_full(url_base_pathname: Incomplete | None = None, requests_pathname_prefix: Incomplete | None = None, routes_pathname_prefix: Incomplete | None = None):
    """Generates the Dash application including callbacks.

    Returns:
        The dash app itself.
    """
def generate_app(ctx, options, url_base_pathname: Incomplete | None = None, requests_pathname_prefix: Incomplete | None = None, routes_pathname_prefix: Incomplete | None = None): ...
