import tensorflow.compat.v2 as tf
from absl.testing import parameterized
from keras.engine import sequential as sequential
from keras.layers.preprocessing import string_lookup as string_lookup
from keras.optimizers.legacy import gradient_descent as gradient_descent
from keras.utils import dataset_creator as dataset_creator

class DatasetCreatorModelFitTestBase(tf.test.TestCase, parameterized.TestCase):
    """The base class for DatasetCreator with Model.fit tests."""
