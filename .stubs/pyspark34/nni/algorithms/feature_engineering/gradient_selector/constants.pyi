from _typeshed import Incomplete

class StorageLevel:
    DISK: str
    SPARSE: str
    DENSE: str

class DataFormat:
    SVM: str
    NUMPY: str
    ALL_FORMATS: Incomplete

class Preprocess:
    """
    center the data to mean 0 and create unit variance
    center the data to mean 0
    """
    ZSCORE: str
    CENTER: str

class Device:
    CUDA: str
    CPU: str

class Checkpoint:
    MODEL: str
    OPT: str
    RNG: str

class NanError(ValueError): ...

class Initialization:
    ZERO: str
    ON: str
    OFF: str
    ON_HIGH: str
    OFF_HIGH: str
    SKLEARN: str
    RANDOM: str
    VALUE_DICT: Incomplete

class Coefficients:
    '''"
    coefficients for sublinear estimator were computed running the sublinear
    paper\'s authors\' code
    '''
    SLE: Incomplete

EPSILON: float
