import _plotly_utils.basevalidators

class NumberValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name: str = 'number', parent_name: str = 'indicator', **kwargs) -> None: ...
