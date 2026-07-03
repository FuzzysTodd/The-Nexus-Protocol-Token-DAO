from .. import constants as constants
from _typeshed import Incomplete

class HfFolder:
    path_token: Incomplete
    @classmethod
    def save_token(cls, token: str) -> None:
        """
        Save token, creating folder as needed.

        Token is saved in the huggingface home folder. You can configure it by setting
        the `HF_HOME` environment variable.

        Args:
            token (`str`):
                The token to save to the [`HfFolder`]
        """
    @classmethod
    def get_token(cls) -> str | None:
        """
        Get token or None if not existent.

        Note that a token can be also provided using the `HUGGING_FACE_HUB_TOKEN` environment variable.

        Token is saved in the huggingface home folder. You can configure it by setting
        the `HF_HOME` environment variable. Previous location was `~/.huggingface/token`.
        If token is found in old location but not in new location, it is copied there first.
        For more details, see https://github.com/huggingface/huggingface_hub/issues/1232.

        Returns:
            `str` or `None`: The token, `None` if it doesn't exist.
        """
    @classmethod
    def delete_token(cls) -> None:
        """
        Deletes the token from storage. Does not fail if token does not exist.
        """
