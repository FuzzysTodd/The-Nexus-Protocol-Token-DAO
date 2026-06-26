import _plotly_utils.basevalidators

class TracesValidator(_plotly_utils.basevalidators.AnyValidator):
    def __init__(self, plotly_name: str = 'traces', parent_name: str = 'frame', **kwargs) -> None: ...
