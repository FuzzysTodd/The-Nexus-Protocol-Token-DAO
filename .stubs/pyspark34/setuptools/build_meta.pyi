import setuptools
from _typeshed import Incomplete
from collections.abc import Generator

__all__ = ['get_requires_for_build_sdist', 'get_requires_for_build_wheel', 'prepare_metadata_for_build_wheel', 'build_wheel', 'build_sdist', 'get_requires_for_build_editable', 'prepare_metadata_for_build_editable', 'build_editable', '__legacy__', 'SetupRequirementsError']

class SetupRequirementsError(BaseException):
    specifiers: Incomplete
    def __init__(self, specifiers) -> None: ...

class Distribution(setuptools.dist.Distribution):
    def fetch_build_eggs(self, specifiers) -> None: ...
    @classmethod
    def patch(cls) -> Generator[None, None, None]:
        """
        Replace
        distutils.dist.Distribution with this class
        for the duration of this context.
        """

class _ConfigSettingsTranslator:
    """Translate ``config_settings`` into distutils-style command arguments.
    Only a limited number of options is currently supported.
    """

class _BuildMetaBackend(_ConfigSettingsTranslator):
    def run_setup(self, setup_script: str = 'setup.py') -> None: ...
    def get_requires_for_build_wheel(self, config_settings: Incomplete | None = None): ...
    def get_requires_for_build_sdist(self, config_settings: Incomplete | None = None): ...
    def prepare_metadata_for_build_wheel(self, metadata_directory, config_settings: Incomplete | None = None): ...
    def build_wheel(self, wheel_directory, config_settings: Incomplete | None = None, metadata_directory: Incomplete | None = None): ...
    def build_sdist(self, sdist_directory, config_settings: Incomplete | None = None): ...
    def build_editable(self, wheel_directory, config_settings: Incomplete | None = None, metadata_directory: Incomplete | None = None): ...
    def get_requires_for_build_editable(self, config_settings: Incomplete | None = None): ...
    def prepare_metadata_for_build_editable(self, metadata_directory, config_settings: Incomplete | None = None): ...

class _BuildMetaLegacyBackend(_BuildMetaBackend):
    """Compatibility backend for setuptools

    This is a version of setuptools.build_meta that endeavors
    to maintain backwards
    compatibility with pre-PEP 517 modes of invocation. It
    exists as a temporary
    bridge between the old packaging mechanism and the new
    packaging mechanism,
    and will eventually be removed.
    """
    def run_setup(self, setup_script: str = 'setup.py') -> None: ...

get_requires_for_build_wheel: Incomplete
get_requires_for_build_sdist: Incomplete
prepare_metadata_for_build_wheel: Incomplete
build_wheel: Incomplete
build_sdist: Incomplete
get_requires_for_build_editable: Incomplete
prepare_metadata_for_build_editable: Incomplete
build_editable: Incomplete
__legacy__: Incomplete
