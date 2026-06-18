import _plotly_utils.basevalidators

class StreamtubeValidator(_plotly_utils.basevalidators.CompoundArrayValidator):
    def __init__(self, plotly_name: str = 'streamtube', parent_name: str = 'layout.template.data', **kwargs) -> None: ...
