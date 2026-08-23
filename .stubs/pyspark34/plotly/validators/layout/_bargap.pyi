import _plotly_utils.basevalidators

class BargapValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name: str = 'bargap', parent_name: str = 'layout', **kwargs) -> None: ...
