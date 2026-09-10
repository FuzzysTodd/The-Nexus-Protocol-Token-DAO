from _typeshed import Incomplete
from typing import Dict, List

class MachineInfo:
    """Class encapsulating Machine Info logic."""
    silent: Incomplete
    logger: Incomplete
    machine_info: Incomplete
    def __init__(self, silent: bool = False, logger: Incomplete | None = None) -> None: ...
    def get_machine_info(self):
        """Get machine info in metric format"""
    def get_memory_info(self) -> Dict:
        """Get memory info"""
    def get_cpu_info(self) -> Dict:
        """Get CPU info"""
    def get_gpu_info_by_nvml(self) -> Dict:
        """Get GPU info using nvml"""
    def get_related_packages(self) -> List[str]: ...
    def get_onnxruntime_info(self) -> Dict: ...
    def get_pytorch_info(self) -> Dict: ...
    def get_tensorflow_info(self) -> Dict: ...

def parse_arguments(): ...
def get_machine_info(silent: bool = True) -> str: ...
