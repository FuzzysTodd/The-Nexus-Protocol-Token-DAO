import _plotly_utils.basevalidators

class LabelValidator(_plotly_utils.basevalidators.StringValidator):
    def __init__(self, plotly_name: str = 'label', parent_name: str = 'layout.updatemenu.button', **kwargs) -> None: ...
