import _plotly_utils.basevalidators

class SymmetricValidator(_plotly_utils.basevalidators.BooleanValidator):
    def __init__(self, plotly_name: str = 'symmetric', parent_name: str = 'scattergl.error_y', **kwargs) -> None: ...
