import _plotly_utils.basevalidators

class PadValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name: str = 'pad', parent_name: str = 'treemap.tiling', **kwargs) -> None: ...
