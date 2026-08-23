import _plotly_utils.basevalidators

class LenValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name: str = 'len', parent_name: str = 'layout.coloraxis.colorbar', **kwargs) -> None: ...
