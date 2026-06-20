import abc
from _typeshed import Incomplete
from pip._internal.index.package_finder import PackageFinder as PackageFinder
from pip._internal.metadata.base import BaseDistribution as BaseDistribution
from pip._internal.req import InstallRequirement as InstallRequirement

class AbstractDistribution(metaclass=abc.ABCMeta):
    """A base class for handling installable artifacts.

    The requirements for anything installable are as follows:

     - we must be able to determine the requirement name
       (or we can't correctly handle the non-upgrade case).

     - for packages with setup requirements, we must also be able
       to determine their requirements without installing additional
       packages (for the same reason as run-time dependencies)

     - we must be able to create a Distribution object exposing the
       above metadata.

     - if we need to do work in the build tracker, we must be able to generate a unique
       string to identify the requirement in the build tracker.
    """
    req: Incomplete
    def __init__(self, req: InstallRequirement) -> None: ...
    @property
    @abc.abstractmethod
    def build_tracker_id(self) -> str | None:
        """A string that uniquely identifies this requirement to the build tracker.

        If None, then this dist has no work to do in the build tracker, and
        ``.prepare_distribution_metadata()`` will not be called."""
    @abc.abstractmethod
    def get_metadata_distribution(self) -> BaseDistribution: ...
    @abc.abstractmethod
    def prepare_distribution_metadata(self, finder: PackageFinder, build_isolation: bool, check_build_deps: bool) -> None: ...
