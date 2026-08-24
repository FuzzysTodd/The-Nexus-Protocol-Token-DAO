from .table import SimpleTable as SimpleTable
from .tableformatting import fmt_latex as fmt_latex, fmt_txt as fmt_txt
from _typeshed import Incomplete
from statsmodels.compat.python import lzip as lzip

class Summary:
    tables: Incomplete
    settings: Incomplete
    extra_txt: Incomplete
    title: Incomplete
    def __init__(self) -> None: ...
    def add_df(self, df, index: bool = True, header: bool = True, float_format: str = '%.4f', align: str = 'r') -> None:
        """
        Add the contents of a DataFrame to summary table

        Parameters
        ----------
        df : DataFrame
        header : bool
            Reproduce the DataFrame column labels in summary table
        index : bool
            Reproduce the DataFrame row labels in summary table
        float_format : str
            Formatting to float data columns
        align : str
            Data alignment (l/c/r)
        """
    def add_array(self, array, align: str = 'r', float_format: str = '%.4f') -> None:
        """Add the contents of a Numpy array to summary table

        Parameters
        ----------
        array : numpy array (2D)
        float_format : str
            Formatting to array if type is float
        align : str
            Data alignment (l/c/r)
        """
    def add_dict(self, d, ncols: int = 2, align: str = 'l', float_format: str = '%.4f'):
        """Add the contents of a Dict to summary table

        Parameters
        ----------
        d : dict
            Keys and values are automatically coerced to strings with str().
            Users are encouraged to format them before using add_dict.
        ncols : int
            Number of columns of the output table
        align : str
            Data alignment (l/c/r)
        float_format : str
            Formatting to float data columns
        """
    def add_text(self, string) -> None:
        """Append a note to the bottom of the summary table. In ASCII tables,
        the note will be wrapped to table width. Notes are not indented.
        """
    def add_title(self, title: Incomplete | None = None, results: Incomplete | None = None) -> None:
        """Insert a title on top of the summary table. If a string is provided
        in the title argument, that string is printed. If no title string is
        provided but a results instance is provided, statsmodels attempts
        to construct a useful title automatically.
        """
    def add_base(self, results, alpha: float = 0.05, float_format: str = '%.4f', title: Incomplete | None = None, xname: Incomplete | None = None, yname: Incomplete | None = None) -> None:
        """Try to construct a basic summary instance.

        Parameters
        ----------
        results : Model results instance
        alpha : float
            significance level for the confidence intervals (optional)
        float_format: str
            Float formatting for summary of parameters (optional)
        title : str
            Title of the summary table (optional)
        xname : list[str] of length equal to the number of parameters
            Names of the independent variables (optional)
        yname : str
            Name of the dependent variable (optional)
        """
    def as_text(self):
        """Generate ASCII Summary Table
        """
    def as_html(self):
        """Generate HTML Summary Table
        """
    def as_latex(self, label: str = ''):
        """Generate LaTeX Summary Table

        Parameters
        ----------
        label : str
            Label of the summary table that can be referenced
            in a latex document (optional)
        """

def summary_model(results):
    """
    Create a dict with information about the model
    """
def summary_params(results, yname: Incomplete | None = None, xname: Incomplete | None = None, alpha: float = 0.05, use_t: bool = True, skip_header: bool = False, float_format: str = '%.4f'):
    '''create a summary table of parameters from results instance

    Parameters
    ----------
    res : results instance
        some required information is directly taken from the result
        instance
    yname : {str, None}
        optional name for the endogenous variable, default is "y"
    xname : {list[str], None}
        optional names for the exogenous variables, default is "var_xx"
    alpha : float
        significance level for the confidence intervals
    use_t : bool
        indicator whether the p-values are based on the Student-t
        distribution (if True) or on the normal distribution (if False)
    skip_header : bool
        If false (default), then the header row is added. If true, then no
        header row is added.
    float_format : str
        float formatting options (e.g. ".3g")

    Returns
    -------
    params_table : SimpleTable instance
    '''
def summary_col(results, float_format: str = '%.4f', model_names=(), stars: bool = False, info_dict: Incomplete | None = None, regressor_order=(), drop_omitted: bool = False, include_r2: bool = True):
    '''
    Summarize multiple results instances side-by-side (coefs and SEs)

    Parameters
    ----------
    results : statsmodels results instance or list of result instances
    float_format : str, optional
        float format for coefficients and standard errors
        Default : \'%.4f\'
    model_names : list[str], optional
        Must have same length as the number of results. If the names are not
        unique, a roman number will be appended to all model names
    stars : bool
        print significance stars
    info_dict : dict, default None
        dict of functions to be applied to results instances to retrieve
        model info. To use specific information for different models, add a
        (nested) info_dict with model name as the key.
        Example: `info_dict = {"N":lambda x:(x.nobs), "R2": ..., "OLS":{
        "R2":...}}` would only show `R2` for OLS regression models, but
        additionally `N` for all other results.
        Default : None (use the info_dict specified in
        result.default_model_infos, if this property exists)
    regressor_order : list[str], optional
        list of names of the regressors in the desired order. All regressors
        not specified will be appended to the end of the list.
    drop_omitted : bool, optional
        Includes regressors that are not specified in regressor_order. If
        False, regressors not specified will be appended to end of the list.
        If True, only regressors in regressor_order will be included.
    include_r2 : bool, optional
        Includes R2 and adjusted R2 in the summary table.
    '''
