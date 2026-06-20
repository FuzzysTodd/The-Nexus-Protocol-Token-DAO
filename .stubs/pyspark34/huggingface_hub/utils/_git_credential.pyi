from ..constants import ENDPOINT as ENDPOINT
from ._subprocess import run_interactive_subprocess as run_interactive_subprocess, run_subprocess as run_subprocess
from typing import List

def list_credential_helpers(folder: str | None = None) -> List[str]:
    '''Return the list of git credential helpers configured.

    See https://git-scm.com/docs/gitcredentials.

    Credentials are saved in all configured helpers (store, cache, macOS keychain,...).
    Calls "`git credential approve`" internally. See https://git-scm.com/docs/git-credential.

    Args:
        folder (`str`, *optional*):
            The folder in which to check the configured helpers.
    '''
def set_git_credential(token: str, username: str = 'hf_user', folder: str | None = None) -> None:
    '''Save a username/token pair in git credential for HF Hub registry.

    Credentials are saved in all configured helpers (store, cache, macOS keychain,...).
    Calls "`git credential approve`" internally. See https://git-scm.com/docs/git-credential.

    Args:
        username (`str`, defaults to `"hf_user"`):
            A git username. Defaults to `"hf_user"`, the default user used in the Hub.
        token (`str`, defaults to `"hf_user"`):
            A git password. In practice, the User Access Token for the Hub.
            See https://huggingface.co/settings/tokens.
        folder (`str`, *optional*):
            The folder in which to check the configured helpers.
    '''
def unset_git_credential(username: str = 'hf_user', folder: str | None = None) -> None:
    '''Erase credentials from git credential for HF Hub registry.

    Credentials are erased from the configured helpers (store, cache, macOS
    keychain,...), if any. If `username` is not provided, any credential configured for
    HF Hub endpoint is erased.
    Calls "`git credential erase`" internally. See https://git-scm.com/docs/git-credential.

    Args:
        username (`str`, defaults to `"hf_user"`):
            A git username. Defaults to `"hf_user"`, the default user used in the Hub.
        folder (`str`, *optional*):
            The folder in which to check the configured helpers.
    '''
