import _plotly_utils.basevalidators

class ParcatsValidator(_plotly_utils.basevalidators.CompoundArrayValidator):
    def __init__(self, plotly_name: str = 'parcats', parent_name: str = 'layout.template.data', **kwargs) -> None: ...
