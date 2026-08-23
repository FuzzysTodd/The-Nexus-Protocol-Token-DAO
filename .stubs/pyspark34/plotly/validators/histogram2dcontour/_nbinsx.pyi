import _plotly_utils.basevalidators

class NbinsxValidator(_plotly_utils.basevalidators.IntegerValidator):
    def __init__(self, plotly_name: str = 'nbinsx', parent_name: str = 'histogram2dcontour', **kwargs) -> None: ...
