import _plotly_utils.basevalidators

class DbValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name: str = 'db', parent_name: str = 'carpet', **kwargs) -> None: ...
