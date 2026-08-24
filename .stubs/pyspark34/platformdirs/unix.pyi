from .api import PlatformDirsABC
from pathlib import Path

__all__ = ['Unix']

class Unix(PlatformDirsABC):
    """
    On Unix/Linux, we follow the
    `XDG Basedir Spec <https://specifications.freedesktop.org/basedir-spec/basedir-spec-latest.html>`_. The spec allows
    overriding directories with environment variables. The examples show are the default values, alongside the name of
    the environment variable that overrides them. Makes use of the
    `appname <platformdirs.api.PlatformDirsABC.appname>`,
    `version <platformdirs.api.PlatformDirsABC.version>`,
    `multipath <platformdirs.api.PlatformDirsABC.multipath>`,
    `opinion <platformdirs.api.PlatformDirsABC.opinion>`,
    `ensure_exists <platformdirs.api.PlatformDirsABC.ensure_exists>`.
    """
    @property
    def user_data_dir(self) -> str:
        """
        :return: data directory tied to the user, e.g. ``~/.local/share/$appname/$version`` or
         ``$XDG_DATA_HOME/$appname/$version``
        """
    @property
    def site_data_dir(self) -> str:
        """
        :return: data directories shared by users (if `multipath <platformdirs.api.PlatformDirsABC.multipath>` is
         enabled and ``XDG_DATA_DIR`` is set and a multi path the response is also a multi path separated by the OS
         path separator), e.g. ``/usr/local/share/$appname/$version`` or ``/usr/share/$appname/$version``
        """
    @property
    def user_config_dir(self) -> str:
        """
        :return: config directory tied to the user, e.g. ``~/.config/$appname/$version`` or
         ``$XDG_CONFIG_HOME/$appname/$version``
        """
    @property
    def site_config_dir(self) -> str:
        """
        :return: config directories shared by users (if `multipath <platformdirs.api.PlatformDirsABC.multipath>`
         is enabled and ``XDG_DATA_DIR`` is set and a multi path the response is also a multi path separated by the OS
         path separator), e.g. ``/etc/xdg/$appname/$version``
        """
    @property
    def user_cache_dir(self) -> str:
        """
        :return: cache directory tied to the user, e.g. ``~/.cache/$appname/$version`` or
         ``~/$XDG_CACHE_HOME/$appname/$version``
        """
    @property
    def site_cache_dir(self) -> str:
        """
        :return: cache directory shared by users, e.g. ``/var/tmp/$appname/$version``
        """
    @property
    def user_state_dir(self) -> str:
        """
        :return: state directory tied to the user, e.g. ``~/.local/state/$appname/$version`` or
         ``$XDG_STATE_HOME/$appname/$version``
        """
    @property
    def user_log_dir(self) -> str:
        """
        :return: log directory tied to the user, same as `user_state_dir` if not opinionated else ``log`` in it
        """
    @property
    def user_documents_dir(self) -> str:
        """
        :return: documents directory tied to the user, e.g. ``~/Documents``
        """
    @property
    def user_pictures_dir(self) -> str:
        """
        :return: pictures directory tied to the user, e.g. ``~/Pictures``
        """
    @property
    def user_videos_dir(self) -> str:
        """
        :return: videos directory tied to the user, e.g. ``~/Videos``
        """
    @property
    def user_music_dir(self) -> str:
        """
        :return: music directory tied to the user, e.g. ``~/Music``
        """
    @property
    def user_runtime_dir(self) -> str:
        """
        :return: runtime directory tied to the user, e.g. ``/run/user/$(id -u)/$appname/$version`` or
         ``$XDG_RUNTIME_DIR/$appname/$version``
        """
    @property
    def site_data_path(self) -> Path:
        """:return: data path shared by users. Only return first item, even if ``multipath`` is set to ``True``"""
    @property
    def site_config_path(self) -> Path:
        """:return: config path shared by the users. Only return first item, even if ``multipath`` is set to ``True``"""
    @property
    def site_cache_path(self) -> Path:
        """:return: cache path shared by users. Only return first item, even if ``multipath`` is set to ``True``"""
