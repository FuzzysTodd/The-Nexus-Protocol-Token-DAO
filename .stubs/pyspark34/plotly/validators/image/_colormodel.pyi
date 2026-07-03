import _plotly_utils.basevalidators

class ColormodelValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(self, plotly_name: str = 'colormodel', parent_name: str = 'image', **kwargs) -> None: ...
