def compute_scores_and_write_to_csv(target_filepattern, prediction_filepattern, output_filename, scorer, aggregator, delimiter: str = '\n') -> None:
    """Runs aggregate score calculations and outputs results to a CSV file.

  Args:
    target_filepattern: Pattern for files containing target text.
    prediction_filepattern: Pattern for files containing prediction text.
    output_filename: Name of file to write results to.
    scorer: A BaseScorer object to compute scores.
    aggregator: An aggregator to aggregate scores. If None, outputs are
      per-example scores.
    delimiter: Record delimiter.
  """
