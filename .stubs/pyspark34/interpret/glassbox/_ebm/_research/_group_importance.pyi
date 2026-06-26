from _typeshed import Incomplete

def compute_group_importance(term_list, ebm, X, contributions: Incomplete | None = None):
    """Computes the importance of a group of terms.

    Args:
        term_list: A list of term names or indices
        ebm: A fitted EBM
        X (numpy array): Samples used to compute the group importance
        contributions (numpy array, optional): Contributions of all terms per X's row

    Returns:
        float: term_list's group importance
    """
def append_group_importance(term_list, ebm, X, group_name: Incomplete | None = None, global_exp: Incomplete | None = None, global_exp_name: Incomplete | None = None, contributions: Incomplete | None = None):
    """Computes the importance of a group of terms and appends it to a global explanation.

    In case a global explanation is provided, the group importance will be appended to it and returned.
    Otherwise, a new global explanation will be creted and returned.

    The group importance will only be displayed in the Summary graph.

    Args:
        term_list: A list of term names or indices
        ebm: A fitted EBM
        X (numpy array): Samples used to compute the group importance
        group_name (str, optional): User-defined group name
        global_exp (EBMExplanation, optional): User-defined global explanation object
        global_exp_name (str, optional): User-defined name when creating a new global explanation
        contributions (numpy array, optional): Contributions of all terms per X's row

    Returns:
        EBMExplanation: A global explanation with the group importance appended to it
    """
def get_group_and_individual_importances(term_groups_list, ebm, X, contributions: Incomplete | None = None):
    '''Returns a dict containing the importances of the groups in term_groups_list as well as
        all other EBM terms

    The dict will de sorted in descending order w.r.t. the importances

    Args:
        term_groups_list: A list of term groups, which are lists of term names or indices
            e.g. [["Feature 1", "Feature 2], ["Feature 3", "Feature 4"]]
        ebm: A fitted EBM
        X (numpy array): Samples used to compute the group importance
        contributions (numpy array, optional): Contributions of all terms per X\'s row

    Returns:
       a dict where each entry is in the form \'term_name: term_importance\'
    '''
def get_individual_importances(ebm, X, contributions: Incomplete | None = None):
    """Returns a dict containing the importances of all EBM terms

    The dict will de sorted in descending order w.r.t. the importances

    Args:
        ebm: A fitted EBM
        X (numpy array): Samples used to compute the group importance
        contributions (numpy array, optional): Contributions of all terms per X's row

    Returns:
       a dict where each entry is in the form 'term_name: term_importance'
    """
def get_importance_per_top_groups(ebm, X):
    """Returns a Dataframe with the importances of groups of terms, such that:

    The first group is the term with the highest individual importance (i.e. top term), the second group is
    composed by the top 2 terms, and so on. For example:
        Group 1 - ['Age']
        Group 2 - ['Age', 'MaritalStatus']
        Group 3 - ['Age', 'MaritalStatus', 'CapitalGain']
        ...
        Group N - All terms

    Args:
        ebm: A fitted EBM
        X (numpy array): Samples used to compute the group importance

    Returns:
       a pandas Dataframe with three columns: group_names, terms_per_group and importances
    """
def plot_importance_per_top_groups(ebm, X) -> None:
    """Plots a plotly graph where the x-axis represents groups of top K terms and the y-axis their importances.

    The first group is the terms with the highest individual importance (i.e. top term), the second group is
    composed by the top 2 terms, and so on. For example:
        Group 1 - ['Age']
        Group 2 - ['Age', 'MaritalStatus']
        Group 3 - ['Age', 'MaritalStatus', 'CapitalGain']
        ...
        Group N - All terms

    Args:
        ebm: A fitted EBM
        X (numpy array): Samples used to compute the group importance
    """
