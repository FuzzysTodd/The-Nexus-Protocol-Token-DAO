import _plotly_utils.basevalidators

class ItemwidthValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name: str = 'itemwidth', parent_name: str = 'layout.legend', **kwargs) -> None: ...
