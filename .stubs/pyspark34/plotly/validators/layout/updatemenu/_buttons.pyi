import _plotly_utils.basevalidators

class ButtonsValidator(_plotly_utils.basevalidators.CompoundArrayValidator):
    def __init__(self, plotly_name: str = 'buttons', parent_name: str = 'layout.updatemenu', **kwargs) -> None: ...
