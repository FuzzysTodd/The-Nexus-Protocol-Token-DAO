import _plotly_utils.basevalidators

class ConnectorValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name: str = 'connector', parent_name: str = 'waterfall', **kwargs) -> None: ...
