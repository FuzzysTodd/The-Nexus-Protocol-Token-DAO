import _plotly_utils.basevalidators

class IcicleValidator(_plotly_utils.basevalidators.CompoundArrayValidator):
    def __init__(self, plotly_name: str = 'icicle', parent_name: str = 'layout.template.data', **kwargs) -> None: ...
