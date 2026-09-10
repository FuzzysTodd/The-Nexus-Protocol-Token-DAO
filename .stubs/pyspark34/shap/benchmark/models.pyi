from _typeshed import Incomplete

class KerasWrap:
    """ A wrapper that allows us to set parameters in the constructor and do a reset before fitting.
    """
    model: Incomplete
    epochs: Incomplete
    flatten_output: Incomplete
    init_weights: Incomplete
    scaler: Incomplete
    def __init__(self, model, epochs, flatten_output: bool = False) -> None: ...
    def fit(self, X, y, verbose: int = 0): ...
    def predict(self, X): ...

def corrgroups60__lasso():
    """ Lasso Regression
    """
def corrgroups60__ridge():
    """ Ridge Regression
    """
def corrgroups60__decision_tree():
    """ Decision Tree
    """
def corrgroups60__random_forest():
    """ Random Forest
    """
def corrgroups60__gbm():
    """ Gradient Boosted Trees
    """
def corrgroups60__ffnn():
    """ 4-Layer Neural Network
    """
def independentlinear60__lasso():
    """ Lasso Regression
    """
def independentlinear60__ridge():
    """ Ridge Regression
    """
def independentlinear60__decision_tree():
    """ Decision Tree
    """
def independentlinear60__random_forest():
    """ Random Forest
    """
def independentlinear60__gbm():
    """ Gradient Boosted Trees
    """
def independentlinear60__ffnn():
    """ 4-Layer Neural Network
    """
def cric__lasso():
    """ Lasso Regression
    """
def cric__ridge():
    """ Ridge Regression
    """
def cric__decision_tree():
    """ Decision Tree
    """
def cric__random_forest():
    """ Random Forest
    """
def cric__gbm():
    """ Gradient Boosted Trees
    """
def cric__ffnn():
    """ 4-Layer Neural Network
    """
def human__decision_tree():
    """ Decision Tree
    """
