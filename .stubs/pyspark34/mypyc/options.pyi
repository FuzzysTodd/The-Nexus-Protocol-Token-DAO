from _typeshed import Incomplete

class CompilerOptions:
    strip_asserts: Incomplete
    multi_file: Incomplete
    verbose: Incomplete
    separate: Incomplete
    global_opts: Incomplete
    target_dir: Incomplete
    include_runtime_files: Incomplete
    capi_version: Incomplete
    python_version: Incomplete
    def __init__(self, strip_asserts: bool = False, multi_file: bool = False, verbose: bool = False, separate: bool = False, target_dir: str | None = None, include_runtime_files: bool | None = None, capi_version: tuple[int, int] | None = None, python_version: tuple[int, int] | None = None) -> None: ...
