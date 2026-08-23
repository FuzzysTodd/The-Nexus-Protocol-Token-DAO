import _plotly_utils.basevalidators

class ZerolinewidthValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name: str = 'zerolinewidth', parent_name: str = 'layout.scene.yaxis', **kwargs) -> None: ...
