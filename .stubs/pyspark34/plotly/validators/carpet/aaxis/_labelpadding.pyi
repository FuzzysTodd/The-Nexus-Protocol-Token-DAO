import _plotly_utils.basevalidators

class LabelpaddingValidator(_plotly_utils.basevalidators.IntegerValidator):
    def __init__(self, plotly_name: str = 'labelpadding', parent_name: str = 'carpet.aaxis', **kwargs) -> None: ...
