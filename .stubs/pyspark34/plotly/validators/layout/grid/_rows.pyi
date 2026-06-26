import _plotly_utils.basevalidators

class RowsValidator(_plotly_utils.basevalidators.IntegerValidator):
    def __init__(self, plotly_name: str = 'rows', parent_name: str = 'layout.grid', **kwargs) -> None: ...
