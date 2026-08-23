from . import lib_data as lib_data
from _typeshed import Incomplete

def next_hyperparameter_expected_improvement(fun_prediction, fun_prediction_args, x_bounds, x_types, samples_y_aggregation, minimize_starting_points, minimize_constraints_fun: Incomplete | None = None):
    '''
    "Expected Improvement" acquisition function
    '''
def next_hyperparameter_lowest_confidence(fun_prediction, fun_prediction_args, x_bounds, x_types, minimize_starting_points, minimize_constraints_fun: Incomplete | None = None):
    '''
    "Lowest Confidence" acquisition function
    '''
def next_hyperparameter_lowest_mu(fun_prediction, fun_prediction_args, x_bounds, x_types, minimize_starting_points, minimize_constraints_fun: Incomplete | None = None):
    '''
    "Lowest Mu" acquisition function
    '''
