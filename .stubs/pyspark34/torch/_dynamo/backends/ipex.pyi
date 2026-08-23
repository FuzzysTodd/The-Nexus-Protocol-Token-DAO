from .common import fake_tensor_unsupported as fake_tensor_unsupported
from _typeshed import Incomplete
from torch._dynamo import register_backend as register_backend

log: Incomplete

def ipex(model, inputs): ...
def has_ipex(): ...
