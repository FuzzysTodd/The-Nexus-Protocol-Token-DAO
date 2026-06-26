from .. import lib_acquisition_function as lib_acquisition_function, lib_constraint_summation as lib_constraint_summation, lib_data as lib_data
from _typeshed import Incomplete

CONSTRAINT_LOWERBOUND: Incomplete
CONSTRAINT_UPPERBOUND: Incomplete
CONSTRAINT_PARAMS_IDX: Incomplete

def selection_r(acquisition_function, samples_y_aggregation, x_bounds, x_types, regressor_gp, num_starting_points: int = 100, minimize_constraints_fun: Incomplete | None = None):
    """
    Selecte R value
    """
def selection(acquisition_function, samples_y_aggregation, x_bounds, x_types, regressor_gp, minimize_starting_points, minimize_constraints_fun: Incomplete | None = None):
    """
    selection
    """
