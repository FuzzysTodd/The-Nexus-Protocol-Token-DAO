from _typeshed import Incomplete
from collections.abc import Generator
from virtualenv.seed.embed.base_embed import BaseEmbed

__all__ = ['PipInvoke']

class PipInvoke(BaseEmbed):
    def __init__(self, options) -> None: ...
    def run(self, creator) -> None: ...
    def get_pip_install_cmd(self, exe, for_py_version) -> Generator[Incomplete, None, None]: ...
