import _plotly_utils.basevalidators

class PieValidator(_plotly_utils.basevalidators.CompoundArrayValidator):
    def __init__(self, plotly_name: str = 'pie', parent_name: str = 'layout.template.data', **kwargs) -> None: ...
