import _plotly_utils.basevalidators

class IsosurfaceValidator(_plotly_utils.basevalidators.CompoundArrayValidator):
    def __init__(self, plotly_name: str = 'isosurface', parent_name: str = 'layout.template.data', **kwargs) -> None: ...
