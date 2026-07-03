from _typeshed import Incomplete
from torch.distributed.elastic.multiprocessing import Std as Std, start_processes as start_processes

format_str: str
logger: Incomplete

class _CPUinfo:
    """
    Get CPU inforamation, such as cores list and NUMA information.
    """
    cpuinfo: Incomplete
    node_nums: Incomplete
    node_physical_cores: Incomplete
    node_logical_cores: Incomplete
    physical_core_node_map: Incomplete
    logical_core_node_map: Incomplete
    def __init__(self, test_input: str = '') -> None: ...
    def get_node_physical_cores(self, node_id): ...
    def get_node_logical_cores(self, node_id): ...
    def get_all_physical_cores(self): ...
    def get_all_logical_cores(self): ...
    def numa_aware_check(self, core_list):
        """
        Check whether all cores in core_list are in the same NUMA node. cross NUMA will reduce perforamnce.
        We strongly advice to not use cores on different nodes.
        """

class _Launcher:
    """
     Class for launcher
    """
    msg_lib_notfound: Incomplete
    cpuinfo: Incomplete
    def __init__(self) -> None: ...
    def add_lib_preload(self, lib_type):
        """
        Enale TCMalloc/JeMalloc/intel OpenMP
        """
    def set_memory_allocator(self, enable_tcmalloc: bool = True, enable_jemalloc: bool = False, use_default_allocator: bool = False) -> None:
        """
        Enable TCMalloc/JeMalloc with LD_PRELOAD and set configuration for JeMalloc.
        By default, PTMalloc will be used for PyTorch, but TCMalloc and JeMalloc can get better
        memory resue and reduce page fault to improve performance.
        """
    def log_env_var(self, env_var_name: str = '') -> None: ...
    def set_env(self, env_name, env_value) -> None: ...
    def set_multi_thread_and_allocator(self, ncores_per_instance, disable_iomp: bool = False, set_kmp_affinity: bool = True, enable_tcmalloc: bool = True, enable_jemalloc: bool = False, use_default_allocator: bool = False) -> None:
        """
        Set multi-thread configuration and enable Intel openMP and TCMalloc/JeMalloc.
        By default, GNU openMP and PTMalloc are used in PyTorch. but Intel openMP and TCMalloc/JeMalloc are better alternatives
        to get performance benifit.
        """
    def launch(self, args) -> None: ...

def create_args(parser: Incomplete | None = None) -> None:
    """
    Helper function parsing the command line options
    @retval ArgumentParser
    """
def main(args) -> None: ...
