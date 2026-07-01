import _plotly_utils.basevalidators

class BgcolorValidator(_plotly_utils.basevalidators.ColorValidator):
    def __init__(self, plotly_name: str = 'bgcolor', parent_name: str = 'layout.coloraxis.colorbar', **kwargs) -> None: ...
