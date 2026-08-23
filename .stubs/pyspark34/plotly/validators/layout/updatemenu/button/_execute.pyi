import _plotly_utils.basevalidators

class ExecuteValidator(_plotly_utils.basevalidators.BooleanValidator):
    def __init__(self, plotly_name: str = 'execute', parent_name: str = 'layout.updatemenu.button', **kwargs) -> None: ...
