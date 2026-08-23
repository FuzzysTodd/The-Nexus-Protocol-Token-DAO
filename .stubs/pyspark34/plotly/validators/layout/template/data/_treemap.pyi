import _plotly_utils.basevalidators

class TreemapValidator(_plotly_utils.basevalidators.CompoundArrayValidator):
    def __init__(self, plotly_name: str = 'treemap', parent_name: str = 'layout.template.data', **kwargs) -> None: ...
