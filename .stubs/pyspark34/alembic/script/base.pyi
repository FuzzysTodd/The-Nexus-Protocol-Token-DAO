from . import revision as revision, write_hooks as write_hooks
from .. import util as util
from ..config import Config as Config, MessagingOptions as MessagingOptions
from ..runtime import migration as migration
from ..runtime.migration import RevisionStep as RevisionStep, StampStep as StampStep
from ..util import not_none as not_none
from .revision import Revision as Revision, _RevIdType
from _typeshed import Incomplete
from types import ModuleType
from typing import Any, Iterator, List, Mapping, Set, Tuple

class ScriptDirectory:
    '''Provides operations upon an Alembic script directory.

    This object is useful to get information as to current revisions,
    most notably being able to get at the "head" revision, for schemes
    that want to test if the current revision in the database is the most
    recent::

        from alembic.script import ScriptDirectory
        from alembic.config import Config
        config = Config()
        config.set_main_option("script_location", "myapp:migrations")
        script = ScriptDirectory.from_config(config)

        head_revision = script.get_current_head()



    '''
    dir: Incomplete
    file_template: Incomplete
    version_locations: Incomplete
    truncate_slug_length: Incomplete
    sourceless: Incomplete
    output_encoding: Incomplete
    revision_map: Incomplete
    timezone: Incomplete
    hook_config: Incomplete
    recursive_version_locations: Incomplete
    messaging_opts: Incomplete
    def __init__(self, dir: str, file_template: str = ..., truncate_slug_length: int | None = 40, version_locations: List[str] | None = None, sourceless: bool = False, output_encoding: str = 'utf-8', timezone: str | None = None, hook_config: Mapping[str, str] | None = None, recursive_version_locations: bool = False, messaging_opts: MessagingOptions = ...) -> None: ...
    @property
    def versions(self) -> str: ...
    @classmethod
    def from_config(cls, config: Config) -> ScriptDirectory:
        """Produce a new :class:`.ScriptDirectory` given a :class:`.Config`
        instance.

        The :class:`.Config` need only have the ``script_location`` key
        present.

        """
    def walk_revisions(self, base: str = 'base', head: str = 'heads') -> Iterator[Script]:
        '''Iterate through all revisions.

        :param base: the base revision, or "base" to start from the
         empty revision.

        :param head: the head revision; defaults to "heads" to indicate
         all head revisions.  May also be "head" to indicate a single
         head revision.

        '''
    def get_revisions(self, id_: _RevIdType) -> Tuple[Script | None, ...]:
        """Return the :class:`.Script` instance with the given rev identifier,
        symbolic name, or sequence of identifiers.

        """
    def get_all_current(self, id_: Tuple[str, ...]) -> Set[Script | None]: ...
    def get_revision(self, id_: str) -> Script | None:
        """Return the :class:`.Script` instance with the given rev id.

        .. seealso::

            :meth:`.ScriptDirectory.get_revisions`

        """
    def as_revision_number(self, id_: str | None) -> str | Tuple[str, ...] | None:
        """Convert a symbolic revision, i.e. 'head' or 'base', into
        an actual revision number."""
    def iterate_revisions(self, upper: str | Tuple[str, ...] | None, lower: str | Tuple[str, ...] | None, **kw: Any) -> Iterator[Script]:
        """Iterate through script revisions, starting at the given
        upper revision identifier and ending at the lower.

        The traversal uses strictly the `down_revision`
        marker inside each migration script, so
        it is a requirement that upper >= lower,
        else you'll get nothing back.

        The iterator yields :class:`.Script` objects.

        .. seealso::

            :meth:`.RevisionMap.iterate_revisions`

        """
    def get_current_head(self) -> str | None:
        """Return the current head revision.

        If the script directory has multiple heads
        due to branching, an error is raised;
        :meth:`.ScriptDirectory.get_heads` should be
        preferred.

        :return: a string revision number.

        .. seealso::

            :meth:`.ScriptDirectory.get_heads`

        """
    def get_heads(self) -> List[str]:
        '''Return all "versioned head" revisions as strings.

        This is normally a list of length one,
        unless branches are present.  The
        :meth:`.ScriptDirectory.get_current_head()` method
        can be used normally when a script directory
        has only one head.

        :return: a tuple of string revision numbers.
        '''
    def get_base(self) -> str | None:
        '''Return the "base" revision as a string.

        This is the revision number of the script that
        has a ``down_revision`` of None.

        If the script directory has multiple bases, an error is raised;
        :meth:`.ScriptDirectory.get_bases` should be
        preferred.

        '''
    def get_bases(self) -> List[str]:
        '''return all "base" revisions as strings.

        This is the revision number of all scripts that
        have a ``down_revision`` of None.

        '''
    def run_env(self) -> None:
        """Run the script environment.

        This basically runs the ``env.py`` script present
        in the migration environment.   It is called exclusively
        by the command functions in :mod:`alembic.command`.


        """
    @property
    def env_py_location(self): ...
    def generate_revision(self, revid: str, message: str | None, head: str | None = None, refresh: bool = False, splice: bool | None = False, branch_labels: _RevIdType | None = None, version_path: str | None = None, depends_on: _RevIdType | None = None, **kw: Any) -> Script | None:
        '''Generate a new revision file.

        This runs the ``script.py.mako`` template, given
        template arguments, and creates a new file.

        :param revid: String revision id.  Typically this
         comes from ``alembic.util.rev_id()``.
        :param message: the revision message, the one passed
         by the -m argument to the ``revision`` command.
        :param head: the head revision to generate against.  Defaults
         to the current "head" if no branches are present, else raises
         an exception.
        :param splice: if True, allow the "head" version to not be an
         actual head; otherwise, the selected head must be a head
         (e.g. endpoint) revision.
        :param refresh: deprecated.

        '''

class Script(revision.Revision):
    """Represent a single revision file in a ``versions/`` directory.

    The :class:`.Script` instance is returned by methods
    such as :meth:`.ScriptDirectory.iterate_revisions`.

    """
    module: Incomplete
    path: Incomplete
    def __init__(self, module: ModuleType, rev_id: str, path: str) -> None: ...
    @property
    def doc(self) -> str:
        """Return the docstring given in the script."""
    @property
    def longdoc(self) -> str:
        """Return the docstring given in the script."""
    @property
    def log_entry(self) -> str: ...
    def cmd_format(self, verbose: bool, include_branches: bool = False, include_doc: bool = False, include_parents: bool = False, tree_indicators: bool = True) -> str: ...
