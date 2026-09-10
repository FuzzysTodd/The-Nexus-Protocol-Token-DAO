from ..spec import AbstractFileSystem as AbstractFileSystem
from ..utils import infer_storage_options as infer_storage_options
from .memory import MemoryFile as MemoryFile
from _typeshed import Incomplete

class GithubFileSystem(AbstractFileSystem):
    '''Interface to files in github

    An instance of this class provides the files residing within a remote github
    repository. You may specify a point in the repos history, by SHA, branch
    or tag (default is current master).

    Given that code files tend to be small, and that github does not support
    retrieving partial content, we always fetch whole files.

    When using fsspec.open, allows URIs of the form:

    - "github://path/file", in which case you must specify org, repo and
      may specify sha in the extra args
    - \'github://org:repo@/precip/catalog.yml\', where the org and repo are
      part of the URI
    - \'github://org:repo@sha/precip/catalog.yml\', where the sha is also included

    ``sha`` can be the full or abbreviated hex of the commit you want to fetch
    from, or a branch or tag name (so long as it doesn\'t contain special characters
    like "/", "?", which would have to be HTTP-encoded).

    For authorised access, you must provide username and token, which can be made
    at https://github.com/settings/tokens
    '''
    url: str
    rurl: str
    protocol: str
    org: Incomplete
    repo: Incomplete
    username: Incomplete
    token: Incomplete
    root: Incomplete
    def __init__(self, org, repo, sha: Incomplete | None = None, username: Incomplete | None = None, token: Incomplete | None = None, **kwargs) -> None: ...
    @property
    def kw(self): ...
    @classmethod
    def repos(cls, org_or_user, is_org: bool = True):
        """List repo names for given org or user

        This may become the top level of the FS

        Parameters
        ----------
        org_or_user: str
            Name of the github org or user to query
        is_org: bool (default True)
            Whether the name is an organisation (True) or user (False)

        Returns
        -------
        List of string
        """
    @property
    def tags(self):
        """Names of tags in the repo"""
    @property
    def branches(self):
        """Names of branches in the repo"""
    @property
    def refs(self):
        """Named references, tags and branches"""
    def ls(self, path, detail: bool = False, sha: Incomplete | None = None, _sha: Incomplete | None = None, **kwargs):
        """List files at given path

        Parameters
        ----------
        path: str
            Location to list, relative to repo root
        detail: bool
            If True, returns list of dicts, one per file; if False, returns
            list of full filenames only
        sha: str (optional)
            List at the given point in the repo history, branch or tag name or commit
            SHA
        _sha: str (optional)
            List this specific tree object (used internally to descend into trees)
        """
    def invalidate_cache(self, path: Incomplete | None = None) -> None: ...
