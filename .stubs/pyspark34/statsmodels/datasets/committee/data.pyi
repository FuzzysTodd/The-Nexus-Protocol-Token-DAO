__docformat__: str
COPYRIGHT: str
TITLE = __doc__
SOURCE: str
DESCRSHORT: str
DESCRLONG: str
NOTE: str

def load_pandas(): ...
def load():
    """Load the committee data and returns a data class.

    Returns
    -------
    Dataset
        See DATASET_PROPOSAL.txt for more information.
    """
