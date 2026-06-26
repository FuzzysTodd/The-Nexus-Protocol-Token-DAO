import _plotly_utils.basevalidators

class StreamValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name: str = 'stream', parent_name: str = 'pie', **kwargs) -> None: ...
