import plotly.validators

class DataValidator(plotly.validators.DataValidator):
    def __init__(self, plotly_name: str = 'data', parent_name: str = 'frame', **kwargs) -> None: ...
