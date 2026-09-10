from .commands._cli_utils import ANSI as ANSI
from .hf_api import get_token_permission as get_token_permission
from .utils import HfFolder as HfFolder, capture_output as capture_output, is_google_colab as is_google_colab, is_notebook as is_notebook, list_credential_helpers as list_credential_helpers, logging as logging, run_subprocess as run_subprocess, set_git_credential as set_git_credential, unset_git_credential as unset_git_credential
from _typeshed import Incomplete

logger: Incomplete

def login(token: str | None = None, add_to_git_credential: bool = False, new_session: bool = True, write_permission: bool = False) -> None:
    """Login the machine to access the Hub.

    The `token` is persisted in cache and set as a git credential. Once done, the machine
    is logged in and the access token will be available across all `huggingface_hub`
    components. If `token` is not provided, it will be prompted to the user either with
    a widget (in a notebook) or via the terminal.

    To login from outside of a script, one can also use `huggingface-cli login` which is
    a cli command that wraps [`login`].

    <Tip>

    [`login`] is a drop-in replacement method for [`notebook_login`] as it wraps and
    extends its capabilities.

    </Tip>

    <Tip>

    When the token is not passed, [`login`] will automatically detect if the script runs
    in a notebook or not. However, this detection might not be accurate due to the
    variety of notebooks that exists nowadays. If that is the case, you can always force
    the UI by using [`notebook_login`] or [`interpreter_login`].

    </Tip>

    Args:
        token (`str`, *optional*):
            User access token to generate from https://huggingface.co/settings/token.
        add_to_git_credential (`bool`, defaults to `False`):
            If `True`, token will be set as git credential. If no git credential helper
            is configured, a warning will be displayed to the user. If `token` is `None`,
            the value of `add_to_git_credential` is ignored and will be prompted again
            to the end user.
        new_session (`bool`, defaults to `True`):
            If `True`, will request a token even if one is already saved on the machine.
        write_permission (`bool`, defaults to `False`):
            If `True`, requires a token with write permission.
    Raises:
        [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError)
            If an organization token is passed. Only personal account tokens are valid
            to login.
        [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError)
            If token is invalid.
        [`ImportError`](https://docs.python.org/3/library/exceptions.html#ImportError)
            If running in a notebook but `ipywidgets` is not installed.
    """
def logout() -> None:
    """Logout the machine from the Hub.

    Token is deleted from the machine and removed from git credential.
    """
def interpreter_login(new_session: bool = True, write_permission: bool = False) -> None:
    """
    Displays a prompt to login to the HF website and store the token.

    This is equivalent to [`login`] without passing a token when not run in a notebook.
    [`interpreter_login`] is useful if you want to force the use of the terminal prompt
    instead of a notebook widget.

    For more details, see [`login`].

    Args:
        new_session (`bool`, defaults to `True`):
            If `True`, will request a token even if one is already saved on the machine.
        write_permission (`bool`, defaults to `False`):
            If `True`, requires a token with write permission.

    """

NOTEBOOK_LOGIN_PASSWORD_HTML: str
NOTEBOOK_LOGIN_TOKEN_HTML_START: str
NOTEBOOK_LOGIN_TOKEN_HTML_END: str

def notebook_login(new_session: bool = True, write_permission: bool = False) -> None:
    """
    Displays a widget to login to the HF website and store the token.

    This is equivalent to [`login`] without passing a token when run in a notebook.
    [`notebook_login`] is useful if you want to force the use of the notebook widget
    instead of a prompt in the terminal.

    For more details, see [`login`].

    Args:
        new_session (`bool`, defaults to `True`):
            If `True`, will request a token even if one is already saved on the machine.
        write_permission (`bool`, defaults to `False`):
            If `True`, requires a token with write permission.
    """
