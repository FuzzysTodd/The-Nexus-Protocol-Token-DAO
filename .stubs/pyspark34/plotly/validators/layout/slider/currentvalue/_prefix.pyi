import _plotly_utils.basevalidators

class PrefixValidator(_plotly_utils.basevalidators.StringValidator):
    def __init__(self, plotly_name: str = 'prefix', parent_name: str = 'layout.slider.currentvalue', **kwargs) -> None: ...
