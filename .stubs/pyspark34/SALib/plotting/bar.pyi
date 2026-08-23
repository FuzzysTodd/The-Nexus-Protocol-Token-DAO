from _typeshed import Incomplete

__all__ = ['plot']

def plot(Si_df, ax: Incomplete | None = None):
    """Create bar chart of results.


    Examples
    --------
        >>> from SALib.plotting.bar import plot as barplot
        >>> from SALib.test_functions import Ishigami
        >>>
        >>> # See README for example problem specification
        >>>
        >>> X = saltelli.sample(problem, 512)
        >>> Y = Ishigami.evaluate(X)
        >>> Si = sobol.analyze(problem, Y, print_to_console=False)
        >>> total, first, second = Si.to_df()
        >>> barplot(total)


    Parameters
    ----------
    * Si_df: pd.DataFrame, of sensitivity results

    Returns
    -------
    * ax : matplotlib axes object
    """
