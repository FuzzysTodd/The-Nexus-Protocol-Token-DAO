import _plotly_utils.basevalidators

class ActiveValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name: str = 'active', parent_name: str = 'layout.slider', **kwargs) -> None: ...
