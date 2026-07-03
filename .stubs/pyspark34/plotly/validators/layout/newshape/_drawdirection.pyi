import _plotly_utils.basevalidators

class DrawdirectionValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(self, plotly_name: str = 'drawdirection', parent_name: str = 'layout.newshape', **kwargs) -> None: ...
