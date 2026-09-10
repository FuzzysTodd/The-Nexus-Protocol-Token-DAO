import _plotly_utils.basevalidators

class AnnotationsValidator(_plotly_utils.basevalidators.CompoundArrayValidator):
    def __init__(self, plotly_name: str = 'annotations', parent_name: str = 'layout.scene', **kwargs) -> None: ...
