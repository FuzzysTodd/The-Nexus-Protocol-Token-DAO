import PIL
import matplotlib.figure
import numpy
import pandas
import plotly
from mlflow.data.dataset import Dataset as Dataset
from mlflow.entities import DatasetInput as DatasetInput, Experiment as Experiment, InputTag as InputTag, Metric as Metric, Param as Param, Run as Run, RunStatus as RunStatus, RunTag as RunTag, ViewType as ViewType
from mlflow.entities.lifecycle_stage import LifecycleStage as LifecycleStage
from mlflow.environment_variables import MLFLOW_EXPERIMENT_ID as MLFLOW_EXPERIMENT_ID, MLFLOW_EXPERIMENT_NAME as MLFLOW_EXPERIMENT_NAME, MLFLOW_RUN_ID as MLFLOW_RUN_ID
from mlflow.exceptions import MlflowException as MlflowException
from mlflow.protos.databricks_pb2 import INVALID_PARAMETER_VALUE as INVALID_PARAMETER_VALUE, RESOURCE_DOES_NOT_EXIST as RESOURCE_DOES_NOT_EXIST
from mlflow.store.tracking import SEARCH_MAX_RESULTS_DEFAULT as SEARCH_MAX_RESULTS_DEFAULT
from mlflow.tracking import artifact_utils as artifact_utils
from mlflow.tracking.client import MlflowClient as MlflowClient
from mlflow.utils import get_results_from_paginated_fn as get_results_from_paginated_fn
from mlflow.utils.annotations import experimental as experimental
from mlflow.utils.autologging_utils import AUTOLOGGING_CONF_KEY_IS_GLOBALLY_CONFIGURED as AUTOLOGGING_CONF_KEY_IS_GLOBALLY_CONFIGURED, AUTOLOGGING_INTEGRATIONS as AUTOLOGGING_INTEGRATIONS, autologging_integration as autologging_integration, autologging_is_disabled as autologging_is_disabled, is_testing as is_testing
from mlflow.utils.databricks_utils import is_in_databricks_runtime as is_in_databricks_runtime
from mlflow.utils.import_hooks import register_post_import_hook as register_post_import_hook
from mlflow.utils.mlflow_tags import MLFLOW_DATASET_CONTEXT as MLFLOW_DATASET_CONTEXT, MLFLOW_EXPERIMENT_PRIMARY_METRIC_GREATER_IS_BETTER as MLFLOW_EXPERIMENT_PRIMARY_METRIC_GREATER_IS_BETTER, MLFLOW_EXPERIMENT_PRIMARY_METRIC_NAME as MLFLOW_EXPERIMENT_PRIMARY_METRIC_NAME, MLFLOW_PARENT_RUN_ID as MLFLOW_PARENT_RUN_ID, MLFLOW_RUN_NAME as MLFLOW_RUN_NAME, MLFLOW_RUN_NOTE as MLFLOW_RUN_NOTE
from mlflow.utils.time_utils import get_current_time_millis as get_current_time_millis
from typing import Any, Dict, List

SEARCH_MAX_RESULTS_PANDAS: int
NUM_RUNS_PER_PAGE_PANDAS: int

def set_experiment(experiment_name: str = None, experiment_id: str = None) -> Experiment:
    '''
    Set the given experiment as the active experiment. The experiment must either be specified by
    name via `experiment_name` or by ID via `experiment_id`. The experiment name and ID cannot
    both be specified.

    :param experiment_name: Case sensitive name of the experiment to be activated. If an experiment
                            with this name does not exist, a new experiment wth this name is
                            created. On certain platforms such as Databricks, the experiment name
                            must an absolute path, e.g. ``"/Users/<username>/my-experiment"``.
    :param experiment_id: ID of the experiment to be activated. If an experiment with this ID
                          does not exist, an exception is thrown.
    :return: An instance of :py:class:`mlflow.entities.Experiment` representing the new active
             experiment.

    .. test-code-block:: python
        :caption: Example

        import mlflow

        # Set an experiment name, which must be unique and case-sensitive.
        experiment = mlflow.set_experiment("Social NLP Experiments")

        # Get Experiment Details
        print("Experiment_id: {}".format(experiment.experiment_id))
        print("Artifact Location: {}".format(experiment.artifact_location))
        print("Tags: {}".format(experiment.tags))
        print("Lifecycle_stage: {}".format(experiment.lifecycle_stage))

    .. code-block:: text
        :caption: Output

        Experiment_id: 1
        Artifact Location: file:///.../mlruns/1
        Tags: {}
        Lifecycle_stage: active
    '''

class ActiveRun(Run):
    """Wrapper around :py:class:`mlflow.entities.Run` to enable using Python ``with`` syntax."""
    def __init__(self, run) -> None: ...
    def __enter__(self): ...
    def __exit__(self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: types.TracebackType | None): ...

def start_run(run_id: str = None, experiment_id: str | None = None, run_name: str | None = None, nested: bool = False, tags: Dict[str, Any] | None = None, description: str | None = None) -> ActiveRun:
    '''
    Start a new MLflow run, setting it as the active run under which metrics and parameters
    will be logged. The return value can be used as a context manager within a ``with`` block;
    otherwise, you must call ``end_run()`` to terminate the current run.

    If you pass a ``run_id`` or the ``MLFLOW_RUN_ID`` environment variable is set,
    ``start_run`` attempts to resume a run with the specified run ID and
    other parameters are ignored. ``run_id`` takes precedence over ``MLFLOW_RUN_ID``.

    If resuming an existing run, the run status is set to ``RunStatus.RUNNING``.

    MLflow sets a variety of default tags on the run, as defined in
    :ref:`MLflow system tags <system_tags>`.

    :param run_id: If specified, get the run with the specified UUID and log parameters
                     and metrics under that run. The run\'s end time is unset and its status
                     is set to running, but the run\'s other attributes (``source_version``,
                     ``source_type``, etc.) are not changed.
    :param experiment_id: ID of the experiment under which to create the current run (applicable
                          only when ``run_id`` is not specified). If ``experiment_id`` argument
                          is unspecified, will look for valid experiment in the following order:
                          activated using ``set_experiment``, ``MLFLOW_EXPERIMENT_NAME``
                          environment variable, ``MLFLOW_EXPERIMENT_ID`` environment variable,
                          or the default experiment as defined by the tracking server.
    :param run_name: Name of new run.
                     Used only when ``run_id`` is unspecified. If a new run is created and
                     ``run_name`` is not specified, a unique name will be generated for the run.
    :param nested: Controls whether run is nested in parent run. ``True`` creates a nested run.
    :param tags: An optional dictionary of string keys and values to set as tags on the run.
                 If a run is being resumed, these tags are set on the resumed run. If a new run is
                 being created, these tags are set on the new run.
    :param description: An optional string that populates the description box of the run.
                        If a run is being resumed, the description is set on the resumed run.
                        If a new run is being created, the description is set on the new run.
    :return: :py:class:`mlflow.ActiveRun` object that acts as a context manager wrapping
             the run\'s state.

    .. test-code-block:: python
        :caption: Example

        import mlflow

        # Create nested runs
        experiment_id = mlflow.create_experiment("experiment1")
        with mlflow.start_run(
            run_name="PARENT_RUN",
            experiment_id=experiment_id,
            tags={"version": "v1", "priority": "P1"},
            description="parent",
        ) as parent_run:
            mlflow.log_param("parent", "yes")
            with mlflow.start_run(
                run_name="CHILD_RUN",
                experiment_id=experiment_id,
                description="child",
                nested=True,
            ) as child_run:
                mlflow.log_param("child", "yes")

        print("parent run:")

        print("run_id: {}".format(parent_run.info.run_id))
        print("description: {}".format(parent_run.data.tags.get("mlflow.note.content")))
        print("version tag value: {}".format(parent_run.data.tags.get("version")))
        print("priority tag value: {}".format(parent_run.data.tags.get("priority")))
        print("--")

        # Search all child runs with a parent id
        query = "tags.mlflow.parentRunId = \'{}\'".format(parent_run.info.run_id)
        results = mlflow.search_runs(experiment_ids=[experiment_id], filter_string=query)
        print("child runs:")
        print(results[["run_id", "params.child", "tags.mlflow.runName"]])

    .. code-block:: text
        :caption: Output

        parent run:
        run_id: 8979459433a24a52ab3be87a229a9cdf
        description: starting a parent for experiment 7
        version tag value: v1
        priority tag value: P1
        --
        child runs:
                                     run_id params.child tags.mlflow.runName
        0  7d175204675e40328e46d9a6a5a7ee6a          yes           CHILD_RUN
    '''
def end_run(status: str = ...) -> None:
    '''End an active MLflow run (if there is one).

    .. test-code-block:: python
        :caption: Example

        import mlflow

        # Start run and get status
        mlflow.start_run()
        run = mlflow.active_run()
        print("run_id: {}; status: {}".format(run.info.run_id, run.info.status))

        # End run and get status
        mlflow.end_run()
        run = mlflow.get_run(run.info.run_id)
        print("run_id: {}; status: {}".format(run.info.run_id, run.info.status))
        print("--")

        # Check for any active runs
        print("Active run: {}".format(mlflow.active_run()))

    .. code-block:: text
        :caption: Output

        run_id: b47ee4563368419880b44ad8535f6371; status: RUNNING
        run_id: b47ee4563368419880b44ad8535f6371; status: FINISHED
        --
        Active run: None
    '''
def active_run() -> ActiveRun | None:
    '''Get the currently active ``Run``, or None if no such run exists.

    **Note**: You cannot access currently-active run attributes
    (parameters, metrics, etc.) through the run returned by ``mlflow.active_run``. In order
    to access such attributes, use the :py:class:`mlflow.client.MlflowClient` as follows:

    .. test-code-block:: python
        :caption: Example

        import mlflow

        mlflow.start_run()
        run = mlflow.active_run()
        print("Active run_id: {}".format(run.info.run_id))
        mlflow.end_run()

    .. code-block:: text
        :caption: Output

        Active run_id: 6f252757005748708cd3aad75d1ff462
    '''
def last_active_run() -> Run | None:
    """
    Gets the most recent active run.

    Examples:

    .. test-code-block:: python
        :caption: To retrieve the most recent autologged run:

        import mlflow

        from sklearn.model_selection import train_test_split
        from sklearn.datasets import load_diabetes
        from sklearn.ensemble import RandomForestRegressor

        mlflow.autolog()

        db = load_diabetes()
        X_train, X_test, y_train, y_test = train_test_split(db.data, db.target)

        # Create and train models.
        rf = RandomForestRegressor(n_estimators=100, max_depth=6, max_features=3)
        rf.fit(X_train, y_train)

        # Use the model to make predictions on the test dataset.
        predictions = rf.predict(X_test)
        autolog_run = mlflow.last_active_run()

    .. test-code-block:: python
        :caption: To get the most recently active run that ended:

        import mlflow

        mlflow.start_run()
        mlflow.end_run()
        run = mlflow.last_active_run()

    .. test-code-block:: python
        :caption: To retrieve the currently active run:

        import mlflow

        mlflow.start_run()
        run = mlflow.last_active_run()
        mlflow.end_run()

    :return: The active run (this is equivalent to ``mlflow.active_run()``) if one exists.
             Otherwise, the last run started from the current Python process that reached
             a terminal status (i.e. FINISHED, FAILED, or KILLED).
    """
def get_run(run_id: str) -> Run:
    '''
    Fetch the run from backend store. The resulting :py:class:`Run <mlflow.entities.Run>`
    contains a collection of run metadata -- :py:class:`RunInfo <mlflow.entities.RunInfo>`,
    as well as a collection of run parameters, tags, and metrics --
    :py:class:`RunData <mlflow.entities.RunData>`. It also contains a collection of run
    inputs (experimental), including information about datasets used by the run --
    :py:class:`RunInputs <mlflow.entities.RunInputs>`. In the case where multiple metrics with the
    same key are logged for the run, the :py:class:`RunData <mlflow.entities.RunData>` contains the
    most recently logged value at the largest step for each metric.

    :param run_id: Unique identifier for the run.

    :return: A single :py:class:`mlflow.entities.Run` object, if the run exists. Otherwise,
                raises an exception.

    .. test-code-block:: python
        :caption: Example

        import mlflow

        with mlflow.start_run() as run:
            mlflow.log_param("p", 0)

        run_id = run.info.run_id
        print(
            "run_id: {}; lifecycle_stage: {}".format(
                run_id, mlflow.get_run(run_id).info.lifecycle_stage
            )
        )

    .. code-block:: text
        :caption: Output

        run_id: 7472befefc754e388e8e922824a0cca5; lifecycle_stage: active
    '''
def get_parent_run(run_id: str) -> Run | None:
    '''
    Gets the parent run for the given run id if one exists.

    :param run_id: Unique identifier for the child run.

    :return: A single :py:class:`mlflow.entities.Run` object, if the parent run exists. Otherwise,
                returns None.

    .. test-code-block:: python
        :caption: Example

        import mlflow

        # Create nested runs
        with mlflow.start_run():
            with mlflow.start_run(nested=True) as child_run:
                child_run_id = child_run.info.run_id

        parent_run = mlflow.get_parent_run(child_run_id)

        print("child_run_id: {}".format(child_run_id))
        print("parent_run_id: {}".format(parent_run.info.run_id))

    .. code-block:: text
        :caption: Output

        child_run_id: 7d175204675e40328e46d9a6a5a7ee6a
        parent_run_id: 8979459433a24a52ab3be87a229a9cdf
    '''
def log_param(key: str, value: Any) -> Any:
    '''
    Log a parameter (e.g. model hyperparameter) under the current run. If no run is active,
    this method will create a new active run.

    :param key: Parameter name (string). This string may only contain alphanumerics,
                underscores (_), dashes (-), periods (.), spaces ( ), and slashes (/).
                All backend stores support keys up to length 250, but some may
                support larger keys.
    :param value: Parameter value (string, but will be string-ified if not).
                  All backend stores support values up to length 500, but some
                  may support larger values.

    :return: the parameter value that is logged.

    .. test-code-block:: python
        :caption: Example

        import mlflow

        with mlflow.start_run():
            value = mlflow.log_param("learning_rate", 0.01)
            assert value == 0.01
    '''
def set_experiment_tag(key: str, value: Any) -> None:
    '''
    Set a tag on the current experiment. Value is converted to a string.

    :param key: Tag name (string). This string may only contain alphanumerics, underscores
                (_), dashes (-), periods (.), spaces ( ), and slashes (/).
                All backend stores will support keys up to length 250, but some may
                support larger keys.
    :param value: Tag value (string, but will be string-ified if not).
                  All backend stores will support values up to length 5000, but some
                  may support larger values.

    .. test-code-block:: python
        :caption: Example

        import mlflow

        with mlflow.start_run():
            mlflow.set_experiment_tag("release.version", "2.2.0")
    '''
def set_tag(key: str, value: Any) -> None:
    '''
    Set a tag under the current run. If no run is active, this method will create a
    new active run.

    :param key: Tag name (string). This string may only contain alphanumerics, underscores
                (_), dashes (-), periods (.), spaces ( ), and slashes (/).
                All backend stores will support keys up to length 250, but some may
                support larger keys.
    :param value: Tag value (string, but will be string-ified if not).
                  All backend stores will support values up to length 5000, but some
                  may support larger values.

    .. test-code-block:: python
        :caption: Example

        import mlflow

        with mlflow.start_run():
            mlflow.set_tag("release.version", "2.2.0")
    '''
def delete_tag(key: str) -> None:
    '''
    Delete a tag from a run. This is irreversible. If no run is active, this method
    will create a new active run.

    :param key: Name of the tag

    .. test-code-block:: python
        :caption: Example

        import mlflow

        tags = {"engineering": "ML Platform", "engineering_remote": "ML Platform"}

        with mlflow.start_run() as run:
            mlflow.set_tags(tags)

        with mlflow.start_run(run_id=run.info.run_id):
            mlflow.delete_tag("engineering_remote")
    '''
def log_metric(key: str, value: float, step: int | None = None) -> None:
    '''
    Log a metric under the current run. If no run is active, this method will create
    a new active run.

    :param key: Metric name (string). This string may only contain alphanumerics, underscores (_),
                dashes (-), periods (.), spaces ( ), and slashes (/).
                All backend stores will support keys up to length 250, but some may
                support larger keys.
    :param value: Metric value (float). Note that some special values such as +/- Infinity may be
                  replaced by other values depending on the store. For example, the
                  SQLAlchemy store replaces +/- Infinity with max / min float values.
                  All backend stores will support values up to length 5000, but some
                  may support larger values.
    :param step: Metric step (int). Defaults to zero if unspecified.

    .. test-code-block:: python
        :caption: Example

        import mlflow

        with mlflow.start_run():
            mlflow.log_metric("mse", 2500.00)
    '''
def log_metrics(metrics: Dict[str, float], step: int | None = None) -> None:
    '''
    Log multiple metrics for the current run. If no run is active, this method will create a new
    active run.

    :param metrics: Dictionary of metric_name: String -> value: Float. Note that some special
                    values such as +/- Infinity may be replaced by other values depending on
                    the store. For example, sql based store may replace +/- Infinity with
                    max / min float values.
    :param step: A single integer step at which to log the specified
                 Metrics. If unspecified, each metric is logged at step zero.

    :returns: None

    .. test-code-block:: python
        :caption: Example

        import mlflow

        metrics = {"mse": 2500.00, "rmse": 50.00}

        # Log a batch of metrics
        with mlflow.start_run():
            mlflow.log_metrics(metrics)
    '''
def log_params(params: Dict[str, Any]) -> None:
    '''
    Log a batch of params for the current run. If no run is active, this method will create a
    new active run.

    :param params: Dictionary of param_name: String -> value: (String, but will be string-ified if
                   not)
    :returns: None

    .. test-code-block:: python
        :caption: Example

        import mlflow

        params = {"learning_rate": 0.01, "n_estimators": 10}

        # Log a batch of parameters
        with mlflow.start_run():
            mlflow.log_params(params)
    '''
def log_input(dataset: Dataset, context: str | None = None, tags: Dict[str, str] | None = None) -> None:
    '''
    Log a dataset used in the current run.

    :param dataset: :py:class:`mlflow.data.dataset.Dataset` object to be logged.
    :param context: Context in which the dataset is used. For example: "training", "testing".
                    This will be set as an input tag with key `mlflow.data.context`.
    :param tags: Tags to be associated with the dataset. Dictionary of tag_key -> tag_value.
    :returns: None

    .. test-code-block:: python
        :caption: Example

        import numpy as np
        import mlflow

        array = np.asarray([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        dataset = mlflow.data.from_numpy(array, source="data.csv")

        # Log an input dataset used for training
        with mlflow.start_run():
            mlflow.log_input(dataset, context="training")
    '''
def set_experiment_tags(tags: Dict[str, Any]) -> None:
    '''
    Set tags for the current active experiment.

    :param tags: Dictionary containing tag names and corresponding values.

    .. test-code-block:: python
        :caption: Example

        import mlflow

        tags = {
            "engineering": "ML Platform",
            "release.candidate": "RC1",
            "release.version": "2.2.0",
        }

        # Set a batch of tags
        with mlflow.start_run():
            mlflow.set_experiment_tags(tags)
    '''
def set_tags(tags: Dict[str, Any]) -> None:
    '''
    Log a batch of tags for the current run. If no run is active, this method will create a
    new active run.

    :param tags: Dictionary of tag_name: String -> value: (String, but will be string-ified if
                 not)
    :returns: None

    .. test-code-block:: python
        :caption: Example

        import mlflow

        tags = {
            "engineering": "ML Platform",
            "release.candidate": "RC1",
            "release.version": "2.2.0",
        }

        # Set a batch of tags
        with mlflow.start_run():
            mlflow.set_tags(tags)
    '''
def log_artifact(local_path: str, artifact_path: str | None = None) -> None:
    '''
    Log a local file or directory as an artifact of the currently active run. If no run is
    active, this method will create a new active run.

    :param local_path: Path to the file to write.
    :param artifact_path: If provided, the directory in ``artifact_uri`` to write to.

    .. test-code-block:: python
        :caption: Example

        import mlflow

        # Create a features.txt artifact file
        features = "rooms, zipcode, median_price, school_rating, transport"
        with open("features.txt", "w") as f:
            f.write(features)

        # With artifact_path=None write features.txt under
        # root artifact_uri/artifacts directory
        with mlflow.start_run():
            mlflow.log_artifact("features.txt")
    '''
def log_artifacts(local_dir: str, artifact_path: str | None = None) -> None:
    '''
    Log all the contents of a local directory as artifacts of the run. If no run is active,
    this method will create a new active run.

    :param local_dir: Path to the directory of files to write.
    :param artifact_path: If provided, the directory in ``artifact_uri`` to write to.

    .. test-code-block:: python
        :caption: Example

        import json
        import os
        import mlflow

        # Create some files to preserve as artifacts
        features = "rooms, zipcode, median_price, school_rating, transport"
        data = {"state": "TX", "Available": 25, "Type": "Detached"}

        # Create couple of artifact files under the directory "data"
        os.makedirs("data", exist_ok=True)
        with open("data/data.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
        with open("data/features.txt", "w") as f:
            f.write(features)

        # Write all files in "data" to root artifact_uri/states
        with mlflow.start_run():
            mlflow.log_artifacts("data", artifact_path="states")
    '''
def log_text(text: str, artifact_file: str) -> None:
    '''
    Log text as an artifact.

    :param text: String containing text to log.
    :param artifact_file: The run-relative artifact file path in posixpath format to which
                          the text is saved (e.g. "dir/file.txt").

    .. test-code-block:: python
        :caption: Example

        import mlflow

        with mlflow.start_run():
            # Log text to a file under the run\'s root artifact directory
            mlflow.log_text("text1", "file1.txt")

            # Log text in a subdirectory of the run\'s root artifact directory
            mlflow.log_text("text2", "dir/file2.txt")

            # Log HTML text
            mlflow.log_text("<h1>header</h1>", "index.html")
    '''
def log_dict(dictionary: Dict[str, Any], artifact_file: str) -> None:
    '''
    Log a JSON/YAML-serializable object (e.g. `dict`) as an artifact. The serialization
    format (JSON or YAML) is automatically inferred from the extension of `artifact_file`.
    If the file extension doesn\'t exist or match any of [".json", ".yml", ".yaml"],
    JSON format is used.

    :param dictionary: Dictionary to log.
    :param artifact_file: The run-relative artifact file path in posixpath format to which
                          the dictionary is saved (e.g. "dir/data.json").

    .. test-code-block:: python
        :caption: Example

        import mlflow

        dictionary = {"k": "v"}

        with mlflow.start_run():
            # Log a dictionary as a JSON file under the run\'s root artifact directory
            mlflow.log_dict(dictionary, "data.json")

            # Log a dictionary as a YAML file in a subdirectory of the run\'s root artifact directory
            mlflow.log_dict(dictionary, "dir/data.yml")

            # If the file extension doesn\'t exist or match any of [".json", ".yaml", ".yml"],
            # JSON format is used.
            mlflow.log_dict(dictionary, "data")
            mlflow.log_dict(dictionary, "data.txt")
    '''
def log_figure(figure: matplotlib.figure.Figure | plotly.graph_objects.Figure, artifact_file: str, *, save_kwargs: Dict[str, Any] | None = None) -> None:
    '''
    Log a figure as an artifact. The following figure objects are supported:

    - `matplotlib.figure.Figure`_
    - `plotly.graph_objects.Figure`_

    .. _matplotlib.figure.Figure:
        https://matplotlib.org/api/_as_gen/matplotlib.figure.Figure.html

    .. _plotly.graph_objects.Figure:
        https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html

    :param figure: Figure to log.
    :param artifact_file: The run-relative artifact file path in posixpath format to which
                          the figure is saved (e.g. "dir/file.png").
    :param save_kwargs: Additional keyword arguments passed to the method that saves the figure.

    .. test-code-block:: python
        :caption: Matplotlib Example

        import mlflow
        import matplotlib.pyplot as plt

        fig, ax = plt.subplots()
        ax.plot([0, 1], [2, 3])

        with mlflow.start_run():
            mlflow.log_figure(fig, "figure.png")

    .. test-code-block:: python
        :caption: Plotly Example

        import mlflow
        from plotly import graph_objects as go

        fig = go.Figure(go.Scatter(x=[0, 1], y=[2, 3]))

        with mlflow.start_run():
            mlflow.log_figure(fig, "figure.html")
    '''
def log_image(image: numpy.ndarray | PIL.Image.Image, artifact_file: str) -> None:
    '''
    Log an image as an artifact. The following image objects are supported:

    - `numpy.ndarray`_
    - `PIL.Image.Image`_

    .. _numpy.ndarray:
        https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html

    .. _PIL.Image.Image:
        https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image

    Numpy array support
        - data type (( ) represents a valid value range):

            - bool
            - integer (0 ~ 255)
            - unsigned integer (0 ~ 255)
            - float (0.0 ~ 1.0)

            .. warning::

                - Out-of-range integer values will be **clipped** to [0, 255].
                - Out-of-range float values will be **clipped** to [0, 1].

        - shape (H: height, W: width):

            - H x W (Grayscale)
            - H x W x 1 (Grayscale)
            - H x W x 3 (an RGB channel order is assumed)
            - H x W x 4 (an RGBA channel order is assumed)

    :param image: Image to log.
    :param artifact_file: The run-relative artifact file path in posixpath format to which
                          the image is saved (e.g. "dir/image.png").

    .. test-code-block:: python
        :caption: Numpy Example

        import mlflow
        import numpy as np

        image = np.random.randint(0, 256, size=(100, 100, 3), dtype=np.uint8)

        with mlflow.start_run():
            mlflow.log_image(image, "image.png")

    .. test-code-block:: python
        :caption: Pillow Example

        import mlflow
        from PIL import Image

        image = Image.new("RGB", (100, 100))

        with mlflow.start_run():
            mlflow.log_image(image, "image.png")
    '''
def log_table(data: Dict[str, Any] | pandas.DataFrame, artifact_file: str) -> None:
    '''
    Log a table to MLflow Tracking as a JSON artifact. If the artifact_file already exists
    in the run, the data would be appended to the existing artifact_file.

    :param data: Dictionary or pandas.DataFrame to log.
    :param artifact_file: The run-relative artifact file path in posixpath format to which
                              the table is saved (e.g. "dir/file.json").
    :return: None

    .. test-code-block:: python
        :caption: Dictionary Example

        import mlflow

        table_dict = {
            "inputs": ["What is MLflow?", "What is Databricks?"],
            "outputs": ["MLflow is ...", "Databricks is ..."],
            "toxicity": [0.0, 0.0],
        }

        with mlflow.start_run():
            # Log the dictionary as a table
            mlflow.log_table(data=table_dict, artifact_file="qabot_eval_results.json")

    .. test-code-block:: python
        :caption: Pandas DF Example

        import mlflow
        import pandas as pd

        table_dict = {
            "inputs": ["What is MLflow?", "What is Databricks?"],
            "outputs": ["MLflow is ...", "Databricks is ..."],
            "toxicity": [0.0, 0.0],
        }
        df = pd.DataFrame.from_dict(table_dict)

        with mlflow.start_run():
            # Log the df as a table
            mlflow.log_table(data=df, artifact_file="qabot_eval_results.json")
    '''
def load_table(artifact_file: str, run_ids: List[str] | None = None, extra_columns: List[str] | None = None) -> pandas.DataFrame:
    '''
    Load a table from MLflow Tracking as a pandas.DataFrame. The table is loaded from the
    specified artifact_file in the specified run_ids. The extra_columns are columns that
    are not in the table but are augmented with run information and added to the DataFrame.

    :param artifact_file: The run-relative artifact file path in posixpath format to which
                          table to load (e.g. "dir/file.json").
    :param run_ids: Optional list of run_ids to load the table from. If no run_ids are specified,
                    the table is loaded from all runs in the current experiment.
    :param extra_columns: Optional list of extra columns to add to the returned DataFrame
                          For example, if extra_columns=["run_id"], then the returned DataFrame
                          will have a column named run_id.

    :return: pandas.DataFrame containing the loaded table if the artifact exists
             or else throw a MlflowException.

    .. test-code-block:: python
        :caption: Example with passing run_ids

        import mlflow

        table_dict = {
            "inputs": ["What is MLflow?", "What is Databricks?"],
            "outputs": ["MLflow is ...", "Databricks is ..."],
            "toxicity": [0.0, 0.0],
        }

        with mlflow.start_run() as run:
            # Log the dictionary as a table
            mlflow.log_table(data=table_dict, artifact_file="qabot_eval_results.json")
            run_id = run.info.run_id

        loaded_table = mlflow.load_table(
            artifact_file="qabot_eval_results.json",
            run_ids=[run_id],
            # Append a column containing the associated run ID for each row
            extra_columns=["run_id"],
        )

    .. test-code-block:: python
        :caption: Example with passing no run_ids

        # Loads the table with the specified name for all runs in the given
        # experiment and joins them together
        import mlflow

        table_dict = {
            "inputs": ["What is MLflow?", "What is Databricks?"],
            "outputs": ["MLflow is ...", "Databricks is ..."],
            "toxicity": [0.0, 0.0],
        }

        with mlflow.start_run():
            # Log the dictionary as a table
            mlflow.log_table(data=table_dict, artifact_file="qabot_eval_results.json")

        loaded_table = mlflow.load_table(
            "qabot_eval_results.json",
            # Append the run ID and the parent run ID to the table
            extra_columns=["run_id"],
        )
    '''
def get_experiment(experiment_id: str) -> Experiment:
    '''
    Retrieve an experiment by experiment_id from the backend store

    :param experiment_id: The string-ified experiment ID returned from ``create_experiment``.
    :return: :py:class:`mlflow.entities.Experiment`

    .. test-code-block:: python
        :caption: Example

        import mlflow

        experiment = mlflow.get_experiment("0")
        print("Name: {}".format(experiment.name))
        print("Artifact Location: {}".format(experiment.artifact_location))
        print("Tags: {}".format(experiment.tags))
        print("Lifecycle_stage: {}".format(experiment.lifecycle_stage))
        print("Creation timestamp: {}".format(experiment.creation_time))

    .. code-block:: text
        :caption: Output

        Name: Default
        Artifact Location: file:///.../mlruns/0
        Tags: {}
        Lifecycle_stage: active
        Creation timestamp: 1662004217511
    '''
def get_experiment_by_name(name: str) -> Experiment | None:
    '''
    Retrieve an experiment by experiment name from the backend store

    :param name: The case sensitive experiment name.
    :return: An instance of :py:class:`mlflow.entities.Experiment`
             if an experiment with the specified name exists, otherwise None.

    .. test-code-block:: python
        :caption: Example

        import mlflow

        # Case sensitive name
        experiment = mlflow.get_experiment_by_name("Default")
        print("Experiment_id: {}".format(experiment.experiment_id))
        print("Artifact Location: {}".format(experiment.artifact_location))
        print("Tags: {}".format(experiment.tags))
        print("Lifecycle_stage: {}".format(experiment.lifecycle_stage))
        print("Creation timestamp: {}".format(experiment.creation_time))

    .. code-block:: text
        :caption: Output

        Experiment_id: 0
        Artifact Location: file:///.../mlruns/0
        Tags: {}
        Lifecycle_stage: active
        Creation timestamp: 1662004217511
    '''
def search_experiments(view_type: int = ..., max_results: int | None = None, filter_string: str | None = None, order_by: List[str] | None = None) -> List[Experiment]:
    '''
    Search for experiments that match the specified search query.

    :param view_type: One of enum values ``ACTIVE_ONLY``, ``DELETED_ONLY``, or ``ALL``
                      defined in :py:class:`mlflow.entities.ViewType`.
    :param max_results: If passed, specifies the maximum number of experiments desired. If not
                        passed, all experiments will be returned.
    :param filter_string:
        Filter query string (e.g., ``"name = \'my_experiment\'"``), defaults to searching for all
        experiments. The following identifiers, comparators, and logical operators are supported.

        Identifiers
          - ``name``: Experiment name
          - ``creation_time``: Experiment creation time
          - ``last_update_time``: Experiment last update time
          - ``tags.<tag_key>``: Experiment tag. If ``tag_key`` contains
            spaces, it must be wrapped with backticks (e.g., ``"tags.`extra key`"``).

        Comparators for string attributes and tags
            - ``=``: Equal to
            - ``!=``: Not equal to
            - ``LIKE``: Case-sensitive pattern match
            - ``ILIKE``: Case-insensitive pattern match

        Comparators for numeric attributes
            - ``=``: Equal to
            - ``!=``: Not equal to
            - ``<``: Less than
            - ``<=``: Less than or equal to
            - ``>``: Greater than
            - ``>=``: Greater than or equal to

        Logical operators
          - ``AND``: Combines two sub-queries and returns True if both of them are True.

    :param order_by:
        List of columns to order by. The ``order_by`` column can contain an optional ``DESC`` or
        ``ASC`` value (e.g., ``"name DESC"``). The default ordering is ``ASC``, so ``"name"`` is
        equivalent to ``"name ASC"``. If unspecified, defaults to ``["last_update_time DESC"]``,
        which lists experiments updated most recently first. The following fields are supported:

            - ``experiment_id``: Experiment ID
            - ``name``: Experiment name
            - ``creation_time``: Experiment creation time
            - ``last_update_time``: Experiment last update time

    :return: A list of :py:class:`Experiment <mlflow.entities.Experiment>` objects.

    .. test-code-block:: python
        :caption: Example

        import mlflow


        def assert_experiment_names_equal(experiments, expected_names):
            actual_names = [e.name for e in experiments if e.name != "Default"]
            assert actual_names == expected_names, (actual_names, expected_names)


        mlflow.set_tracking_uri("sqlite:///:memory:")

        # Create experiments
        for name, tags in [
            ("a", None),
            ("b", None),
            ("ab", {"k": "v"}),
            ("bb", {"k": "V"}),
        ]:
            mlflow.create_experiment(name, tags=tags)

        # Search for experiments with name "a"
        experiments = mlflow.search_experiments(filter_string="name = \'a\'")
        assert_experiment_names_equal(experiments, ["a"])

        # Search for experiments with name starting with "a"
        experiments = mlflow.search_experiments(filter_string="name LIKE \'a%\'")
        assert_experiment_names_equal(experiments, ["ab", "a"])

        # Search for experiments with tag key "k" and value ending with "v" or "V"
        experiments = mlflow.search_experiments(filter_string="tags.k ILIKE \'%v\'")
        assert_experiment_names_equal(experiments, ["bb", "ab"])

        # Search for experiments with name ending with "b" and tag {"k": "v"}
        experiments = mlflow.search_experiments(filter_string="name LIKE \'%b\' AND tags.k = \'v\'")
        assert_experiment_names_equal(experiments, ["ab"])

        # Sort experiments by name in ascending order
        experiments = mlflow.search_experiments(order_by=["name"])
        assert_experiment_names_equal(experiments, ["a", "ab", "b", "bb"])

        # Sort experiments by ID in descending order
        experiments = mlflow.search_experiments(order_by=["experiment_id DESC"])
        assert_experiment_names_equal(experiments, ["bb", "ab", "b", "a"])
    '''
def create_experiment(name: str, artifact_location: str | None = None, tags: Dict[str, Any] | None = None) -> str:
    '''
    Create an experiment.

    :param name: The experiment name, which must be unique and is case sensitive
    :param artifact_location: The location to store run artifacts.
                              If not provided, the server picks an appropriate default.
    :param tags: An optional dictionary of string keys and values to set as
                            tags on the experiment.
    :return: String ID of the created experiment.

    .. test-code-block:: python
        :caption: Example

        import mlflow
        from pathlib import Path

        # Create an experiment name, which must be unique and case sensitive
        experiment_id = mlflow.create_experiment(
            "Social NLP Experiments",
            artifact_location=Path.cwd().joinpath("mlruns").as_uri(),
            tags={"version": "v1", "priority": "P1"},
        )
        experiment = mlflow.get_experiment(experiment_id)
        print("Name: {}".format(experiment.name))
        print("Experiment_id: {}".format(experiment.experiment_id))
        print("Artifact Location: {}".format(experiment.artifact_location))
        print("Tags: {}".format(experiment.tags))
        print("Lifecycle_stage: {}".format(experiment.lifecycle_stage))
        print("Creation timestamp: {}".format(experiment.creation_time))

    .. code-block:: text
        :caption: Output

        Name: Social NLP Experiments
        Experiment_id: 1
        Artifact Location: file:///.../mlruns
        Tags: {\'version\': \'v1\', \'priority\': \'P1\'}
        Lifecycle_stage: active
        Creation timestamp: 1662004217511
    '''
def delete_experiment(experiment_id: str) -> None:
    '''
    Delete an experiment from the backend store.

    :param experiment_id: The The string-ified experiment ID returned from ``create_experiment``.

    .. test-code-block:: python
        :caption: Example

        import mlflow

        experiment_id = mlflow.create_experiment("New Experiment")
        mlflow.delete_experiment(experiment_id)

        # Examine the deleted experiment details.
        experiment = mlflow.get_experiment(experiment_id)
        print("Name: {}".format(experiment.name))
        print("Artifact Location: {}".format(experiment.artifact_location))
        print("Lifecycle_stage: {}".format(experiment.lifecycle_stage))
        print("Last Updated timestamp: {}".format(experiment.last_update_time))
    .. code-block:: text
        :caption: Output

        Name: New Experiment
        Artifact Location: file:///.../mlruns/2
        Lifecycle_stage: deleted
        Last Updated timestamp: 1662004217511
    '''
def delete_run(run_id: str) -> None:
    '''
    Deletes a run with the given ID.

    :param run_id: Unique identifier for the run to delete.

    .. test-code-block:: python
        :caption: Example

        import mlflow

        with mlflow.start_run() as run:
            mlflow.log_param("p", 0)

        run_id = run.info.run_id
        mlflow.delete_run(run_id)

        print(
            "run_id: {}; lifecycle_stage: {}".format(
                run_id, mlflow.get_run(run_id).info.lifecycle_stage
            )
        )

    .. code-block:: text
        :caption: Output

        run_id: 45f4af3e6fd349e58579b27fcb0b8277; lifecycle_stage: deleted
    '''
def get_artifact_uri(artifact_path: str | None = None) -> str:
    '''
    Get the absolute URI of the specified artifact in the currently active run.
    If `path` is not specified, the artifact root URI of the currently active
    run will be returned; calls to ``log_artifact`` and ``log_artifacts`` write
    artifact(s) to subdirectories of the artifact root URI.

    If no run is active, this method will create a new active run.

    :param artifact_path: The run-relative artifact path for which to obtain an absolute URI.
                          For example, "path/to/artifact". If unspecified, the artifact root URI
                          for the currently active run will be returned.
    :return: An *absolute* URI referring to the specified artifact or the currently active run\'s
             artifact root. For example, if an artifact path is provided and the currently active
             run uses an S3-backed store, this may be a uri of the form
             ``s3://<bucket_name>/path/to/artifact/root/path/to/artifact``. If an artifact path
             is not provided and the currently active run uses an S3-backed store, this may be a
             URI of the form ``s3://<bucket_name>/path/to/artifact/root``.

    .. test-code-block:: python
        :caption: Example

        import mlflow

        features = "rooms, zipcode, median_price, school_rating, transport"
        with open("features.txt", "w") as f:
            f.write(features)

        # Log the artifact in a directory "features" under the root artifact_uri/features
        with mlflow.start_run():
            mlflow.log_artifact("features.txt", artifact_path="features")

            # Fetch the artifact uri root directory
            artifact_uri = mlflow.get_artifact_uri()
            print("Artifact uri: {}".format(artifact_uri))

            # Fetch a specific artifact uri
            artifact_uri = mlflow.get_artifact_uri(artifact_path="features/features.txt")
            print("Artifact uri: {}".format(artifact_uri))

    .. code-block:: text
        :caption: Output

        Artifact uri: file:///.../0/a46a80f1c9644bd8f4e5dd5553fffce/artifacts
        Artifact uri: file:///.../0/a46a80f1c9644bd8f4e5dd5553fffce/artifacts/features/features.txt
    '''
def search_runs(experiment_ids: List[str] | None = None, filter_string: str = '', run_view_type: int = ..., max_results: int = ..., order_by: List[str] | None = None, output_format: str = 'pandas', search_all_experiments: bool = False, experiment_names: List[str] | None = None) -> List[Run] | pandas.DataFrame:
    '''
    Search for Runs that fit the specified criteria.

    :param experiment_ids: List of experiment IDs. Search can work with experiment IDs or
                           experiment names, but not both in the same call. Values other than
                           ``None`` or ``[]`` will result in error if ``experiment_names`` is
                           also not ``None`` or ``[]``. ``None`` will default to the active
                           experiment if ``experiment_names`` is ``None`` or ``[]``.
    :param filter_string: Filter query string, defaults to searching all runs.
    :param run_view_type: one of enum values ``ACTIVE_ONLY``, ``DELETED_ONLY``, or ``ALL`` runs
                            defined in :py:class:`mlflow.entities.ViewType`.
    :param max_results: The maximum number of runs to put in the dataframe. Default is 100,000
                        to avoid causing out-of-memory issues on the user\'s machine.
    :param order_by: List of columns to order by (e.g., "metrics.rmse"). The ``order_by`` column
                     can contain an optional ``DESC`` or ``ASC`` value. The default is ``ASC``.
                     The default ordering is to sort by ``start_time DESC``, then ``run_id``.
    :param output_format: The output format to be returned. If ``pandas``, a ``pandas.DataFrame``
                          is returned and, if ``list``, a list of :py:class:`mlflow.entities.Run`
                          is returned.
    :param search_all_experiments: Boolean specifying whether all experiments should be searched.
        Only honored if ``experiment_ids`` is ``[]`` or ``None``.
    :param experiment_names: List of experiment names. Search can work with experiment IDs or
                             experiment names, but not both in the same call. Values other
                             than ``None`` or ``[]`` will result in error if ``experiment_ids``
                             is also not ``None`` or ``[]``. ``None`` will default to the active
                             experiment if ``experiment_ids`` is ``None`` or ``[]``.
    :return: If output_format is ``list``: a list of :py:class:`mlflow.entities.Run`. If
             output_format is ``pandas``: ``pandas.DataFrame`` of runs, where each metric,
             parameter, and tag is expanded into its own column named metrics.*, params.*, or
             tags.* respectively. For runs that don\'t have a particular metric, parameter, or tag,
             the value for the corresponding column is (NumPy) ``Nan``, ``None``, or ``None``
             respectively.

    .. test-code-block:: python
        :caption: Example

        import mlflow

        # Create an experiment and log two runs under it
        experiment_name = "Social NLP Experiments"
        experiment_id = mlflow.create_experiment(experiment_name)
        with mlflow.start_run(experiment_id=experiment_id):
            mlflow.log_metric("m", 1.55)
            mlflow.set_tag("s.release", "1.1.0-RC")
        with mlflow.start_run(experiment_id=experiment_id):
            mlflow.log_metric("m", 2.50)
            mlflow.set_tag("s.release", "1.2.0-GA")

        # Search for all the runs in the experiment with the given experiment ID
        df = mlflow.search_runs([experiment_id], order_by=["metrics.m DESC"])
        print(df[["metrics.m", "tags.s.release", "run_id"]])
        print("--")

        # Search the experiment_id using a filter_string with tag
        # that has a case insensitive pattern
        filter_string = "tags.s.release ILIKE \'%rc%\'"
        df = mlflow.search_runs([experiment_id], filter_string=filter_string)
        print(df[["metrics.m", "tags.s.release", "run_id"]])
        print("--")

        # Search for all the runs in the experiment with the given experiment name
        df = mlflow.search_runs(experiment_names=[experiment_name], order_by=["metrics.m DESC"])
        print(df[["metrics.m", "tags.s.release", "run_id"]])


    .. code-block:: text
        :caption: Output

           metrics.m tags.s.release                            run_id
        0       2.50       1.2.0-GA  147eed886ab44633902cc8e19b2267e2
        1       1.55       1.1.0-RC  5cc7feaf532f496f885ad7750809c4d4
        --
           metrics.m tags.s.release                            run_id
        0       1.55       1.1.0-RC  5cc7feaf532f496f885ad7750809c4d4
        --
           metrics.m tags.s.release                            run_id
        0       2.50       1.2.0-GA  147eed886ab44633902cc8e19b2267e2
        1       1.55       1.1.0-RC  5cc7feaf532f496f885ad7750809c4d4
    '''
def autolog(log_input_examples: bool = False, log_model_signatures: bool = True, log_models: bool = True, log_datasets: bool = True, disable: bool = False, exclusive: bool = False, disable_for_unsupported_versions: bool = False, silent: bool = False, extra_tags: Dict[str, str] | None = None) -> None:
    '''
    Enables (or disables) and configures autologging for all supported integrations.

    The parameters are passed to any autologging integrations that support them.

    See the :ref:`tracking docs <automatic-logging>` for a list of supported autologging
    integrations.

    Note that framework-specific configurations set at any point will take precedence over
    any configurations set by this function. For example:

    .. test-code-block:: python

        import mlflow

        mlflow.autolog(log_models=False, exclusive=True)
        import sklearn

    would enable autologging for `sklearn` with `log_models=False` and `exclusive=True`,
    but

    .. test-code-block:: python

        import mlflow

        mlflow.autolog(log_models=False, exclusive=True)

        import sklearn

        mlflow.sklearn.autolog(log_models=True)

    would enable autologging for `sklearn` with `log_models=True` and `exclusive=False`,
    the latter resulting from the default value for `exclusive` in `mlflow.sklearn.autolog`;
    other framework autolog functions (e.g. `mlflow.tensorflow.autolog`) would use the
    configurations set by `mlflow.autolog` (in this instance, `log_models=False`, `exclusive=True`),
    until they are explicitly called by the user.

    :param log_input_examples: If ``True``, input examples from training datasets are collected and
                               logged along with model artifacts during training. If ``False``,
                               input examples are not logged.
                               Note: Input examples are MLflow model attributes
                               and are only collected if ``log_models`` is also ``True``.
    :param log_model_signatures: If ``True``,
                                 :py:class:`ModelSignatures <mlflow.models.ModelSignature>`
                                 describing model inputs and outputs are collected and logged along
                                 with model artifacts during training. If ``False``, signatures are
                                 not logged. Note: Model signatures are MLflow model attributes
                                 and are only collected if ``log_models`` is also ``True``.
    :param log_models: If ``True``, trained models are logged as MLflow model artifacts.
                       If ``False``, trained models are not logged.
                       Input examples and model signatures, which are attributes of MLflow models,
                       are also omitted when ``log_models`` is ``False``.
    :param log_datasets: If ``True``, dataset information is logged to MLflow Tracking.
                         If ``False``, dataset information is not logged.
    :param disable: If ``True``, disables all supported autologging integrations. If ``False``,
                    enables all supported autologging integrations.
    :param exclusive: If ``True``, autologged content is not logged to user-created fluent runs.
                      If ``False``, autologged content is logged to the active fluent run,
                      which may be user-created.
    :param disable_for_unsupported_versions: If ``True``, disable autologging for versions of
                      all integration libraries that have not been tested against this version
                      of the MLflow client or are incompatible.
    :param silent: If ``True``, suppress all event logs and warnings from MLflow during autologging
                   setup and training execution. If ``False``, show all events and warnings during
                   autologging setup and training execution.
    :param extra_tags: A dictionary of extra tags to set on each managed run created by autologging.

    .. test-code-block:: python
        :caption: Example

        import numpy as np
        import mlflow.sklearn
        from mlflow import MlflowClient
        from sklearn.linear_model import LinearRegression


        def print_auto_logged_info(r):
            tags = {k: v for k, v in r.data.tags.items() if not k.startswith("mlflow.")}
            artifacts = [f.path for f in MlflowClient().list_artifacts(r.info.run_id, "model")]
            print("run_id: {}".format(r.info.run_id))
            print("artifacts: {}".format(artifacts))
            print("params: {}".format(r.data.params))
            print("metrics: {}".format(r.data.metrics))
            print("tags: {}".format(tags))


        # prepare training data
        X = np.array([[1, 1], [1, 2], [2, 2], [2, 3]])
        y = np.dot(X, np.array([1, 2])) + 3

        # Auto log all the parameters, metrics, and artifacts
        mlflow.autolog()
        model = LinearRegression()
        with mlflow.start_run() as run:
            model.fit(X, y)

        # fetch the auto logged parameters and metrics for ended run
        print_auto_logged_info(mlflow.get_run(run_id=run.info.run_id))

    .. code-block:: text
        :caption: Output

        run_id: fd10a17d028c47399a55ab8741721ef7
        artifacts: [\'model/MLmodel\', \'model/conda.yaml\', \'model/model.pkl\']
        params: {\'copy_X\': \'True\',
                 \'normalize\': \'False\',
                 \'fit_intercept\': \'True\',
                 \'n_jobs\': \'None\'}
        metrics: {\'training_score\': 1.0,
                  \'training_root_mean_squared_error\': 4.440892098500626e-16,
                  \'training_r2_score\': 1.0,
                  \'training_mean_absolute_error\': 2.220446049250313e-16,
                  \'training_mean_squared_error\': 1.9721522630525295e-31}
        tags: {\'estimator_class\': \'sklearn.linear_model._base.LinearRegression\',
               \'estimator_name\': \'LinearRegression\'}
    '''
