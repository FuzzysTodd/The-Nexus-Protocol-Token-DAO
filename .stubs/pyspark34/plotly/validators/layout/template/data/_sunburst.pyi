import _plotly_utils.basevalidators

class SunburstValidator(_plotly_utils.basevalidators.CompoundArrayValidator):
    def __init__(self, plotly_name: str = 'sunburst', parent_name: str = 'layout.template.data', **kwargs) -> None: ...
