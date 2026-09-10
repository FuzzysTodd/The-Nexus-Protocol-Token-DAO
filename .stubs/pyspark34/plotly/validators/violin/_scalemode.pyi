import _plotly_utils.basevalidators

class ScalemodeValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(self, plotly_name: str = 'scalemode', parent_name: str = 'violin', **kwargs) -> None: ...
