import _plotly_utils.basevalidators

class CameraValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name: str = 'camera', parent_name: str = 'layout.scene', **kwargs) -> None: ...
