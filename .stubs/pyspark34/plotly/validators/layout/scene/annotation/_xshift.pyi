import _plotly_utils.basevalidators

class XshiftValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name: str = 'xshift', parent_name: str = 'layout.scene.annotation', **kwargs) -> None: ...
