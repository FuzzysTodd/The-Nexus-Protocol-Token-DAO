from ..auto import tqdm as tqdm_auto
from .utils_worker import MonoWorker
from _typeshed import Incomplete

__all__ = ['SlackIO', 'tqdm_slack', 'tsrange', 'tqdm', 'trange']

class SlackIO(MonoWorker):
    """Non-blocking file-like IO using a Slack app."""
    client: Incomplete
    text: Incomplete
    message: Incomplete
    def __init__(self, token, channel) -> None:
        """Creates a new message in the given `channel`."""
    def write(self, s):
        """Replaces internal `message`'s text with `s`."""

class tqdm_slack(tqdm_auto):
    """
    Standard `tqdm.auto.tqdm` but also sends updates to a Slack app.
    May take a few seconds to create (`__init__`).

    - create a Slack app with the `chat:write` scope & invite it to a
      channel: <https://api.slack.com/authentication/basics>
    - copy the bot `{token}` & `{channel}` and paste below
    >>> from tqdm.contrib.slack import tqdm, trange
    >>> for i in tqdm(iterable, token='{token}', channel='{channel}'):
    ...     ...
    """
    sio: Incomplete
    def __init__(self, *args, **kwargs) -> None:
        """
        Parameters
        ----------
        token  : str, required. Slack token
            [default: ${TQDM_SLACK_TOKEN}].
        channel  : int, required. Slack channel
            [default: ${TQDM_SLACK_CHANNEL}].
        mininterval  : float, optional.
          Minimum of [default: 1.5] to avoid rate limit.

        See `tqdm.auto.tqdm.__init__` for other parameters.
        """
    def display(self, **kwargs) -> None: ...
    def clear(self, *args, **kwargs) -> None: ...

def tsrange(*args, **kwargs):
    """Shortcut for `tqdm.contrib.slack.tqdm(range(*args), **kwargs)`."""
tqdm = tqdm_slack
trange = tsrange
