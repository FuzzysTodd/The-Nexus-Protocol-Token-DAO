import _plotly_utils.basevalidators

class AyrefValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(self, plotly_name: str = 'ayref', parent_name: str = 'layout.annotation', **kwargs) -> None: ...
