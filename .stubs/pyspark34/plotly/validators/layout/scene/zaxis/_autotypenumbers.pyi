import _plotly_utils.basevalidators

class AutotypenumbersValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(self, plotly_name: str = 'autotypenumbers', parent_name: str = 'layout.scene.zaxis', **kwargs) -> None: ...
