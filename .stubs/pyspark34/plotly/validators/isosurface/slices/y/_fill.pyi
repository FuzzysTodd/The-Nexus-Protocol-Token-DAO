import _plotly_utils.basevalidators

class FillValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name: str = 'fill', parent_name: str = 'isosurface.slices.y', **kwargs) -> None: ...
