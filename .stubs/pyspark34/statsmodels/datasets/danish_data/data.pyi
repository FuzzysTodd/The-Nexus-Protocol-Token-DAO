from _typeshed import Incomplete

__docformat__: str
COPYRIGHT: str
TITLE = __doc__
SOURCE: str
DESCRSHORT: str
DESCRLONG = DESCRSHORT
NOTE: str

def load_pandas(): ...
def load():
    """
    Load the US macro data and return a Dataset class.

    Returns
    -------
    Dataset
        See DATASET_PROPOSAL.txt for more information.

    Notes
    -----
    The Dataset instance does not contain endog and exog attributes.
    """

variable_names: Incomplete
