import pandas as pd
from mlflow.exceptions import MlflowException as MlflowException
from mlflow.protos import facet_feature_statistics_pb2 as facet_feature_statistics_pb2
from mlflow.recipes.cards import histogram_generator as histogram_generator
from typing import Iterable, Tuple

HISTOGRAM_CATEGORICAL_LEVELS_COUNT: int

def get_facet_type_from_numpy_type(dtype):
    """Converts a Numpy dtype to the FeatureNameStatistics.Type proto enum."""
def datetime_and_timedelta_converter(dtype):
    """
    Converts a Numpy dtype to a converter method if applicable.
    The converter method takes in a numpy array of objects of the provided
    dtype and returns a numpy array of the numbers backing that object for
    statistical analysis. Returns None if no converter is necessary.
    :param dtype: The numpy dtype to make a converter for.
    :return: The converter method or None.
    """
def compute_common_stats(column) -> facet_feature_statistics_pb2.CommonStatistics:
    """
    Computes common statistics for a given column in the DataFrame.

    :param column: A column from a DataFrame.
    :return: A CommonStatistics proto.
    """
def convert_to_dataset_feature_statistics(df: pd.DataFrame) -> facet_feature_statistics_pb2.DatasetFeatureStatistics:
    """
    Converts the data statistics from DataFrame format to DatasetFeatureStatistics proto.

    :param df: The DataFrame for which feature statistics need to be computed.
    :return: A DatasetFeatureStatistics proto.
    """
def convert_to_proto(df: pd.DataFrame) -> facet_feature_statistics_pb2.DatasetFeatureStatisticsList:
    """
    Converts the data from DataFrame format to DatasetFeatureStatisticsList proto.

    :param df: The DataFrame for which feature statistics need to be computed.
    :return: A DatasetFeatureStatisticsList proto.
    """
def convert_to_comparison_proto(dfs: Iterable[Tuple[str, pd.DataFrame]]) -> facet_feature_statistics_pb2.DatasetFeatureStatisticsList:
    '''
    Converts a collection of named stats DataFrames to a single DatasetFeatureStatisticsList proto.
    :param dfs: The named "glimpses" that contain the DataFrame. Each "glimpse"
        DataFrame has the same properties as the input to `convert_to_proto()`.
    :return: A DatasetFeatureStatisticsList proto which contains a translation
        of the glimpses with the given names.
    '''
def get_facets_polyfills() -> str:
    '''
    A JS polyfill/monkey-patching function that fixes issue where objectURL passed as a
    "base" argument to the URL constructor ends up in a "invalid URL" exception.

    Polymer is using parent\'s URL in its internal asset URL resolution system, while MLFLow
    artifact rendering engine uses object URLs to display iframed artifacts code. This ends up
    in object URL being used in `new URL()` constructor which needs to be patched.

    Original function code:

    (function patchURLConstructor() {
        const _originalURLConstructor = window.URL;
        window.URL = function (url, base) {
            if (typeof base === "string" && base.startsWith("blob:")) {
                return new URL(base);
            }
            return new _originalURLConstructor(url, base);
        };
    })();
    '''
def construct_facets_html(proto: facet_feature_statistics_pb2.DatasetFeatureStatisticsList, compare: bool = False) -> str:
    """
    Constructs the facets HTML to visualize the serialized FeatureStatisticsList proto.
    :param proto: A DatasetFeatureStatisticsList proto which contains the statistics for a DataFrame
    :param compare: If True, then the returned visualization switches on the comparison
        mode for several stats.
    :return: the HTML for Facets visualization
    """
def get_html(inputs: pd.DataFrame | Iterable[Tuple[str, pd.DataFrame]]) -> str:
    '''Rendering the data statistics in a HTML format.

    :param inputs: Either a single "glimpse" DataFrame that contains the statistics, or a
        collection of (name, DataFrame) pairs where each pair names a separate "glimpse"
        and they are all visualized in comparison mode.
    :return: None
    '''
