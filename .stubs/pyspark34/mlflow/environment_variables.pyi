from _typeshed import Incomplete

class _EnvironmentVariable:
    """
    Represents an environment variable.
    """
    name: Incomplete
    type: Incomplete
    default: Incomplete
    def __init__(self, name, type_, default) -> None: ...
    @property
    def is_defined(self): ...
    def get_raw(self): ...
    def set(self, value) -> None: ...
    def unset(self) -> None: ...
    def get(self):
        """
        Reads the value of the environment variable if it exists and converts it to the desired
        type. Otherwise, returns the default value.
        """
    def __format__(self, format_spec: str) -> str: ...

class _BooleanEnvironmentVariable(_EnvironmentVariable):
    """
    Represents a boolean environment variable.
    """
    def __init__(self, name, default) -> None: ...
    def get(self): ...

MLFLOW_TRACKING_URI: Incomplete
MLFLOW_REGISTRY_URI: Incomplete
MLFLOW_DFS_TMP: Incomplete
MLFLOW_HTTP_REQUEST_MAX_RETRIES: Incomplete
MLFLOW_HTTP_REQUEST_BACKOFF_FACTOR: Incomplete
MLFLOW_HTTP_REQUEST_TIMEOUT: Incomplete
MLFLOW_TRACKING_AWS_SIGV4: Incomplete
MLFLOW_GCS_DOWNLOAD_CHUNK_SIZE: Incomplete
MLFLOW_GCS_UPLOAD_CHUNK_SIZE: Incomplete
MLFLOW_GCS_DEFAULT_TIMEOUT: Incomplete
MLFLOW_S3_ENDPOINT_URL: Incomplete
MLFLOW_S3_IGNORE_TLS: Incomplete
MLFLOW_S3_UPLOAD_EXTRA_ARGS: Incomplete
MLFLOW_KERBEROS_TICKET_CACHE: Incomplete
MLFLOW_KERBEROS_USER: Incomplete
MLFLOW_PYARROW_EXTRA_CONF: Incomplete
MLFLOW_SQLALCHEMYSTORE_POOL_SIZE: Incomplete
MLFLOW_SQLALCHEMYSTORE_POOL_RECYCLE: Incomplete
MLFLOW_SQLALCHEMYSTORE_MAX_OVERFLOW: Incomplete
MLFLOW_SQLALCHEMYSTORE_ECHO: Incomplete
MLFLOW_DISABLE_ENV_MANAGER_CONDA_WARNING: Incomplete
MLFLOW_SQLALCHEMYSTORE_POOLCLASS: Incomplete
MLFLOW_REQUIREMENTS_INFERENCE_TIMEOUT: Incomplete
MLFLOW_SCORING_SERVER_REQUEST_TIMEOUT: Incomplete
MLFLOW_ARTIFACT_UPLOAD_DOWNLOAD_TIMEOUT: Incomplete
MLFLOW_DEFAULT_PREDICTION_DEVICE: Incomplete
MLFLOW_HUGGINGFACE_DISABLE_ACCELERATE_FEATURES: Incomplete
MLFLOW_HUGGINGFACE_USE_DEVICE_MAP: Incomplete
MLFLOW_HUGGINGFACE_DEVICE_MAP_STRATEGY: Incomplete
MLFLOW_HUGGINGFACE_USE_LOW_CPU_MEM_USAGE: Incomplete
MLFLOW_HUGGINGFACE_MODEL_MAX_SHARD_SIZE: Incomplete
MLFLOW_ALLOW_FILE_URI_AS_MODEL_VERSION_SOURCE: Incomplete
MLFLOW_OPENAI_SECRET_SCOPE: Incomplete
MLFLOW_OPENAI_RETRIES_ENABLED: Incomplete
MLFLOW_WHEELED_MODEL_PIP_DOWNLOAD_OPTIONS: Incomplete
MLFLOW_ENABLE_MULTIPART_DOWNLOAD: Incomplete
MLFLOW_TRACKING_USERNAME: Incomplete
MLFLOW_TRACKING_PASSWORD: Incomplete
MLFLOW_TRACKING_TOKEN: Incomplete
MLFLOW_TRACKING_INSECURE_TLS: Incomplete
MLFLOW_TRACKING_SERVER_CERT_PATH: Incomplete
MLFLOW_TRACKING_CLIENT_CERT_PATH: Incomplete
MLFLOW_RUN_ID: Incomplete
MLFLOW_TRACKING_DIR: Incomplete
MLFLOW_REGISTRY_DIR: Incomplete
MLFLOW_EXPERIMENT_ID: Incomplete
MLFLOW_EXPERIMENT_NAME: Incomplete
MLFLOW_AUTH_CONFIG_PATH: Incomplete
MLFLOW_ENV_ROOT: Incomplete
MLFLOW_ENABLE_DBFS_FUSE_ARTIFACT_REPO: Incomplete
MLFLOW_GATEWAY_URI: Incomplete
MLFLOW_ENABLE_ARTIFACTS_PROGRESS_BAR: Incomplete
MLFLOW_CONDA_CREATE_ENV_CMD: Incomplete
MLFLOW_RECIPES_EXECUTION_DIRECTORY: Incomplete
MLFLOW_RECIPES_EXECUTION_TARGET_STEP_NAME: Incomplete
