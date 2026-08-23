from _typeshed import Incomplete

def credsfromfile(creds_file: Incomplete | None = None, subdir: Incomplete | None = None, verbose: bool = False):
    """
    Convenience function for authentication
    """

class Authenticate:
    """
    Methods for authenticating with Twitter.
    """
    creds_file: str
    creds_fullpath: Incomplete
    oauth: Incomplete
    twitter_dir: Incomplete
    creds_subdir: Incomplete
    def __init__(self) -> None: ...
    def load_creds(self, creds_file: Incomplete | None = None, subdir: Incomplete | None = None, verbose: bool = False):
        """
        Read OAuth credentials from a text file.

        File format for OAuth 1::

           app_key=YOUR_APP_KEY
           app_secret=YOUR_APP_SECRET
           oauth_token=OAUTH_TOKEN
           oauth_token_secret=OAUTH_TOKEN_SECRET


        File format for OAuth 2::

           app_key=YOUR_APP_KEY
           app_secret=YOUR_APP_SECRET
           access_token=ACCESS_TOKEN

        :param str file_name: File containing credentials. ``None`` (default) reads
            data from `TWITTER/'credentials.txt'`
        """

def add_access_token(creds_file: Incomplete | None = None) -> None:
    """
    For OAuth 2, retrieve an access token for an app and append it to a
    credentials file.
    """
def guess_path(pth):
    """
    If the path is not absolute, guess that it is a subdirectory of the
    user's home directory.

    :param str pth: The pathname of the directory where files of tweets should be written
    """
