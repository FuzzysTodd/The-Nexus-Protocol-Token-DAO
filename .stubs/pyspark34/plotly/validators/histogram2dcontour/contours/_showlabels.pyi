import _plotly_utils.basevalidators

class ShowlabelsValidator(_plotly_utils.basevalidators.BooleanValidator):
    def __init__(self, plotly_name: str = 'showlabels', parent_name: str = 'histogram2dcontour.contours', **kwargs) -> None: ...
