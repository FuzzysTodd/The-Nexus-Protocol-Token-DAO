import _plotly_utils.basevalidators

class RiverwidthValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name: str = 'riverwidth', parent_name: str = 'layout.geo', **kwargs) -> None: ...
