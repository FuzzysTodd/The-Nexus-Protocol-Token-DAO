import _plotly_utils.basevalidators

class MinorValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name: str = 'minor', parent_name: str = 'layout.xaxis', **kwargs) -> None: ...
