import _plotly_utils.basevalidators

class ColumnValidator(_plotly_utils.basevalidators.IntegerValidator):
    def __init__(self, plotly_name: str = 'column', parent_name: str = 'parcoords.domain', **kwargs) -> None: ...
