import _plotly_utils.basevalidators

class ProjectionValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name: str = 'projection', parent_name: str = 'layout.scene.camera', **kwargs) -> None: ...
