import _plotly_utils.basevalidators

class StartlineValidator(_plotly_utils.basevalidators.BooleanValidator):
    def __init__(self, plotly_name: str = 'startline', parent_name: str = 'carpet.baxis', **kwargs) -> None: ...
