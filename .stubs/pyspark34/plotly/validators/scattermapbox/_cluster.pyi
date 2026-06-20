import _plotly_utils.basevalidators

class ClusterValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name: str = 'cluster', parent_name: str = 'scattermapbox', **kwargs) -> None: ...
