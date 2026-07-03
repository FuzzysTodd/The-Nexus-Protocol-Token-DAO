import _plotly_utils.basevalidators

class TicktextValidator(_plotly_utils.basevalidators.DataArrayValidator):
    def __init__(self, plotly_name: str = 'ticktext', parent_name: str = 'layout.scene.yaxis', **kwargs) -> None: ...
