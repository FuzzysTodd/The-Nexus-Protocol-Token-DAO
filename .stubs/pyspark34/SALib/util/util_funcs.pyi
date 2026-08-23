from _typeshed import Incomplete

def avail_approaches(pkg):
    """Create list of available modules.

    Parameters
    ----------
    pkg : module
        module to inspect

    Returns
    -------
    method : list
        A list of available submodules
    """
def read_param_file(filename, delimiter: Incomplete | None = None):
    """Unpacks a parameter file into a dictionary

    Reads a parameter file of format::

        Param1,0,1,Group1,dist1
        Param2,0,1,Group2,dist2
        Param3,0,1,Group3,dist3

    (Group and Dist columns are optional)

    Returns a dictionary containing:
        - names - the names of the parameters
        - bounds - a list of lists of lower and upper bounds
        - num_vars - a scalar indicating the number of variables
                     (the length of names)
        - groups - a list of group names (strings) for each variable
        - dists - a list of distributions for the problem,
                    None if not specified or all uniform

    Parameters
    ----------
    filename : str
        The path to the parameter file
    delimiter : str, default=None
        The delimiter used in the file to distinguish between columns

    """
