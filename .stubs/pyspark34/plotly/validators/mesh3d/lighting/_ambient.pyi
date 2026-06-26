import _plotly_utils.basevalidators

class AmbientValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name: str = 'ambient', parent_name: str = 'mesh3d.lighting', **kwargs) -> None: ...
