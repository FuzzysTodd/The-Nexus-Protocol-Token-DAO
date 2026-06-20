import _plotly_utils.basevalidators

class ImagesValidator(_plotly_utils.basevalidators.CompoundArrayValidator):
    def __init__(self, plotly_name: str = 'images', parent_name: str = 'layout', **kwargs) -> None: ...
