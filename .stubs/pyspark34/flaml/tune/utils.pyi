from . import sample as sample
from _typeshed import Incomplete
from typing import Sequence

def choice(categories: Sequence, order: Incomplete | None = None):
    """Sample a categorical value.
    Sampling from ``tune.choice([1, 2])`` is equivalent to sampling from
    ``np.random.choice([1, 2])``

    Args:
        categories (Sequence): Sequence of categories to sample from.
        order (bool): Whether the categories have an order. If None, will be decided autoamtically:
            Numerical categories have an order, while string categories do not.
    """
