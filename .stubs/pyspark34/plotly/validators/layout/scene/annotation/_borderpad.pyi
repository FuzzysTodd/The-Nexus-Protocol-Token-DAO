import _plotly_utils.basevalidators

class BorderpadValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name: str = 'borderpad', parent_name: str = 'layout.scene.annotation', **kwargs) -> None: ...
