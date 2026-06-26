import _plotly_utils.basevalidators

class IndicatorValidator(_plotly_utils.basevalidators.CompoundArrayValidator):
    def __init__(self, plotly_name: str = 'indicator', parent_name: str = 'layout.template.data', **kwargs) -> None: ...
