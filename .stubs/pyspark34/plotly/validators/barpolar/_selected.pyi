import _plotly_utils.basevalidators

class SelectedValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name: str = 'selected', parent_name: str = 'barpolar', **kwargs) -> None: ...
