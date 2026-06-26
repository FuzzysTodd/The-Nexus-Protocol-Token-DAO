import _plotly_utils.basevalidators

class Mesh3DValidator(_plotly_utils.basevalidators.CompoundArrayValidator):
    def __init__(self, plotly_name: str = 'mesh3d', parent_name: str = 'layout.template.data', **kwargs) -> None: ...
