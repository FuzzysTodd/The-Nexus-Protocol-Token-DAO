import _plotly_utils.basevalidators

class ProjectValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name: str = 'project', parent_name: str = 'surface.contours.x', **kwargs) -> None: ...
