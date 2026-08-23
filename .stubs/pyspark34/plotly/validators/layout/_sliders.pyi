import _plotly_utils.basevalidators

class SlidersValidator(_plotly_utils.basevalidators.CompoundArrayValidator):
    def __init__(self, plotly_name: str = 'sliders', parent_name: str = 'layout', **kwargs) -> None: ...
