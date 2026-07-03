from optuna.multi_objective._hypervolume import BaseHypervolume as BaseHypervolume

class WFG(BaseHypervolume):
    '''Hypervolume calculator for any dimension.

    This class exactly calculates the hypervolume for any dimension by using the WFG algorithm.
    For detail, see `While, Lyndon, Lucas Bradstreet, and Luigi Barone. "A fast way of
    calculating exact hypervolumes." Evolutionary Computation, IEEE Transactions on 16.1 (2012)
    : 86-95.`.
    '''
    def __init__(self) -> None: ...
