import _plotly_utils.basevalidators

class OrientationValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(self, plotly_name: str = 'orientation', parent_name: str = 'mesh3d.colorbar', **kwargs) -> None: ...
