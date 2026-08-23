import _plotly_utils.basevalidators

class ColumnwidthValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name: str = 'columnwidth', parent_name: str = 'table', **kwargs) -> None: ...
