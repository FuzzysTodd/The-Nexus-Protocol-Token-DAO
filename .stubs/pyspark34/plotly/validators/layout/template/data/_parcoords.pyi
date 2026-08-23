import _plotly_utils.basevalidators

class ParcoordsValidator(_plotly_utils.basevalidators.CompoundArrayValidator):
    def __init__(self, plotly_name: str = 'parcoords', parent_name: str = 'layout.template.data', **kwargs) -> None: ...
