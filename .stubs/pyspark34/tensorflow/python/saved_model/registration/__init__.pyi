from _typeshed import Incomplete
from tensorflow.python.saved_model.registration.registration import RegisteredSaver as RegisteredSaver, get_registered_class as get_registered_class, get_registered_class_name as get_registered_class_name, get_registered_saver_name as get_registered_saver_name, get_restore_function as get_restore_function, get_save_function as get_save_function, get_strict_predicate_restore as get_strict_predicate_restore, register_checkpoint_saver as register_checkpoint_saver, register_serializable as register_serializable, validate_restore_function as validate_restore_function

def register_tf_serializable(name: Incomplete | None = None, predicate: Incomplete | None = None):
    """See the docstring for `register_serializable`."""
def register_tf_checkpoint_saver(name: Incomplete | None = None, predicate: Incomplete | None = None, save_fn: Incomplete | None = None, restore_fn: Incomplete | None = None, strict_predicate_restore: bool = True):
    """See the docstring for `register_checkpoint_saver`."""
