import _plotly_utils.basevalidators

class XclickValidator(_plotly_utils.basevalidators.AnyValidator):
    def __init__(self, plotly_name: str = 'xclick', parent_name: str = 'layout.annotation', **kwargs) -> None: ...
