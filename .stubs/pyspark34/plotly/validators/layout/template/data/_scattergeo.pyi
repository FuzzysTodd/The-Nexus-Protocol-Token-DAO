import _plotly_utils.basevalidators

class ScattergeoValidator(_plotly_utils.basevalidators.CompoundArrayValidator):
    def __init__(self, plotly_name: str = 'scattergeo', parent_name: str = 'layout.template.data', **kwargs) -> None: ...
