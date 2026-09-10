import _plotly_utils.basevalidators

class PeriodValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name: str = 'period', parent_name: str = 'layout.polar.angularaxis', **kwargs) -> None: ...
