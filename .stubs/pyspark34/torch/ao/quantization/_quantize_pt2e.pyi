from .backend_config import BackendConfig as BackendConfig
from .fx import prepare as prepare
from .qconfig_mapping import QConfigMapping as QConfigMapping
from torch.fx import GraphModule as GraphModule
from typing import Any, Tuple

def prepare_pt2e(model: GraphModule, qconfig_mapping: QConfigMapping, example_inputs: Tuple[Any, ...], backend_config: BackendConfig): ...
def convert_pt2e(model: GraphModule): ...
