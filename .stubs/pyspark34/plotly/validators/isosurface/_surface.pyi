import _plotly_utils.basevalidators

class SurfaceValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name: str = 'surface', parent_name: str = 'isosurface', **kwargs) -> None: ...
