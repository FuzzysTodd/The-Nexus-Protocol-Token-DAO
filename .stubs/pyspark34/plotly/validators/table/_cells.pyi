import _plotly_utils.basevalidators

class CellsValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name: str = 'cells', parent_name: str = 'table', **kwargs) -> None: ...
