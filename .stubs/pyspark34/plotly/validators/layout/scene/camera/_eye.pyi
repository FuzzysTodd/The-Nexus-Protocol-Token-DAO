import _plotly_utils.basevalidators

class EyeValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name: str = 'eye', parent_name: str = 'layout.scene.camera', **kwargs) -> None: ...
