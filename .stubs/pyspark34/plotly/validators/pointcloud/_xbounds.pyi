import _plotly_utils.basevalidators

class XboundsValidator(_plotly_utils.basevalidators.DataArrayValidator):
    def __init__(self, plotly_name: str = 'xbounds', parent_name: str = 'pointcloud', **kwargs) -> None: ...
