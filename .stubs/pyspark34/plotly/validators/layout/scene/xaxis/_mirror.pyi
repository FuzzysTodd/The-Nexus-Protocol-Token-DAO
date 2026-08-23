import _plotly_utils.basevalidators

class MirrorValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(self, plotly_name: str = 'mirror', parent_name: str = 'layout.scene.xaxis', **kwargs) -> None: ...
