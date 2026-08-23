from _typeshed import Incomplete

def gen_perf_dicts(scores, y, is_classification, classes: Incomplete | None = None): ...
def gen_global_selector(n_features, term_names, term_types, unique_val_counts, importance_scores, round: int = 3): ...
def gen_local_selector(data_dicts, round: int = 3, is_classification: bool = True): ...
def gen_name_from_class(obj):
    """Generates a name for a given class.

    Args:
        obj: An object.

    Returns:
        A generated name as a string that uses
        class name and a static counter.
    """
