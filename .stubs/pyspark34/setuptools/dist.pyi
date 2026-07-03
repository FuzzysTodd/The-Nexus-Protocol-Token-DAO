from .warnings import SetuptoolsDeprecationWarning
from _typeshed import Incomplete
from collections.abc import Generator

__all__ = ['Distribution']

class Distribution(_Distribution):
    '''Distribution with support for tests and package data

    This is an enhanced version of \'distutils.dist.Distribution\' that
    effectively adds the following new optional keyword arguments to \'setup()\':

     \'install_requires\' -- a string or sequence of strings specifying project
        versions that the distribution requires when installed, in the format
        used by \'pkg_resources.require()\'.  They will be installed
        automatically when the package is installed.  If you wish to use
        packages that are not available in PyPI, or want to give your users an
        alternate download location, you can add a \'find_links\' option to the
        \'[easy_install]\' section of your project\'s \'setup.cfg\' file, and then
        setuptools will scan the listed web pages for links that satisfy the
        requirements.

     \'extras_require\' -- a dictionary mapping names of optional "extras" to the
        additional requirement(s) that using those extras incurs. For example,
        this::

            extras_require = dict(reST = ["docutils>=0.3", "reSTedit"])

        indicates that the distribution can optionally provide an extra
        capability called "reST", but it can only be used if docutils and
        reSTedit are installed.  If the user installs your package using
        EasyInstall and requests one of your extras, the corresponding
        additional requirements will be installed if needed.

     \'test_suite\' -- the name of a test suite to run for the \'test\' command.
        If the user runs \'python setup.py test\', the package will be installed,
        and the named test suite will be run.  The format is the same as
        would be used on a \'unittest.py\' command line.  That is, it is the
        dotted name of an object to import and call to generate a test suite.

     \'package_data\' -- a dictionary mapping package names to lists of filenames
        or globs to use to find data files contained in the named packages.
        If the dictionary has filenames or globs listed under \'""\' (the empty
        string), those names will be searched for in every package, in addition
        to any names for the specific package.  Data files found using these
        names/globs will be installed along with the package, in the same
        location as the package.  Note that globs are allowed to reference
        the contents of non-package subdirectories, as long as you use \'/\' as
        a path separator.  (Globs are automatically converted to
        platform-specific paths at runtime.)

    In addition to these new keywords, this class also has several new methods
    for manipulating the distribution\'s contents.  For example, the \'include()\'
    and \'exclude()\' methods can be thought of as in-place add and subtract
    commands that add or remove packages, modules, extensions, and so on from
    the distribution.
    '''
    def patch_missing_pkg_info(self, attrs) -> None: ...
    package_data: Incomplete
    dist_files: Incomplete
    src_root: Incomplete
    dependency_links: Incomplete
    setup_requires: Incomplete
    set_defaults: Incomplete
    def __init__(self, attrs: Incomplete | None = None) -> None: ...
    def warn_dash_deprecation(self, opt, section): ...
    def make_option_lowercase(self, opt, section): ...
    def parse_config_files(self, filenames: Incomplete | None = None, ignore_option_errors: bool = False) -> None:
        """Parses configuration files from various levels
        and loads configuration.
        """
    def fetch_build_eggs(self, requires):
        """Resolve pre-setup requirements"""
    def finalize_options(self):
        """
        Allow plugins to apply arbitrary operations to the
        distribution. Each hook may optionally define a 'order'
        to influence the order of execution. Smaller numbers
        go first and the default is 0.
        """
    def get_egg_cache_dir(self): ...
    def fetch_build_egg(self, req):
        """Fetch an egg needed for building"""
    def get_command_class(self, command):
        """Pluggable version of get_command_class()"""
    def print_commands(self): ...
    def get_command_list(self): ...
    def include(self, **attrs) -> None:
        '''Add items to distribution that are named in keyword arguments

        For example, \'dist.include(py_modules=["x"])\' would add \'x\' to
        the distribution\'s \'py_modules\' attribute, if it was not already
        there.

        Currently, this method only supports inclusion for attributes that are
        lists or tuples.  If you need to add support for adding to other
        attributes in this or a subclass, you can add an \'_include_X\' method,
        where \'X\' is the name of the attribute.  The method will be called with
        the value passed to \'include()\'.  So, \'dist.include(foo={"bar":"baz"})\'
        will try to call \'dist._include_foo({"bar":"baz"})\', which can then
        handle whatever special inclusion logic is needed.
        '''
    packages: Incomplete
    py_modules: Incomplete
    ext_modules: Incomplete
    def exclude_package(self, package) -> None:
        """Remove packages, modules, and extensions in named package"""
    def has_contents_for(self, package):
        """Return true if 'exclude_package(package)' would do something"""
    def exclude(self, **attrs) -> None:
        '''Remove items from distribution that are named in keyword arguments

        For example, \'dist.exclude(py_modules=["x"])\' would remove \'x\' from
        the distribution\'s \'py_modules\' attribute.  Excluding packages uses
        the \'exclude_package()\' method, so all of the package\'s contained
        packages, modules, and extensions are also excluded.

        Currently, this method only supports exclusion from attributes that are
        lists or tuples.  If you need to add support for excluding from other
        attributes in this or a subclass, you can add an \'_exclude_X\' method,
        where \'X\' is the name of the attribute.  The method will be called with
        the value passed to \'exclude()\'.  So, \'dist.exclude(foo={"bar":"baz"})\'
        will try to call \'dist._exclude_foo({"bar":"baz"})\', which can then
        handle whatever special exclusion logic is needed.
        '''
    def get_cmdline_options(self):
        """Return a '{cmd: {opt:val}}' map of all command-line options

        Option names are all long, but do not include the leading '--', and
        contain dashes rather than underscores.  If the option doesn't take
        an argument (e.g. '--quiet'), the 'val' is 'None'.

        Note that options provided by config files are intentionally excluded.
        """
    def iter_distribution_names(self) -> Generator[Incomplete, None, None]:
        """Yield all packages, modules, and extension names in distribution"""
    def handle_display_options(self, option_order):
        '''If there were any non-global "display-only" options
        (--help-commands or the metadata display options) on the command
        line, display the requested info and return true; else return
        false.
        '''
    def run_command(self, command) -> None: ...

class DistDeprecationWarning(SetuptoolsDeprecationWarning):
    """Class for warning about deprecations in dist in
    setuptools. Not ignored by default, unlike DeprecationWarning."""
