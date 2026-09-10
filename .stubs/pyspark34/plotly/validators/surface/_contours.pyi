import _plotly_utils.basevalidators

class ContoursValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name: str = 'contours', parent_name: str = 'surface', **kwargs) -> None: ...
