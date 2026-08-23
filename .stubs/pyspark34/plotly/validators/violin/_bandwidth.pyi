import _plotly_utils.basevalidators

class BandwidthValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name: str = 'bandwidth', parent_name: str = 'violin', **kwargs) -> None: ...
