import _plotly_utils.basevalidators

class AspectratioValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name: str = 'aspectratio', parent_name: str = 'layout.scene', **kwargs) -> None: ...
