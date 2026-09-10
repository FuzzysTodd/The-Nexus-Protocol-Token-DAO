import tensorflow.compat.v2 as tf
from absl.testing import parameterized

class DTensorBaseTest(tf.test.TestCase, parameterized.TestCase):
    """Provides comparison helper for dtensor vs local results."""
    @classmethod
    def setUpClass(cls) -> None: ...
    def tearDown(self) -> None: ...
    @staticmethod
    def configTestMesh(device_type_mesh_map):
        """Configs corresponding mesh given test context.

        If runs on a CPU mesh, set virtual device on CPU.
        If runs on a GPU mesh, sets virtual device on GPU with proper memory
        limits.
        if runs on a TPU mesh, initializes TPU system.

        Args:
          device_type_mesh_map: A dictionary containing device_type -> mesh
            mapping.

        Returns:
          A properly configured mesh for use in test.
        """

def create_device_array(shape, device_type): ...
def create_device_list(shape, device_type): ...
def create_device_ids_array(shape): ...
def reset_context() -> None: ...
def reset_logical_devices(device_type, count) -> None:
    """Resets logical devices for CPU/GPU.

    Logical devices can only be instantiated once on a particular context. For
    now, context re-use is triggering some function duplication errors, so we
    reset the context on each call.

    Args:
      device_type: The device_type to reset.
      count: numbers of virtual device to reset to.
    """
def reset_dtensor() -> None: ...
