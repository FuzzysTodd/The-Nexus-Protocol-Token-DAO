from _typeshed import Incomplete

preprocessing: Incomplete
BATCH_SIZE: int
DS_SIZE: Incomplete
STEPS: Incomplete
VOCAB_SIZE: int

def make_dataset():
    """Make a simple structured dataset.

    The dataset contains three feature columns.
      - float_col: an unnormalized numeric column.
      - int_col: an column of integer IDs.
      - string_col: a column of fixed vocabulary terms.

    Returns:
      The dataset.
    """
def make_preprocessing_model(file_dir):
    """Make a standalone preprocessing model."""
def make_training_model():
    """Make a trainable model for the preprocessed inputs."""
