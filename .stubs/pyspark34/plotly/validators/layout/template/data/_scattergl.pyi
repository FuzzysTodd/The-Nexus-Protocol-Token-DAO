import _plotly_utils.basevalidators

class ScatterglValidator(_plotly_utils.basevalidators.CompoundArrayValidator):
    def __init__(self, plotly_name: str = 'scattergl', parent_name: str = 'layout.template.data', **kwargs) -> None: ...
