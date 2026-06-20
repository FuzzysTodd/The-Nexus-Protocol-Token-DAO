import _plotly_utils.basevalidators

class ColumnsValidator(_plotly_utils.basevalidators.IntegerValidator):
    def __init__(self, plotly_name: str = 'columns', parent_name: str = 'layout.grid', **kwargs) -> None: ...
