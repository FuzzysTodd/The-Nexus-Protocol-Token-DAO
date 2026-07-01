import _plotly_utils.basevalidators

class BackgroundcolorValidator(_plotly_utils.basevalidators.ColorValidator):
    def __init__(self, plotly_name: str = 'backgroundcolor', parent_name: str = 'layout.scene.zaxis', **kwargs) -> None: ...
