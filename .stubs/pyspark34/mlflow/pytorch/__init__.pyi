from _typeshed import Incomplete
from mlflow import pyfunc as pyfunc
from mlflow.environment_variables import MLFLOW_DEFAULT_PREDICTION_DEVICE as MLFLOW_DEFAULT_PREDICTION_DEVICE
from mlflow.exceptions import MlflowException as MlflowException
from mlflow.models import Model as Model, ModelSignature as ModelSignature
from mlflow.models.model import MLMODEL_FILE_NAME as MLMODEL_FILE_NAME
from mlflow.models.utils import ModelInputExample as ModelInputExample
from mlflow.protos.databricks_pb2 import RESOURCE_DOES_NOT_EXIST as RESOURCE_DOES_NOT_EXIST
from mlflow.tracking._model_registry import DEFAULT_AWAIT_MAX_SLEEP_SECONDS as DEFAULT_AWAIT_MAX_SLEEP_SECONDS
from mlflow.utils.autologging_utils import autologging_integration as autologging_integration, safe_patch as safe_patch
from mlflow.utils.docstring_utils import LOG_MODEL_PARAM_DOCS as LOG_MODEL_PARAM_DOCS, format_docstring as format_docstring
from mlflow.utils.file_utils import TempDir as TempDir, write_to as write_to
from typing import Any, Dict

FLAVOR_NAME: str
MIN_REQ_VERSION: Incomplete
MAX_REQ_VERSION: Incomplete

def get_default_pip_requirements():
    """
    :return: A list of default pip requirements for MLflow Models produced by this flavor.
             Calls to :func:`save_model()` and :func:`log_model()` produce a pip environment
             that, at minimum, contains these requirements.
    """
def get_default_conda_env():
    '''
    :return: The default Conda environment as a dictionary for MLflow Models produced by calls to
             :func:`save_model()` and :func:`log_model()`.

    .. code-block:: python
        :caption: Example

        import mlflow.pytorch

        # Log PyTorch model
        with mlflow.start_run() as run:
            mlflow.pytorch.log_model(model, "model", signature=signature)

        # Fetch the associated conda environment
        env = mlflow.pytorch.get_default_conda_env()
        print("conda env: {}".format(env))

    .. code-block:: text
        :caption: Output

        conda env {\'name\': \'mlflow-env\',
                   \'channels\': [\'conda-forge\'],
                   \'dependencies\': [\'python=3.8.15\',
                                    {\'pip\': [\'torch==1.5.1\',
                                             \'mlflow\',
                                             \'cloudpickle==1.6.0\']}]}
    '''
def log_model(pytorch_model, artifact_path, conda_env: Incomplete | None = None, code_paths: Incomplete | None = None, pickle_module: Incomplete | None = None, registered_model_name: Incomplete | None = None, signature: ModelSignature = None, input_example: ModelInputExample = None, await_registration_for=..., requirements_file: Incomplete | None = None, extra_files: Incomplete | None = None, pip_requirements: Incomplete | None = None, extra_pip_requirements: Incomplete | None = None, metadata: Incomplete | None = None, **kwargs):
    '''
    Log a PyTorch model as an MLflow artifact for the current run.

        .. warning::

            Log the model with a signature to avoid inference errors.
            If the model is logged without a signature, the MLflow Model Server relies on the
            default inferred data type from NumPy. However, PyTorch often expects different
            defaults, particularly when parsing floats. You must include the signature to ensure
            that the model is logged with the correct data type so that the MLflow model server
            can correctly provide valid input.

    :param pytorch_model: PyTorch model to be saved. Can be either an eager model (subclass of
                          ``torch.nn.Module``) or scripted model prepared via ``torch.jit.script``
                          or ``torch.jit.trace``.

                          The model accept a single ``torch.FloatTensor`` as
                          input and produce a single output tensor.

                          If saving an eager model, any code dependencies of the
                          model\'s class, including the class definition itself, should be
                          included in one of the following locations:

                          - The package(s) listed in the model\'s Conda environment, specified
                            by the ``conda_env`` parameter.
                          - One or more of the files specified by the ``code_paths`` parameter.

    :param artifact_path: Run-relative artifact path.
    :param conda_env: {{ conda_env }}
    :param code_paths: A list of local filesystem paths to Python file dependencies (or directories
                       containing file dependencies). These files are *prepended* to the system
                       path when the model is loaded.
    :param pickle_module: The module that PyTorch should use to serialize ("pickle") the specified
                          ``pytorch_model``. This is passed as the ``pickle_module`` parameter
                          to ``torch.save()``. By default, this module is also used to
                          deserialize ("unpickle") the PyTorch model at load time.
    :param registered_model_name: If given, create a model version under
                                  ``registered_model_name``, also creating a registered model if one
                                  with the given name does not exist.
    :param signature: {{ signature }}
    :param input_example: {{ input_example }}
    :param await_registration_for: Number of seconds to wait for the model version to finish
                            being created and is in ``READY`` status. By default, the function
                            waits for five minutes. Specify 0 or None to skip waiting.

    :param requirements_file:

        .. warning::

            ``requirements_file`` has been deprecated. Please use ``pip_requirements`` instead.

        A string containing the path to requirements file. Remote URIs are resolved to absolute
        filesystem paths. For example, consider the following ``requirements_file`` string:

        .. code-block:: python

            requirements_file = "s3://my-bucket/path/to/my_file"

        In this case, the ``"my_file"`` requirements file is downloaded from S3. If ``None``,
        no requirements file is added to the model.

    :param extra_files: A list containing the paths to corresponding extra files. Remote URIs
                      are resolved to absolute filesystem paths.
                      For example, consider the following ``extra_files`` list -

                      extra_files = ["s3://my-bucket/path/to/my_file1",
                                    "s3://my-bucket/path/to/my_file2"]

                      In this case, the ``"my_file1 & my_file2"`` extra file is downloaded from S3.

                      If ``None``, no extra files are added to the model.
    :param pip_requirements: {{ pip_requirements }}
    :param extra_pip_requirements: {{ extra_pip_requirements }}
    :param metadata: Custom metadata dictionary passed to the model and stored in the MLmodel file.

                     .. Note:: Experimental: This parameter may change or be removed in a future
                                             release without warning.
    :param kwargs: kwargs to pass to ``torch.save`` method.
    :return: A :py:class:`ModelInfo <mlflow.models.model.ModelInfo>` instance that contains the
             metadata of the logged model.

    .. code-block:: python
        :caption: Example

        import numpy as np
        import torch
        import mlflow
        from mlflow import MlflowClient
        from mlflow.models import infer_signature

        # Define model, loss, and optimizer
        model = nn.Linear(1, 1)
        criterion = torch.nn.MSELoss()
        optimizer = torch.optim.SGD(model.parameters(), lr=0.001)

        # Create training data with relationship y = 2X
        X = torch.arange(1.0, 26.0).reshape(-1, 1)
        y = X * 2

        # Training loop
        epochs = 250
        for epoch in range(epochs):
            # Forward pass: Compute predicted y by passing X to the model
            y_pred = model(X)

            # Compute the loss
            loss = criterion(y_pred, y)

            # Zero gradients, perform a backward pass, and update the weights.
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

        # Create model signature
        signature = infer_signature(X.numpy(), model(X).detach().numpy())

        # Log the model
        with mlflow.start_run() as run:
            mlflow.pytorch.log_model(model, "model")

            # convert to scripted model and log the model
            scripted_pytorch_model = torch.jit.script(model)
            mlflow.pytorch.log_model(scripted_pytorch_model, "scripted_model")

        # Fetch the logged model artifacts
        print("run_id: {}".format(run.info.run_id))
        for artifact_path in ["model/data", "scripted_model/data"]:
            artifacts = [
                f.path for f in MlflowClient().list_artifacts(run.info.run_id, artifact_path)
            ]
            print("artifacts: {}".format(artifacts))

    .. code-block:: text
        :caption: Output

        run_id: 1a1ec9e413ce48e9abf9aec20efd6f71
        artifacts: [\'model/data/model.pth\',
                    \'model/data/pickle_module_info.txt\']
        artifacts: [\'scripted_model/data/model.pth\',
                    \'scripted_model/data/pickle_module_info.txt\']

    .. figure:: ../_static/images/pytorch_logged_models.png

        PyTorch logged models
    '''
def save_model(pytorch_model, path, conda_env: Incomplete | None = None, mlflow_model: Incomplete | None = None, code_paths: Incomplete | None = None, pickle_module: Incomplete | None = None, signature: ModelSignature = None, input_example: ModelInputExample = None, requirements_file: Incomplete | None = None, extra_files: Incomplete | None = None, pip_requirements: Incomplete | None = None, extra_pip_requirements: Incomplete | None = None, metadata: Incomplete | None = None, **kwargs):
    '''
    Save a PyTorch model to a path on the local file system.

    :param pytorch_model: PyTorch model to be saved. Can be either an eager model (subclass of
                          ``torch.nn.Module``) or scripted model prepared via ``torch.jit.script``
                          or ``torch.jit.trace``.

                          The model accept a single ``torch.FloatTensor`` as
                          input and produce a single output tensor.

                          If saving an eager model, any code dependencies of the
                          model\'s class, including the class definition itself, should be
                          included in one of the following locations:

                          - The package(s) listed in the model\'s Conda environment, specified
                            by the ``conda_env`` parameter.
                          - One or more of the files specified by the ``code_paths`` parameter.

    :param path: Local path where the model is to be saved.
    :param conda_env: {{ conda_env }}
    :param mlflow_model: :py:mod:`mlflow.models.Model` this flavor is being added to.
    :param code_paths: A list of local filesystem paths to Python file dependencies (or directories
                       containing file dependencies). These files are *prepended* to the system
                       path when the model is loaded.
    :param pickle_module: The module that PyTorch should use to serialize ("pickle") the specified
                          ``pytorch_model``. This is passed as the ``pickle_module`` parameter
                          to ``torch.save()``. By default, this module is also used to
                          deserialize ("unpickle") the PyTorch model at load time.
    :param signature: {{ signature }}
    :param input_example: {{ input_example }}
    :param requirements_file:

        .. warning::

            ``requirements_file`` has been deprecated. Please use ``pip_requirements`` instead.

        A string containing the path to requirements file. Remote URIs are resolved to absolute
        filesystem paths. For example, consider the following ``requirements_file`` string:

        .. code-block:: python

            requirements_file = "s3://my-bucket/path/to/my_file"

        In this case, the ``"my_file"`` requirements file is downloaded from S3. If ``None``,
        no requirements file is added to the model.

    :param extra_files: A list containing the paths to corresponding extra files. Remote URIs
                      are resolved to absolute filesystem paths.
                      For example, consider the following ``extra_files`` list -

                      extra_files = ["s3://my-bucket/path/to/my_file1",
                                    "s3://my-bucket/path/to/my_file2"]

                      In this case, the ``"my_file1 & my_file2"`` extra file is downloaded from S3.

                      If ``None``, no extra files are added to the model.
    :param pip_requirements: {{ pip_requirements }}
    :param extra_pip_requirements: {{ extra_pip_requirements }}
    :param metadata: Custom metadata dictionary passed to the model and stored in the MLmodel file.

                     .. Note:: Experimental: This parameter may change or be removed in a future
                                             release without warning.
    :param kwargs: kwargs to pass to ``torch.save`` method.

    .. code-block:: python
        :caption: Example

        import os

        import torch
        import mlflow.pytorch


        # Class defined here
        class LinearNNModel(torch.nn.Module):
            ...


        # Initialize our model, criterion and optimizer
        ...

        # Training loop
        ...

        # Save PyTorch models to current working directory
        with mlflow.start_run() as run:
            mlflow.pytorch.save_model(model, "model")

            # Convert to a scripted model and save it
            scripted_pytorch_model = torch.jit.script(model)
            mlflow.pytorch.save_model(scripted_pytorch_model, "scripted_model")

        # Load each saved model for inference
        for model_path in ["model", "scripted_model"]:
            model_uri = "{}/{}".format(os.getcwd(), model_path)
            loaded_model = mlflow.pytorch.load_model(model_uri)
            print("Loaded {}:".format(model_path))
            for x in [6.0, 8.0, 12.0, 30.0]:
                X = torch.Tensor([[x]])
                y_pred = loaded_model(X)
                print("predict X: {}, y_pred: {:.2f}".format(x, y_pred.data.item()))
            print("--")

    .. code-block:: text
        :caption: Output

        Loaded model:
        predict X: 6.0, y_pred: 11.90
        predict X: 8.0, y_pred: 15.92
        predict X: 12.0, y_pred: 23.96
        predict X: 30.0, y_pred: 60.13
        --
        Loaded scripted_model:
        predict X: 6.0, y_pred: 11.90
        predict X: 8.0, y_pred: 15.92
        predict X: 12.0, y_pred: 23.96
        predict X: 30.0, y_pred: 60.13
    '''
def load_model(model_uri, dst_path: Incomplete | None = None, **kwargs):
    '''
    Load a PyTorch model from a local file or a run.

    :param model_uri: The location, in URI format, of the MLflow model, for example:

                      - ``/Users/me/path/to/local/model``
                      - ``relative/path/to/local/model``
                      - ``s3://my_bucket/path/to/model``
                      - ``runs:/<mlflow_run_id>/run-relative/path/to/model``
                      - ``models:/<model_name>/<model_version>``
                      - ``models:/<model_name>/<stage>``

                      For more information about supported URI schemes, see
                      `Referencing Artifacts <https://www.mlflow.org/docs/latest/concepts.html#
                      artifact-locations>`_.
    :param dst_path: The local filesystem path to which to download the model artifact.
                     This directory must already exist. If unspecified, a local output
                     path will be created.

    :param kwargs: kwargs to pass to ``torch.load`` method.
    :return: A PyTorch model.

    .. code-block:: python
        :caption: Example

        import torch
        import mlflow.pytorch


        # Class defined here
        class LinearNNModel(torch.nn.Module):
            ...


        # Initialize our model, criterion and optimizer
        ...

        # Training loop
        ...

        # Log the model
        with mlflow.start_run() as run:
            mlflow.pytorch.log_model(model, "model", signature=signature)

        # Inference after loading the logged model
        model_uri = "runs:/{}/model".format(run.info.run_id)
        loaded_model = mlflow.pytorch.load_model(model_uri)
        for x in [4.0, 6.0, 30.0]:
            X = torch.Tensor([[x]])
            y_pred = loaded_model(X)
            print("predict X: {}, y_pred: {:.2f}".format(x, y_pred.data.item()))

    .. code-block:: text
        :caption: Output

        predict X: 4.0, y_pred: 7.57
        predict X: 6.0, y_pred: 11.64
        predict X: 30.0, y_pred: 60.48
    '''

class _PyTorchWrapper:
    """
    Wrapper class that creates a predict function such that
    predict(data: pd.DataFrame) -> model's output as pd.DataFrame (pandas DataFrame)
    """
    pytorch_model: Incomplete
    def __init__(self, pytorch_model) -> None: ...
    def predict(self, data, params: Dict[str, Any] | None = None):
        """
        :param data: Model input data.
        :param params: Additional parameters to pass to the model for inference.

                       .. Note:: Experimental: This parameter may change or be removed in a future
                                               release without warning.

        :return: Model predictions.
        """

def log_state_dict(state_dict, artifact_path, **kwargs) -> None:
    '''
    Log a state_dict as an MLflow artifact for the current run.

    .. warning::
        This function just logs a state_dict as an artifact and doesn\'t generate
        an :ref:`MLflow Model <models>`.

    :param state_dict: state_dict to be saved.
    :param artifact_path: Run-relative artifact path.
    :param kwargs: kwargs to pass to ``torch.save``.

    .. code-block:: python
        :caption: Example

        # Log a model as a state_dict
        with mlflow.start_run():
            state_dict = model.state_dict()
            mlflow.pytorch.log_state_dict(state_dict, artifact_path="model")

        # Log a checkpoint as a state_dict
        with mlflow.start_run():
            state_dict = {
                "model": model.state_dict(),
                "optimizer": optimizer.state_dict(),
                "epoch": epoch,
                "loss": loss,
            }
            mlflow.pytorch.log_state_dict(state_dict, artifact_path="checkpoint")
    '''
def save_state_dict(state_dict, path, **kwargs) -> None:
    """
    Save a state_dict to a path on the local file system

    :param state_dict: state_dict to be saved.
    :param path: Local path where the state_dict is to be saved.
    :param kwargs: kwargs to pass to ``torch.save``.
    """
def load_state_dict(state_dict_uri, **kwargs):
    '''
    Load a state_dict from a local file or a run.

    :param state_dict_uri: The location, in URI format, of the state_dict, for example:

                    - ``/Users/me/path/to/local/state_dict``
                    - ``relative/path/to/local/state_dict``
                    - ``s3://my_bucket/path/to/state_dict``
                    - ``runs:/<mlflow_run_id>/run-relative/path/to/state_dict``

                    For more information about supported URI schemes, see
                    `Referencing Artifacts <https://www.mlflow.org/docs/latest/concepts.html#
                    artifact-locations>`_.

    :param kwargs: kwargs to pass to ``torch.load``.
    :return: A state_dict

    .. code-block:: python
        :caption: Example

        with mlflow.start_run():
            artifact_path = "model"
            mlflow.pytorch.log_state_dict(model.state_dict(), artifact_path)
            state_dict_uri = mlflow.get_artifact_uri(artifact_path)

        state_dict = mlflow.pytorch.load_state_dict(state_dict_uri)
    '''
def autolog(log_every_n_epoch: int = 1, log_every_n_step: Incomplete | None = None, log_models: bool = True, log_datasets: bool = True, disable: bool = False, exclusive: bool = False, disable_for_unsupported_versions: bool = False, silent: bool = False, registered_model_name: Incomplete | None = None, extra_tags: Incomplete | None = None) -> None:
    '''
    Enables (or disables) and configures autologging from `PyTorch Lightning
    <https://pytorch-lightning.readthedocs.io/en/latest>`_ to MLflow.

    Autologging is performed when you call the `fit` method of
    `pytorch_lightning.Trainer()     <https://pytorch-lightning.readthedocs.io/en/latest/trainer.html#>`_.

    Explore the complete `PyTorch MNIST     <https://github.com/mlflow/mlflow/tree/master/examples/pytorch/MNIST>`_ for
    an expansive example with implementation of additional lightening steps.

    **Note**: Full autologging is only supported for PyTorch Lightning models,
    i.e., models that subclass
    `pytorch_lightning.LightningModule     <https://pytorch-lightning.readthedocs.io/en/latest/lightning_module.html>`_.
    Autologging support for vanilla PyTorch (ie models that only subclass
    `torch.nn.Module <https://pytorch.org/docs/stable/generated/torch.nn.Module.html>`_)
    only autologs calls to
    `torch.utils.tensorboard.SummaryWriter <https://pytorch.org/docs/stable/tensorboard.html>`_\'s
    ``add_scalar`` and ``add_hparams`` methods to mlflow. In this case, there\'s also
    no notion of an "epoch".

    .. Note:: Only pytorch-lightning modules between versions MIN_REQ_VERSION and
              MAX_REQ_VERSION are known to be compatible with mlflow\'s autologging.

    :param log_every_n_epoch: If specified, logs metrics once every `n` epochs. By default, metrics
                       are logged after every epoch.
    :param log_every_n_step: If specified, logs batch metrics once every `n` global step.
                       By default, metrics are not logged for steps. Note that setting this to 1 can
                       cause performance issues and is not recommended.
    :param log_models: If ``True``, trained models are logged as MLflow model artifacts.
                       If ``False``, trained models are not logged.
    :param log_datasets: If ``True``, dataset information is logged to MLflow Tracking.
                         If ``False``, dataset information is not logged.
    :param disable: If ``True``, disables the PyTorch Lightning autologging integration.
                    If ``False``, enables the PyTorch Lightning autologging integration.
    :param exclusive: If ``True``, autologged content is not logged to user-created fluent runs.
                      If ``False``, autologged content is logged to the active fluent run,
                      which may be user-created.
    :param disable_for_unsupported_versions: If ``True``, disable autologging for versions of
                      pytorch and pytorch-lightning that have not been tested against this version
                      of the MLflow client or are incompatible.
    :param silent: If ``True``, suppress all event logs and warnings from MLflow during PyTorch
                   Lightning autologging. If ``False``, show all events and warnings during
                   PyTorch Lightning autologging.
    :param registered_model_name: If given, each time a model is trained, it is registered as a
                                  new model version of the registered model with this name.
                                  The registered model is created if it does not already exist.
    :param extra_tags: A dictionary of extra tags to set on each managed run created by autologging.

    .. code-block:: python
        :caption: Example

        import os

        import pytorch_lightning as pl
        import torch
        from torch.nn import functional as F
        from torch.utils.data import DataLoader
        from torchvision import transforms
        from torchvision.datasets import MNIST

        try:
            from torchmetrics.functional import accuracy
        except ImportError:
            from pytorch_lightning.metrics.functional import accuracy

        import mlflow.pytorch
        from mlflow import MlflowClient

        # For brevity, here is the simplest most minimal example with just a training
        # loop step, (no validation, no testing). It illustrates how you can use MLflow
        # to auto log parameters, metrics, and models.


        class MNISTModel(pl.LightningModule):
            def __init__(self):
                super().__init__()
                self.l1 = torch.nn.Linear(28 * 28, 10)

            def forward(self, x):
                return torch.relu(self.l1(x.view(x.size(0), -1)))

            def training_step(self, batch, batch_nb):
                x, y = batch
                logits = self(x)
                loss = F.cross_entropy(logits, y)
                pred = logits.argmax(dim=1)
                acc = accuracy(pred, y)

                # Use the current of PyTorch logger
                self.log("train_loss", loss, on_epoch=True)
                self.log("acc", acc, on_epoch=True)
                return loss

            def configure_optimizers(self):
                return torch.optim.Adam(self.parameters(), lr=0.02)


        def print_auto_logged_info(r):
            tags = {k: v for k, v in r.data.tags.items() if not k.startswith("mlflow.")}
            artifacts = [f.path for f in MlflowClient().list_artifacts(r.info.run_id, "model")]
            print("run_id: {}".format(r.info.run_id))
            print("artifacts: {}".format(artifacts))
            print("params: {}".format(r.data.params))
            print("metrics: {}".format(r.data.metrics))
            print("tags: {}".format(tags))


        # Initialize our model
        mnist_model = MNISTModel()

        # Initialize DataLoader from MNIST Dataset
        train_ds = MNIST(
            os.getcwd(), train=True, download=True, transform=transforms.ToTensor()
        )
        train_loader = DataLoader(train_ds, batch_size=32)

        # Initialize a trainer
        trainer = pl.Trainer(max_epochs=20, progress_bar_refresh_rate=20)

        # Auto log all MLflow entities
        mlflow.pytorch.autolog()

        # Train the model
        with mlflow.start_run() as run:
            trainer.fit(mnist_model, train_loader)

        # fetch the auto logged parameters and metrics
        print_auto_logged_info(mlflow.get_run(run_id=run.info.run_id))

    .. code-block:: text
        :caption: Output

        run_id: 42caa17b60cb489c8083900fb52506a7
        artifacts: [\'model/MLmodel\', \'model/conda.yaml\', \'model/data\']
        params: {\'betas\': \'(0.9, 0.999)\',
                 \'weight_decay\': \'0\',
                 \'epochs\': \'20\',
                 \'eps\': \'1e-08\',
                 \'lr\': \'0.02\',
                 \'optimizer_name\': \'Adam\', \'
                 amsgrad\': \'False\'}
        metrics: {\'acc_step\': 0.0,
                  \'train_loss_epoch\': 1.0917967557907104,
                  \'train_loss_step\': 1.0794280767440796,
                  \'train_loss\': 1.0794280767440796,
                  \'acc_epoch\': 0.0033333334140479565,
                  \'acc\': 0.0}
        tags: {\'Mode\': \'training\'}

    .. figure:: ../_static/images/pytorch_lightening_autolog.png

        PyTorch autologged MLflow entities
    '''
