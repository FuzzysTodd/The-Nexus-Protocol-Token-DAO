import _plotly_utils.basevalidators

class SpikemodeValidator(_plotly_utils.basevalidators.FlaglistValidator):
    def __init__(self, plotly_name: str = 'spikemode', parent_name: str = 'layout.xaxis', **kwargs) -> None: ...
