def pivot_dataframe(dataframe):
    """Gets a pivoted wide-form pandas dataframe.

    The wide-form DataFrame has all its tags included as columns of the
    DataFrame, which is more convenient to work. If the condition of having
    uniform sets of step values across all tags in all runs is not met,
    this will error.

    Args:
      dataframe: pandas dataframe to pivot.

    Returns:
      Pivoted wide-form pandas dataframe.
    Raises:
      ValueError if step values across all tags are not uniform.
    """
