from _typeshed import Incomplete
from argparse import ArgumentParser
from datasets.builder import DatasetBuilder as DatasetBuilder
from datasets.commands import BaseDatasetsCLICommand as BaseDatasetsCLICommand
from datasets.download.download_manager import DownloadMode as DownloadMode
from datasets.load import dataset_module_factory as dataset_module_factory, import_main_class as import_main_class
from datasets.utils.info_utils import VerificationMode as VerificationMode
from datasets.utils.logging import ERROR as ERROR, get_logger as get_logger

logger: Incomplete

class TestCommand(BaseDatasetsCLICommand):
    __test__: bool
    @staticmethod
    def register_subcommand(parser: ArgumentParser): ...
    def __init__(self, dataset: str, name: str, cache_dir: str, data_dir: str, all_configs: bool, save_infos: bool, ignore_verifications: bool, force_redownload: bool, clear_cache: bool) -> None: ...
    def run(self) -> None: ...
