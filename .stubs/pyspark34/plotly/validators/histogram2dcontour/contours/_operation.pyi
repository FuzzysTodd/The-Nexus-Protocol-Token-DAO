import _plotly_utils.basevalidators

class OperationValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(self, plotly_name: str = 'operation', parent_name: str = 'histogram2dcontour.contours', **kwargs) -> None: ...
