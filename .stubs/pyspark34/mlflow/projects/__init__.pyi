from _typeshed import Incomplete
from mlflow.projects.submitted_run import SubmittedRun as SubmittedRun

__all__ = ['run', 'SubmittedRun']

def run(uri, entry_point: str = 'main', version: Incomplete | None = None, parameters: Incomplete | None = None, docker_args: Incomplete | None = None, experiment_name: Incomplete | None = None, experiment_id: Incomplete | None = None, backend: str = 'local', backend_config: Incomplete | None = None, storage_dir: Incomplete | None = None, synchronous: bool = True, run_id: Incomplete | None = None, run_name: Incomplete | None = None, env_manager: Incomplete | None = None, build_image: bool = False, docker_auth: Incomplete | None = None):
    '''
    Run an MLflow project. The project can be local or stored at a Git URI.

    MLflow provides built-in support for running projects locally or remotely on a Databricks or
    Kubernetes cluster. You can also run projects against other targets by installing an appropriate
    third-party plugin. See `Community Plugins <../plugins.html#community-plugins>`_ for more
    information.

    For information on using this method in chained workflows, see `Building Multistep Workflows
    <../projects.html#building-multistep-workflows>`_.

    :raises: :py:class:`mlflow.exceptions.ExecutionException` If a run launched in blocking mode
             is unsuccessful.

    :param uri: URI of project to run. A local filesystem path
                or a Git repository URI (e.g. https://github.com/mlflow/mlflow-example)
                pointing to a project directory containing an MLproject file.
    :param entry_point: Entry point to run within the project. If no entry point with the specified
                        name is found, runs the project file ``entry_point`` as a script,
                        using "python" to run ``.py`` files and the default shell (specified by
                        environment variable ``$SHELL``) to run ``.sh`` files.
    :param version: For Git-based projects, either a commit hash or a branch name.
    :param parameters: Parameters (dictionary) for the entry point command.
    :param docker_args: Arguments (dictionary) for the docker command.
    :param experiment_name: Name of experiment under which to launch the run.
    :param experiment_id: ID of experiment under which to launch the run.
    :param backend: Execution backend for the run: MLflow provides built-in support for "local",
                    "databricks", and "kubernetes" (experimental) backends. If running against
                    Databricks, will run against a Databricks workspace determined as follows:
                    if a Databricks tracking URI of the form ``databricks://profile`` has been set
                    (e.g. by setting the MLFLOW_TRACKING_URI environment variable), will run
                    against the workspace specified by <profile>. Otherwise, runs against the
                    workspace specified by the default Databricks CLI profile.
    :param backend_config: A dictionary, or a path to a JSON file (must end in \'.json\'), which will
                           be passed as config to the backend. The exact content which should be
                           provided is different for each execution backend and is documented
                           at https://www.mlflow.org/docs/latest/projects.html.
    :param storage_dir: Used only if ``backend`` is "local". MLflow downloads artifacts from
                        distributed URIs passed to parameters of type ``path`` to subdirectories of
                        ``storage_dir``.
    :param synchronous: Whether to block while waiting for a run to complete. Defaults to True.
                        Note that if ``synchronous`` is False and ``backend`` is "local", this
                        method will return, but the current process will block when exiting until
                        the local run completes. If the current process is interrupted, any
                        asynchronous runs launched via this method will be terminated. If
                        ``synchronous`` is True and the run fails, the current process will
                        error out as well.
    :param run_id: Note: this argument is used internally by the MLflow project APIs and should
                   not be specified. If specified, the run ID will be used instead of
                   creating a new run.
    :param run_name: The name to give the MLflow Run associated with the project execution.
                     If ``None``, the MLflow Run name is left unset.
    :param env_manager: Specify an environment manager to create a new environment for the run and
                        install project dependencies within that environment. The following values
                        are supported:

                        - local: use the local environment
                        - virtualenv: use virtualenv (and pyenv for Python version management)
                        - conda: use conda

                        If unspecified, MLflow automatically determines the environment manager to
                        use by inspecting files in the project directory. For example, if
                        ``python_env.yaml`` is present, virtualenv will be used.
    :param build_image: Whether to build a new docker image of the project or to reuse an existing
                        image. Default: False (reuse an existing image)
    :param docker_auth: A dictionary representing information to authenticate with a Docker
                        registry. See `docker.client.DockerClient.login
                        <https://docker-py.readthedocs.io/en/stable/client.html#docker.client.DockerClient.login>`_
                        for available options.
    :return: :py:class:`mlflow.projects.SubmittedRun` exposing information (e.g. run ID)
             about the launched run.

    .. code-block:: python
        :caption: Example

        import mlflow

        project_uri = "https://github.com/mlflow/mlflow-example"
        params = {"alpha": 0.5, "l1_ratio": 0.01}

        # Run MLflow project and create a reproducible conda environment
        # on a local host
        mlflow.run(project_uri, parameters=params)

    .. code-block:: text
        :caption: Output

        ...
        ...
        Elasticnet model (alpha=0.500000, l1_ratio=0.010000):
        RMSE: 0.788347345611717
        MAE: 0.6155576449938276
        R2: 0.19729662005412607
        ... mlflow.projects: === Run (ID \'6a5109febe5e4a549461e149590d0a7c\') succeeded ===
    '''
