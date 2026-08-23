import _plotly_utils.basevalidators

class FresnelValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name: str = 'fresnel', parent_name: str = 'cone.lighting', **kwargs) -> None: ...
