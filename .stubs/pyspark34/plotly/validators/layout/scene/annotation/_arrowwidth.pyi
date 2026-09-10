import _plotly_utils.basevalidators

class ArrowwidthValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name: str = 'arrowwidth', parent_name: str = 'layout.scene.annotation', **kwargs) -> None: ...
