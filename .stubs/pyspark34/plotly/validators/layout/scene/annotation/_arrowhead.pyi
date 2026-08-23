import _plotly_utils.basevalidators

class ArrowheadValidator(_plotly_utils.basevalidators.IntegerValidator):
    def __init__(self, plotly_name: str = 'arrowhead', parent_name: str = 'layout.scene.annotation', **kwargs) -> None: ...
