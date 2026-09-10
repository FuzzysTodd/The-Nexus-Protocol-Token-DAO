import _plotly_utils.basevalidators

class FillruleValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(self, plotly_name: str = 'fillrule', parent_name: str = 'layout.newshape', **kwargs) -> None: ...
