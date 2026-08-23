import _plotly_utils.basevalidators

class HoverlabelValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name: str = 'hoverlabel', parent_name: str = 'layout.scene.annotation', **kwargs) -> None: ...
