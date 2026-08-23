import _plotly_utils.basevalidators

class PitchValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name: str = 'pitch', parent_name: str = 'layout.mapbox', **kwargs) -> None: ...
