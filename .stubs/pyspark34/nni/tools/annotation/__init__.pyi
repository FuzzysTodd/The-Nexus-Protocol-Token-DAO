from _typeshed import Incomplete

__all__ = ['generate_search_space', 'expand_annotations']

def generate_search_space(code_dir):
    """Generate search space from Python source code.
    Return a serializable search space object.
    code_dir: directory path of source files (str)
    """
def expand_annotations(src_dir, dst_dir, exp_id: str = '', trial_id: str = '', nas_mode: Incomplete | None = None):
    """Expand annotations in user code.
    Return dst_dir if annotation detected; return src_dir if not.
    src_dir: directory path of user code (str)
    dst_dir: directory to place generated files (str)
    nas_mode: the mode of NAS given that NAS interface is used
    """
