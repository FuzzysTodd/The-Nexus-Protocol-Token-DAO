import pandas as pd
from _typeshed import Incomplete
from mlflow import pyfunc as pyfunc
from mlflow.models import Model as Model, ModelInputExample as ModelInputExample, ModelSignature as ModelSignature
from mlflow.models.model import MLMODEL_FILE_NAME as MLMODEL_FILE_NAME
from mlflow.tracking._model_registry import DEFAULT_AWAIT_MAX_SLEEP_SECONDS as DEFAULT_AWAIT_MAX_SLEEP_SECONDS
from mlflow.types.schema import ColSpec as ColSpec, DataType as DataType, Schema as Schema
from mlflow.utils.annotations import experimental as experimental
from mlflow.utils.docstring_utils import LOG_MODEL_PARAM_DOCS as LOG_MODEL_PARAM_DOCS, format_docstring as format_docstring
from mlflow.utils.file_utils import write_to as write_to
from typing import Any, Dict, List, NamedTuple

logger: Incomplete
FLAVOR_NAME: str

def get_default_pip_requirements():
    """
    :return: A list of default pip requirements for MLflow Models produced by this flavor.
             Calls to :func:`save_model()` and :func:`log_model()` produce a pip environment
             that, at a minimum, contains these requirements.
    """
def get_default_conda_env():
    """
    :return: The default Conda environment for MLflow Models produced by calls to
             :func:`save_model()` and :func:`log_model()`.
    """

class _SpecialChainInfo(NamedTuple):
    loader_arg: str

def save_model(lc_model, path, conda_env: Incomplete | None = None, code_paths: Incomplete | None = None, mlflow_model: Incomplete | None = None, signature: ModelSignature = None, input_example: ModelInputExample = None, pip_requirements: Incomplete | None = None, extra_pip_requirements: Incomplete | None = None, metadata: Incomplete | None = None, loader_fn: Incomplete | None = None, persist_dir: Incomplete | None = None):
    '''
    Save a LangChain model to a path on the local file system.

    :param lc_model: A LangChain model, which could be a
                     `Chain <https://python.langchain.com/docs/modules/chains/>`_,
                     `Agent <https://python.langchain.com/docs/modules/agents/>`_, or
                     `retriever <https://python.langchain.com/docs/modules/data_connection/retrievers/>`_.
    :param path: Local path where the serialized model (as YAML) is to be saved.
    :param conda_env: {{ conda_env }}
    :param code_paths: A list of local filesystem paths to Python file dependencies (or directories
                       containing file dependencies). These files are *prepended* to the system
                       path when the model is loaded.
    :param mlflow_model: :py:mod:`mlflow.models.Model` this flavor is being added to.
    :param signature: :py:class:`ModelSignature <mlflow.models.ModelSignature>`
                      describes model input and output :py:class:`Schema <mlflow.types.Schema>`.
                      If not specified, the model signature would be set according to
                      `lc_model.input_keys` and `lc_model.output_keys` as columns names, and
                      `DataType.string` as the column type.
                      Alternatively, you can explicitly specify the model signature.
                      The model signature can be :py:func:`inferred <mlflow.models.infer_signature>`
                      from datasets with valid model input (e.g. the training dataset with target
                      column omitted) and valid model output (e.g. model predictions generated on
                      the training dataset), for example:

                      .. code-block:: python

                        from mlflow.models import infer_signature

                        chain = LLMChain(llm=llm, prompt=prompt)
                        prediction = chain.run(input_str)
                        input_columns = [
                            {"type": "string", "name": input_key} for input_key in chain.input_keys
                        ]
                        signature = infer_signature(input_columns, predictions)

    :param input_example: Input example provides one or several instances of valid
                          model input. The example can be used as a hint of what data to feed the
                          model. The given example will be converted to a Pandas DataFrame and then
                          serialized to json using the Pandas split-oriented format. Bytes are
                          base64-encoded.
    :param pip_requirements: {{ pip_requirements }}
    :param extra_pip_requirements: {{ extra_pip_requirements }}
    :param metadata: Custom metadata dictionary passed to the model and stored in the MLmodel file.

                     .. Note:: Experimental: This parameter may change or be removed in a future
                                             release without warning.
    :param loader_fn: A function that\'s required for models containing objects that aren\'t natively
                      serialized by LangChain.
                      This function takes a string `persist_dir` as an argument and returns the
                      specific object that the model needs. Depending on the model,
                      this could be a retriever, vectorstore, requests_wrapper, embeddings, or
                      database. For RetrievalQA Chain and retriever models, the object is a
                      (`retriever <https://python.langchain.com/docs/modules/data_connection/retrievers/>`_).
                      For APIChain models, it\'s a
                      (`requests_wrapper <https://python.langchain.com/docs/modules/agents/tools/integrations/requests>`_).
                      For HypotheticalDocumentEmbedder models, it\'s an
                      (`embeddings <https://python.langchain.com/docs/modules/data_connection/text_embedding/>`_).
                      For SQLDatabaseChain models, it\'s a
                      (`database <https://python.langchain.com/docs/modules/agents/toolkits/sql_database>`_).
    :param persist_dir: The directory where the object is stored. The `loader_fn`
                        takes this string as the argument to load the object.
                        This is optional for models containing objects that aren\'t natively
                        serialized by LangChain. MLflow logs the content in this directory as
                        artifacts in the subdirectory named `persist_dir_data`.

                        Here is the code snippet for logging a RetrievalQA chain with `loader_fn`
                        and `persist_dir`:

                        .. code-block:: python

                            qa = RetrievalQA.from_llm(llm=OpenAI(), retriever=db.as_retriever())


                            def load_retriever(persist_directory):
                                embeddings = OpenAIEmbeddings()
                                vectorstore = FAISS.load_local(persist_directory, embeddings)
                                return vectorstore.as_retriever()


                            with mlflow.start_run() as run:
                                logged_model = mlflow.langchain.log_model(
                                    qa,
                                    artifact_path="retrieval_qa",
                                    loader_fn=load_retriever,
                                    persist_dir=persist_dir,
                                )

                        See a complete example in examples/langchain/retrieval_qa_chain.py.
    '''
def log_model(lc_model, artifact_path, conda_env: Incomplete | None = None, code_paths: Incomplete | None = None, registered_model_name: Incomplete | None = None, signature: ModelSignature = None, input_example: ModelInputExample = None, await_registration_for=..., pip_requirements: Incomplete | None = None, extra_pip_requirements: Incomplete | None = None, metadata: Incomplete | None = None, loader_fn: Incomplete | None = None, persist_dir: Incomplete | None = None):
    '''
    Log a LangChain model as an MLflow artifact for the current run.

    :param lc_model: A LangChain model, which could be a
                     `Chain <https://python.langchain.com/docs/modules/chains/>`_,
                     `Agent <https://python.langchain.com/docs/modules/agents/>`_, or
                     `retriever <https://python.langchain.com/docs/modules/data_connection/retrievers/>`_.
    :param artifact_path: Run-relative artifact path.
    :param conda_env: {{ conda_env }}
    :param code_paths: A list of local filesystem paths to Python file dependencies (or directories
                       containing file dependencies). These files are *prepended* to the system
                       path when the model is loaded.

    :param registered_model_name: This argument may change or be removed in a
                                  future release without warning. If given, create a model
                                  version under ``registered_model_name``, also creating a
                                  registered model if one with the given name does not exist.
    :param signature: :py:class:`ModelSignature <mlflow.models.ModelSignature>`
                      describes model input and output
                      :py:class:`Schema <mlflow.types.Schema>`.
                      If not specified, the model signature would be set according to
                      `lc_model.input_keys` and `lc_model.output_keys` as columns names, and
                      `DataType.string` as the column type.
                      Alternatively, you can explicitly specify the model signature.
                      The model signature can be :py:func:`inferred
                      <mlflow.models.infer_signature>` from datasets with valid model input
                      (e.g. the training dataset with target column omitted) and valid model
                      output (e.g. model predictions generated on the training dataset),
                      for example:

                      .. code-block:: python

                        from mlflow.models import infer_signature

                        chain = LLMChain(llm=llm, prompt=prompt)
                        prediction = chain.run(input_str)
                        input_columns = [
                            {"type": "string", "name": input_key} for input_key in chain.input_keys
                        ]
                        signature = infer_signature(input_columns, predictions)

    :param input_example: Input example provides one or several instances of valid
                          model input. The example can be used as a hint of what data to
                          feed the model. The given example will be converted to a
                          Pandas DataFrame and then serialized to json using the
                          Pandas split-oriented format. Bytes are base64-encoded.

    :param await_registration_for: Number of seconds to wait for the model version
                        to finish being created and is in ``READY`` status.
                        By default, the function waits for five minutes.
                        Specify 0 or None to skip waiting.
    :param pip_requirements: {{ pip_requirements }}
    :param extra_pip_requirements: {{ extra_pip_requirements }}
    :param metadata: Custom metadata dictionary passed to the model and stored in the MLmodel file.

                     .. Note:: Experimental: This parameter may change or be removed in a future
                                             release without warning.
    :param loader_fn: A function that\'s required for models containing objects that aren\'t natively
                      serialized by LangChain.
                      This function takes a string `persist_dir` as an argument and returns the
                      specific object that the model needs. Depending on the model,
                      this could be a retriever, vectorstore, requests_wrapper, embeddings, or
                      database. For RetrievalQA Chain and retriever models, the object is a
                      (`retriever <https://python.langchain.com/docs/modules/data_connection/retrievers/>`_).
                      For APIChain models, it\'s a
                      (`requests_wrapper <https://python.langchain.com/docs/modules/agents/tools/integrations/requests>`_).
                      For HypotheticalDocumentEmbedder models, it\'s an
                      (`embeddings <https://python.langchain.com/docs/modules/data_connection/text_embedding/>`_).
                      For SQLDatabaseChain models, it\'s a
                      (`database <https://python.langchain.com/docs/modules/agents/toolkits/sql_database>`_).
    :param persist_dir: The directory where the object is stored. The `loader_fn`
                        takes this string as the argument to load the object.
                        This is optional for models containing objects that aren\'t natively
                        serialized by LangChain. MLflow logs the content in this directory as
                        artifacts in the subdirectory named `persist_dir_data`.

                        Here is the code snippet for logging a RetrievalQA chain with `loader_fn`
                        and `persist_dir`:

                        .. code-block:: python

                            qa = RetrievalQA.from_llm(llm=OpenAI(), retriever=db.as_retriever())


                            def load_retriever(persist_directory):
                                embeddings = OpenAIEmbeddings()
                                vectorstore = FAISS.load_local(persist_directory, embeddings)
                                return vectorstore.as_retriever()


                            with mlflow.start_run() as run:
                                logged_model = mlflow.langchain.log_model(
                                    qa,
                                    artifact_path="retrieval_qa",
                                    loader_fn=load_retriever,
                                    persist_dir=persist_dir,
                                )

                        See a complete example in examples/langchain/retrieval_qa_chain.py.
    :return: A :py:class:`ModelInfo <mlflow.models.model.ModelInfo>` instance that contains the
             metadata of the logged model.
    '''

class _LangChainModelWrapper:
    lc_model: Incomplete
    def __init__(self, lc_model) -> None: ...
    def predict(self, data: pd.DataFrame | List[str | Dict[str, Any]], params: Dict[str, Any] | None = None) -> List[str]:
        """
        :param data: Model input data.
        :param params: Additional parameters to pass to the model for inference.

                       .. Note:: Experimental: This parameter may change or be removed in a future
                                               release without warning.

        :return: Model predictions.
        """

class _TestLangChainWrapper(_LangChainModelWrapper):
    """
    A wrapper class that should be used for testing purposes only.
    """
    def predict(self, data, params: Dict[str, Any] | None = None):
        """
        :param data: Model input data.
        :param params: Additional parameters to pass to the model for inference.

                       .. Note:: Experimental: This parameter may change or be removed in a future
                                               release without warning.

        :return: Model predictions.
        """

def load_model(model_uri, dst_path: Incomplete | None = None):
    """
    Load a LangChain model from a local file or a run.

    :param model_uri: The location, in URI format, of the MLflow model. For example:

                      - ``/Users/me/path/to/local/model``
                      - ``relative/path/to/local/model``
                      - ``s3://my_bucket/path/to/model``
                      - ``runs:/<mlflow_run_id>/run-relative/path/to/model``

                      For more information about supported URI schemes, see
                      `Referencing Artifacts <https://www.mlflow.org/docs/latest/tracking.html#
                      artifact-locations>`_.
    :param dst_path: The local filesystem path to which to download the model artifact.
                     This directory must already exist. If unspecified, a local output
                     path will be created.

    :return: A LangChain model instance
    """
