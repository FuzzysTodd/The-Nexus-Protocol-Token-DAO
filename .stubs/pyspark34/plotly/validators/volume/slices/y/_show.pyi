import _plotly_utils.basevalidators

class ShowValidator(_plotly_utils.basevalidators.BooleanValidator):
    def __init__(self, plotly_name: str = 'show', parent_name: str = 'volume.slices.y', **kwargs) -> None: ...
