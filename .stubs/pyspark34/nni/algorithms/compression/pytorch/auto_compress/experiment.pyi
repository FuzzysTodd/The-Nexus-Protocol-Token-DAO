from _typeshed import Incomplete
from nni.algorithms.compression.pytorch.auto_compress.interface import AbstractAutoCompressionModule as AbstractAutoCompressionModule
from nni.experiment import Experiment as Experiment, ExperimentConfig as ExperimentConfig

class AutoCompressionExperiment(Experiment):
    module_file_path: Incomplete
    module_name: Incomplete
    def __init__(self, auto_compress_module: AbstractAutoCompressionModule, config_or_platform: ExperimentConfig | str | list[str]) -> None:
        """
        Prepare an auto compression experiment.

        Parameters
        ----------
        auto_compress_module
            The module provided by the user implements the `AbstractAutoCompressionModule` interfaces.
            Remember put the module file under `trial_code_directory`.
        config_or_platform
            Experiment configuration or training service name.
        """
    def start(self, port: int, debug: bool) -> None: ...
