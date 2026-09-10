import _plotly_utils.basevalidators

class EndlineValidator(_plotly_utils.basevalidators.BooleanValidator):
    def __init__(self, plotly_name: str = 'endline', parent_name: str = 'carpet.baxis', **kwargs) -> None: ...
