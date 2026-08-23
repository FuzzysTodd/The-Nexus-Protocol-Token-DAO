import _plotly_utils.basevalidators

class HeatmapValidator(_plotly_utils.basevalidators.CompoundArrayValidator):
    def __init__(self, plotly_name: str = 'heatmap', parent_name: str = 'layout.template.data', **kwargs) -> None: ...
