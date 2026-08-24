import _plotly_utils.basevalidators

class AxValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name: str = 'ax', parent_name: str = 'layout.scene.annotation', **kwargs) -> None: ...
