import _plotly_utils.basevalidators

class AllowoverlapValidator(_plotly_utils.basevalidators.BooleanValidator):
    def __init__(self, plotly_name: str = 'allowoverlap', parent_name: str = 'scattermapbox.marker', **kwargs) -> None: ...
