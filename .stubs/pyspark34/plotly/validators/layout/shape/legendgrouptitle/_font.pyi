import _plotly_utils.basevalidators

class FontValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name: str = 'font', parent_name: str = 'layout.shape.legendgrouptitle', **kwargs) -> None: ...
