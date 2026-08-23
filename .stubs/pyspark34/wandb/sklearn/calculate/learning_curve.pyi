from _typeshed import Incomplete
from wandb.sklearn import utils as utils

def learning_curve(model, X, y, cv: Incomplete | None = None, shuffle: bool = False, random_state: Incomplete | None = None, train_sizes: Incomplete | None = None, n_jobs: int = 1, scoring: Incomplete | None = None):
    """Train model on datasets of varying size and generates plot of score vs size.

    Called by plot_learning_curve to visualize learning curve. Please use the function
    plot_learning_curve() if you wish to visualize your learning curves.
    """
def make_table(train, test, train_sizes): ...
