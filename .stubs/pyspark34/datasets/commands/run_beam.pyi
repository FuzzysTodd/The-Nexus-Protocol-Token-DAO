from argparse import ArgumentParser
from datasets import config as config
from datasets.builder import DatasetBuilder as DatasetBuilder
from datasets.commands import BaseDatasetsCLICommand as BaseDatasetsCLICommand
from datasets.download.download_config import DownloadConfig as DownloadConfig
from datasets.download.download_manager import DownloadMode as DownloadMode
from datasets.load import dataset_module_factory as dataset_module_factory, import_main_class as import_main_class
from datasets.utils.info_utils import VerificationMode as VerificationMode

def run_beam_command_factory(args, **kwargs): ...

class RunBeamCommand(BaseDatasetsCLICommand):
    @staticmethod
    def register_subcommand(parser: ArgumentParser): ...
    def __init__(self, dataset: str, name: str, cache_dir: str, beam_pipeline_options: str, data_dir: str, all_configs: bool, save_infos: bool, ignore_verifications: bool, force_redownload: bool, **config_kwargs) -> None: ...
    def run(self) -> None: ...
