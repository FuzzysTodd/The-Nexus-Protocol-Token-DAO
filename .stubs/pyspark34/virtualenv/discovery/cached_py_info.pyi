from _typeshed import Incomplete
from virtualenv.app_data import AppDataDisabled as AppDataDisabled
from virtualenv.discovery.py_info import PythonInfo as PythonInfo
from virtualenv.util.subprocess import subprocess as subprocess

def from_exe(cls, app_data, exe, env: Incomplete | None = None, raise_on_error: bool = True, ignore_cache: bool = False): ...

COOKIE_LENGTH: int

def gen_cookie(): ...

class LogCmd:
    cmd: Incomplete
    env: Incomplete
    def __init__(self, cmd, env: Incomplete | None = None) -> None: ...

def clear(app_data) -> None: ...

___all___: Incomplete
