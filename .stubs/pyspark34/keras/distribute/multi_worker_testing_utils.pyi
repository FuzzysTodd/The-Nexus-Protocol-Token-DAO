from _typeshed import Incomplete
from keras.optimizers.legacy import gradient_descent as gradient_descent

ASSIGNED_PORTS: Incomplete
lock: Incomplete

def mnist_synthetic_dataset(batch_size, steps_per_epoch, target_values: str = 'constant'):
    """Generate synthetic MNIST dataset for testing."""
def get_mnist_model(input_shape):
    """Define a deterministically-initialized CNN model for MNIST testing."""
def make_parameter_server_cluster(num_workers, num_ps): ...
def pick_unused_port():
    """Returns an unused and unassigned local port."""
def create_in_process_cluster(num_workers, num_ps, has_chief: bool = False, has_eval: bool = False, rpc_layer: str = 'grpc'):
    """Create an in-process cluster that consists of only standard server."""
