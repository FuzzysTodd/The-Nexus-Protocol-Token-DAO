from .api import PlatformDirsABC as PlatformDirsABC
from .version import __version__ as __version__, __version_tuple__ as __version_info__
from _typeshed import Incomplete
from pathlib import Path
from typing import Literal

__all__ = ['__version__', '__version_info__', 'PlatformDirs', 'AppDirs', 'PlatformDirsABC', 'user_data_dir', 'user_config_dir', 'user_cache_dir', 'user_state_dir', 'user_log_dir', 'user_documents_dir', 'user_pictures_dir', 'user_videos_dir', 'user_music_dir', 'user_runtime_dir', 'site_data_dir', 'site_config_dir', 'site_cache_dir', 'user_data_path', 'user_config_path', 'user_cache_path', 'user_state_path', 'user_log_path', 'user_documents_path', 'user_pictures_path', 'user_videos_path', 'user_music_path', 'user_runtime_path', 'site_data_path', 'site_config_path', 'site_cache_path']

PlatformDirs: Incomplete
AppDirs = PlatformDirs

def user_data_dir(appname: str | None = None, appauthor: str | None | Literal[False] = None, version: str | None = None, roaming: bool = False, ensure_exists: bool = False) -> str:
    """
    :param appname: See `appname <platformdirs.api.PlatformDirsABC.appname>`.
    :param appauthor: See `appauthor <platformdirs.api.PlatformDirsABC.appauthor>`.
    :param version: See `version <platformdirs.api.PlatformDirsABC.version>`.
    :param roaming: See `roaming <platformdirs.api.PlatformDirsABC.roaming>`.
    :param ensure_exists: See `ensure_exists <platformdirs.api.PlatformDirsABC.ensure_exists>`.
    :returns: data directory tied to the user
    """
def site_data_dir(appname: str | None = None, appauthor: str | None | Literal[False] = None, version: str | None = None, multipath: bool = False, ensure_exists: bool = False) -> str:
    """
    :param appname: See `appname <platformdirs.api.PlatformDirsABC.appname>`.
    :param appauthor: See `appauthor <platformdirs.api.PlatformDirsABC.appauthor>`.
    :param version: See `version <platformdirs.api.PlatformDirsABC.version>`.
    :param multipath: See `roaming <platformdirs.api.PlatformDirsABC.multipath>`.
    :param ensure_exists: See `ensure_exists <platformdirs.api.PlatformDirsABC.ensure_exists>`.
    :returns: data directory shared by users
    """
def user_config_dir(appname: str | None = None, appauthor: str | None | Literal[False] = None, version: str | None = None, roaming: bool = False, ensure_exists: bool = False) -> str:
    """
    :param appname: See `appname <platformdirs.api.PlatformDirsABC.appname>`.
    :param appauthor: See `appauthor <platformdirs.api.PlatformDirsABC.appauthor>`.
    :param version: See `version <platformdirs.api.PlatformDirsABC.version>`.
    :param roaming: See `roaming <platformdirs.api.PlatformDirsABC.roaming>`.
    :param ensure_exists: See `ensure_exists <platformdirs.api.PlatformDirsABC.ensure_exists>`.
    :returns: config directory tied to the user
    """
def site_config_dir(appname: str | None = None, appauthor: str | None | Literal[False] = None, version: str | None = None, multipath: bool = False, ensure_exists: bool = False) -> str:
    """
    :param appname: See `appname <platformdirs.api.PlatformDirsABC.appname>`.
    :param appauthor: See `appauthor <platformdirs.api.PlatformDirsABC.appauthor>`.
    :param version: See `version <platformdirs.api.PlatformDirsABC.version>`.
    :param multipath: See `roaming <platformdirs.api.PlatformDirsABC.multipath>`.
    :param ensure_exists: See `ensure_exists <platformdirs.api.PlatformDirsABC.ensure_exists>`.
    :returns: config directory shared by the users
    """
def user_cache_dir(appname: str | None = None, appauthor: str | None | Literal[False] = None, version: str | None = None, opinion: bool = True, ensure_exists: bool = False) -> str:
    """
    :param appname: See `appname <platformdirs.api.PlatformDirsABC.appname>`.
    :param appauthor: See `appauthor <platformdirs.api.PlatformDirsABC.appauthor>`.
    :param version: See `version <platformdirs.api.PlatformDirsABC.version>`.
    :param opinion: See `roaming <platformdirs.api.PlatformDirsABC.opinion>`.
    :param ensure_exists: See `ensure_exists <platformdirs.api.PlatformDirsABC.ensure_exists>`.
    :returns: cache directory tied to the user
    """
def site_cache_dir(appname: str | None = None, appauthor: str | None | Literal[False] = None, version: str | None = None, opinion: bool = True, ensure_exists: bool = False) -> str:
    """
    :param appname: See `appname <platformdirs.api.PlatformDirsABC.appname>`.
    :param appauthor: See `appauthor <platformdirs.api.PlatformDirsABC.appauthor>`.
    :param version: See `version <platformdirs.api.PlatformDirsABC.version>`.
    :param opinion: See `opinion <platformdirs.api.PlatformDirsABC.opinion>`.
    :param ensure_exists: See `ensure_exists <platformdirs.api.PlatformDirsABC.ensure_exists>`.
    :returns: cache directory tied to the user
    """
def user_state_dir(appname: str | None = None, appauthor: str | None | Literal[False] = None, version: str | None = None, roaming: bool = False, ensure_exists: bool = False) -> str:
    """
    :param appname: See `appname <platformdirs.api.PlatformDirsABC.appname>`.
    :param appauthor: See `appauthor <platformdirs.api.PlatformDirsABC.appauthor>`.
    :param version: See `version <platformdirs.api.PlatformDirsABC.version>`.
    :param roaming: See `roaming <platformdirs.api.PlatformDirsABC.roaming>`.
    :param ensure_exists: See `ensure_exists <platformdirs.api.PlatformDirsABC.ensure_exists>`.
    :returns: state directory tied to the user
    """
def user_log_dir(appname: str | None = None, appauthor: str | None | Literal[False] = None, version: str | None = None, opinion: bool = True, ensure_exists: bool = False) -> str:
    """
    :param appname: See `appname <platformdirs.api.PlatformDirsABC.appname>`.
    :param appauthor: See `appauthor <platformdirs.api.PlatformDirsABC.appauthor>`.
    :param version: See `version <platformdirs.api.PlatformDirsABC.version>`.
    :param opinion: See `roaming <platformdirs.api.PlatformDirsABC.opinion>`.
    :param ensure_exists: See `ensure_exists <platformdirs.api.PlatformDirsABC.ensure_exists>`.
    :returns: log directory tied to the user
    """
def user_documents_dir() -> str:
    """
    :returns: documents directory tied to the user
    """
def user_pictures_dir() -> str:
    """
    :returns: pictures directory tied to the user
    """
def user_videos_dir() -> str:
    """
    :returns: videos directory tied to the user
    """
def user_music_dir() -> str:
    """
    :returns: music directory tied to the user
    """
def user_runtime_dir(appname: str | None = None, appauthor: str | None | Literal[False] = None, version: str | None = None, opinion: bool = True, ensure_exists: bool = False) -> str:
    """
    :param appname: See `appname <platformdirs.api.PlatformDirsABC.appname>`.
    :param appauthor: See `appauthor <platformdirs.api.PlatformDirsABC.appauthor>`.
    :param version: See `version <platformdirs.api.PlatformDirsABC.version>`.
    :param opinion: See `opinion <platformdirs.api.PlatformDirsABC.opinion>`.
    :param ensure_exists: See `ensure_exists <platformdirs.api.PlatformDirsABC.ensure_exists>`.
    :returns: runtime directory tied to the user
    """
def user_data_path(appname: str | None = None, appauthor: str | None | Literal[False] = None, version: str | None = None, roaming: bool = False, ensure_exists: bool = False) -> Path:
    """
    :param appname: See `appname <platformdirs.api.PlatformDirsABC.appname>`.
    :param appauthor: See `appauthor <platformdirs.api.PlatformDirsABC.appauthor>`.
    :param version: See `version <platformdirs.api.PlatformDirsABC.version>`.
    :param roaming: See `roaming <platformdirs.api.PlatformDirsABC.roaming>`.
    :param ensure_exists: See `ensure_exists <platformdirs.api.PlatformDirsABC.ensure_exists>`.
    :returns: data path tied to the user
    """
def site_data_path(appname: str | None = None, appauthor: str | None | Literal[False] = None, version: str | None = None, multipath: bool = False, ensure_exists: bool = False) -> Path:
    """
    :param appname: See `appname <platformdirs.api.PlatformDirsABC.appname>`.
    :param appauthor: See `appauthor <platformdirs.api.PlatformDirsABC.appauthor>`.
    :param version: See `version <platformdirs.api.PlatformDirsABC.version>`.
    :param multipath: See `multipath <platformdirs.api.PlatformDirsABC.multipath>`.
    :param ensure_exists: See `ensure_exists <platformdirs.api.PlatformDirsABC.ensure_exists>`.
    :returns: data path shared by users
    """
def user_config_path(appname: str | None = None, appauthor: str | None | Literal[False] = None, version: str | None = None, roaming: bool = False, ensure_exists: bool = False) -> Path:
    """
    :param appname: See `appname <platformdirs.api.PlatformDirsABC.appname>`.
    :param appauthor: See `appauthor <platformdirs.api.PlatformDirsABC.appauthor>`.
    :param version: See `version <platformdirs.api.PlatformDirsABC.version>`.
    :param roaming: See `roaming <platformdirs.api.PlatformDirsABC.roaming>`.
    :param ensure_exists: See `ensure_exists <platformdirs.api.PlatformDirsABC.ensure_exists>`.
    :returns: config path tied to the user
    """
def site_config_path(appname: str | None = None, appauthor: str | None | Literal[False] = None, version: str | None = None, multipath: bool = False, ensure_exists: bool = False) -> Path:
    """
    :param appname: See `appname <platformdirs.api.PlatformDirsABC.appname>`.
    :param appauthor: See `appauthor <platformdirs.api.PlatformDirsABC.appauthor>`.
    :param version: See `version <platformdirs.api.PlatformDirsABC.version>`.
    :param multipath: See `roaming <platformdirs.api.PlatformDirsABC.multipath>`.
    :param ensure_exists: See `ensure_exists <platformdirs.api.PlatformDirsABC.ensure_exists>`.
    :returns: config path shared by the users
    """
def site_cache_path(appname: str | None = None, appauthor: str | None | Literal[False] = None, version: str | None = None, opinion: bool = True, ensure_exists: bool = False) -> Path:
    """
    :param appname: See `appname <platformdirs.api.PlatformDirsABC.appname>`.
    :param appauthor: See `appauthor <platformdirs.api.PlatformDirsABC.appauthor>`.
    :param version: See `version <platformdirs.api.PlatformDirsABC.version>`.
    :param opinion: See `opinion <platformdirs.api.PlatformDirsABC.opinion>`.
    :param ensure_exists: See `ensure_exists <platformdirs.api.PlatformDirsABC.ensure_exists>`.
    :returns: cache directory tied to the user
    """
def user_cache_path(appname: str | None = None, appauthor: str | None | Literal[False] = None, version: str | None = None, opinion: bool = True, ensure_exists: bool = False) -> Path:
    """
    :param appname: See `appname <platformdirs.api.PlatformDirsABC.appname>`.
    :param appauthor: See `appauthor <platformdirs.api.PlatformDirsABC.appauthor>`.
    :param version: See `version <platformdirs.api.PlatformDirsABC.version>`.
    :param opinion: See `roaming <platformdirs.api.PlatformDirsABC.opinion>`.
    :param ensure_exists: See `ensure_exists <platformdirs.api.PlatformDirsABC.ensure_exists>`.
    :returns: cache path tied to the user
    """
def user_state_path(appname: str | None = None, appauthor: str | None | Literal[False] = None, version: str | None = None, roaming: bool = False, ensure_exists: bool = False) -> Path:
    """
    :param appname: See `appname <platformdirs.api.PlatformDirsABC.appname>`.
    :param appauthor: See `appauthor <platformdirs.api.PlatformDirsABC.appauthor>`.
    :param version: See `version <platformdirs.api.PlatformDirsABC.version>`.
    :param roaming: See `roaming <platformdirs.api.PlatformDirsABC.roaming>`.
    :param ensure_exists: See `ensure_exists <platformdirs.api.PlatformDirsABC.ensure_exists>`.
    :returns: state path tied to the user
    """
def user_log_path(appname: str | None = None, appauthor: str | None | Literal[False] = None, version: str | None = None, opinion: bool = True, ensure_exists: bool = False) -> Path:
    """
    :param appname: See `appname <platformdirs.api.PlatformDirsABC.appname>`.
    :param appauthor: See `appauthor <platformdirs.api.PlatformDirsABC.appauthor>`.
    :param version: See `version <platformdirs.api.PlatformDirsABC.version>`.
    :param opinion: See `roaming <platformdirs.api.PlatformDirsABC.opinion>`.
    :param ensure_exists: See `ensure_exists <platformdirs.api.PlatformDirsABC.ensure_exists>`.
    :returns: log path tied to the user
    """
def user_documents_path() -> Path:
    """
    :returns: documents path tied to the user
    """
def user_pictures_path() -> Path:
    """
    :returns: pictures path tied to the user
    """
def user_videos_path() -> Path:
    """
    :returns: videos path tied to the user
    """
def user_music_path() -> Path:
    """
    :returns: music path tied to the user
    """
def user_runtime_path(appname: str | None = None, appauthor: str | None | Literal[False] = None, version: str | None = None, opinion: bool = True, ensure_exists: bool = False) -> Path:
    """
    :param appname: See `appname <platformdirs.api.PlatformDirsABC.appname>`.
    :param appauthor: See `appauthor <platformdirs.api.PlatformDirsABC.appauthor>`.
    :param version: See `version <platformdirs.api.PlatformDirsABC.version>`.
    :param opinion: See `opinion <platformdirs.api.PlatformDirsABC.opinion>`.
    :param ensure_exists: See `ensure_exists <platformdirs.api.PlatformDirsABC.ensure_exists>`.
    :returns: runtime path tied to the user
    """
