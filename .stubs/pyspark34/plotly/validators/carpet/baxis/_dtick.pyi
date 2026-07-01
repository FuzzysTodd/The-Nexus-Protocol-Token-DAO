import _plotly_utils.basevalidators

class DtickValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name: str = 'dtick', parent_name: str = 'carpet.baxis', **kwargs) -> None: ...
