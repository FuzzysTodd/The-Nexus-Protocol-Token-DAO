import _plotly_utils.basevalidators

class DragmodeValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(self, plotly_name: str = 'dragmode', parent_name: str = 'layout.scene', **kwargs) -> None: ...
