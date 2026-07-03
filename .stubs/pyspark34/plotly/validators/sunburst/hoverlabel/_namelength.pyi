import _plotly_utils.basevalidators

class NamelengthValidator(_plotly_utils.basevalidators.IntegerValidator):
    def __init__(self, plotly_name: str = 'namelength', parent_name: str = 'sunburst.hoverlabel', **kwargs) -> None: ...
