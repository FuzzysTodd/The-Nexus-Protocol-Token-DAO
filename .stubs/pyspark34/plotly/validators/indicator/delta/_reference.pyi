import _plotly_utils.basevalidators

class ReferenceValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name: str = 'reference', parent_name: str = 'indicator.delta', **kwargs) -> None: ...
