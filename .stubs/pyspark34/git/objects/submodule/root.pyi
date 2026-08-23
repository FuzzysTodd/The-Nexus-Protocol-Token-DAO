from .base import Submodule, UpdateProgress
from _typeshed import Incomplete
from git.repo import Repo
from git.types import Commit_ish

__all__ = ['RootModule', 'RootUpdateProgress']

class RootUpdateProgress(UpdateProgress):
    """Utility class which adds more opcodes to the UpdateProgress"""
    REMOVE: Incomplete
    PATHCHANGE: Incomplete
    BRANCHCHANGE: Incomplete
    URLCHANGE: Incomplete

class RootModule(Submodule):
    """A (virtual) Root of all submodules in the given repository. It can be used
    to more easily traverse all submodules of the master repository"""
    k_root_name: str
    def __init__(self, repo: Repo) -> None: ...
    def update(self, previous_commit: Commit_ish | None = None, recursive: bool = True, force_remove: bool = False, init: bool = True, to_latest_revision: bool = False, progress: None | RootUpdateProgress = None, dry_run: bool = False, force_reset: bool = False, keep_going: bool = False) -> RootModule:
        """Update the submodules of this repository to the current HEAD commit.
        This method behaves smartly by determining changes of the path of a submodules
        repository, next to changes to the to-be-checked-out commit or the branch to be
        checked out. This works if the submodules ID does not change.
        Additionally it will detect addition and removal of submodules, which will be handled
        gracefully.

        :param previous_commit: If set to a commit'ish, the commit we should use
            as the previous commit the HEAD pointed to before it was set to the commit it points to now.
            If None, it defaults to HEAD@{1} otherwise
        :param recursive: if True, the children of submodules will be updated as well
            using the same technique
        :param force_remove: If submodules have been deleted, they will be forcibly removed.
            Otherwise the update may fail if a submodule's repository cannot be deleted as
            changes have been made to it (see Submodule.update() for more information)
        :param init: If we encounter a new module which would need to be initialized, then do it.
        :param to_latest_revision: If True, instead of checking out the revision pointed to
            by this submodule's sha, the checked out tracking branch will be merged with the
            latest remote branch fetched from the repository's origin.
            Unless force_reset is specified, a local tracking branch will never be reset into its past, therefore
            the remote branch must be in the future for this to have an effect.
        :param force_reset: if True, submodules may checkout or reset their branch even if the repository has
            pending changes that would be overwritten, or if the local tracking branch is in the future of the
            remote tracking branch and would be reset into its past.
        :param progress: RootUpdateProgress instance or None if no progress should be sent
        :param dry_run: if True, operations will not actually be performed. Progress messages
            will change accordingly to indicate the WOULD DO state of the operation.
        :param keep_going: if True, we will ignore but log all errors, and keep going recursively.
            Unless dry_run is set as well, keep_going could cause subsequent/inherited errors you wouldn't see
            otherwise.
            In conjunction with dry_run, it can be useful to anticipate all errors when updating submodules
        :return: self"""
    def module(self) -> Repo:
        """:return: the actual repository containing the submodules"""
