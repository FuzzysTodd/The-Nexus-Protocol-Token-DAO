from .kernelapp import IPKernelApp as IPKernelApp
from _typeshed import Incomplete

def embed_kernel(module: Incomplete | None = None, local_ns: Incomplete | None = None, **kwargs) -> None:
    """Embed and start an IPython kernel in a given scope.

    Parameters
    ----------
    module : ModuleType, optional
        The module to load into IPython globals (default: caller)
    local_ns : dict, optional
        The namespace to load into IPython user namespace (default: caller)
    kwargs : dict, optional
        Further keyword args are relayed to the IPKernelApp constructor,
        allowing configuration of the Kernel.  Will only have an effect
        on the first embed_kernel call for a given process.

    """
