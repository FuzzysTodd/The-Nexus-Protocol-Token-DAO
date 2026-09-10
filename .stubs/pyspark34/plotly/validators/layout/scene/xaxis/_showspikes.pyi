import _plotly_utils.basevalidators

class ShowspikesValidator(_plotly_utils.basevalidators.BooleanValidator):
    def __init__(self, plotly_name: str = 'showspikes', parent_name: str = 'layout.scene.xaxis', **kwargs) -> None: ...
