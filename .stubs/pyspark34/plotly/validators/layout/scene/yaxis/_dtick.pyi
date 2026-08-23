import _plotly_utils.basevalidators

class DtickValidator(_plotly_utils.basevalidators.AnyValidator):
    def __init__(self, plotly_name: str = 'dtick', parent_name: str = 'layout.scene.yaxis', **kwargs) -> None: ...
