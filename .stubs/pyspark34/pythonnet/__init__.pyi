import clr_loader

__all__ = ['set_runtime', 'set_runtime_from_env', 'load', 'unload', 'get_runtime_info']

def set_runtime(runtime: clr_loader.Runtime | str, **params: str) -> None:
    """Set up a clr_loader runtime without loading it

    :param runtime:
        Either an already initialised `clr_loader` runtime, or one of netfx,
        coreclr, mono, or default. If a string parameter is given, the runtime
        will be created.
    """
def get_runtime_info() -> clr_loader.RuntimeInfo | None:
    """Retrieve information on the configured runtime"""
def set_runtime_from_env() -> None:
    """Set up the runtime using the environment

    This will use the environment variable PYTHONNET_RUNTIME to decide the
    runtime to use, which may be one of netfx, coreclr or mono. The parameters
    of the respective clr_loader.get_<runtime> functions can also be given as
    environment variables, named `PYTHONNET_<RUNTIME>_<PARAM_NAME>`. In
    particular, to use `PYTHONNET_RUNTIME=coreclr`, the variable
    `PYTHONNET_CORECLR_RUNTIME_CONFIG` has to be set to a valid
    `.runtimeconfig.json`.

    If no environment variable is specified, a globally installed Mono is used
    for all environments but Windows, on Windows the legacy .NET Framework is
    used.
    """
def load(runtime: clr_loader.Runtime | str | None = None, **params: str) -> None:
    """Load Python.NET in the specified runtime

    The same parameters as for `set_runtime` can be used. By default,
    `set_default_runtime` is called if no environment has been set yet and no
    parameters are passed."""
def unload() -> None:
    """Explicitly unload a loaded runtime and shut down Python.NET"""
