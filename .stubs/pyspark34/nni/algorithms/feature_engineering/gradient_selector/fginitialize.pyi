from . import constants as constants, syssettings as syssettings
from _typeshed import Incomplete
from torch.utils.data import DataLoader, Dataset

sparsetensor: Incomplete
BYTESPERREAL: float
BYTESPERGB: Incomplete

class PrepareData(Dataset):
    path_data: Incomplete
    disk_size: Incomplete
    format: Incomplete
    classification: Incomplete
    ordinal: Incomplete
    balanced: Incomplete
    MAXMEMGB: Incomplete
    preprocess: Incomplete
    set_params: Incomplete
    verbose: Incomplete
    n_classes: Incomplete
    device: Incomplete
    path_data_stats: Incomplete
    X: Incomplete
    y: Incomplete
    storage_level: Incomplete
    dense_size_gb: Incomplete
    max_rows: Incomplete
    n_to_estimate: Incomplete
    ix_statistics: Incomplete
    n_features: Incomplete
    def __init__(self, path_data: Incomplete | None = None, data_format=..., D: Incomplete | None = None, N: Incomplete | None = None, classification: bool = True, ordinal: bool = False, balanced: bool = True, preprocess: Incomplete | None = None, n_to_estimate: Incomplete | None = None, MAXMEMGB=..., set_params: bool = True, path_mappings: Incomplete | None = None, X: Incomplete | None = None, y: Incomplete | None = None, verbose: int = 0, n_classes: Incomplete | None = None, device=...) -> None:
        '''
        Dataset class with helpful features and functions for being included in a dataloader
        and managing memory usage.
        can read following formats:
            svm:        svm light format (sklearn.datasets.load_svmlight_file)
            numpy:      Pass X and y as numpy or sparse arrays

        assumes
            1. if classification, y is in {-1, 1} or continuous and 0 indexed
            2. y can fit into memory
            3. consecutive calls to __getitem__() have consecutive idx values

        notes:
            1. this implementation is not careful wrt/ precise memory reqts. for
            example, being able to store one dense row in memory is necessary,
            but not sufficient.
            2. for y with 4.2 billion elements, 31.3 GB of memory is  necessary
            @ 8 bytes/scalar. Use partial fit to avoid loading the entire dataset
            at once
            3. disk_size always refer to size of complete data file, even after
            a split().


        Parameters
        ----------
        path_data : str
            Path to load data from
        data_format : str
            File ending for path data.
            "numpy" is the default when passing in X and y
        D : int
            Number of features.
        N : int
            Number of rows.
        classification : bool
            If True, problem is classification, else regression.
        ordinal: bool
            If True, problem is ordinal classification. Requires classification to be True.
        balanced : bool
            If true, each class is weighted equally in optimization, otherwise
            weighted is done via support of each class. Requires classification to be True.
        prerocess : str
            \'zscore\' which refers to centering and normalizing data to unit variance or
            \'center\' which only centers the data to 0 mean
        n_to_estimate : int
            Number of rows of data to estimate
        MAXMEMGB : float
            Maximum allowable size for a minibatch
        set_params : bool
            Whether or not to determine the statistics of the dataset
        path_mappings : str
            Used when streaming from disk
        X : array-like
            Shape = [n_samples, n_features]
            The training input samples.
        y : array-like
            Shape = [n_samples]
            The target values (class labels in classification, real numbers in
            regression).
        verbose : int
            Controls the verbosity when fitting. Set to 0 for no printing
            1 or higher for printing every verbose number of gradient steps.
        device : str
            \'cpu\' to run on CPU and \'cuda\' to run on GPU. Runs much faster on GPU
        n_classes : int
            number of classes
        '''
    def get_dense_size(self): ...
    def set_dense_X(self) -> None: ...
    return_np: Incomplete
    def set_return_np(self, boolean) -> None: ...
    return_raw: Incomplete
    def set_return_raw(self, boolean) -> None: ...
    def save_data_stats(self, path_data_stats) -> None:
        """
        Dumps dataset statistics to pickle file.
        """
    def load_data_stats(self, path_data_stats) -> None: ...
    def reset(self) -> None:
        """
        Resets the dataloader. Only implemented for disk StorageLevel.
        """
    def todense(self): ...
    def split(self, ix): ...
    @staticmethod
    def sparse_std(X, X_mean):
        """
        Calculate the column wise standard deviations of a sparse matrix.
        """
    def compute_data_stats(self):
        """
        1. computes/estimates feature means
        2. if preprocess == 'zscore', computes/estimates feature standard devs
        3. if not classification, computes/estimates target mean/standard dev
        4. estimates largest singular value of data matrix
        """
    Xmn: Incomplete
    sv1: Incomplete
    Xsd: Incomplete
    ymn: Incomplete
    ysd: Incomplete
    def set_data_stats(self, Xmn, sv1, Xsd: float = 1.0, ymn: float = 0.0, ysd: float = 1.0) -> None:
        """
        Saves dataset stats to self to be used for preprocessing.
        """
    def apply_preprocess(self, X, y):
        """
        Faster on gpu device, while dataloading takes up a large portion of the time.
        """
    def max_batch_size(self):
        """
        Return the maximum batchsize for the dataset.
        """
    def apply(self, ix_rows: Incomplete | None = None, ix_cols: Incomplete | None = None, f_Xy: Incomplete | None = None) -> None: ...
    def get_dense_data(self, ix_cols: Incomplete | None = None, ix_rows: Incomplete | None = None): ...
    def __len__(self) -> int: ...
    def getXy(self, idx): ...
    def __getitem__(self, idx): ...

class ChunkDataLoader(DataLoader):
    """
    DataLoader class used to more quickly load a batch of indices at once.
    """
    def __iter__(self): ...

class _ChunkDataLoaderIter:
    """
    DataLoaderIter class used to more quickly load a batch of indices at once.
    """
    iter: Incomplete
    def __init__(self, dataloader) -> None: ...
    def __next__(self): ...
