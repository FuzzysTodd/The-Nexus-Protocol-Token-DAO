import _plotly_utils.basevalidators

class SpikethicknessValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name: str = 'spikethickness', parent_name: str = 'layout.scene.xaxis', **kwargs) -> None: ...
