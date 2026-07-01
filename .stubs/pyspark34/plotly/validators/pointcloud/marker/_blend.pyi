import _plotly_utils.basevalidators

class BlendValidator(_plotly_utils.basevalidators.BooleanValidator):
    def __init__(self, plotly_name: str = 'blend', parent_name: str = 'pointcloud.marker', **kwargs) -> None: ...
