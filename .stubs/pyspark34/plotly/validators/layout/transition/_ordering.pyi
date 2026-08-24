import _plotly_utils.basevalidators

class OrderingValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(self, plotly_name: str = 'ordering', parent_name: str = 'layout.transition', **kwargs) -> None: ...
