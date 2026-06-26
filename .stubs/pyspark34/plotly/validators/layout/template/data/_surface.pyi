import _plotly_utils.basevalidators

class SurfaceValidator(_plotly_utils.basevalidators.CompoundArrayValidator):
    def __init__(self, plotly_name: str = 'surface', parent_name: str = 'layout.template.data', **kwargs) -> None: ...
