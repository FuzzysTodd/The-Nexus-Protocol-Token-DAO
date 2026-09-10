import _plotly_utils.basevalidators

class DiffuseValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name: str = 'diffuse', parent_name: str = 'streamtube.lighting', **kwargs) -> None: ...
