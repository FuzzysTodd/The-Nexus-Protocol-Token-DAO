__docformat__: str
COPYRIGHT: str
TITLE: str
SOURCE: str
DESCRSHORT: str
DESCRLONG = DESCRSHORT
NOTE: str

def load_pandas(): ...
def load():
    """
    Load the statecrime data and return a Dataset class instance.

    Returns
    -------
    Dataset
        See DATASET_PROPOSAL.txt for more information.
    """
