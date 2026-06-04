def check_feasibility(x_bounds, lowerbound, upperbound):
    """
    This can have false positives.
    For examples, parameters can only be 0 or 5, and the summation constraint is between 6 and 7.
    """
def rand(x_bounds, x_types, lowerbound, upperbound, max_retries: int = 100):
    """
    Key idea is that we try to move towards upperbound, by randomly choose one
    value for each parameter. However, for the last parameter,
    we need to make sure that its value can help us get above lowerbound
    """
