import _plotly_utils.basevalidators

class BarmodeValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(self, plotly_name: str = 'barmode', parent_name: str = 'layout.polar', **kwargs) -> None: ...
