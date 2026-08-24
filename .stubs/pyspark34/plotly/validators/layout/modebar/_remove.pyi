import _plotly_utils.basevalidators

class RemoveValidator(_plotly_utils.basevalidators.StringValidator):
    def __init__(self, plotly_name: str = 'remove', parent_name: str = 'layout.modebar', **kwargs) -> None: ...
