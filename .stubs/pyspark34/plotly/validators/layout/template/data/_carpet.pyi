import _plotly_utils.basevalidators

class CarpetValidator(_plotly_utils.basevalidators.CompoundArrayValidator):
    def __init__(self, plotly_name: str = 'carpet', parent_name: str = 'layout.template.data', **kwargs) -> None: ...
