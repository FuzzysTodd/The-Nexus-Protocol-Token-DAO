import pandas as pd
from pyspark.pandas._typing import Dtype
from pyspark.pandas.frame import DataFrame
from pyspark.pandas.series import Series

__all__ = ['PythonModelWrapper', 'load_model']

class PythonModelWrapper:
    """
    A wrapper around MLflow's Python object model.

    This wrapper acts as a predictor on pandas-on-Spark

    """
    def __init__(self, model_uri: str, return_type_hint: str | type | Dtype) -> None: ...
    def predict(self, data: DataFrame | pd.DataFrame) -> Series | pd.Series:
        """
        Returns a prediction on the data.

        If the data is a pandas-on-Spark DataFrame, the return is a pandas-on-Spark Series.

        If the data is a pandas Dataframe, the return is the expected output of the underlying
        pyfunc object (typically a pandas Series or a numpy array).
        """

def load_model(model_uri: str, predict_type: str | type | Dtype = 'infer') -> PythonModelWrapper:
    '''
    Loads an MLflow model into a wrapper that can be used both for pandas and pandas-on-Spark
    DataFrame.

    Parameters
    ----------
    model_uri : str
        URI pointing to the model. See MLflow documentation for more details.
    predict_type : a python basic type, a numpy basic type, a Spark type or \'infer\'.
       This is the return type that is expected when calling the predict function of the model.
       If \'infer\' is specified, the wrapper will attempt to automatically determine the return type
       based on the model type.

    Returns
    -------
    PythonModelWrapper
        A wrapper around MLflow PythonModel objects. This wrapper is expected to adhere to the
        interface of mlflow.pyfunc.PythonModel.

    Examples
    --------
    Here is a full example that creates a model with scikit-learn and saves the model with
     MLflow. The model is then loaded as a predictor that can be applied on a pandas-on-Spark
     Dataframe.

    We first initialize our MLflow environment:

    >>> from mlflow.tracking import MlflowClient, set_tracking_uri
    >>> import mlflow.sklearn
    >>> from tempfile import mkdtemp
    >>> d = mkdtemp("pandas_on_spark_mlflow")
    >>> set_tracking_uri("file:%s"%d)
    >>> client = MlflowClient()
    >>> exp_id = mlflow.create_experiment("my_experiment")
    >>> exp = mlflow.set_experiment("my_experiment")

    We aim at learning this numerical function using a simple linear regressor.

    >>> from sklearn.linear_model import LinearRegression
    >>> train = pd.DataFrame({"x1": np.arange(8), "x2": np.arange(8)**2,
    ...                       "y": np.log(2 + np.arange(8))})
    >>> train_x = train[["x1", "x2"]]
    >>> train_y = train[["y"]]
    >>> with mlflow.start_run():
    ...     lr = LinearRegression()
    ...     lr.fit(train_x, train_y)
    ...     mlflow.sklearn.log_model(lr, "model")
    LinearRegression...

    Now that our model is logged using MLflow, we load it back and apply it on a pandas-on-Spark
    dataframe:

    >>> from pyspark.pandas.mlflow import load_model
    >>> run_info = client.search_runs(exp_id)[-1].info
    >>> model = load_model("runs:/{run_id}/model".format(run_id=run_info.run_id))
    >>> prediction_df = ps.DataFrame({"x1": [2.0], "x2": [4.0]})
    >>> prediction_df["prediction"] = model.predict(prediction_df)
    >>> prediction_df
        x1   x2  prediction
    0  2.0  4.0    1.355551

    The model also works on pandas DataFrames as expected:

    >>> model.predict(prediction_df[["x1", "x2"]].to_pandas())
    array([[1.35555142]])

    Notes
    -----
    Currently, the model prediction can only be merged back with the existing dataframe.
    Other columns must be manually joined.
    For example, this code will not work:

    >>> df = ps.DataFrame({"x1": [2.0], "x2": [3.0], "z": [-1]})
    >>> features = df[["x1", "x2"]]
    >>> y = model.predict(features)
    >>> # Works:
    >>> features["y"] = y   # doctest: +SKIP
    >>> # Will fail with a message about dataframes not aligned.
    >>> df["y"] = y   # doctest: +SKIP

    A current workaround is to use the .merge() function, using the feature values
    as merging keys.

    >>> features[\'y\'] = y
    >>> everything = df.merge(features, on=[\'x1\', \'x2\'])
    >>> everything
        x1   x2  z         y
    0  2.0  3.0 -1  1.376932
    '''
