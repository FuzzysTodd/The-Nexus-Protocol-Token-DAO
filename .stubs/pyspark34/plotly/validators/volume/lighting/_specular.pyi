import _plotly_utils.basevalidators

class SpecularValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name: str = 'specular', parent_name: str = 'volume.lighting', **kwargs) -> None: ...
