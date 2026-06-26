from ..auto import tqdm as tqdm_auto
from .utils_worker import MonoWorker
from _typeshed import Incomplete

__all__ = ['TelegramIO', 'tqdm_telegram', 'ttgrange', 'tqdm', 'trange']

class TelegramIO(MonoWorker):
    """Non-blocking file-like IO using a Telegram Bot."""
    API: str
    token: Incomplete
    chat_id: Incomplete
    session: Incomplete
    text: Incomplete
    def __init__(self, token, chat_id) -> None:
        """Creates a new message in the given `chat_id`."""
    @property
    def message_id(self): ...
    def write(self, s):
        """Replaces internal `message_id`'s text with `s`."""
    def delete(self):
        """Deletes internal `message_id`."""

class tqdm_telegram(tqdm_auto):
    """
    Standard `tqdm.auto.tqdm` but also sends updates to a Telegram Bot.
    May take a few seconds to create (`__init__`).

    - create a bot <https://core.telegram.org/bots#6-botfather>
    - copy its `{token}`
    - add the bot to a chat and send it a message such as `/start`
    - go to <https://api.telegram.org/bot`{token}`/getUpdates> to find out
      the `{chat_id}`
    - paste the `{token}` & `{chat_id}` below

    >>> from tqdm.contrib.telegram import tqdm, trange
    >>> for i in tqdm(iterable, token='{token}', chat_id='{chat_id}'):
    ...     ...
    """
    tgio: Incomplete
    def __init__(self, *args, **kwargs) -> None:
        """
        Parameters
        ----------
        token  : str, required. Telegram token
            [default: ${TQDM_TELEGRAM_TOKEN}].
        chat_id  : str, required. Telegram chat ID
            [default: ${TQDM_TELEGRAM_CHAT_ID}].

        See `tqdm.auto.tqdm.__init__` for other parameters.
        """
    def display(self, **kwargs) -> None: ...
    def clear(self, *args, **kwargs) -> None: ...
    def close(self) -> None: ...

def ttgrange(*args, **kwargs):
    """Shortcut for `tqdm.contrib.telegram.tqdm(range(*args), **kwargs)`."""
tqdm = tqdm_telegram
trange = ttgrange
