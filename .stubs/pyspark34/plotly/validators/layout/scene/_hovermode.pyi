import _plotly_utils.basevalidators

class HovermodeValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(self, plotly_name: str = 'hovermode', parent_name: str = 'layout.scene', **kwargs) -> None: ...
