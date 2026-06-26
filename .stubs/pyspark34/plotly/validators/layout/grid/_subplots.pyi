import _plotly_utils.basevalidators

class SubplotsValidator(_plotly_utils.basevalidators.InfoArrayValidator):
    def __init__(self, plotly_name: str = 'subplots', parent_name: str = 'layout.grid', **kwargs) -> None: ...
