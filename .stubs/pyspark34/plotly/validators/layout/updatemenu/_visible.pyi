import _plotly_utils.basevalidators

class VisibleValidator(_plotly_utils.basevalidators.BooleanValidator):
    def __init__(self, plotly_name: str = 'visible', parent_name: str = 'layout.updatemenu', **kwargs) -> None: ...
