import _plotly_utils.basevalidators

class FamilyValidator(_plotly_utils.basevalidators.StringValidator):
    def __init__(self, plotly_name: str = 'family', parent_name: str = 'layout.xaxis.title.font', **kwargs) -> None: ...
