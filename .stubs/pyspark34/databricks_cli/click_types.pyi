from _typeshed import Incomplete
from click import Option, ParamType

class OutputClickType(ParamType):
    name: str
    help: str
    def convert(self, value, param, ctx): ...
    @classmethod
    def is_json(cls, value): ...
    @classmethod
    def is_table(cls, value): ...

class JsonClickType(ParamType):
    name: str
    @classmethod
    def help(cls, endpoint): ...

class JobIdClickType(ParamType):
    name: str
    help: str

class RunIdClickType(ParamType):
    name: str

class ClusterIdClickType(ParamType):
    name: str
    help: str

class ClusterPolicyIdClickType(ParamType):
    name: str
    help: str

class InstancePoolIdClickType(ParamType):
    name: str
    help: str

class SecretScopeClickType(ParamType):
    name: str
    help: str

class SecretKeyClickType(ParamType):
    name: str
    help: str

class SecretPrincipalClickType(ParamType):
    name: str
    help: str

class PipelineSpecClickType(ParamType):
    name: str
    help: Incomplete

class PipelineSettingClickType(ParamType):
    name: str
    help: str

class PipelineIdClickType(ParamType):
    name: str
    help: str

class MetastoreIdClickType(ParamType):
    name: str
    help: str

class WorkspaceIdClickType(ParamType):
    name: str
    help: str

class OneOfOption(Option):
    one_of: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...
    def handle_parse_result(self, ctx, opts, args): ...

class OptionalOneOfOption(Option):
    one_of: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...
    def handle_parse_result(self, ctx, opts, args): ...

class ContextObject:
    def __init__(self) -> None: ...
    def set_debug(self, debug: bool = False) -> None: ...
    @property
    def debug_mode(self): ...
    def set_profile(self, profile) -> None: ...
    def get_profile(self): ...

class RequiredOptions(Option):
    one_of: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...
    def handle_parse_result(self, ctx, opts, args): ...
