import _plotly_utils.basevalidators

class AspectmodeValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(self, plotly_name: str = 'aspectmode', parent_name: str = 'layout.scene', **kwargs) -> None: ...
