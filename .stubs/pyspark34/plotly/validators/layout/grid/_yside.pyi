import _plotly_utils.basevalidators

class YsideValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(self, plotly_name: str = 'yside', parent_name: str = 'layout.grid', **kwargs) -> None: ...
