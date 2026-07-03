import _plotly_utils.basevalidators

class GeojsonValidator(_plotly_utils.basevalidators.AnyValidator):
    def __init__(self, plotly_name: str = 'geojson', parent_name: str = 'choropleth', **kwargs) -> None: ...
