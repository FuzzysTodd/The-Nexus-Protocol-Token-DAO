import _plotly_utils.basevalidators

class CapsValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name: str = 'caps', parent_name: str = 'volume', **kwargs) -> None: ...
