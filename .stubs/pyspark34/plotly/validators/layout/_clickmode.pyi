import _plotly_utils.basevalidators

class ClickmodeValidator(_plotly_utils.basevalidators.FlaglistValidator):
    def __init__(self, plotly_name: str = 'clickmode', parent_name: str = 'layout', **kwargs) -> None: ...
