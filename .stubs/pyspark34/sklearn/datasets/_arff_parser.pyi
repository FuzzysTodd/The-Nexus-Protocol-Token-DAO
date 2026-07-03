from ..externals._arff import ArffSparseDataType as ArffSparseDataType
from ..utils import check_pandas_support as check_pandas_support, get_chunk_n_rows as get_chunk_n_rows
from _typeshed import Incomplete

def load_arff_from_gzip_file(gzip_file, parser, output_type, openml_columns_info, feature_names_to_select, target_names_to_select, shape: Incomplete | None = None, read_csv_kwargs: Incomplete | None = None):
    '''Load a compressed ARFF file using a given parser.

    Parameters
    ----------
    gzip_file : GzipFile instance
        The file compressed to be read.

    parser : {"pandas", "liac-arff"}
        The parser used to parse the ARFF file. "pandas" is recommended
        but only supports loading dense datasets.

    output_type : {"numpy", "sparse", "pandas"}
        The type of the arrays that will be returned. The possibilities ara:

        - `"numpy"`: both `X` and `y` will be NumPy arrays;
        - `"sparse"`: `X` will be sparse matrix and `y` will be a NumPy array;
        - `"pandas"`: `X` will be a pandas DataFrame and `y` will be either a
          pandas Series or DataFrame.

    openml_columns_info : dict
        The information provided by OpenML regarding the columns of the ARFF
        file.

    feature_names_to_select : list of str
        A list of the feature names to be selected.

    target_names_to_select : list of str
        A list of the target names to be selected.

    read_csv_kwargs : dict, default=None
        Keyword arguments to pass to `pandas.read_csv`. It allows to overwrite
        the default options.

    Returns
    -------
    X : {ndarray, sparse matrix, dataframe}
        The data matrix.

    y : {ndarray, dataframe, series}
        The target.

    frame : dataframe or None
        A dataframe containing both `X` and `y`. `None` if
        `output_array_type != "pandas"`.

    categories : list of str or None
        The names of the features that are categorical. `None` if
        `output_array_type == "pandas"`.
    '''
