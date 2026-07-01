import _plotly_utils.basevalidators

class ZaxisValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name: str = 'zaxis', parent_name: str = 'layout.scene', **kwargs) -> None: ...
