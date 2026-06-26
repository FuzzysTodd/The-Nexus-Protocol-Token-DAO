from pbr import packaging as packaging
from pbr.hooks import base as base

class BackwardsCompatConfig(base.BaseConfig):
    section: str
    def hook(self) -> None: ...
