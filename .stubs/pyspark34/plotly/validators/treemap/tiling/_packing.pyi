import _plotly_utils.basevalidators

class PackingValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(self, plotly_name: str = 'packing', parent_name: str = 'treemap.tiling', **kwargs) -> None: ...
