import datetime
from . import base
from .tree import Tree
from .util import Serializable, TraversableIterableObj
from _typeshed import Incomplete
from git.diff import Diffable
from git.refs import SymbolicReference
from git.repo import Repo
from git.types import Literal, PathLike
from git.util import Actor, Stats
from typing import Any, Dict, Iterator, List, Sequence, Tuple

__all__ = ['Commit']

class Commit(base.Object, TraversableIterableObj, Diffable, Serializable):
    """Wraps a git Commit object.

    This class will act lazily on some of its attributes and will query the
    value on demand only if it involves calling the git binary."""
    env_author_date: str
    env_committer_date: str
    conf_encoding: str
    default_encoding: str
    type: Literal['commit']
    binsha: Incomplete
    tree: Incomplete
    author: Incomplete
    authored_date: Incomplete
    author_tz_offset: Incomplete
    committer: Incomplete
    committed_date: Incomplete
    committer_tz_offset: Incomplete
    message: Incomplete
    parents: Incomplete
    encoding: Incomplete
    gpgsig: Incomplete
    def __init__(self, repo: Repo, binsha: bytes, tree: Tree | None = None, author: Actor | None = None, authored_date: int | None = None, author_tz_offset: None | float = None, committer: Actor | None = None, committed_date: int | None = None, committer_tz_offset: None | float = None, message: str | bytes | None = None, parents: Sequence['Commit'] | None = None, encoding: str | None = None, gpgsig: str | None = None) -> None:
        """Instantiate a new Commit. All keyword arguments taking None as default will
        be implicitly set on first query.

        :param binsha: 20 byte sha1
        :param parents: tuple( Commit, ... )
            is a tuple of commit ids or actual Commits
        :param tree: Tree object
        :param author: Actor
            is the author Actor object
        :param authored_date: int_seconds_since_epoch
            is the authored DateTime - use time.gmtime() to convert it into a
            different format
        :param author_tz_offset: int_seconds_west_of_utc
            is the timezone that the authored_date is in
        :param committer: Actor
            is the committer string
        :param committed_date: int_seconds_since_epoch
            is the committed DateTime - use time.gmtime() to convert it into a
            different format
        :param committer_tz_offset: int_seconds_west_of_utc
            is the timezone that the committed_date is in
        :param message: string
            is the commit message
        :param encoding: string
            encoding of the message, defaults to UTF-8
        :param parents:
            List or tuple of Commit objects which are our parent(s) in the commit
            dependency graph
        :return: git.Commit

        :note:
            Timezone information is in the same format and in the same sign
            as what time.altzone returns. The sign is inverted compared to git's
            UTC timezone."""
    def replace(self, **kwargs: Any) -> Commit:
        """Create new commit object from existing commit object.

        Any values provided as keyword arguments will replace the
        corresponding attribute in the new object.
        """
    @property
    def authored_datetime(self) -> datetime.datetime: ...
    @property
    def committed_datetime(self) -> datetime.datetime: ...
    @property
    def summary(self) -> str | bytes:
        """:return: First line of the commit message"""
    def count(self, paths: PathLike | Sequence[PathLike] = '', **kwargs: Any) -> int:
        """Count the number of commits reachable from this commit

        :param paths:
            is an optional path or a list of paths restricting the return value
            to commits actually containing the paths

        :param kwargs:
            Additional options to be passed to git-rev-list. They must not alter
            the output style of the command, or parsing will yield incorrect results
        :return: int defining the number of reachable commits"""
    @property
    def name_rev(self) -> str:
        """
        :return:
            String describing the commits hex sha based on the closest Reference.
            Mostly useful for UI purposes"""
    @classmethod
    def iter_items(cls, repo: Repo, rev: str | Commit | SymbolicReference, paths: PathLike | Sequence[PathLike] = '', **kwargs: Any) -> Iterator['Commit']:
        """Find all commits matching the given criteria.

        :param repo: is the Repo
        :param rev: revision specifier, see git-rev-parse for viable options
        :param paths:
            is an optional path or list of paths, if set only Commits that include the path
            or paths will be considered
        :param kwargs:
            optional keyword arguments to git rev-list where
            ``max_count`` is the maximum number of commits to fetch
            ``skip`` is the number of commits to skip
            ``since`` all commits since i.e. '1970-01-01'
        :return: iterator yielding Commit items"""
    def iter_parents(self, paths: PathLike | Sequence[PathLike] = '', **kwargs: Any) -> Iterator['Commit']:
        """Iterate _all_ parents of this commit.

        :param paths:
            Optional path or list of paths limiting the Commits to those that
            contain at least one of the paths
        :param kwargs: All arguments allowed by git-rev-list
        :return: Iterator yielding Commit objects which are parents of self"""
    @property
    def stats(self) -> Stats:
        """Create a git stat from changes between this commit and its first parent
        or from all changes done if this is the very first commit.

        :return: git.Stats"""
    @property
    def trailers(self) -> Dict[str, str]:
        """Get the trailers of the message as a dictionary

        :note: This property is deprecated, please use either ``Commit.trailers_list`` or ``Commit.trailers_dict``.

        :return:
            Dictionary containing whitespace stripped trailer information.
            Only contains the latest instance of each trailer key.
        """
    @property
    def trailers_list(self) -> List[Tuple[str, str]]:
        '''Get the trailers of the message as a list

        Git messages can contain trailer information that are similar to RFC 822
        e-mail headers (see: https://git-scm.com/docs/git-interpret-trailers).

        This functions calls ``git interpret-trailers --parse`` onto the message
        to extract the trailer information, returns the raw trailer data as a list.

        Valid message with trailer::

            Subject line

            some body information

            another information

            key1: value1.1
            key1: value1.2
            key2 :    value 2 with inner spaces


        Returned list will look like this::

            [
                ("key1", "value1.1"),
                ("key1", "value1.2"),
                ("key2", "value 2 with inner spaces"),
            ]


        :return:
            List containing key-value tuples of whitespace stripped trailer information.
        '''
    @property
    def trailers_dict(self) -> Dict[str, List[str]]:
        '''Get the trailers of the message as a dictionary

        Git messages can contain trailer information that are similar to RFC 822
        e-mail headers (see: https://git-scm.com/docs/git-interpret-trailers).

        This functions calls ``git interpret-trailers --parse`` onto the message
        to extract the trailer information. The key value pairs are stripped of
        leading and trailing whitespaces before they get saved into a dictionary.

        Valid message with trailer::

            Subject line

            some body information

            another information

            key1: value1.1
            key1: value1.2
            key2 :    value 2 with inner spaces


        Returned dictionary will look like this::

            {
                "key1": ["value1.1", "value1.2"],
                "key2": ["value 2 with inner spaces"],
            }


        :return:
            Dictionary containing whitespace stripped trailer information.
            Mapping trailer keys to a list of their corresponding values.
        '''
    @classmethod
    def create_from_tree(cls, repo: Repo, tree: Tree | str, message: str, parent_commits: None | List['Commit'] = None, head: bool = False, author: None | Actor = None, committer: None | Actor = None, author_date: None | str | datetime.datetime = None, commit_date: None | str | datetime.datetime = None) -> Commit:
        """Commit the given tree, creating a commit object.

        :param repo: Repo object the commit should be part of
        :param tree: Tree object or hex or bin sha
            the tree of the new commit
        :param message: Commit message. It may be an empty string if no message is provided.
            It will be converted to a string , in any case.
        :param parent_commits:
            Optional Commit objects to use as parents for the new commit.
            If empty list, the commit will have no parents at all and become
            a root commit.
            If None , the current head commit will be the parent of the
            new commit object
        :param head:
            If True, the HEAD will be advanced to the new commit automatically.
            Else the HEAD will remain pointing on the previous commit. This could
            lead to undesired results when diffing files.
        :param author: The name of the author, optional. If unset, the repository
            configuration is used to obtain this value.
        :param committer: The name of the committer, optional. If unset, the
            repository configuration is used to obtain this value.
        :param author_date: The timestamp for the author field
        :param commit_date: The timestamp for the committer field

        :return: Commit object representing the new commit

        :note:
            Additional information about the committer and Author are taken from the
            environment or from the git configuration, see git-commit-tree for
            more information"""
    @property
    def co_authors(self) -> List[Actor]:
        """
        Search the commit message for any co-authors of this commit.
        Details on co-authors: https://github.blog/2018-01-29-commit-together-with-co-authors/

        :return: List of co-authors for this commit (as Actor objects).
        """
