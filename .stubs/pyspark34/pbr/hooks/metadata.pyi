from pbr import packaging as packaging
from pbr.hooks import base as base

class MetadataConfig(base.BaseConfig):
    section: str
    def hook(self) -> None: ...
    def get_name(self): ...
