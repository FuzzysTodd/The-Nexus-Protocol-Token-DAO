import _plotly_utils.basevalidators

class HistogramValidator(_plotly_utils.basevalidators.CompoundArrayValidator):
    def __init__(self, plotly_name: str = 'histogram', parent_name: str = 'layout.template.data', **kwargs) -> None: ...
