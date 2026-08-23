import _plotly_utils.basevalidators

class PointcloudValidator(_plotly_utils.basevalidators.CompoundArrayValidator):
    def __init__(self, plotly_name: str = 'pointcloud', parent_name: str = 'layout.template.data', **kwargs) -> None: ...
