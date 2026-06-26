import _plotly_utils.basevalidators

class AxrefValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(self, plotly_name: str = 'axref', parent_name: str = 'layout.annotation', **kwargs) -> None: ...
