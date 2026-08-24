import _plotly_utils.basevalidators

class XrefValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(self, plotly_name: str = 'xref', parent_name: str = 'volume.colorbar', **kwargs) -> None: ...
