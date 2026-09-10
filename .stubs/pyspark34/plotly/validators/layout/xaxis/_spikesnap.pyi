import _plotly_utils.basevalidators

class SpikesnapValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(self, plotly_name: str = 'spikesnap', parent_name: str = 'layout.xaxis', **kwargs) -> None: ...
