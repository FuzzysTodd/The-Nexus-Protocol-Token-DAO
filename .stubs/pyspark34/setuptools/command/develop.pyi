from _typeshed import Incomplete
from setuptools import namespaces as namespaces
from setuptools.command.easy_install import easy_install as easy_install

class develop(namespaces.DevelopInstaller, easy_install):
    """Set up package for development"""
    description: str
    user_options: Incomplete
    boolean_options: Incomplete
    command_consumes_arguments: bool
    multi_version: bool
    def run(self) -> None: ...
    uninstall: Incomplete
    egg_path: Incomplete
    setup_path: Incomplete
    always_copy_from: str
    def initialize_options(self) -> None: ...
    args: Incomplete
    egg_link: Incomplete
    egg_base: Incomplete
    dist: Incomplete
    def finalize_options(self) -> None: ...
    def install_for_development(self) -> None: ...
    def uninstall_link(self) -> None: ...
    def install_egg_scripts(self, dist): ...
    def install_wrapper_scripts(self, dist): ...

class VersionlessRequirement:
    """
    Adapt a pkg_resources.Distribution to simply return the project
    name as the 'requirement' so that scripts will work across
    multiple versions.

    >>> from pkg_resources import Distribution
    >>> dist = Distribution(project_name='foo', version='1.0')
    >>> str(dist.as_requirement())
    'foo==1.0'
    >>> adapted_dist = VersionlessRequirement(dist)
    >>> str(adapted_dist.as_requirement())
    'foo'
    """
    def __init__(self, dist) -> None: ...
    def __getattr__(self, name): ...
    def as_requirement(self): ...
