import _plotly_utils.basevalidators

class RoworderValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(self, plotly_name: str = 'roworder', parent_name: str = 'layout.grid', **kwargs) -> None: ...
