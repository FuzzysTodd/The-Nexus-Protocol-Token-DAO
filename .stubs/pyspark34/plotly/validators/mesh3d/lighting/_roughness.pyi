import _plotly_utils.basevalidators

class RoughnessValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name: str = 'roughness', parent_name: str = 'mesh3d.lighting', **kwargs) -> None: ...
