from ..qconfig_mapping import QConfigMapping as QConfigMapping
from ..utils import get_qconfig_dtypes as get_qconfig_dtypes
from torch.ao.quantization import QConfig as QConfig
from torch.ao.quantization.backend_config import BackendConfig as BackendConfig, DTypeConfig as DTypeConfig
from torch.ao.quantization.backend_config.utils import get_module_to_qat_module as get_module_to_qat_module
from torch.ao.quantization.qconfig import QConfigAny as QConfigAny, qconfig_equals as qconfig_equals
from torch.fx import GraphModule as GraphModule
from torch.fx.graph import Graph as Graph
