import _plotly_utils.basevalidators

class XtypeValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(self, plotly_name: str = 'xtype', parent_name: str = 'heatmap', **kwargs) -> None: ...
