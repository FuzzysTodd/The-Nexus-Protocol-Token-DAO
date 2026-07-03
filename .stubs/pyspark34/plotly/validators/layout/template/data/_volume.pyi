import _plotly_utils.basevalidators

class VolumeValidator(_plotly_utils.basevalidators.CompoundArrayValidator):
    def __init__(self, plotly_name: str = 'volume', parent_name: str = 'layout.template.data', **kwargs) -> None: ...
