import _plotly_utils.basevalidators

class ItemclickValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(self, plotly_name: str = 'itemclick', parent_name: str = 'layout.legend', **kwargs) -> None: ...
