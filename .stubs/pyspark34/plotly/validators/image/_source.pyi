import _plotly_utils.basevalidators

class SourceValidator(_plotly_utils.basevalidators.StringValidator):
    def __init__(self, plotly_name: str = 'source', parent_name: str = 'image', **kwargs) -> None: ...
