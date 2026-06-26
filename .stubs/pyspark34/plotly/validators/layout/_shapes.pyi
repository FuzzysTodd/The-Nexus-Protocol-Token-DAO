import _plotly_utils.basevalidators

class ShapesValidator(_plotly_utils.basevalidators.CompoundArrayValidator):
    def __init__(self, plotly_name: str = 'shapes', parent_name: str = 'layout', **kwargs) -> None: ...
