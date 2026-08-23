import _plotly_utils.basevalidators

class StandoffValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name: str = 'standoff', parent_name: str = 'layout.scene.annotation', **kwargs) -> None: ...
