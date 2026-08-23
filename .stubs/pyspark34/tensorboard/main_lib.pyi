from tensorboard.compat import tf as tf

def global_init() -> None:
    """Modifies the global environment for running TensorBoard as main.

    This functions changes global state in the Python process, so it should
    not be called from library routines.
    """
