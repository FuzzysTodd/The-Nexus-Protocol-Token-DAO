import _plotly_utils.basevalidators

class SizemodeValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(self, plotly_name: str = 'sizemode', parent_name: str = 'scatter3d.marker', **kwargs) -> None: ...
