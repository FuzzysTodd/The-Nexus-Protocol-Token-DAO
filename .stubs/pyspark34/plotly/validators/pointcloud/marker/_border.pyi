import _plotly_utils.basevalidators

class BorderValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name: str = 'border', parent_name: str = 'pointcloud.marker', **kwargs) -> None: ...
