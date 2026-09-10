import _plotly_utils.basevalidators

class AutoexpandValidator(_plotly_utils.basevalidators.BooleanValidator):
    def __init__(self, plotly_name: str = 'autoexpand', parent_name: str = 'layout.margin', **kwargs) -> None: ...
