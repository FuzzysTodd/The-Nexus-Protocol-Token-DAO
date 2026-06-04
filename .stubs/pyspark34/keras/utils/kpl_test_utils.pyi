import tensorflow.compat.v2 as tf
from _typeshed import Incomplete
from keras.layers.preprocessing import string_lookup as string_lookup

class DistributeKplTestUtils(tf.test.TestCase):
    """Utils for test of tf.distribute + KPL."""
    FEATURE_VOCAB: Incomplete
    LABEL_VOCAB: Incomplete
    def define_kpls_for_training(self, use_adapt):
        """Function that defines KPL used for unit tests of tf.distribute.

        Args:
          use_adapt: if adapt will be called. False means there will be
            precomputed statistics.

        Returns:
          feature_mapper: a simple keras model with one keras StringLookup layer
          which maps feature to index.
          label_mapper: similar to feature_mapper, but maps label to index.

        """
    def dataset_fn(self, feature_mapper, label_mapper):
        """Function that generates dataset for test of tf.distribute + KPL.

        Args:
          feature_mapper: a simple keras model with one keras StringLookup layer
            which maps feature to index.
          label_mapper: similar to feature_mapper, but maps label to index.

        Returns:
          Generated dataset for test of tf.distribute + KPL.

        """
    def define_model(self):
        """A simple model for test of tf.distribute + KPL."""
    def define_reverse_lookup_layer(self):
        """Create string reverse lookup layer for serving."""
    def create_serving_signature(self, model, feature_mapper, label_inverse_lookup_layer):
        """Create serving signature for the given model."""
    def test_save_load_serving_model(self, model, feature_mapper, label_inverse_lookup_layer) -> None:
        """Test save/load/serving model."""
