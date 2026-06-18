from .common_utils import get_file_lock as get_file_lock
from .constants import NNI_HOME_DIR as NNI_HOME_DIR
from _typeshed import Incomplete

def config_v0_to_v1(config: dict) -> dict: ...

class Config:
    """a util class to load and save config"""
    experiment_id: Incomplete
    conn: Incomplete
    def __init__(self, experiment_id: str, log_dir: str) -> None: ...
    config: Incomplete
    def refresh_config(self) -> None:
        """refresh to get latest config"""
    def get_config(self):
        """get a value according to key"""

class Experiments:
    """Maintain experiment list"""
    experiment_file: Incomplete
    lock: Incomplete
    experiments: Incomplete
    def __init__(self, home_dir=...) -> None: ...
    def add_experiment(self, expId, port, startTime, platform, experiment_name, endTime: str = 'N/A', status: str = 'INITIALIZED', tag=[], pid: Incomplete | None = None, webuiUrl=[], logDir: str = '', prefixUrl: Incomplete | None = None) -> None:
        """set {key:value} pairs to self.experiment"""
    def update_experiment(self, expId, key, value):
        """Update experiment"""
    def remove_experiment(self, expId) -> None:
        """remove an experiment by id"""
    def get_all_experiments(self):
        """return all of experiments"""
    def write_file(self):
        """save config to local file"""
    def read_file(self):
        """load config from local file"""
