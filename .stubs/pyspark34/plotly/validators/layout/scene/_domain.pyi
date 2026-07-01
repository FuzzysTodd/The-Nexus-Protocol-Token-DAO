import _plotly_utils.basevalidators

class DomainValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name: str = 'domain', parent_name: str = 'layout.scene', **kwargs) -> None: ...
