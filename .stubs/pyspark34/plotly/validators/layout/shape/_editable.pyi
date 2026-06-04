import _plotly_utils.basevalidators

class EditableValidator(_plotly_utils.basevalidators.BooleanValidator):
    def __init__(self, plotly_name: str = 'editable', parent_name: str = 'layout.shape', **kwargs) -> None: ...
