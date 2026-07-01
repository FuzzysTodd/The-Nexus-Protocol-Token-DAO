import _plotly_utils.basevalidators

class ColorscalesValidator(_plotly_utils.basevalidators.CompoundArrayValidator):
    def __init__(self, plotly_name: str = 'colorscales', parent_name: str = 'sankey.link', **kwargs) -> None: ...
