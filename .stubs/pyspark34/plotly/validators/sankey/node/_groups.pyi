import _plotly_utils.basevalidators

class GroupsValidator(_plotly_utils.basevalidators.InfoArrayValidator):
    def __init__(self, plotly_name: str = 'groups', parent_name: str = 'sankey.node', **kwargs) -> None: ...
