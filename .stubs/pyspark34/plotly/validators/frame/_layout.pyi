import plotly.validators

class LayoutValidator(plotly.validators.LayoutValidator):
    def __init__(self, plotly_name: str = 'layout', parent_name: str = 'frame', **kwargs) -> None: ...
