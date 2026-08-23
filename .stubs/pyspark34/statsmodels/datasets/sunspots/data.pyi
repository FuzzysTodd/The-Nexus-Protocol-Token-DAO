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
    Load the yearly sunspot data and returns a data class.

    Returns
    -------
    Dataset
        See DATASET_PROPOSAL.txt for more information.

    Notes
    -----
    This dataset only contains data for one variable, so the attributes
    data, raw_data, and endog are all the same variable.  There is no exog
    attribute defined.
    """
