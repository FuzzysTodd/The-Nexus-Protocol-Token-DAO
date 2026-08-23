import _plotly_utils.basevalidators

class ShowticklabelsValidator(_plotly_utils.basevalidators.BooleanValidator):
    def __init__(self, plotly_name: str = 'showticklabels', parent_name: str = 'layout.coloraxis.colorbar', **kwargs) -> None: ...
