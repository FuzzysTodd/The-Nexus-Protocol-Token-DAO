from .. import lib_acquisition_function as lib_acquisition_function, lib_constraint_summation as lib_constraint_summation
from _typeshed import Incomplete

CONSTRAINT_LOWERBOUND: Incomplete
CONSTRAINT_UPPERBOUND: Incomplete
CONSTRAINT_PARAMS_IDX: Incomplete

def selection_r(x_bounds, x_types, clusteringmodel_gmm_good, clusteringmodel_gmm_bad, num_starting_points: int = 100, minimize_constraints_fun: Incomplete | None = None):
    """
    Select using different types.
    """
def selection(x_bounds, x_types, clusteringmodel_gmm_good, clusteringmodel_gmm_bad, minimize_starting_points, minimize_constraints_fun: Incomplete | None = None):
    """
    Select the lowest mu value
    """
