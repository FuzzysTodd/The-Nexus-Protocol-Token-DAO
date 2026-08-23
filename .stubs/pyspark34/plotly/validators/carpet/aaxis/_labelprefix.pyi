import _plotly_utils.basevalidators

class LabelprefixValidator(_plotly_utils.basevalidators.StringValidator):
    def __init__(self, plotly_name: str = 'labelprefix', parent_name: str = 'carpet.aaxis', **kwargs) -> None: ...
