from _typeshed import Incomplete
from collections.abc import Generator

__all__ = ['PandaSQL', 'PandaSQLException', 'sqldf']

class PandaSQLException(Exception): ...

class PandaSQL:
    engine: Incomplete
    persist: Incomplete
    loaded_tables: Incomplete
    def __init__(self, db_uri: str = 'sqlite:///:memory:', persist: bool = False) -> None:
        """
        Initialize with a specific database.

        :param db_uri: SQLAlchemy-compatible database URI.
        :param persist: keep tables in database between different calls on the same object of this class.
        """
    def __call__(self, query, env: Incomplete | None = None):
        """
        Execute the SQL query.
        Automatically creates tables mentioned in the query from dataframes before executing.

        :param query: SQL query string, which can reference pandas dataframes as SQL tables.
        :param env: Variables environment - a dict mapping table names to pandas dataframes.
        If not specified use local and global variables of the caller.
        :return: Pandas dataframe with the result of the SQL query.
        """
    @property
    def conn(self) -> Generator[Incomplete, None, None]: ...

def sqldf(query, env: Incomplete | None = None, db_uri: str = 'sqlite:///:memory:'):
    '''
    Query pandas data frames using sql syntax
    This function is meant for backward compatibility only. New users are encouraged to use the PandaSQL class.

    Parameters
    ----------
    query: string
        a sql query using DataFrames as tables
    env: locals() or globals()
        variable environment; locals() or globals() in your function
        allows sqldf to access the variables in your python environment
    db_uri: string
        SQLAlchemy-compatible database URI

    Returns
    -------
    result: DataFrame
        returns a DataFrame with your query\'s result

    Examples
    --------
    >>> import pandas as pd
    >>> df = pd.DataFrame({
        "x": range(100),
        "y": range(100)
    })
    >>> from pandasql import sqldf
    >>> sqldf("select * from df;", globals())
    >>> sqldf("select * from df;", locals())
    >>> sqldf("select avg(x) from df;", locals())
    '''
