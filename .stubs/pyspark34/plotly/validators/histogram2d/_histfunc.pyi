import _plotly_utils.basevalidators

class HistfuncValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(self, plotly_name: str = 'histfunc', parent_name: str = 'histogram2d', **kwargs) -> None: ...
