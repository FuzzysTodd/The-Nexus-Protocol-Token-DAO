from .api import PlatformDirsABC

__all__ = ['Windows']

class Windows(PlatformDirsABC):
    """`MSDN on where to store app data files
    <http://support.microsoft.com/default.aspx?scid=kb;en-us;310294#XSLTH3194121123120121120120>`_.
    Makes use of the
    `appname <platformdirs.api.PlatformDirsABC.appname>`,
    `appauthor <platformdirs.api.PlatformDirsABC.appauthor>`,
    `version <platformdirs.api.PlatformDirsABC.version>`,
    `roaming <platformdirs.api.PlatformDirsABC.roaming>`,
    `opinion <platformdirs.api.PlatformDirsABC.opinion>`,
    `ensure_exists <platformdirs.api.PlatformDirsABC.ensure_exists>`.
    """
    @property
    def user_data_dir(self) -> str:
        """
        :return: data directory tied to the user, e.g.
         ``%USERPROFILE%\\AppData\\Local\\$appauthor\\$appname`` (not roaming) or
         ``%USERPROFILE%\\AppData\\Roaming\\$appauthor\\$appname`` (roaming)
        """
    @property
    def site_data_dir(self) -> str:
        """:return: data directory shared by users, e.g. ``C:\\ProgramData\\$appauthor\\$appname``"""
    @property
    def user_config_dir(self) -> str:
        """:return: config directory tied to the user, same as `user_data_dir`"""
    @property
    def site_config_dir(self) -> str:
        """:return: config directory shared by the users, same as `site_data_dir`"""
    @property
    def user_cache_dir(self) -> str:
        """
        :return: cache directory tied to the user (if opinionated with ``Cache`` folder within ``$appname``) e.g.
         ``%USERPROFILE%\\AppData\\Local\\$appauthor\\$appname\\Cache\\$version``
        """
    @property
    def site_cache_dir(self) -> str:
        """:return: cache directory shared by users, e.g. ``C:\\ProgramData\\$appauthor\\$appname\\Cache\\$version``"""
    @property
    def user_state_dir(self) -> str:
        """:return: state directory tied to the user, same as `user_data_dir`"""
    @property
    def user_log_dir(self) -> str:
        """
        :return: log directory tied to the user, same as `user_data_dir` if not opinionated else ``Logs`` in it
        """
    @property
    def user_documents_dir(self) -> str:
        """
        :return: documents directory tied to the user e.g. ``%USERPROFILE%\\Documents``
        """
    @property
    def user_pictures_dir(self) -> str:
        """
        :return: pictures directory tied to the user e.g. ``%USERPROFILE%\\Pictures``
        """
    @property
    def user_videos_dir(self) -> str:
        """
        :return: videos directory tied to the user e.g. ``%USERPROFILE%\\Videos``
        """
    @property
    def user_music_dir(self) -> str:
        """
        :return: music directory tied to the user e.g. ``%USERPROFILE%\\Music``
        """
    @property
    def user_runtime_dir(self) -> str:
        """
        :return: runtime directory tied to the user, e.g.
         ``%USERPROFILE%\\AppData\\Local\\Temp\\$appauthor\\$appname``
        """
