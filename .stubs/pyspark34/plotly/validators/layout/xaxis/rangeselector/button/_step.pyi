import _plotly_utils.basevalidators

class StepValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(self, plotly_name: str = 'step', parent_name: str = 'layout.xaxis.rangeselector.button', **kwargs) -> None: ...
