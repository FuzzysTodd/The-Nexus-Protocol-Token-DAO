import _plotly_utils.basevalidators

class ZValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name: str = 'z', parent_name: str = 'isosurface.lightposition', **kwargs) -> None: ...
