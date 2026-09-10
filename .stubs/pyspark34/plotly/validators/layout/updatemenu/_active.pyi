import _plotly_utils.basevalidators

class ActiveValidator(_plotly_utils.basevalidators.IntegerValidator):
    def __init__(self, plotly_name: str = 'active', parent_name: str = 'layout.updatemenu', **kwargs) -> None: ...
