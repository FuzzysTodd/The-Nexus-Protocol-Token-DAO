import _plotly_utils.basevalidators

class HoleValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name: str = 'hole', parent_name: str = 'layout.polar', **kwargs) -> None: ...
