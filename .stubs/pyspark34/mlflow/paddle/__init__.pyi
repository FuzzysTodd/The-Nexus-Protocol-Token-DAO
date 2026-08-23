from _typeshed import Incomplete
from mlflow import pyfunc as pyfunc
from mlflow.models import Model as Model, ModelInputExample as ModelInputExample, ModelSignature as ModelSignature
from mlflow.models.model import MLMODEL_FILE_NAME as MLMODEL_FILE_NAME
from mlflow.tracking._model_registry import DEFAULT_AWAIT_MAX_SLEEP_SECONDS as DEFAULT_AWAIT_MAX_SLEEP_SECONDS
from mlflow.utils.autologging_utils import autologging_integration as autologging_integration, safe_patch as safe_patch
from mlflow.utils.docstring_utils import LOG_MODEL_PARAM_DOCS as LOG_MODEL_PARAM_DOCS, format_docstring as format_docstring
from mlflow.utils.file_utils import write_to as write_to
from typing import Any, Dict

FLAVOR_NAME: str

def get_default_pip_requirements():
    """
    :return: A list of default pip requirements for MLflow Models produced by this flavor.
             Calls to :func:`save_model()` and :func:`log_model()` produce a pip environment
             that, at minimum, contains these requirements.
    """
def get_default_conda_env():
    """
    :return: The default Conda environment for MLflow Models produced by calls to
             :func:`save_model()` and :func:`log_model()`.
    """
def save_model(pd_model, path, training: bool = False, conda_env: Incomplete | None = None, code_paths: Incomplete | None = None, mlflow_model: Incomplete | None = None, signature: ModelSignature = None, input_example: ModelInputExample = None, pip_requirements: Incomplete | None = None, extra_pip_requirements: Incomplete | None = None, metadata: Incomplete | None = None):
    '''
    Save a paddle model to a path on the local file system. Produces an MLflow Model
    containing the following flavors:

        - :py:mod:`mlflow.paddle`
        - :py:mod:`mlflow.pyfunc`. NOTE: This flavor is only included for paddle models
          that define `predict()`, since `predict()` is required for pyfunc model inference.

    :param pd_model: paddle model to be saved.
    :param path: Local path where the model is to be saved.
    :param training: Only valid when saving a model trained using the PaddlePaddle high level API.
                     If set to True, the saved model supports both re-training and
                     inference. If set to False, it only supports inference.
    :param conda_env: {{ conda_env }}
    :param code_paths: A list of local filesystem paths to Python file dependencies (or directories
                       containing file dependencies). These files are *prepended* to the system
                       path when the model is loaded.
    :param mlflow_model: :py:mod:`mlflow.models.Model` this flavor is being added to.
    :param signature: {{ signature }}
    :param input_example: {{ input_example }}
    :param pip_requirements: {{ pip_requirements }}
    :param extra_pip_requirements: {{ extra_pip_requirements }}
    :param metadata: Custom metadata dictionary passed to the model and stored in the MLmodel file.

                     .. Note:: Experimental: This parameter may change or be removed in a future
                                             release without warning.

    .. code-block:: python
        :caption: Example

        import mlflow.paddle
        import paddle
        from paddle.nn import Linear
        import paddle.nn.functional as F
        import numpy as np
        import os
        import random
        from sklearn.datasets import load_diabetes
        from sklearn.model_selection import train_test_split
        from sklearn import preprocessing


        def load_data():
            # dataset on boston housing prediction
            X, y = load_diabetes(return_X_y=True, as_frame=True)

            min_max_scaler = preprocessing.MinMaxScaler()
            X_min_max = min_max_scaler.fit_transform(X)
            X_normalized = preprocessing.scale(X_min_max, with_std=False)

            X_train, X_test, y_train, y_test = train_test_split(
                X_normalized, y, test_size=0.2, random_state=42
            )

            y_train = y_train.reshape(-1, 1)
            y_test = y_test.reshape(-1, 1)
            return np.concatenate((X_train, y_train), axis=1), np.concatenate(
                (X_test, y_test), axis=1
            )


        class Regressor(paddle.nn.Layer):
            def __init__(self):
                super().__init__()

                self.fc = Linear(in_features=13, out_features=1)

            @paddle.jit.to_static
            def forward(self, inputs):
                x = self.fc(inputs)
                return x


        model = Regressor()
        model.train()
        training_data, test_data = load_data()
        opt = paddle.optimizer.SGD(learning_rate=0.01, parameters=model.parameters())

        EPOCH_NUM = 10
        BATCH_SIZE = 10

        for epoch_id in range(EPOCH_NUM):
            np.random.shuffle(training_data)
            mini_batches = [
                training_data[k : k + BATCH_SIZE]
                for k in range(0, len(training_data), BATCH_SIZE)
            ]
            for iter_id, mini_batch in enumerate(mini_batches):
                x = np.array(mini_batch[:, :-1]).astype("float32")
                y = np.array(mini_batch[:, -1:]).astype("float32")
                house_features = paddle.to_tensor(x)
                prices = paddle.to_tensor(y)

                predicts = model(house_features)

                loss = F.square_error_cost(predicts, label=prices)
                avg_loss = paddle.mean(loss)
                if iter_id % 20 == 0:
                    print(
                        "epoch: {}, iter: {}, loss is: {}".format(
                            epoch_id, iter_id, avg_loss.numpy()
                        )
                    )

                avg_loss.backward()
                opt.step()
                opt.clear_grad()

        mlflow.log_param("learning_rate", 0.01)
        mlflow.paddle.log_model(model, "model")
        sk_path_dir = "./test-out"
        mlflow.paddle.save_model(model, sk_path_dir)
        print("Model saved in run %s" % mlflow.active_run().info.run_uuid)
    '''
def load_model(model_uri, model: Incomplete | None = None, dst_path: Incomplete | None = None, **kwargs):
    '''
    Load a paddle model from a local file or a run.
    :param model_uri: The location, in URI format, of the MLflow model, for example:

            - ``/Users/me/path/to/local/model``
            - ``relative/path/to/local/model``
            - ``s3://my_bucket/path/to/model``
            - ``runs:/<mlflow_run_id>/run-relative/path/to/model``
            - ``models:/<model_name>/<model_version>``
            - ``models:/<model_name>/<stage>``

    :param model: Required when loading a `paddle.Model` model saved with `training=True`.
    :param dst_path: The local filesystem path to which to download the model artifact.
                     This directory must already exist. If unspecified, a local output
                     path will be created.
    :param kwargs: The keyword arguments to pass to `paddle.jit.load`
                   or `model.load`.

    For more information about supported URI schemes, see
    `Referencing Artifacts <https://www.mlflow.org/docs/latest/concepts.html#
    artifact-locations>`_.

    :return: A paddle model.

    .. code-block:: python
        :caption: Example

        import mlflow.paddle

        pd_model = mlflow.paddle.load_model("runs:/96771d893a5e46159d9f3b49bf9013e2/pd_models")
        # use Pandas DataFrame to make predictions
        np_array = ...
        predictions = pd_model(np_array)
    '''
def log_model(pd_model, artifact_path, training: bool = False, conda_env: Incomplete | None = None, code_paths: Incomplete | None = None, registered_model_name: Incomplete | None = None, signature: ModelSignature = None, input_example: ModelInputExample = None, await_registration_for=..., pip_requirements: Incomplete | None = None, extra_pip_requirements: Incomplete | None = None, metadata: Incomplete | None = None):
    '''
    Log a paddle model as an MLflow artifact for the current run. Produces an MLflow Model
    containing the following flavors:

        - :py:mod:`mlflow.paddle`
        - :py:mod:`mlflow.pyfunc`. NOTE: This flavor is only included for paddle models
          that define `predict()`, since `predict()` is required for pyfunc model inference.

    :param pd_model: paddle model to be saved.
    :param artifact_path: Run-relative artifact path.
    :param training: Only valid when saving a model trained using the PaddlePaddle high level API.
                     If set to True, the saved model supports both re-training and
                     inference. If set to False, it only supports inference.
    :param conda_env: {{ conda_env }}
    :param code_paths: A list of local filesystem paths to Python file dependencies (or directories
                       containing file dependencies). These files are *prepended* to the system
                       path when the model is loaded.
    :param registered_model_name: If given, create a model version under
                                  ``registered_model_name``, also creating a registered model if one
                                  with the given name does not exist.
    :param signature: {{ signature }}
    :param input_example: {{ input_example }}
    :param await_registration_for: Number of seconds to wait for the model version to finish
                            being created and is in ``READY`` status. By default, the function
                            waits for five minutes. Specify 0 or None to skip waiting.
    :param pip_requirements: {{ pip_requirements }}
    :param extra_pip_requirements: {{ extra_pip_requirements }}
    :param metadata: Custom metadata dictionary passed to the model and stored in the MLmodel file.

                     .. Note:: Experimental: This parameter may change or be removed in a future
                                             release without warning.
    :return: A :py:class:`ModelInfo <mlflow.models.model.ModelInfo>` instance that contains the
             metadata of the logged model.

    .. code-block:: python
        :caption: Example

        import mlflow.paddle


        def load_data():
            ...


        class Regressor:
            ...


        model = Regressor()
        model.train()
        training_data, test_data = load_data()
        opt = paddle.optimizer.SGD(learning_rate=0.01, parameters=model.parameters())

        EPOCH_NUM = 10
        BATCH_SIZE = 10

        for epoch_id in range(EPOCH_NUM):
            ...

        mlflow.log_param("learning_rate", 0.01)
        mlflow.paddle.log_model(model, "model")
        sk_path_dir = ...
        mlflow.paddle.save_model(model, sk_path_dir)
    '''

class _PaddleWrapper:
    """
    Wrapper class that creates a predict function such that
    predict(data: pd.DataFrame) -> model's output as pd.DataFrame (pandas DataFrame)
    """
    pd_model: Incomplete
    def __init__(self, pd_model) -> None: ...
    def predict(self, data, params: Dict[str, Any] | None = None):
        """
        :param data: Model input data.
        :param params: Additional parameters to pass to the model for inference.

                       .. Note:: Experimental: This parameter may change or be removed in a future
                                               release without warning.

        :return: Model predictions.
        """

def autolog(log_every_n_epoch: int = 1, log_models: bool = True, disable: bool = False, exclusive: bool = False, silent: bool = False, registered_model_name: Incomplete | None = None, extra_tags: Incomplete | None = None) -> None:
    '''
    Enables (or disables) and configures autologging from PaddlePaddle to MLflow.

    Autologging is performed when the `fit` method of `paddle.Model`_ is called.

    .. _paddle.Model:
        https://www.paddlepaddle.org.cn/documentation/docs/en/api/paddle/Model_en.html

    :param log_every_n_epoch: If specified, logs metrics once every `n` epochs. By default, metrics
                       are logged after every epoch.
    :param log_models: If ``True``, trained models are logged as MLflow model artifacts.
                       If ``False``, trained models are not logged.
    :param disable: If ``True``, disables the PaddlePaddle autologging integration.
                    If ``False``, enables the PaddlePaddle autologging integration.
    :param exclusive: If ``True``, autologged content is not logged to user-created fluent runs.
                      If ``False``, autologged content is logged to the active fluent run,
                      which may be user-created.
    :param silent: If ``True``, suppress all event logs and warnings from MLflow during PyTorch
                   Lightning autologging. If ``False``, show all events and warnings during
                   PaddlePaddle autologging.
    :param registered_model_name: If given, each time a model is trained, it is registered as a
                                  new model version of the registered model with this name.
                                  The registered model is created if it does not already exist.
    :param extra_tags: A dictionary of extra tags to set on each managed run created by autologging.

    .. code-block:: python
        :caption: Example

        import paddle
        import mlflow
        from mlflow import MlflowClient


        def show_run_data(run_id):
            run = mlflow.get_run(run_id)
            print("params: {}".format(run.data.params))
            print("metrics: {}".format(run.data.metrics))
            client = MlflowClient()
            artifacts = [f.path for f in client.list_artifacts(run.info.run_id, "model")]
            print("artifacts: {}".format(artifacts))


        class LinearRegression(paddle.nn.Layer):
            def __init__(self):
                super().__init__()
                self.fc = paddle.nn.Linear(13, 1)

            def forward(self, feature):
                return self.fc(feature)


        train_dataset = paddle.text.datasets.UCIHousing(mode="train")
        eval_dataset = paddle.text.datasets.UCIHousing(mode="test")

        model = paddle.Model(LinearRegression())
        optim = paddle.optimizer.SGD(learning_rate=1e-2, parameters=model.parameters())
        model.prepare(optim, paddle.nn.MSELoss(), paddle.metric.Accuracy())

        mlflow.paddle.autolog()

        with mlflow.start_run() as run:
            model.fit(train_dataset, eval_dataset, batch_size=16, epochs=10)

        show_run_data(run.info.run_id)

    .. code-block:: text
        :caption: Output

        params: {
            "learning_rate": "0.01",
            "optimizer_name": "SGD",
        }
        metrics: {
            "loss": 17.482044,
            "step": 25.0,
            "acc": 0.0,
            "eval_step": 6.0,
            "eval_acc": 0.0,
            "eval_batch_size": 6.0,
            "batch_size": 4.0,
            "eval_loss": 24.717455,
        }
        artifacts: [
            "model/MLmodel",
            "model/conda.yaml",
            "model/model.pdiparams",
            "model/model.pdiparams.info",
            "model/model.pdmodel",
            "model/requirements.txt",
        ]
    '''
