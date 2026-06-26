import configparser
from _typeshed import Incomplete
from collections.abc import Generator
from pkg_resources import Environment

__all__ = ['PackageIndex', 'distros_for_url', 'parse_bdist_wininst', 'interpret_distro_name']

def parse_bdist_wininst(name):
    """Return (base,pyversion) or (None,None) for possible .exe name"""
def distros_for_url(url, metadata: Incomplete | None = None) -> Generator[Incomplete, None, None]:
    """Yield egg or source distribution objects that might be found at a URL"""
def interpret_distro_name(location, basename, metadata, py_version: Incomplete | None = None, precedence=..., platform: Incomplete | None = None) -> Generator[Incomplete, None, None]:
    """Generate the interpretation of a source distro name

    Note: if `location` is a filesystem filename, you should call
    ``pkg_resources.normalize_path()`` on it before passing it to this
    routine!
    """

class ContentChecker:
    """
    A null content checker that defines the interface for checking content
    """
    def feed(self, block) -> None:
        """
        Feed a block of data to the hash.
        """
    def is_valid(self):
        """
        Check the hash. Return False if validation fails.
        """
    def report(self, reporter, template) -> None:
        """
        Call reporter with information about the checker (hash name)
        substituted into the template.
        """

class HashChecker(ContentChecker):
    pattern: Incomplete
    hash_name: Incomplete
    hash: Incomplete
    expected: Incomplete
    def __init__(self, hash_name, expected) -> None: ...
    @classmethod
    def from_url(cls, url):
        """Construct a (possibly null) ContentChecker from a URL"""
    def feed(self, block) -> None: ...
    def is_valid(self): ...
    def report(self, reporter, template): ...

class PackageIndex(Environment):
    """A distribution index that scans web pages for download URLs"""
    index_url: Incomplete
    scanned_urls: Incomplete
    fetched_urls: Incomplete
    package_pages: Incomplete
    allows: Incomplete
    to_scan: Incomplete
    opener: Incomplete
    def __init__(self, index_url: str = 'https://pypi.org/simple/', hosts=('*',), ca_bundle: Incomplete | None = None, verify_ssl: bool = True, *args, **kw) -> None: ...
    def add(self, dist): ...
    def process_url(self, url, retrieve: bool = False) -> None:
        """Evaluate a URL as a possible download, and maybe retrieve it"""
    def process_filename(self, fn, nested: bool = False) -> None: ...
    def url_ok(self, url, fatal: bool = False): ...
    def scan_egg_links(self, search_path) -> None: ...
    def scan_egg_link(self, path, entry) -> None: ...
    def process_index(self, url, page):
        """Process the contents of a PyPI page"""
    def need_version_info(self, url) -> None: ...
    def scan_all(self, msg: Incomplete | None = None, *args) -> None: ...
    def find_packages(self, requirement) -> None: ...
    def obtain(self, requirement, installer: Incomplete | None = None): ...
    def check_hash(self, checker, filename, tfp) -> None:
        """
        checker is a ContentChecker
        """
    def add_find_links(self, urls) -> None:
        """Add `urls` to the list that will be prescanned for searches"""
    def prescan(self) -> None:
        """Scan urls scheduled for prescanning (e.g. --find-links)"""
    def not_found_in_index(self, requirement) -> None: ...
    def download(self, spec, tmpdir):
        """Locate and/or download `spec` to `tmpdir`, returning a local path

        `spec` may be a ``Requirement`` object, or a string containing a URL,
        an existing local filename, or a project/version requirement spec
        (i.e. the string form of a ``Requirement`` object).  If it is the URL
        of a .py file with an unambiguous ``#egg=name-version`` tag (i.e., one
        that escapes ``-`` as ``_`` throughout), a trivial ``setup.py`` is
        automatically created alongside the downloaded file.

        If `spec` is a ``Requirement`` object or a string containing a
        project/version requirement spec, this method returns the location of
        a matching distribution (possibly after downloading it to `tmpdir`).
        If `spec` is a locally existing file or directory name, it is simply
        returned unchanged.  If `spec` is a URL, it is downloaded to a subpath
        of `tmpdir`, and the local filename is returned.  Various errors may be
        raised if a problem occurs during downloading.
        """
    def fetch_distribution(self, requirement, tmpdir, force_scan: bool = False, source: bool = False, develop_ok: bool = False, local_index: Incomplete | None = None):
        """Obtain a distribution suitable for fulfilling `requirement`

        `requirement` must be a ``pkg_resources.Requirement`` instance.
        If necessary, or if the `force_scan` flag is set, the requirement is
        searched for in the (online) package index as well as the locally
        installed packages.  If a distribution matching `requirement` is found,
        the returned distribution's ``location`` is the value you would have
        gotten from calling the ``download()`` method with the matching
        distribution's URL or filename.  If no matching distribution is found,
        ``None`` is returned.

        If the `source` flag is set, only source distributions and source
        checkout links will be considered.  Unless the `develop_ok` flag is
        set, development and system eggs (i.e., those using the ``.egg-info``
        format) will be ignored.
        """
    def fetch(self, requirement, tmpdir, force_scan: bool = False, source: bool = False):
        """Obtain a file suitable for fulfilling `requirement`

        DEPRECATED; use the ``fetch_distribution()`` method now instead.  For
        backward compatibility, this routine is identical but returns the
        ``location`` of the downloaded distribution instead of a distribution
        object.
        """
    def gen_setup(self, filename, fragment, tmpdir): ...
    dl_blocksize: int
    def reporthook(self, url, filename, blocknum, blksize, size) -> None: ...
    def open_url(self, url, warning: Incomplete | None = None): ...
    def scan_url(self, url) -> None: ...
    def debug(self, msg, *args) -> None: ...
    def info(self, msg, *args) -> None: ...
    def warn(self, msg, *args) -> None: ...

class Credential:
    """
    A username/password pair. Use like a namedtuple.
    """
    username: Incomplete
    password: Incomplete
    def __init__(self, username, password) -> None: ...
    def __iter__(self): ...

class PyPIConfig(configparser.RawConfigParser):
    def __init__(self) -> None:
        """
        Load from ~/.pypirc
        """
    @property
    def creds_by_repository(self): ...
    def find_credential(self, url):
        """
        If the URL indicated appears to be a repository defined in this
        config, return the credential for that repository.
        """
