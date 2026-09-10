import _plotly_utils.basevalidators

class MinsizeValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name: str = 'minsize', parent_name: str = 'layout.uniformtext', **kwargs) -> None: ...
