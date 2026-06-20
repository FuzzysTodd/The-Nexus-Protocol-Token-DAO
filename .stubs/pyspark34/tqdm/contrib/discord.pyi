from ..auto import tqdm as tqdm_auto
from .utils_worker import MonoWorker
from _typeshed import Incomplete

__all__ = ['DiscordIO', 'tqdm_discord', 'tdrange', 'tqdm', 'trange']

class DiscordIO(MonoWorker):
    """Non-blocking file-like IO using a Discord Bot."""
    text: Incomplete
    message: Incomplete
    def __init__(self, token, channel_id) -> None:
        """Creates a new message in the given `channel_id`."""
    def write(self, s):
        """Replaces internal `message`'s text with `s`."""

class tqdm_discord(tqdm_auto):
    """
    Standard `tqdm.auto.tqdm` but also sends updates to a Discord Bot.
    May take a few seconds to create (`__init__`).

    - create a discord bot (not public, no requirement of OAuth2 code
      grant, only send message permissions) & invite it to a channel:
      <https://discordpy.readthedocs.io/en/latest/discord.html>
    - copy the bot `{token}` & `{channel_id}` and paste below

    >>> from tqdm.contrib.discord import tqdm, trange
    >>> for i in tqdm(iterable, token='{token}', channel_id='{channel_id}'):
    ...     ...
    """
    dio: Incomplete
    def __init__(self, *args, **kwargs) -> None:
        """
        Parameters
        ----------
        token  : str, required. Discord token
            [default: ${TQDM_DISCORD_TOKEN}].
        channel_id  : int, required. Discord channel ID
            [default: ${TQDM_DISCORD_CHANNEL_ID}].
        mininterval  : float, optional.
          Minimum of [default: 1.5] to avoid rate limit.

        See `tqdm.auto.tqdm.__init__` for other parameters.
        """
    def display(self, **kwargs) -> None: ...
    def clear(self, *args, **kwargs) -> None: ...

def tdrange(*args, **kwargs):
    """Shortcut for `tqdm.contrib.discord.tqdm(range(*args), **kwargs)`."""
tqdm = tqdm_discord
trange = tdrange
