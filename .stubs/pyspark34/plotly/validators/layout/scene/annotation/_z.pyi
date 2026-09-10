import _plotly_utils.basevalidators

class ZValidator(_plotly_utils.basevalidators.AnyValidator):
    def __init__(self, plotly_name: str = 'z', parent_name: str = 'layout.scene.annotation', **kwargs) -> None: ...
