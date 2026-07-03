import _plotly_utils.basevalidators

class UpValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name: str = 'up', parent_name: str = 'layout.scene.camera', **kwargs) -> None: ...
