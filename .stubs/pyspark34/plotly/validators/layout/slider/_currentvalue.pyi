import _plotly_utils.basevalidators

class CurrentvalueValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name: str = 'currentvalue', parent_name: str = 'layout.slider', **kwargs) -> None: ...
