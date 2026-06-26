import _plotly_utils.basevalidators

class ShowtickprefixValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(self, plotly_name: str = 'showtickprefix', parent_name: str = 'layout.ternary.caxis', **kwargs) -> None: ...
