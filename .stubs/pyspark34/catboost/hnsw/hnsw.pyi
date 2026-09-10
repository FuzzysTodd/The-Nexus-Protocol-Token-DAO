from _typeshed import Incomplete
from collections.abc import Generator
from enum import IntEnum

def get_so_paths(dir_name): ...
def get_hnsw_bin_module(): ...
def log_fixup() -> Generator[None, None, None]: ...

class EDistance(IntEnum):
    DotProduct: int
    L1: int
    L2Sqr: int

class EVectorComponentType(IntEnum):
    Float: int
    I8: int
    I32: int

HnswException: Incomplete

class Pool:
    """
    Pool is a storage of vectors
    """
    vectors_path: Incomplete
    dtype: Incomplete
    dimension: Incomplete
    def __init__(self, vectors_path, dtype, dimension, vectors_bin_data: Incomplete | None = None) -> None:
        """
        Pool is a storage of vectors. You can create it from row-major binary file or
        binary data of vectors.

        Parameters
        ----------
        vectors_path : string
            Path to binary file with vectors.

        dtype : EVectorComponentType
            Type of vectors.

        dimension : int
            Dimension of vectors.

        vectors_bin_data : bytes
            Binary data of vectors.
        """
    @classmethod
    def from_file(cls, vectors_path, dtype, dimension):
        """
        Create pool from binary file.

        Parameters
        ----------
        vectors_path : string
            Path to binary file with vectors.

        dtype : EVectorComponentType
            Type of vectors.

        dimension : int
            Dimension of vectors.
        """
    @classmethod
    def from_bytes(cls, vectors_bin_data, dtype, dimension):
        """
        Create pool from binary data.

        Parameters
        ----------
        vectors_bin_data : bytes
            Binary data of vectors.

        dtype : EVectorComponentType
            Type of vectors.

        dimension : int
            Dimension of vectors.
        """
    def get_item(self, id):
        """
        Get item from storage by id.

        Parameters
        ----------
        id : int
            Index of item in storage.

        Returns
        -------
        item : numpy.ndarray
        """
    def get_num_items(self):
        """
        Get the number of items in storage.

        Returns
        -------
        num_items : int
        """

def transform_mobius(pool):
    """
    Transform pool for fast dot product search on HNSW graph
    https://papers.nips.cc/paper/9032-mobius-transformation-for-fast-inner-product-search-on-graph.pdf

    Parameters
    ----------
    pool : Pool

    Returns
    -------
    transformed_pool : Pool
    """

class Hnsw:
    """
    Class for building, loading and working with Hierarchical Navigable Small World index.
    """
    def __init__(self) -> None:
        """
        Create object for working with HNSW.
        """
    def build(self, pool, distance, max_neighbors: Incomplete | None = None, search_neighborhood_size: Incomplete | None = None, num_exact_candidates: Incomplete | None = None, batch_size: Incomplete | None = None, upper_level_batch_size: Incomplete | None = None, level_size_decay: Incomplete | None = None, num_threads: Incomplete | None = None, verbose: bool = False, report_progress: bool = True, snapshot_file: Incomplete | None = None, snapshot_interval: Incomplete | None = None) -> None:
        """
        Build index with given options.

        Parameters
        ----------
        pool : Pool
            Pool of vectors for which index will be built.

        distance : EDistance
            Distance that should be used for finding nearest vectors.

        max_neighbors : int (default=32)
            Maximum number of neighbors that every item can be connected with.

        search_neighborhood_size : int (default=300)
            Search neighborhood size for ANN-search.
            Higher values improve search quality in expense of building time.

        num_exact_candidates : int (default=100)
            Number of nearest vectors to take from batch.
            Higher values improve search quality in expense of building time.

        batch_size : int (default=1000)
            Number of items that added to graph on each step of algorithm.

        upper_level_batch_size : int (default=40000)
            Batch size for building upper levels.

        level_size_decay : int (default=max_neighbors/2)
            Base of exponent for decaying level sizes.

        num_threads : int (default=number of CPUs)
            Number of threads for building index.

        report_progress : bool (default=True)
            Print progress of building.

        verbose : bool (default=False)
            Print additional information about time of building.

        snapshot_file : string (default=None)
            Path for saving snapshots during the index building.

        snapshot_interval : int (default=600)
            Interval between saving snapshots (seconds).
            Snapshot is saved after building each level also.
        """
    def save(self, index_path) -> None:
        """
        Save index to file.

        Parameters
        ----------
        index_path : string
            Path to file for saving index.
        """
    def load(self, index_path, pool, distance) -> None:
        """
        Load index from file.

        Parameters
        ----------
        index_path : string
            Path to file for loading index.

        pool : Pool
            Pool of vectors for which index will be loaded.

        distance : EDistance
            Distance that should be used for finding nearest vectors.
        """
    def load_from_bytes(self, index_data, pool, distance) -> None:
        """
        Load index from bytes.

        Parameters
        ----------
        index_data : bytes
            Index binary data.

        pool : Pool
            Pool of vectors for which index will be loaded.

        distance : EDistance
            Distance that should be used for finding nearest vectors.
        """
    def get_nearest(self, query, top_size, search_neighborhood_size, distance_calc_limit: int = 0):
        """
        Get approximate nearest neighbors for query from index.

        Parameters
        ----------
        query : list or numpy.ndarray
            Vector for which nearest neighbors should be found.

        top_size : int
            Required number of neighbors.

        search_neighborhood_size : int
            Search neighborhood size for ANN-search.
            Higher values improve search quality in expense of search time.
            It should be equal or greater than top_size.

        distance_calc_limit : int (default=0)
            Limit of distance calculation.
            To guarantee satisfactory search time at the expense of quality.
            0 is equivalent to no limit.

        Returns
        -------
        neighbors : list of tuples (id, distance)
        """

class HnswEstimator:
    """
    Class for building, loading and working with Hierarchical Navigable Small World index with SciKit-Learn
    Estimator compatible interface.
    Mostly drop-in replacement for sklearn.neighbors.NearestNeighbors (except for some parameters)
    """
    def __init__(self, n_neighbors: int = 5, distance=..., max_neighbors: int = 32, search_neighborhood_size: int = 300, num_exact_candidates: int = 100, batch_size: int = 1000, upper_level_batch_size: int = 40000, level_size_decay: Incomplete | None = None) -> None:
        """
        Parameters
        ----------
        n_neighbors : int, default=5
            Number of neighbors to use by default for kneighbors queries.


        distance : EDistance
            Distance that should be used for finding nearest vectors.

        max_neighbors : int (default=32)
            Maximum number of neighbors that every item can be connected with.

        search_neighborhood_size : int (default=300)
            Search neighborhood size for ANN-search.
            Higher values improve search quality in expense of building time.

        num_exact_candidates : int (default=100)
            Number of nearest vectors to take from batch.
            Higher values improve search quality in expense of building time.

        batch_size : int (default=1000)
            Number of items that added to graph on each step of algorithm.

        upper_level_batch_size : int (default=40000)
            Batch size for building upper levels.

        level_size_decay : int (default=max_neighbors/2)
            Base of exponent for decaying level sizes.
        """
    def fit(self, X, y: Incomplete | None = None, num_threads: Incomplete | None = None, verbose: bool = False, report_progress: bool = True, snapshot_file: Incomplete | None = None, snapshot_interval: int = 600):
        """
        Fit the HNSW model.

        Parameters
        ----------
        X : array-like of shape (n_samples, n_values)

        y: None
            Added to be compatible with Estimator API

        num_threads : int (default=number of CPUs)
            Number of threads for building index.

        report_progress : bool (default=True)
            Print progress of building.

        verbose : bool (default=False)
            Print additional information about time of building.

        snapshot_file : string (default=None)
            Path for saving snapshots during the index building.

        snapshot_interval : int (default=600)
            Interval between saving snapshots (seconds).

        Returns
        -------
        model : HnswEstimator

        """
    def get_params(self, deep: bool = True):
        """
        Get parameters for this estimator.
        """
    def set_params(self, **params):
        """
        Set the parameters of this estimator.

        Parameters
        ----------
        **params : dict
            HnswEstimator parameters.

        Returns
        -------
        self : HnswEstimator instance
        """
    @property
    def effective_metric_(self):
        """
        Returns
        -------
        Distance that should be used for finding nearest vectors.
        """
    @property
    def n_samples_fit_(self):
        """
        Returns
        -------
        Number of samples in the fitted data.
        """
    def kneighbors(self, X: Incomplete | None = None, n_neighbors: Incomplete | None = None, return_distance: bool = True, search_neighborhood_size: Incomplete | None = None, distance_calc_limit: int = 0):
        """Finds the approximate K-neighbors of a point.
        Returns indices of and distances to the neighbors of each point.

        Parameters
        ----------
        X : array-like, shape (n_queries, n_features) or None
            The query point or points.
            If not provided, neighbors of each indexed point are returned.
            In this case, the query point is not considered its own neighbor.
        n_neighbors : int, default=None
            Number of neighbors required for each sample. The default is the
            value passed to the constructor.
        return_distance : bool, default=True
            Whether or not to return the distances.

        search_neighborhood_size : int, default=None
            Search neighborhood size for ANN-search.
            Higher values improve search quality in expense of search time.
            It should be equal or greater than top_size.
            If None set to n_neighbors * 2.

        distance_calc_limit : int (default=0)
            Limit of distance calculation.
            To guarantee satisfactory search time at the expense of quality.
            0 is equivalent to no limit.

        Returns
        -------
        neigh_dist :numpy.ndarray of shape (n_queries, n_neighbors)
            Array representing the lengths to points, only present if
            return_distance=True
        neigh_ind : numpy.ndarray of shape (n_queries, n_neighbors)
            Indices of the nearest points in the population matrix.
        """

class OnlineHnsw:
    """
    Class for building and working with Online Hierarchical Navigable Small World index.
    """
    dtype: Incomplete
    dimension: Incomplete
    def __init__(self, dtype, dimension, distance, max_neighbors: Incomplete | None = None, search_neighborhood_size: Incomplete | None = None, num_vertices: Incomplete | None = None, level_size_decay: Incomplete | None = None) -> None:
        """
        Create object with given options.

        Parameters
        ----------
        dtype : EVectorComponentType
            Type of vectors.
        dimension : int
            Dimension of vectors.
        distance : EDistance
            Distance that should be used for finding nearest vectors.
        max_neighbors : int (default=32)
            Maximum number of neighbors that every item can be connected with.
        search_neighborhood_size : int (default=300)
            Search neighborhood size for ANN-search.
            Higher values improve search quality in expense of building time.
        num_vertices : int (default=0)
            Expected number of vectors in storage.
        level_size_decay : int (default=max_neighbors/2)
            Base of exponent for decaying level sizes.
        """
    def get_nearest_and_add_item(self, query):
        """
        Get approximate nearest neighbors for query from index and add item to index

        Parameters
        ----------
        query : list or numpy.ndarray
            Vector for which nearest neighbors should be found.
            Vector which should be added in index.

        Returns
        -------
        neighbors : list of tuples (id, distance) with length = search_neighborhood_size
        """
    def get_nearest(self, query, top_size: int = 0):
        """
        Get approximate nearest neighbors for query from index.

        Parameters
        ----------
        query : list or numpy.ndarray
            Vector for which nearest neighbors should be found.
        top_size : int
            Required number of neighbors.

        Returns
        -------
        neighbors : list of tuples (id, distance)
        """
    def add_item(self, item) -> None:
        """
        Add item in index.

        Parameters
        ----------
        item : list or numpy.ndarray
            Vector which should be added in index.
        """
    def get_item(self, id):
        """
        Get item from storage by id.

        Parameters
        ----------
        id : int
            Index of item in storage.

        Returns
        -------
        item : numpy.ndarray
        """
    def get_num_items(self):
        """
        Get the number of items in storage.

        Returns
        -------
        num_items : int
        """
