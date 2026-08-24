import _plotly_utils.basevalidators

class MeasureValidator(_plotly_utils.basevalidators.DataArrayValidator):
    def __init__(self, plotly_name: str = 'measure', parent_name: str = 'waterfall', **kwargs) -> None: ...
