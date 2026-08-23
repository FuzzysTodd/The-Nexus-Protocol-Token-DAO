import _plotly_utils.basevalidators

class EndValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name: str = 'end', parent_name: str = 'surface.contours.z', **kwargs) -> None: ...
