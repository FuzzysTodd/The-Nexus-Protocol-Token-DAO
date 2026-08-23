__docformat__: str
COPYRIGHT: str
TITLE: str
SOURCE: str
DESCRSHORT: str
DESCRLONG: str
NOTE: str

def load_pandas(): ...
def load():
    """
    Load the El Nino data and return a Dataset class.

    Returns
    -------
    Dataset
        See DATASET_PROPOSAL.txt for more information.

    Notes
    -----
    The elnino Dataset instance does not contain endog and exog attributes.
    """
