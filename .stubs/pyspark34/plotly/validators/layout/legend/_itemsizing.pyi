import _plotly_utils.basevalidators

class ItemsizingValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(self, plotly_name: str = 'itemsizing', parent_name: str = 'layout.legend', **kwargs) -> None: ...
