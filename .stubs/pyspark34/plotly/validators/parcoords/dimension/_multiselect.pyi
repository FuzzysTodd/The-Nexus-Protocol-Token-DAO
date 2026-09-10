import _plotly_utils.basevalidators

class MultiselectValidator(_plotly_utils.basevalidators.BooleanValidator):
    def __init__(self, plotly_name: str = 'multiselect', parent_name: str = 'parcoords.dimension', **kwargs) -> None: ...
