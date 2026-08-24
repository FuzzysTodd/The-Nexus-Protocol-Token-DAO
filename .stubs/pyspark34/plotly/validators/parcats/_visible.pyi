import _plotly_utils.basevalidators

class VisibleValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(self, plotly_name: str = 'visible', parent_name: str = 'parcats', **kwargs) -> None: ...
