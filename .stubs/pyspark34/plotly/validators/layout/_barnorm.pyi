import _plotly_utils.basevalidators

class BarnormValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(self, plotly_name: str = 'barnorm', parent_name: str = 'layout', **kwargs) -> None: ...
