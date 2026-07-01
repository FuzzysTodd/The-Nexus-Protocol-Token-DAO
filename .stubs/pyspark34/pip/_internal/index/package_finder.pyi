import enum
from _typeshed import Incomplete
from pip._internal.index.collector import LinkCollector
from pip._internal.models.candidate import InstallationCandidate
from pip._internal.models.format_control import FormatControl as FormatControl
from pip._internal.models.link import Link
from pip._internal.models.search_scope import SearchScope
from pip._internal.models.selection_prefs import SelectionPreferences
from pip._internal.models.target_python import TargetPython
from pip._internal.req import InstallRequirement
from pip._internal.utils.hashes import Hashes
from pip._vendor.packaging import specifiers
from pip._vendor.packaging.tags import Tag
from typing import FrozenSet, Iterable, List, Tuple

__all__ = ['FormatControl', 'BestCandidateResult', 'PackageFinder']

BuildTag = Tuple[()] | Tuple[int, str]

class LinkType(enum.Enum):
    candidate: Incomplete
    different_project: Incomplete
    yanked: Incomplete
    format_unsupported: Incomplete
    format_invalid: Incomplete
    platform_mismatch: Incomplete
    requires_python_mismatch: Incomplete

class LinkEvaluator:
    """
    Responsible for evaluating links for a particular project.
    """
    project_name: Incomplete
    def __init__(self, project_name: str, canonical_name: str, formats: FrozenSet[str], target_python: TargetPython, allow_yanked: bool, ignore_requires_python: bool | None = None) -> None:
        '''
        :param project_name: The user supplied package name.
        :param canonical_name: The canonical package name.
        :param formats: The formats allowed for this package. Should be a set
            with \'binary\' or \'source\' or both in it.
        :param target_python: The target Python interpreter to use when
            evaluating link compatibility. This is used, for example, to
            check wheel compatibility, as well as when checking the Python
            version, e.g. the Python version embedded in a link filename
            (or egg fragment) and against an HTML link\'s optional PEP 503
            "data-requires-python" attribute.
        :param allow_yanked: Whether files marked as yanked (in the sense
            of PEP 592) are permitted to be candidates for install.
        :param ignore_requires_python: Whether to ignore incompatible
            PEP 503 "data-requires-python" values in HTML links. Defaults
            to False.
        '''
    def evaluate_link(self, link: Link) -> Tuple[LinkType, str]:
        """
        Determine whether a link is a candidate for installation.

        :return: A tuple (result, detail), where *result* is an enum
            representing whether the evaluation found a candidate, or the reason
            why one is not found. If a candidate is found, *detail* will be the
            candidate's version string; if one is not found, it contains the
            reason the link fails to qualify.
        """

class CandidatePreferences:
    """
    Encapsulates some of the preferences for filtering and sorting
    InstallationCandidate objects.
    """
    allow_all_prereleases: Incomplete
    prefer_binary: Incomplete
    def __init__(self, prefer_binary: bool = False, allow_all_prereleases: bool = False) -> None:
        """
        :param allow_all_prereleases: Whether to allow all pre-releases.
        """

class BestCandidateResult:
    """A collection of candidates, returned by `PackageFinder.find_best_candidate`.

    This class is only intended to be instantiated by CandidateEvaluator's
    `compute_best_candidate()` method.
    """
    best_candidate: Incomplete
    def __init__(self, candidates: List[InstallationCandidate], applicable_candidates: List[InstallationCandidate], best_candidate: InstallationCandidate | None) -> None:
        """
        :param candidates: A sequence of all available candidates found.
        :param applicable_candidates: The applicable candidates.
        :param best_candidate: The most preferred candidate found, or None
            if no applicable candidates were found.
        """
    def iter_all(self) -> Iterable[InstallationCandidate]:
        """Iterate through all candidates."""
    def iter_applicable(self) -> Iterable[InstallationCandidate]:
        """Iterate through the applicable candidates."""

class CandidateEvaluator:
    """
    Responsible for filtering and sorting candidates for installation based
    on what tags are valid.
    """
    @classmethod
    def create(cls, project_name: str, target_python: TargetPython | None = None, prefer_binary: bool = False, allow_all_prereleases: bool = False, specifier: specifiers.BaseSpecifier | None = None, hashes: Hashes | None = None) -> CandidateEvaluator:
        """Create a CandidateEvaluator object.

        :param target_python: The target Python interpreter to use when
            checking compatibility. If None (the default), a TargetPython
            object will be constructed from the running Python.
        :param specifier: An optional object implementing `filter`
            (e.g. `packaging.specifiers.SpecifierSet`) to filter applicable
            versions.
        :param hashes: An optional collection of allowed hashes.
        """
    def __init__(self, project_name: str, supported_tags: List[Tag], specifier: specifiers.BaseSpecifier, prefer_binary: bool = False, allow_all_prereleases: bool = False, hashes: Hashes | None = None) -> None:
        """
        :param supported_tags: The PEP 425 tags supported by the target
            Python in order of preference (most preferred first).
        """
    def get_applicable_candidates(self, candidates: List[InstallationCandidate]) -> List[InstallationCandidate]:
        """
        Return the applicable candidates from a list of candidates.
        """
    def sort_best_candidate(self, candidates: List[InstallationCandidate]) -> InstallationCandidate | None:
        """
        Return the best candidate per the instance's sort order, or None if
        no candidate is acceptable.
        """
    def compute_best_candidate(self, candidates: List[InstallationCandidate]) -> BestCandidateResult:
        """
        Compute and return a `BestCandidateResult` instance.
        """

class PackageFinder:
    """This finds packages.

    This is meant to match easy_install's technique for looking for
    packages, by reading pages and looking for appropriate links.
    """
    format_control: Incomplete
    def __init__(self, link_collector: LinkCollector, target_python: TargetPython, allow_yanked: bool, format_control: FormatControl | None = None, candidate_prefs: CandidatePreferences | None = None, ignore_requires_python: bool | None = None) -> None:
        """
        This constructor is primarily meant to be used by the create() class
        method and from tests.

        :param format_control: A FormatControl object, used to control
            the selection of source packages / binary packages when consulting
            the index and links.
        :param candidate_prefs: Options to use when creating a
            CandidateEvaluator object.
        """
    @classmethod
    def create(cls, link_collector: LinkCollector, selection_prefs: SelectionPreferences, target_python: TargetPython | None = None) -> PackageFinder:
        """Create a PackageFinder.

        :param selection_prefs: The candidate selection preferences, as a
            SelectionPreferences object.
        :param target_python: The target Python interpreter to use when
            checking compatibility. If None (the default), a TargetPython
            object will be constructed from the running Python.
        """
    @property
    def target_python(self) -> TargetPython: ...
    @property
    def search_scope(self) -> SearchScope: ...
    @search_scope.setter
    def search_scope(self, search_scope: SearchScope) -> None: ...
    @property
    def find_links(self) -> List[str]: ...
    @property
    def index_urls(self) -> List[str]: ...
    @property
    def trusted_hosts(self) -> Iterable[str]: ...
    @property
    def allow_all_prereleases(self) -> bool: ...
    def set_allow_all_prereleases(self) -> None: ...
    @property
    def prefer_binary(self) -> bool: ...
    def set_prefer_binary(self) -> None: ...
    def requires_python_skipped_reasons(self) -> List[str]: ...
    def make_link_evaluator(self, project_name: str) -> LinkEvaluator: ...
    def get_install_candidate(self, link_evaluator: LinkEvaluator, link: Link) -> InstallationCandidate | None:
        """
        If the link is a candidate for install, convert it to an
        InstallationCandidate and return it. Otherwise, return None.
        """
    def evaluate_links(self, link_evaluator: LinkEvaluator, links: Iterable[Link]) -> List[InstallationCandidate]:
        """
        Convert links that are candidates to InstallationCandidate objects.
        """
    def process_project_url(self, project_url: Link, link_evaluator: LinkEvaluator) -> List[InstallationCandidate]: ...
    def find_all_candidates(self, project_name: str) -> List[InstallationCandidate]:
        """Find all available InstallationCandidate for project_name

        This checks index_urls and find_links.
        All versions found are returned as an InstallationCandidate list.

        See LinkEvaluator.evaluate_link() for details on which files
        are accepted.
        """
    def make_candidate_evaluator(self, project_name: str, specifier: specifiers.BaseSpecifier | None = None, hashes: Hashes | None = None) -> CandidateEvaluator:
        """Create a CandidateEvaluator object to use."""
    def find_best_candidate(self, project_name: str, specifier: specifiers.BaseSpecifier | None = None, hashes: Hashes | None = None) -> BestCandidateResult:
        """Find matches for the given project and specifier.

        :param specifier: An optional object implementing `filter`
            (e.g. `packaging.specifiers.SpecifierSet`) to filter applicable
            versions.

        :return: A `BestCandidateResult` instance.
        """
    def find_requirement(self, req: InstallRequirement, upgrade: bool) -> InstallationCandidate | None:
        """Try to find a Link matching req

        Expects req, an InstallRequirement and upgrade, a boolean
        Returns a InstallationCandidate if found,
        Raises DistributionNotFound or BestVersionAlreadyInstalled otherwise
        """
