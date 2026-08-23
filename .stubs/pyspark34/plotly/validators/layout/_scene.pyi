import _plotly_utils.basevalidators

class SceneValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name: str = 'scene', parent_name: str = 'layout', **kwargs) -> None: ...
