import _plotly_utils.basevalidators

class ContourValidator(_plotly_utils.basevalidators.CompoundArrayValidator):
    def __init__(self, plotly_name: str = 'contour', parent_name: str = 'layout.template.data', **kwargs) -> None: ...
