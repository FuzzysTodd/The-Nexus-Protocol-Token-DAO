import _plotly_utils.basevalidators

class SectorValidator(_plotly_utils.basevalidators.InfoArrayValidator):
    def __init__(self, plotly_name: str = 'sector', parent_name: str = 'layout.polar', **kwargs) -> None: ...
