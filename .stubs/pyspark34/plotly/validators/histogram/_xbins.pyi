import _plotly_utils.basevalidators

class XbinsValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name: str = 'xbins', parent_name: str = 'histogram', **kwargs) -> None: ...
