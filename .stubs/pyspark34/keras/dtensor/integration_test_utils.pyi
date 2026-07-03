from keras import layers as layers, losses as losses, models as models
from keras.datasets import mnist as mnist
from keras.utils import np_utils as np_utils

NUM_CLASS: int

def get_model_with_layout_map(layout_map):
    """Builds a Sequential CNN model to recognize MNIST digits.

    Args:
      layout_map: dict of string name -> Layout, for weights creation.

    Returns:
      a CNN Keras model used for MNIST
    """
def get_all_replicated_layout_map(mesh): ...
def get_mnist_datasets(num_class, batch_size): ...
def train_mnist_model_batch_sharded(model, optimizer, mesh, num_epochs, steps_per_epoch, global_batch_size): ...
def train_step(model, feature, label, loss_obj, optimizer): ...
