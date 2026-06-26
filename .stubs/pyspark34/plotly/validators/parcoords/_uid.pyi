import _plotly_utils.basevalidators

class UidValidator(_plotly_utils.basevalidators.StringValidator):
    def __init__(self, plotly_name: str = 'uid', parent_name: str = 'parcoords', **kwargs) -> None: ...
