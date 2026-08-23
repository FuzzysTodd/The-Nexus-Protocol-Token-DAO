import _plotly_utils.basevalidators

class NbinsyValidator(_plotly_utils.basevalidators.IntegerValidator):
    def __init__(self, plotly_name: str = 'nbinsy', parent_name: str = 'histogram2d', **kwargs) -> None: ...
