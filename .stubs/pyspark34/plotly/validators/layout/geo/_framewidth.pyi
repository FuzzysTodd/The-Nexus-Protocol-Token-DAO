import _plotly_utils.basevalidators

class FramewidthValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name: str = 'framewidth', parent_name: str = 'layout.geo', **kwargs) -> None: ...
