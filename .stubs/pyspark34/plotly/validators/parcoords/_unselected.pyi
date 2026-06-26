import _plotly_utils.basevalidators

class UnselectedValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name: str = 'unselected', parent_name: str = 'parcoords', **kwargs) -> None: ...
