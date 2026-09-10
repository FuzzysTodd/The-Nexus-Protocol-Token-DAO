import _plotly_utils.basevalidators

class DomainValidator(_plotly_utils.basevalidators.InfoArrayValidator):
    def __init__(self, plotly_name: str = 'domain', parent_name: str = 'layout.yaxis', **kwargs) -> None: ...
