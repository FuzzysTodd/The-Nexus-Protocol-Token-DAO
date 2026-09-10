import datetime
import pandas
from dataclasses import dataclass

@dataclass
class RefreshExecutionDetails:
    """
    The status of a refresh request (`Power BI Documentation <https://learn.microsoft.com/en-us/rest/api/power-bi/datasets/get-refresh-execution-details>`_).

    Parameters
    ----------

    start_time : datetime.datetime
        The start time of the refresh request.
    end_time : datetime.datetime, default=None
        The end date and time of the refresh (may be empty if a refresh is in progress).
    type : str
        The type of processing to perform.
    commit_mode : str
        Determines if objects will be committed in batches or only when complete.
    status : str
        Dataset operation general status.
    extended_status : str
        Dataset operation detailed status.
    current_refresh_type : str
       The type of processing for the current iteration. This is useful when commitMode is set to PartialBatch.
    number_of_attempts : int
        The number of attempts for the refresh request.
    objects : pandas.DataFrame
        The objects that were refreshed.
    messages : pandas.DataFrame
        A dataframe of engine error or warning messages for the refresh request.
    refresh_attempts : pandas.DataFrame
        A dataframe of refresh attempts for the refresh request.
    """
    start_time: datetime.datetime
    end_time: datetime.datetime | None
    type: str
    commit_mode: str
    status: str
    extended_status: str
    current_refresh_type: str
    number_of_attempts: int
    objects: pandas.DataFrame
    messages: pandas.DataFrame
    refresh_attempts: pandas.DataFrame
