import _plotly_utils.basevalidators

class AutorangeValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(self, plotly_name: str = 'autorange', parent_name: str = 'carpet.baxis', **kwargs) -> None: ...
