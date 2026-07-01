from typing import Any, Optional
from pyspark.sql import DataFrame

__all__ = ['profile', 'profile_for_data_wrangler']


def profile(data: Any, partial: bool = True) -> Optional[str]:
    """
    Profile a dataset to generate summary statistics and insights.
    
    :param data: The dataset to profile (DataFrame or compatible type)
    :param partial: Whether to perform partial profiling for performance
    :return: Profile output string or None
    """

def profile_for_data_wrangler(df: DataFrame, partial: bool = True) -> str:
    """
    Profile a DataFrame specifically for data wrangler integration.
    
    :param df: Spark DataFrame to profile
    :param partial: Whether to perform partial profiling for performance
    :return: Profile output for data wrangler
    """
