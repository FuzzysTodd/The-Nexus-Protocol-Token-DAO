import _plotly_utils.basevalidators

class RowValidator(_plotly_utils.basevalidators.IntegerValidator):
    def __init__(self, plotly_name: str = 'row', parent_name: str = 'sunburst.domain', **kwargs) -> None: ...
