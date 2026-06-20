import _plotly_utils.basevalidators

class ShowaxeslabelsValidator(_plotly_utils.basevalidators.BooleanValidator):
    def __init__(self, plotly_name: str = 'showaxeslabels', parent_name: str = 'layout.scene.xaxis', **kwargs) -> None: ...
