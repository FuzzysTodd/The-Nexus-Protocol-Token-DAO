import _plotly_utils.basevalidators

class NcontoursValidator(_plotly_utils.basevalidators.IntegerValidator):
    def __init__(self, plotly_name: str = 'ncontours', parent_name: str = 'histogram2dcontour', **kwargs) -> None: ...
