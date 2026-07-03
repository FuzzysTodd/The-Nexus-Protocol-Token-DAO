import _plotly_utils.basevalidators

class ShowbackgroundValidator(_plotly_utils.basevalidators.BooleanValidator):
    def __init__(self, plotly_name: str = 'showbackground', parent_name: str = 'layout.scene.xaxis', **kwargs) -> None: ...
