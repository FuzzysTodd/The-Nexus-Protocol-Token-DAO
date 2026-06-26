import _plotly_utils.basevalidators

class ArrangementValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(self, plotly_name: str = 'arrangement', parent_name: str = 'parcats', **kwargs) -> None: ...
