from . import comptime as comptime, config as config, external_utils as external_utils
from _typeshed import Incomplete

HAS_PRIMS_REFS: bool
SKIP_DIRS: Incomplete
FILENAME_ALLOWLIST: Incomplete
SKIP_DIRS_RE: Incomplete

def add(import_name: str): ...
def check(filename, allow_torch: bool = False):
    """Should skip this file?"""
def is_torch_inline_allowed(filename): ...
def dynamo_dir(): ...
def is_torch(filename): ...
