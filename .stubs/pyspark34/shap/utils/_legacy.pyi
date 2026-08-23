from _typeshed import Incomplete

def kmeans(X, k, round_values: bool = True):
    """ Summarize a dataset with k mean samples weighted by the number of data points they
    each represent.

    Parameters
    ----------
    X : numpy.array or pandas.DataFrame or any scipy.sparse matrix
        Matrix of data samples to summarize (# samples x # features)

    k : int
        Number of means to use for approximation.

    round_values : bool
        For all i, round the ith dimension of each mean sample to match the nearest value
        from X[:,i]. This ensures discrete features always get a valid value.

    Returns
    -------
    DenseData object.
    """

class Instance:
    x: Incomplete
    group_display_values: Incomplete
    def __init__(self, x, group_display_values) -> None: ...

def convert_to_instance(val): ...

class InstanceWithIndex(Instance):
    index_value: Incomplete
    index_name: Incomplete
    column_name: Incomplete
    def __init__(self, x, column_name, index_value, index_name, group_display_values) -> None: ...
    def convert_to_df(self): ...

def convert_to_instance_with_index(val, column_name, index_value, index_name): ...
def match_instance_to_data(instance, data) -> None: ...

class Model:
    f: Incomplete
    out_names: Incomplete
    def __init__(self, f, out_names) -> None: ...

def convert_to_model(val): ...
def match_model_to_data(model, data): ...

class Data:
    def __init__(self) -> None: ...

class SparseData(Data):
    weights: Incomplete
    transposed: bool
    groups: Incomplete
    group_names: Incomplete
    groups_size: Incomplete
    data: Incomplete
    def __init__(self, data, *args) -> None: ...

class DenseData(Data):
    groups: Incomplete
    weights: Incomplete
    transposed: Incomplete
    group_names: Incomplete
    data: Incomplete
    groups_size: Incomplete
    def __init__(self, data, group_names, *args) -> None: ...

class DenseDataWithIndex(DenseData):
    index_value: Incomplete
    index_name: Incomplete
    def __init__(self, data, group_names, index, index_name, *args) -> None: ...
    def convert_to_df(self): ...

def convert_to_data(val, keep_index: bool = False): ...

class Link:
    def __init__(self) -> None: ...

class IdentityLink(Link):
    @staticmethod
    def f(x): ...
    @staticmethod
    def finv(x): ...

class LogitLink(Link):
    @staticmethod
    def f(x): ...
    @staticmethod
    def finv(x): ...

def convert_to_link(val): ...
