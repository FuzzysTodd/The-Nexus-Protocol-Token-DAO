from jax import version as version
from jax._src import lib as lib, xla_bridge as xla_bridge

def try_nvidia_smi() -> str | None: ...
def print_environment_info(return_string: bool = False) -> None | str:
    """Returns a string containing local environment & JAX installation information.

  This is useful information to include when asking a question or filing a bug.

  Args: return_string (bool) : if True, return the string rather than printing
  to stdout.
  """
