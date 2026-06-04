import _plotly_utils.basevalidators

class DataValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name: str = 'data', parent_name: str = 'layout.template', **kwargs) -> None: ...
