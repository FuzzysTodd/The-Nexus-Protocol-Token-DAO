import abc
from _typeshed import Incomplete
from abc import ABC, abstractmethod
from pathlib import Path
from typing import Literal

class PlatformDirsABC(ABC, metaclass=abc.ABCMeta):
    """
    Abstract base class for platform directories.
    """
    appname: Incomplete
    appauthor: Incomplete
    version: Incomplete
    roaming: Incomplete
    multipath: Incomplete
    opinion: Incomplete
    ensure_exists: Incomplete
    def __init__(self, appname: str | None = None, appauthor: str | None | Literal[False] = None, version: str | None = None, roaming: bool = False, multipath: bool = False, opinion: bool = True, ensure_exists: bool = False) -> None:
        """
        Create a new platform directory.

        :param appname: See `appname`.
        :param appauthor: See `appauthor`.
        :param version: See `version`.
        :param roaming: See `roaming`.
        :param multipath: See `multipath`.
        :param opinion: See `opinion`.
        :param ensure_exists: See `ensure_exists`.
        """
    @property
    @abstractmethod
    def user_data_dir(self) -> str:
        """:return: data directory tied to the user"""
    @property
    @abstractmethod
    def site_data_dir(self) -> str:
        """:return: data directory shared by users"""
    @property
    @abstractmethod
    def user_config_dir(self) -> str:
        """:return: config directory tied to the user"""
    @property
    @abstractmethod
    def site_config_dir(self) -> str:
        """:return: config directory shared by the users"""
    @property
    @abstractmethod
    def user_cache_dir(self) -> str:
        """:return: cache directory tied to the user"""
    @property
    @abstractmethod
    def site_cache_dir(self) -> str:
        """:return: cache directory shared by users"""
    @property
    @abstractmethod
    def user_state_dir(self) -> str:
        """:return: state directory tied to the user"""
    @property
    @abstractmethod
    def user_log_dir(self) -> str:
        """:return: log directory tied to the user"""
    @property
    @abstractmethod
    def user_documents_dir(self) -> str:
        """:return: documents directory tied to the user"""
    @property
    @abstractmethod
    def user_pictures_dir(self) -> str:
        """:return: pictures directory tied to the user"""
    @property
    @abstractmethod
    def user_videos_dir(self) -> str:
        """:return: videos directory tied to the user"""
    @property
    @abstractmethod
    def user_music_dir(self) -> str:
        """:return: music directory tied to the user"""
    @property
    @abstractmethod
    def user_runtime_dir(self) -> str:
        """:return: runtime directory tied to the user"""
    @property
    def user_data_path(self) -> Path:
        """:return: data path tied to the user"""
    @property
    def site_data_path(self) -> Path:
        """:return: data path shared by users"""
    @property
    def user_config_path(self) -> Path:
        """:return: config path tied to the user"""
    @property
    def site_config_path(self) -> Path:
        """:return: config path shared by the users"""
    @property
    def user_cache_path(self) -> Path:
        """:return: cache path tied to the user"""
    @property
    def site_cache_path(self) -> Path:
        """:return: cache path shared by users"""
    @property
    def user_state_path(self) -> Path:
        """:return: state path tied to the user"""
    @property
    def user_log_path(self) -> Path:
        """:return: log path tied to the user"""
    @property
    def user_documents_path(self) -> Path:
        """:return: documents path tied to the user"""
    @property
    def user_pictures_path(self) -> Path:
        """:return: pictures path tied to the user"""
    @property
    def user_videos_path(self) -> Path:
        """:return: videos path tied to the user"""
    @property
    def user_music_path(self) -> Path:
        """:return: music path tied to the user"""
    @property
    def user_runtime_path(self) -> Path:
        """:return: runtime path tied to the user"""
