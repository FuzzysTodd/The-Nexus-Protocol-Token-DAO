import pandas as pd

def safe_convert_rest_datetime(val: str | None): ...
def rename_and_validate(df: pd.DataFrame | None, schema: list[tuple[str, str, str]]) -> pd.DataFrame:
    """
    Rename columns in a dataframe according to a schema and validate that the schema is satisfied.

    Parameters
    ----------
    df : pd.DataFrame
        The input data.
    schema : List[Tuple[str, str, str]]
        The expected schema. Each element is a tuple of (source column name, destination column name, column type).

    Returns
    -------
    pd.DataFrame
        The renamed dataframe.
    """
def rename_and_validate_from_records(records, schema: list[tuple[str, str, str]]) -> pd.DataFrame:
    """
    Rename columns in a list of records according to a schema and validate that the schema is satisfied.

    Parameters
    ----------
    records : List[dict]
        The input data.
    schema : List[Tuple[str, str, str]]
        The expected schema. Each element is a tuple of (source column name, destination column name, column type).

    Returns
    -------
    pd.DataFrame
        The renamed dataframe.
    """
