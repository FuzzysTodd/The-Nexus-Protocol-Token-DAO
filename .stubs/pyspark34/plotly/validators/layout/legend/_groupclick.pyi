import _plotly_utils.basevalidators

class GroupclickValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(self, plotly_name: str = 'groupclick', parent_name: str = 'layout.legend', **kwargs) -> None: ...
