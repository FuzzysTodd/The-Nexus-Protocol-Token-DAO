import _plotly_utils.basevalidators

class ShowdividersValidator(_plotly_utils.basevalidators.BooleanValidator):
    def __init__(self, plotly_name: str = 'showdividers', parent_name: str = 'layout.xaxis', **kwargs) -> None: ...
