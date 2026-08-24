import _plotly_utils.basevalidators

class SizemaxValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name: str = 'sizemax', parent_name: str = 'pointcloud.marker', **kwargs) -> None: ...
