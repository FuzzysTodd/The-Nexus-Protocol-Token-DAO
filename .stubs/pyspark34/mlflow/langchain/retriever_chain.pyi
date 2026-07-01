from _typeshed import Incomplete
from langchain.callbacks.manager import AsyncCallbackManagerForChainRun as AsyncCallbackManagerForChainRun, CallbackManagerForChainRun as CallbackManagerForChainRun
from langchain.chains.base import Chain
from langchain.schema import BaseRetriever as BaseRetriever, Document as Document
from mlflow.utils.annotations import experimental as experimental
from pathlib import Path
from typing import Any, List

class _RetrieverChain(Chain):
    """
    Chain that wraps a retriever for use with MLflow.

    The MLflow ``langchain`` flavor provides the functionality to log a retriever object and
    evaluate it individually. This is useful if you want to evaluate the quality of the
    relevant documents returned by a retriever object without directing these documents
    through a large language model (LLM) to yield a summarized response.

    In order to log the retriever object in the ``langchain`` flavor, the retriever object
    needs to be wrapped within a ``_RetrieverChain``.

    See :ref:`log-retriever-chain` for how to log the ``_RetrieverChain``.

    :param retriever: The retriever to wrap.
    """
    input_key: str
    output_key: str
    retriever: BaseRetriever
    class Config:
        """Configuration for this pydantic object."""
        extra: Incomplete
        arbitrary_types_allowed: bool
    @property
    def input_keys(self) -> List[str]:
        """Return the input keys."""
    @property
    def output_keys(self) -> List[str]:
        """Return the output keys."""
    @classmethod
    def load(cls, file: str | Path, **kwargs: Any) -> _RetrieverChain:
        """Load a _RetrieverChain from a file."""
