import _plotly_utils.basevalidators

class AlignValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(self, plotly_name: str = 'align', parent_name: str = 'histogram.hoverlabel', **kwargs) -> None: ...
