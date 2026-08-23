import _plotly_utils.basevalidators

class DimensionsValidator(_plotly_utils.basevalidators.CompoundArrayValidator):
    def __init__(self, plotly_name: str = 'dimensions', parent_name: str = 'parcats', **kwargs) -> None: ...
