import _plotly_utils.basevalidators

class AutomarginValidator(_plotly_utils.basevalidators.FlaglistValidator):
    def __init__(self, plotly_name: str = 'automargin', parent_name: str = 'layout.yaxis', **kwargs) -> None: ...
