import _plotly_utils.basevalidators

class SplomValidator(_plotly_utils.basevalidators.CompoundArrayValidator):
    def __init__(self, plotly_name: str = 'splom', parent_name: str = 'layout.template.data', **kwargs) -> None: ...
