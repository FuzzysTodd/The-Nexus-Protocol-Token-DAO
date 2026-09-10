import _plotly_utils.basevalidators

class GridshapeValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(self, plotly_name: str = 'gridshape', parent_name: str = 'layout.polar', **kwargs) -> None: ...
