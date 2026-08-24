import _plotly_utils.basevalidators

class ShowgridValidator(_plotly_utils.basevalidators.BooleanValidator):
    def __init__(self, plotly_name: str = 'showgrid', parent_name: str = 'carpet.baxis', **kwargs) -> None: ...
