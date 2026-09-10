import _plotly_utils.basevalidators

class AutosizeValidator(_plotly_utils.basevalidators.BooleanValidator):
    def __init__(self, plotly_name: str = 'autosize', parent_name: str = 'layout', **kwargs) -> None: ...
