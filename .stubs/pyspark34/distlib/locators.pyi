from . import DistlibException as DistlibException
from .compat import HTTPError as HTTPError, HTTPRedirectHandler as BaseRedirectHandler, Request as Request, URLError as URLError, build_opener as build_opener, pathname2url as pathname2url, queue as queue, quote as quote, text_type as text_type, unescape as unescape, url2pathname as url2pathname, urljoin as urljoin, urlparse as urlparse, urlunparse as urlunparse
from .database import Distribution as Distribution, DistributionPath as DistributionPath, make_dist as make_dist
from .metadata import Metadata as Metadata, MetadataInvalidError as MetadataInvalidError
from .util import ServerProxy as ServerProxy, cached_property as cached_property, ensure_slash as ensure_slash, get_project_data as get_project_data, normalize_name as normalize_name, parse_name_and_version as parse_name_and_version, parse_requirement as parse_requirement, split_filename as split_filename
from .version import UnsupportedVersionError as UnsupportedVersionError, get_scheme as get_scheme
from .wheel import Wheel as Wheel, is_compatible as is_compatible
from _typeshed import Incomplete

logger: Incomplete
HASHER_HASH: Incomplete
CHARSET: Incomplete
HTML_CONTENT_TYPE: Incomplete
DEFAULT_INDEX: str

def get_all_distribution_names(url: Incomplete | None = None):
    """
    Return all distribution names known by an index.
    :param url: The URL of the index.
    :return: A list of all known distribution names.
    """

class RedirectHandler(BaseRedirectHandler):
    """
    A class to work around a bug in some Python 3.2.x releases.
    """
    def http_error_302(self, req, fp, code, msg, headers): ...
    http_error_301 = http_error_302
    http_error_303 = http_error_302
    http_error_307 = http_error_302

class Locator:
    """
    A base class for locators - things that locate distributions.
    """
    source_extensions: Incomplete
    binary_extensions: Incomplete
    excluded_extensions: Incomplete
    wheel_tags: Incomplete
    downloadable_extensions: Incomplete
    scheme: Incomplete
    opener: Incomplete
    matcher: Incomplete
    errors: Incomplete
    def __init__(self, scheme: str = 'default') -> None:
        """
        Initialise an instance.
        :param scheme: Because locators look for most recent versions, they
                       need to know the version scheme to use. This specifies
                       the current PEP-recommended scheme - use ``'legacy'``
                       if you need to support existing distributions on PyPI.
        """
    def get_errors(self):
        """
        Return any errors which have occurred.
        """
    def clear_errors(self) -> None:
        """
        Clear any errors which may have been logged.
        """
    def clear_cache(self) -> None: ...
    def get_distribution_names(self) -> None:
        """
        Return all the distribution names known to this locator.
        """
    def get_project(self, name):
        """
        For a given project, get a dictionary mapping available versions to Distribution
        instances.

        This calls _get_project to do all the work, and just implements a caching layer on top.
        """
    def score_url(self, url):
        """
        Give an url a score which can be used to choose preferred URLs
        for a given project release.
        """
    def prefer_url(self, url1, url2):
        """
        Choose one of two URLs where both are candidates for distribution
        archives for the same version of a distribution (for example,
        .tar.gz vs. zip).

        The current implementation favours https:// URLs over http://, archives
        from PyPI over those from other locations, wheel compatibility (if a
        wheel) and then the archive name.
        """
    def split_filename(self, filename, project_name):
        """
        Attempt to split a filename in project name, version and Python version.
        """
    def convert_url_to_download_info(self, url, project_name):
        '''
        See if a URL is a candidate for a download URL for a project (the URL
        has typically been scraped from an HTML page).

        If it is, a dictionary is returned with keys "name", "version",
        "filename" and "url"; otherwise, None is returned.
        '''
    def locate(self, requirement, prereleases: bool = False):
        """
        Find the most recent distribution which matches the given
        requirement.

        :param requirement: A requirement of the form 'foo (1.0)' or perhaps
                            'foo (>= 1.0, < 2.0, != 1.3)'
        :param prereleases: If ``True``, allow pre-release versions
                            to be located. Otherwise, pre-release versions
                            are not returned.
        :return: A :class:`Distribution` instance, or ``None`` if no such
                 distribution could be located.
        """

class PyPIRPCLocator(Locator):
    """
    This locator uses XML-RPC to locate distributions. It therefore
    cannot be used with simple mirrors (that only mirror file content).
    """
    base_url: Incomplete
    client: Incomplete
    def __init__(self, url, **kwargs) -> None:
        """
        Initialise an instance.

        :param url: The URL to use for XML-RPC.
        :param kwargs: Passed to the superclass constructor.
        """
    def get_distribution_names(self):
        """
        Return all the distribution names known to this locator.
        """

class PyPIJSONLocator(Locator):
    """
    This locator uses PyPI's JSON interface. It's very limited in functionality
    and probably not worth using.
    """
    base_url: Incomplete
    def __init__(self, url, **kwargs) -> None: ...
    def get_distribution_names(self) -> None:
        """
        Return all the distribution names known to this locator.
        """

class Page:
    """
    This class represents a scraped HTML page.
    """
    data: Incomplete
    base_url: Incomplete
    def __init__(self, data, url) -> None:
        """
        Initialise an instance with the Unicode page contents and the URL they
        came from.
        """
    def links(self):
        '''
        Return the URLs of all the links on a page together with information
        about their "rel" attribute, for determining which ones to treat as
        downloads and which ones to queue for further scraping.
        '''

class SimpleScrapingLocator(Locator):
    """
    A locator which scrapes HTML pages to locate downloads for a distribution.
    This runs multiple threads to do the I/O; performance is at least as good
    as pip's PackageFinder, which works in an analogous fashion.
    """
    decoders: Incomplete
    base_url: Incomplete
    timeout: Incomplete
    skip_externals: bool
    num_workers: Incomplete
    platform_check: bool
    def __init__(self, url, timeout: Incomplete | None = None, num_workers: int = 10, **kwargs) -> None:
        """
        Initialise an instance.
        :param url: The root URL to use for scraping.
        :param timeout: The timeout, in seconds, to be applied to requests.
                        This defaults to ``None`` (no timeout specified).
        :param num_workers: The number of worker threads you want to do I/O,
                            This defaults to 10.
        :param kwargs: Passed to the superclass.
        """
    platform_dependent: Incomplete
    def get_page(self, url):
        """
        Get the HTML for an URL, possibly from an in-memory cache.

        XXX TODO Note: this cache is never actually cleared. It's assumed that
        the data won't get stale over the lifetime of a locator instance (not
        necessarily true for the default_locator).
        """
    def get_distribution_names(self):
        """
        Return all the distribution names known to this locator.
        """

class DirectoryLocator(Locator):
    """
    This class locates distributions in a directory tree.
    """
    recursive: Incomplete
    base_dir: Incomplete
    def __init__(self, path, **kwargs) -> None:
        """
        Initialise an instance.
        :param path: The root of the directory tree to search.
        :param kwargs: Passed to the superclass constructor,
                       except for:
                       * recursive - if True (the default), subdirectories are
                         recursed into. If False, only the top-level directory
                         is searched,
        """
    def should_include(self, filename, parent):
        """
        Should a filename be considered as a candidate for a distribution
        archive? As well as the filename, the directory which contains it
        is provided, though not used by the current implementation.
        """
    def get_distribution_names(self):
        """
        Return all the distribution names known to this locator.
        """

class JSONLocator(Locator):
    """
    This locator uses special extended metadata (not available on PyPI) and is
    the basis of performant dependency resolution in distlib. Other locators
    require archive downloads before dependencies can be determined! As you
    might imagine, that can be slow.
    """
    def get_distribution_names(self) -> None:
        """
        Return all the distribution names known to this locator.
        """

class DistPathLocator(Locator):
    """
    This locator finds installed distributions in a path. It can be useful for
    adding to an :class:`AggregatingLocator`.
    """
    distpath: Incomplete
    def __init__(self, distpath, **kwargs) -> None:
        """
        Initialise an instance.

        :param distpath: A :class:`DistributionPath` instance to search.
        """

class AggregatingLocator(Locator):
    """
    This class allows you to chain and/or merge a list of locators.
    """
    merge: Incomplete
    locators: Incomplete
    def __init__(self, *locators, **kwargs) -> None:
        """
        Initialise an instance.

        :param locators: The list of locators to search.
        :param kwargs: Passed to the superclass constructor,
                       except for:
                       * merge - if False (the default), the first successful
                         search from any of the locators is returned. If True,
                         the results from all locators are merged (this can be
                         slow).
        """
    def clear_cache(self) -> None: ...
    scheme: Incomplete
    def get_distribution_names(self):
        """
        Return all the distribution names known to this locator.
        """

default_locator: Incomplete
locate: Incomplete

class DependencyFinder:
    """
    Locate dependencies for distributions.
    """
    locator: Incomplete
    scheme: Incomplete
    def __init__(self, locator: Incomplete | None = None) -> None:
        """
        Initialise an instance, using the specified locator
        to locate distributions.
        """
    def add_distribution(self, dist) -> None:
        """
        Add a distribution to the finder. This will update internal information
        about who provides what.
        :param dist: The distribution to add.
        """
    def remove_distribution(self, dist) -> None:
        """
        Remove a distribution from the finder. This will update internal
        information about who provides what.
        :param dist: The distribution to remove.
        """
    def get_matcher(self, reqt):
        """
        Get a version matcher for a requirement.
        :param reqt: The requirement
        :type reqt: str
        :return: A version matcher (an instance of
                 :class:`distlib.version.Matcher`).
        """
    def find_providers(self, reqt):
        """
        Find the distributions which can fulfill a requirement.

        :param reqt: The requirement.
         :type reqt: str
        :return: A set of distribution which can fulfill the requirement.
        """
    def try_to_replace(self, provider, other, problems):
        """
        Attempt to replace one provider with another. This is typically used
        when resolving dependencies from multiple sources, e.g. A requires
        (B >= 1.0) while C requires (B >= 1.1).

        For successful replacement, ``provider`` must meet all the requirements
        which ``other`` fulfills.

        :param provider: The provider we are trying to replace with.
        :param other: The provider we're trying to replace.
        :param problems: If False is returned, this will contain what
                         problems prevented replacement. This is currently
                         a tuple of the literal string 'cantreplace',
                         ``provider``, ``other``  and the set of requirements
                         that ``provider`` couldn't fulfill.
        :return: True if we can replace ``other`` with ``provider``, else
                 False.
        """
    provided: Incomplete
    dists: Incomplete
    dists_by_name: Incomplete
    reqts: Incomplete
    def find(self, requirement, meta_extras: Incomplete | None = None, prereleases: bool = False):
        """
        Find a distribution and all distributions it depends on.

        :param requirement: The requirement specifying the distribution to
                            find, or a Distribution instance.
        :param meta_extras: A list of meta extras such as :test:, :build: and
                            so on.
        :param prereleases: If ``True``, allow pre-release versions to be
                            returned - otherwise, don't return prereleases
                            unless they're all that's available.

        Return a set of :class:`Distribution` instances and a set of
        problems.

        The distributions returned should be such that they have the
        :attr:`required` attribute set to ``True`` if they were
        from the ``requirement`` passed to ``find()``, and they have the
        :attr:`build_time_dependency` attribute set to ``True`` unless they
        are post-installation dependencies of the ``requirement``.

        The problems should be a tuple consisting of the string
        ``'unsatisfied'`` and the requirement which couldn't be satisfied
        by any distribution known to the locator.
        """
