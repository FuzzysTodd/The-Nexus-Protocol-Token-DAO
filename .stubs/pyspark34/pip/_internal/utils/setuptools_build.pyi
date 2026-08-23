from typing import List, Sequence

def make_setuptools_shim_args(setup_py_path: str, global_options: Sequence[str] | None = None, no_user_config: bool = False, unbuffered_output: bool = False) -> List[str]:
    """
    Get setuptools command arguments with shim wrapped setup file invocation.

    :param setup_py_path: The path to setup.py to be wrapped.
    :param global_options: Additional global options.
    :param no_user_config: If True, disables personal user configuration.
    :param unbuffered_output: If True, adds the unbuffered switch to the
     argument list.
    """
def make_setuptools_bdist_wheel_args(setup_py_path: str, global_options: Sequence[str], build_options: Sequence[str], destination_dir: str) -> List[str]: ...
def make_setuptools_clean_args(setup_py_path: str, global_options: Sequence[str]) -> List[str]: ...
def make_setuptools_develop_args(setup_py_path: str, *, global_options: Sequence[str], no_user_config: bool, prefix: str | None, home: str | None, use_user_site: bool) -> List[str]: ...
def make_setuptools_egg_info_args(setup_py_path: str, egg_info_dir: str | None, no_user_config: bool) -> List[str]: ...
