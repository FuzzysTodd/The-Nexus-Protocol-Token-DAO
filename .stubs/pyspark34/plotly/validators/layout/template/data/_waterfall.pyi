import _plotly_utils.basevalidators

class WaterfallValidator(_plotly_utils.basevalidators.CompoundArrayValidator):
    def __init__(self, plotly_name: str = 'waterfall', parent_name: str = 'layout.template.data', **kwargs) -> None: ...
