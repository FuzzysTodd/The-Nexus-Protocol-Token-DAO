import faiss
import numpy as np
from .arrow_dataset import Dataset as Dataset
from .utils import logging as logging
from _typeshed import Incomplete
from elasticsearch import Elasticsearch
from pathlib import PurePath
from typing import Dict, List, NamedTuple

logger: Incomplete

class MissingIndex(Exception): ...

class SearchResults(NamedTuple):
    scores: List[float]
    indices: List[int]

class BatchedSearchResults(NamedTuple):
    total_scores: List[List[float]]
    total_indices: List[List[int]]

class NearestExamplesResults(NamedTuple):
    scores: List[float]
    examples: dict

class BatchedNearestExamplesResults(NamedTuple):
    total_scores: List[List[float]]
    total_examples: List[dict]

class BaseIndex:
    """Base class for indexing"""
    def search(self, query, k: int = 10, **kwargs) -> SearchResults:
        """
        To implement.
        This method has to return the scores and the indices of the retrieved examples given a certain query.
        """
    def search_batch(self, queries, k: int = 10, **kwargs) -> BatchedSearchResults:
        """Find the nearest examples indices to the query.

        Args:
            queries (`Union[List[str], np.ndarray]`): The queries as a list of strings if `column` is a text index or as a numpy array if `column` is a vector index.
            k (`int`): The number of examples to retrieve per query.

        Ouput:
            total_scores (`List[List[float]`): The retrieval scores of the retrieved examples per query.
            total_indices (`List[List[int]]`): The indices of the retrieved examples per query.
        """
    def save(self, file: str | PurePath):
        """Serialize the index on disk"""
    @classmethod
    def load(cls, file: str | PurePath) -> BaseIndex:
        """Deserialize the index from disk"""

class ElasticSearchIndex(BaseIndex):
    """
    Sparse index using Elasticsearch. It is used to index text and run queries based on BM25 similarity.
    An Elasticsearch server needs to be accessible, and a python client is declared with
    ```
    es_client = Elasticsearch([{'host': 'localhost', 'port': '9200'}])
    ```
    for example.
    """
    es_client: Incomplete
    es_index_name: Incomplete
    es_index_config: Incomplete
    def __init__(self, host: str | None = None, port: int | None = None, es_client: Elasticsearch | None = None, es_index_name: str | None = None, es_index_config: dict | None = None) -> None: ...
    def add_documents(self, documents: List[str] | Dataset, column: str | None = None):
        """
        Add documents to the index.
        If the documents are inside a certain column, you can specify it using the `column` argument.
        """
    def search(self, query: str, k: int = 10, **kwargs) -> SearchResults:
        """Find the nearest examples indices to the query.

        Args:
            query (`str`): The query as a string.
            k (`int`): The number of examples to retrieve.

        Ouput:
            scores (`List[List[float]`): The retrieval scores of the retrieved examples.
            indices (`List[List[int]]`): The indices of the retrieved examples.
        """
    def search_batch(self, queries, k: int = 10, max_workers: int = 10, **kwargs) -> BatchedSearchResults: ...

class FaissIndex(BaseIndex):
    """
    Dense index using Faiss. It is used to index vectors.
    Faiss is a library for efficient similarity search and clustering of dense vectors.
    It contains algorithms that search in sets of vectors of any size, up to ones that possibly do not fit in RAM.
    You can find more information about Faiss here:
    - For index types and the string factory: https://github.com/facebookresearch/faiss/wiki/The-index-factory
    - For GPU settings: https://github.com/facebookresearch/faiss/wiki/Faiss-on-the-GPU
    """
    device: Incomplete
    string_factory: Incomplete
    metric_type: Incomplete
    faiss_index: Incomplete
    def __init__(self, device: int | List[int] | None = None, string_factory: str | None = None, metric_type: int | None = None, custom_index: faiss.Index | None = None) -> None:
        """
        Create a Dense index using Faiss. You can specify `device` if you want to run it on GPU (`device` must be the GPU index).
        You can find more information about Faiss here:
        - For `string factory`: https://github.com/facebookresearch/faiss/wiki/The-index-factory
        """
    def add_vectors(self, vectors: np.array | Dataset, column: str | None = None, batch_size: int = 1000, train_size: int | None = None, faiss_verbose: bool | None = None):
        """
        Add vectors to the index.
        If the arrays are inside a certain column, you can specify it using the `column` argument.
        """
    def search(self, query: np.array, k: int = 10, **kwargs) -> SearchResults:
        """Find the nearest examples indices to the query.

        Args:
            query (`np.array`): The query as a numpy array.
            k (`int`): The number of examples to retrieve.

        Ouput:
            scores (`List[List[float]`): The retrieval scores of the retrieved examples.
            indices (`List[List[int]]`): The indices of the retrieved examples.
        """
    def search_batch(self, queries: np.array, k: int = 10, **kwargs) -> BatchedSearchResults:
        """Find the nearest examples indices to the queries.

        Args:
            queries (`np.array`): The queries as a numpy array.
            k (`int`): The number of examples to retrieve.

        Ouput:
            total_scores (`List[List[float]`): The retrieval scores of the retrieved examples per query.
            total_indices (`List[List[int]]`): The indices of the retrieved examples per query.
        """
    def save(self, file: str | PurePath, storage_options: Dict | None = None):
        """Serialize the FaissIndex on disk"""
    @classmethod
    def load(cls, file: str | PurePath, device: int | List[int] | None = None, storage_options: Dict | None = None) -> FaissIndex:
        """Deserialize the FaissIndex from disk"""

class IndexableMixin:
    """Add indexing features to `datasets.Dataset`"""
    def __init__(self) -> None: ...
    def __len__(self) -> int: ...
    def __getitem__(self, key) -> None: ...
    def is_index_initialized(self, index_name: str) -> bool: ...
    def list_indexes(self) -> List[str]:
        """List the `colindex_nameumns`/identifiers of all the attached indexes."""
    def get_index(self, index_name: str) -> BaseIndex:
        """List the `index_name`/identifiers of all the attached indexes.

        Args:
            index_name (`str`): Index name.

        Returns:
            [`BaseIndex`]
        """
    def add_faiss_index(self, column: str, index_name: str | None = None, device: int | List[int] | None = None, string_factory: str | None = None, metric_type: int | None = None, custom_index: faiss.Index | None = None, batch_size: int = 1000, train_size: int | None = None, faiss_verbose: bool = False):
        '''Add a dense index using Faiss for fast retrieval.
        The index is created using the vectors of the specified column.
        You can specify `device` if you want to run it on GPU (`device` must be the GPU index, see more below).
        You can find more information about Faiss here:
        - For `string factory`: https://github.com/facebookresearch/faiss/wiki/The-index-factory

        Args:
            column (`str`): The column of the vectors to add to the index.
            index_name (Optional `str`): The index_name/identifier of the index. This is the index_name that is used to call `.get_nearest` or `.search`.
                By default it corresponds to `column`.
            device (Optional `Union[int, List[int]]`): If positive integer, this is the index of the GPU to use. If negative integer, use all GPUs.
                If a list of positive integers is passed in, run only on those GPUs. By default it uses the CPU.
            string_factory (Optional `str`): This is passed to the index factory of Faiss to create the index. Default index class is IndexFlatIP.
            metric_type (Optional `int`): Type of metric. Ex: `faiss.METRIC_INNER_PRODUCT` or `faiss.METRIC_L2`.
            custom_index (Optional `faiss.Index`): Custom Faiss index that you already have instantiated and configured for your needs.
            batch_size (Optional `int`): Size of the batch to use while adding vectors to the FaissIndex. Default value is 1000.
                <Added version="2.4.0"/>
            train_size (Optional `int`): If the index needs a training step, specifies how many vectors will be used to train the index.
            faiss_verbose (`bool`, defaults to False): Enable the verbosity of the Faiss index.
        '''
    def add_faiss_index_from_external_arrays(self, external_arrays: np.array, index_name: str, device: int | List[int] | None = None, string_factory: str | None = None, metric_type: int | None = None, custom_index: faiss.Index | None = None, batch_size: int = 1000, train_size: int | None = None, faiss_verbose: bool = False):
        '''Add a dense index using Faiss for fast retrieval.
        The index is created using the vectors of `external_arrays`.
        You can specify `device` if you want to run it on GPU (`device` must be the GPU index).
        You can find more information about Faiss here:
        - For `string factory`: https://github.com/facebookresearch/faiss/wiki/The-index-factory

        Args:
            external_arrays (`np.array`): If you want to use arrays from outside the lib for the index, you can set `external_arrays`.
                It will use `external_arrays` to create the Faiss index instead of the arrays in the given `column`.
            index_name (`str`): The index_name/identifier of the index. This is the index_name that is used to call `.get_nearest` or `.search`.
            device (Optional `Union[int, List[int]]`): If positive integer, this is the index of the GPU to use. If negative integer, use all GPUs.
                If a list of positive integers is passed in, run only on those GPUs. By default it uses the CPU.
            string_factory (Optional `str`): This is passed to the index factory of Faiss to create the index. Default index class is IndexFlatIP.
            metric_type (Optional `int`): Type of metric. Ex: `faiss.METRIC_INNER_PRODUCT` or `faiss.METRIC_L2`.
            custom_index (Optional `faiss.Index`): Custom Faiss index that you already have instantiated and configured for your needs.
            batch_size (Optional `int`): Size of the batch to use while adding vectors to the FaissIndex. Default value is 1000.
                <Added version="2.4.0"/>
            train_size (Optional `int`): If the index needs a training step, specifies how many vectors will be used to train the index.
            faiss_verbose (`bool`, defaults to False): Enable the verbosity of the Faiss index.
        '''
    def save_faiss_index(self, index_name: str, file: str | PurePath, storage_options: Dict | None = None):
        '''Save a FaissIndex on disk.

        Args:
            index_name (`str`): The index_name/identifier of the index. This is the index_name that is used to call `.get_nearest` or `.search`.
            file (`str`): The path to the serialized faiss index on disk or remote URI (e.g. `"s3://my-bucket/index.faiss"`).
            storage_options (`dict`, *optional*):
                Key/value pairs to be passed on to the file-system backend, if any.

                <Added version="2.11.0"/>

        '''
    def load_faiss_index(self, index_name: str, file: str | PurePath, device: int | List[int] | None = None, storage_options: Dict | None = None):
        '''Load a FaissIndex from disk.

        If you want to do additional configurations, you can have access to the faiss index object by doing
        `.get_index(index_name).faiss_index` to make it fit your needs.

        Args:
            index_name (`str`): The index_name/identifier of the index. This is the index_name that is used to
                call `.get_nearest` or `.search`.
            file (`str`): The path to the serialized faiss index on disk or remote URI (e.g. `"s3://my-bucket/index.faiss"`).
            device (Optional `Union[int, List[int]]`): If positive integer, this is the index of the GPU to use. If negative integer, use all GPUs.
                If a list of positive integers is passed in, run only on those GPUs. By default it uses the CPU.
            storage_options (`dict`, *optional*):
                Key/value pairs to be passed on to the file-system backend, if any.

                <Added version="2.11.0"/>

        '''
    def add_elasticsearch_index(self, column: str, index_name: str | None = None, host: str | None = None, port: int | None = None, es_client: Elasticsearch | None = None, es_index_name: str | None = None, es_index_config: dict | None = None):
        '''Add a text index using ElasticSearch for fast retrieval.

        Args:
            column (`str`): The column of the documents to add to the index.
            index_name (Optional `str`): The index_name/identifier of the index. This is the index name that is used to call `.get_nearest` or `.search`.
                By default it corresponds to `column`.
            host (Optional `str`, defaults to localhost):
                host of where ElasticSearch is running
            port (Optional `str`, defaults to 9200):
                port of where ElasticSearch is running
            es_client (Optional `elasticsearch.Elasticsearch`):
                The elasticsearch client used to create the index if host and port are None.
            es_index_name (Optional `str`): The elasticsearch index name used to create the index.
            es_index_config (Optional `dict`):
                The configuration of the elasticsearch index.
                Default config is:

        Config::

            {
                "settings": {
                    "number_of_shards": 1,
                    "analysis": {"analyzer": {"stop_standard": {"type": "standard", " stopwords": "_english_"}}},
                },
                "mappings": {
                    "properties": {
                        "text": {
                            "type": "text",
                            "analyzer": "standard",
                            "similarity": "BM25"
                        },
                    }
                },
            }
        '''
    def load_elasticsearch_index(self, index_name: str, es_index_name: str, host: str | None = None, port: int | None = None, es_client: Elasticsearch | None = None, es_index_config: dict | None = None):
        '''Load an existing text index using ElasticSearch for fast retrieval.

        Args:
            index_name (`str`):
                The `index_name`/identifier of the index. This is the index name that is used to call `get_nearest` or `search`.
            es_index_name (`str`):
                The name of elasticsearch index to load.
            host (`str`, *optional*, defaults to `localhost`):
                Host of where ElasticSearch is running.
            port (`str`, *optional*, defaults to `9200`):
                Port of where ElasticSearch is running.
            es_client (`elasticsearch.Elasticsearch`, *optional*):
                The elasticsearch client used to create the index if host and port are `None`.
            es_index_config (`dict`, *optional*):
                The configuration of the elasticsearch index.
                Default config is:
                    ```
                    {
                        "settings": {
                            "number_of_shards": 1,
                            "analysis": {"analyzer": {"stop_standard": {"type": "standard", " stopwords": "_english_"}}},
                        },
                        "mappings": {
                            "properties": {
                                "text": {
                                    "type": "text",
                                    "analyzer": "standard",
                                    "similarity": "BM25"
                                },
                            }
                        },
                    }
                    ```
        '''
    def drop_index(self, index_name: str):
        """Drop the index with the specified column.

        Args:
            index_name (`str`):
                The `index_name`/identifier of the index.
        """
    def search(self, index_name: str, query: str | np.array, k: int = 10, **kwargs) -> SearchResults:
        """Find the nearest examples indices in the dataset to the query.

        Args:
            index_name (`str`):
                The name/identifier of the index.
            query (`Union[str, np.ndarray]`):
                The query as a string if `index_name` is a text index or as a numpy array if `index_name` is a vector index.
            k (`int`):
                The number of examples to retrieve.

        Returns:
            `(scores, indices)`:
                A tuple of `(scores, indices)` where:
                - **scores** (`List[List[float]`): the retrieval scores from either FAISS (`IndexFlatL2` by default) or ElasticSearch of the retrieved examples
                - **indices** (`List[List[int]]`): the indices of the retrieved examples
        """
    def search_batch(self, index_name: str, queries: List[str] | np.array, k: int = 10, **kwargs) -> BatchedSearchResults:
        """Find the nearest examples indices in the dataset to the query.

        Args:
            index_name (`str`):
                The `index_name`/identifier of the index.
            queries (`Union[List[str], np.ndarray]`):
                The queries as a list of strings if `index_name` is a text index or as a numpy array if `index_name` is a vector index.
            k (`int`):
                The number of examples to retrieve per query.

        Returns:
            `(total_scores, total_indices)`:
                A tuple of `(total_scores, total_indices)` where:
                - **total_scores** (`List[List[float]`): the retrieval scores from either FAISS (`IndexFlatL2` by default) or ElasticSearch of the retrieved examples per query
                - **total_indices** (`List[List[int]]`): the indices of the retrieved examples per query
        """
    def get_nearest_examples(self, index_name: str, query: str | np.array, k: int = 10, **kwargs) -> NearestExamplesResults:
        """Find the nearest examples in the dataset to the query.

        Args:
            index_name (`str`):
                The index_name/identifier of the index.
            query (`Union[str, np.ndarray]`):
                The query as a string if `index_name` is a text index or as a numpy array if `index_name` is a vector index.
            k (`int`):
                The number of examples to retrieve.

        Returns:
            `(scores, examples)`:
                A tuple of `(scores, examples)` where:
                - **scores** (`List[float]`): the retrieval scores from either FAISS (`IndexFlatL2` by default) or ElasticSearch of the retrieved examples
                - **examples** (`dict`): the retrieved examples
        """
    def get_nearest_examples_batch(self, index_name: str, queries: List[str] | np.array, k: int = 10, **kwargs) -> BatchedNearestExamplesResults:
        """Find the nearest examples in the dataset to the query.

        Args:
            index_name (`str`):
                The `index_name`/identifier of the index.
            queries (`Union[List[str], np.ndarray]`):
                The queries as a list of strings if `index_name` is a text index or as a numpy array if `index_name` is a vector index.
            k (`int`):
                The number of examples to retrieve per query.

        Returns:
            `(total_scores, total_examples)`:
                A tuple of `(total_scores, total_examples)` where:
                - **total_scores** (`List[List[float]`): the retrieval scores from either FAISS (`IndexFlatL2` by default) or ElasticSearch of the retrieved examples per query
                - **total_examples** (`List[dict]`): the retrieved examples per query
        """
