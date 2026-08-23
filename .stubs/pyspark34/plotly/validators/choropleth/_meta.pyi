import _plotly_utils.basevalidators

class MetaValidator(_plotly_utils.basevalidators.AnyValidator):
    def __init__(self, plotly_name: str = 'meta', parent_name: str = 'choropleth', **kwargs) -> None: ...
