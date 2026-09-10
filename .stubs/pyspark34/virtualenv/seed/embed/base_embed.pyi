from _typeshed import Incomplete
from abc import ABCMeta
from virtualenv.seed.seeder import Seeder
from virtualenv.seed.wheels import Version

__all__ = ['BaseEmbed']

class BaseEmbed(Seeder, metaclass=ABCMeta):
    download: Incomplete
    extra_search_dir: Incomplete
    pip_version: Incomplete
    setuptools_version: Incomplete
    wheel_version: Incomplete
    no_pip: Incomplete
    no_setuptools: Incomplete
    no_wheel: Incomplete
    app_data: Incomplete
    periodic_update: Incomplete
    enabled: bool
    def __init__(self, options) -> None: ...
    @classmethod
    def distributions(cls) -> dict[str, Version]: ...
    def distribution_to_versions(self) -> dict[str, str]: ...
    @classmethod
    def add_parser_arguments(cls, parser, interpreter, app_data) -> None: ...
