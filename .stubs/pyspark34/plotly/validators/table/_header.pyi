import _plotly_utils.basevalidators

class HeaderValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name: str = 'header', parent_name: str = 'table', **kwargs) -> None: ...
