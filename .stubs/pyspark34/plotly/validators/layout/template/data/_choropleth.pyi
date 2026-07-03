import _plotly_utils.basevalidators

class ChoroplethValidator(_plotly_utils.basevalidators.CompoundArrayValidator):
    def __init__(self, plotly_name: str = 'choropleth', parent_name: str = 'layout.template.data', **kwargs) -> None: ...
