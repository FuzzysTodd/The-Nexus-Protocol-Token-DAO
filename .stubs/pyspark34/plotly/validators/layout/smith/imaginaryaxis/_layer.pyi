import _plotly_utils.basevalidators

class LayerValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(self, plotly_name: str = 'layer', parent_name: str = 'layout.smith.imaginaryaxis', **kwargs) -> None: ...
