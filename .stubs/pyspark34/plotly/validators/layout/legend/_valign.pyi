import _plotly_utils.basevalidators

class ValignValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(self, plotly_name: str = 'valign', parent_name: str = 'layout.legend', **kwargs) -> None: ...
