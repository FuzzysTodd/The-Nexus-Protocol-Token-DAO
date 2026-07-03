from SALib import analyze as analyze, sample as sample
from SALib.util import avail_approaches as avail_approaches

def parse_subargs(module, parser, method, opts):
    """Attach argument parser for action specific options.

    Parameters
    ----------
    module : module
        name of module to extract action from
    parser : argparser
        argparser object to attach additional arguments to
    method : str
        name of method (morris, sobol, etc).
        Must match one of the available submodules
    opts : list
        A list of argument options to parse

    Returns
    -------
    subargs : argparser namespace object
    """
def main() -> None: ...
