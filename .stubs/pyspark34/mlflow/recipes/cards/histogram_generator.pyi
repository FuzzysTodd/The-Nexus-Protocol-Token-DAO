from mlflow.protos.facet_feature_statistics_pb2 import Histogram as Histogram

def generate_equal_height_histogram(quantiles, num_buckets: int) -> Histogram:
    """Generates the equal height histogram from the input quantiles. The quantiles are assumed to
    be ordered and corresponding to equal distant percentiles.

    :param quantiles: The quantiles that capture the frequency distribution.
    :param num_buckets: The number of buckets in the generated equal height histogram.
    :return: An equal height histogram or None if inputs are invalid.
    """
def generate_equal_width_histogram(quantiles, num_buckets: int, total_freq: float) -> Histogram:
    """Generates the equal width histogram from the input quantiles and total frequency. The
    quantiles are assumed to be ordered and corresponding to equal distant percentiles.

    :param quantiles: the quantiles that capture the frequency distribution.
    :param num_buckets: the number of buckets in the generated histogram.
    :param total_freq: the total frequency (=count of rows).
    :return: equal width histogram or None if inputs are invalid.
    """
