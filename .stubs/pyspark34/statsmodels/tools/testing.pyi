from _typeshed import Incomplete
from statsmodels.tools.tools import Bunch as Bunch

PARAM_LIST: Incomplete

def bunch_factory(attribute, columns):
    """
    Generates a special purpose Bunch class

    Parameters
    ----------
    attribute: str
        Attribute to access when splitting
    columns: List[str]
        List of names to use when splitting the columns of attribute

    Notes
    -----
    After the class is initialized as a Bunch, the columne of attribute
    are split so that Bunch has the keys in columns and
    bunch[column[i]] = bunch[attribute][:, i]
    """

ParamsTableTestBunch: Incomplete
MarginTableTestBunch: Incomplete

class Holder:
    """
    Test-focused class to simplify accessing values by attribute
    """
    def __init__(self, **kwds) -> None: ...

def assert_equal(actual, desired, err_msg: str = '', verbose: bool = True, **kwds) -> None: ...
