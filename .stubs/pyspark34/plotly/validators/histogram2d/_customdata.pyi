import _plotly_utils.basevalidators

class CustomdataValidator(_plotly_utils.basevalidators.DataArrayValidator):
    def __init__(self, plotly_name: str = 'customdata', parent_name: str = 'histogram2d', **kwargs) -> None: ...
