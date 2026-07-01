import _plotly_utils.basevalidators

class Scatter3DValidator(_plotly_utils.basevalidators.CompoundArrayValidator):
    def __init__(self, plotly_name: str = 'scatter3d', parent_name: str = 'layout.template.data', **kwargs) -> None: ...
