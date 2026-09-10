import _plotly_utils.basevalidators

class ShapeValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(self, plotly_name: str = 'shape', parent_name: str = 'scattergl.line', **kwargs) -> None: ...
