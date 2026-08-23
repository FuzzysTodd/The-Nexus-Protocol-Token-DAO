import _plotly_utils.basevalidators

class CalendarValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(self, plotly_name: str = 'calendar', parent_name: str = 'layout.scene.zaxis', **kwargs) -> None: ...
