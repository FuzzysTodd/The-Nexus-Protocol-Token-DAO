import _plotly_utils.basevalidators

class StepsValidator(_plotly_utils.basevalidators.CompoundArrayValidator):
    def __init__(self, plotly_name: str = 'steps', parent_name: str = 'layout.slider', **kwargs) -> None: ...
