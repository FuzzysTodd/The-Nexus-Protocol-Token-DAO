import _plotly_utils.basevalidators

class ScaleratioValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name: str = 'scaleratio', parent_name: str = 'layout.yaxis', **kwargs) -> None: ...
