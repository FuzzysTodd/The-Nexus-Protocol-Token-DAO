import _plotly_utils.basevalidators

class SpikesidesValidator(_plotly_utils.basevalidators.BooleanValidator):
    def __init__(self, plotly_name: str = 'spikesides', parent_name: str = 'layout.scene.zaxis', **kwargs) -> None: ...
