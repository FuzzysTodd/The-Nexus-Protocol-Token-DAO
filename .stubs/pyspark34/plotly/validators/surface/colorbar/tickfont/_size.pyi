import _plotly_utils.basevalidators

class SizeValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name: str = 'size', parent_name: str = 'surface.colorbar.tickfont', **kwargs) -> None: ...
