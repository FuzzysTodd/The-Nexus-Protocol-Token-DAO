import _plotly_utils.basevalidators

class ArrowsizeValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name: str = 'arrowsize', parent_name: str = 'layout.scene.annotation', **kwargs) -> None: ...
