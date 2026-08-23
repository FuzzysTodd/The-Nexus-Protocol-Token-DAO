import _plotly_utils.basevalidators

class ClicktoshowValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(self, plotly_name: str = 'clicktoshow', parent_name: str = 'layout.annotation', **kwargs) -> None: ...
