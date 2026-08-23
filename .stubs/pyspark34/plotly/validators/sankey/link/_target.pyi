import _plotly_utils.basevalidators

class TargetValidator(_plotly_utils.basevalidators.DataArrayValidator):
    def __init__(self, plotly_name: str = 'target', parent_name: str = 'sankey.link', **kwargs) -> None: ...
