import _plotly_utils.basevalidators

class CaptureeventsValidator(_plotly_utils.basevalidators.BooleanValidator):
    def __init__(self, plotly_name: str = 'captureevents', parent_name: str = 'layout.annotation', **kwargs) -> None: ...
