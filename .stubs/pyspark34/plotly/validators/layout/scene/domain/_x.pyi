import _plotly_utils.basevalidators

class XValidator(_plotly_utils.basevalidators.InfoArrayValidator):
    def __init__(self, plotly_name: str = 'x', parent_name: str = 'layout.scene.domain', **kwargs) -> None: ...
