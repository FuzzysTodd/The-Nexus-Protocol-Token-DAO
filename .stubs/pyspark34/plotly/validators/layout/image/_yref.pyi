import _plotly_utils.basevalidators

class YrefValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(self, plotly_name: str = 'yref', parent_name: str = 'layout.image', **kwargs) -> None: ...
