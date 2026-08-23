import _plotly_utils.basevalidators

class AccesstokenValidator(_plotly_utils.basevalidators.StringValidator):
    def __init__(self, plotly_name: str = 'accesstoken', parent_name: str = 'layout.mapbox', **kwargs) -> None: ...
