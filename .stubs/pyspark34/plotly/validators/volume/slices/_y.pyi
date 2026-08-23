import _plotly_utils.basevalidators

class YValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name: str = 'y', parent_name: str = 'volume.slices', **kwargs) -> None: ...
