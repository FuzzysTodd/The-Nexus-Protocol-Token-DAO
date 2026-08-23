import _plotly_utils.basevalidators

class NameValidator(_plotly_utils.basevalidators.StringValidator):
    def __init__(self, plotly_name: str = 'name', parent_name: str = 'layout.yaxis.rangebreak', **kwargs) -> None: ...
