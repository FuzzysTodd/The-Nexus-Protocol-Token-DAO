import _plotly_utils.basevalidators

class SourceValidator(_plotly_utils.basevalidators.ImageUriValidator):
    def __init__(self, plotly_name: str = 'source', parent_name: str = 'layout.image', **kwargs) -> None: ...
