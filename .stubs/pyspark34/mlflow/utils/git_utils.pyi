def get_git_repo_url(path: str) -> str | None:
    """
    Obtains the url of the git repository associated with the specified path,
    returning ``None`` if the path does not correspond to a git repository.
    """
def get_git_commit(path: str) -> str | None:
    """
    Obtains the hash of the latest commit on the current branch of the git repository associated
    with the specified path, returning ``None`` if the path does not correspond to a git
    repository.
    """
def get_git_branch(path: str) -> str | None:
    """
    Obtains the name of the current branch of the git repository associated with the specified
    path, returning ``None`` if the path does not correspond to a git repository.
    """
