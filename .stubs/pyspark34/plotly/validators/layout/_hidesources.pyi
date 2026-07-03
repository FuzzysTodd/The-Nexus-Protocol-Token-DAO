import _plotly_utils.basevalidators

class HidesourcesValidator(_plotly_utils.basevalidators.BooleanValidator):
    def __init__(self, plotly_name: str = 'hidesources', parent_name: str = 'layout', **kwargs) -> None: ...
