import _plotly_utils.basevalidators

class DisplayindexValidator(_plotly_utils.basevalidators.IntegerValidator):
    def __init__(self, plotly_name: str = 'displayindex', parent_name: str = 'parcats.dimension', **kwargs) -> None: ...
