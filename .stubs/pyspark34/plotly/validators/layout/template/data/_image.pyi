import _plotly_utils.basevalidators

class ImageValidator(_plotly_utils.basevalidators.CompoundArrayValidator):
    def __init__(self, plotly_name: str = 'image', parent_name: str = 'layout.template.data', **kwargs) -> None: ...
