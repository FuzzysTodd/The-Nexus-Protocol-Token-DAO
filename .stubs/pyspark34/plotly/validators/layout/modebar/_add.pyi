import _plotly_utils.basevalidators

class AddValidator(_plotly_utils.basevalidators.StringValidator):
    def __init__(self, plotly_name: str = 'add', parent_name: str = 'layout.modebar', **kwargs) -> None: ...
