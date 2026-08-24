import _plotly_utils.basevalidators

class Histogram2DValidator(_plotly_utils.basevalidators.CompoundArrayValidator):
    def __init__(self, plotly_name: str = 'histogram2d', parent_name: str = 'layout.template.data', **kwargs) -> None: ...
