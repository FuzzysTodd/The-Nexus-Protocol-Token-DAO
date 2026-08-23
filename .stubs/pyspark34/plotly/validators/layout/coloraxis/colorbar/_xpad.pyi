import _plotly_utils.basevalidators

class XpadValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name: str = 'xpad', parent_name: str = 'layout.coloraxis.colorbar', **kwargs) -> None: ...
