import _plotly_utils.basevalidators

class SizeyValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name: str = 'sizey', parent_name: str = 'layout.image', **kwargs) -> None: ...
