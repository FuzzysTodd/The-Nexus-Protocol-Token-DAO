import _plotly_utils.basevalidators

class MeanlineValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name: str = 'meanline', parent_name: str = 'violin', **kwargs) -> None: ...
