from _typeshed import Incomplete
from collections.abc import Generator
from keras.utils import io_utils as io_utils

def split_dataset(dataset, left_size: Incomplete | None = None, right_size: Incomplete | None = None, shuffle: bool = False, seed: Incomplete | None = None):
    """Split a dataset into a left half and a right half (e.g. train / test).

    Args:
        dataset: A `tf.data.Dataset` object, or a list/tuple of arrays with the
          same length.
        left_size: If float (in the range `[0, 1]`), it signifies
          the fraction of the data to pack in the left dataset. If integer, it
          signifies the number of samples to pack in the left dataset. If
          `None`, it defaults to the complement to `right_size`.
        right_size: If float (in the range `[0, 1]`), it signifies
          the fraction of the data to pack in the right dataset. If integer, it
          signifies the number of samples to pack in the right dataset. If
          `None`, it defaults to the complement to `left_size`.
        shuffle: Boolean, whether to shuffle the data before splitting it.
        seed: A random seed for shuffling.

    Returns:
        A tuple of two `tf.data.Dataset` objects: the left and right splits.

    Example:

    >>> data = np.random.random(size=(1000, 4))
    >>> left_ds, right_ds = tf.keras.utils.split_dataset(data, left_size=0.8)
    >>> int(left_ds.cardinality())
    800
    >>> int(right_ds.cardinality())
    200

    """
def is_batched(tf_dataset):
    ''' "Check if the `tf.data.Dataset` is batched.'''
def get_batch_size(tf_dataset):
    """Get the batch size of the dataset."""
def index_directory(directory, labels, formats, class_names: Incomplete | None = None, shuffle: bool = True, seed: Incomplete | None = None, follow_links: bool = False):
    '''Make list of all files in `directory`, with their labels.

    Args:
      directory: Directory where the data is located.
          If `labels` is "inferred", it should contain
          subdirectories, each containing files for a class.
          Otherwise, the directory structure is ignored.
      labels: Either "inferred"
          (labels are generated from the directory structure),
          None (no labels),
          or a list/tuple of integer labels of the same size as the number of
          valid files found in the directory. Labels should be sorted according
          to the alphanumeric order of the image file paths
          (obtained via `os.walk(directory)` in Python).
      formats: Allowlist of file extensions to index (e.g. ".jpg", ".txt").
      class_names: Only valid if "labels" is "inferred". This is the explicit
          list of class names (must match names of subdirectories). Used
          to control the order of the classes
          (otherwise alphanumerical order is used).
      shuffle: Whether to shuffle the data. Default: True.
          If set to False, sorts the data in alphanumeric order.
      seed: Optional random seed for shuffling.
      follow_links: Whether to visits subdirectories pointed to by symlinks.

    Returns:
      tuple (file_paths, labels, class_names).
        file_paths: list of file paths (strings).
        labels: list of matching integer labels (same length as file_paths)
        class_names: names of the classes corresponding to these labels, in
          order.
    '''
def iter_valid_files(directory, follow_links, formats) -> Generator[Incomplete, None, Incomplete]: ...
def index_subdirectory(directory, class_indices, follow_links, formats):
    '''Recursively walks directory and list image paths and their class index.

    Args:
      directory: string, target directory.
      class_indices: dict mapping class names to their index.
      follow_links: boolean, whether to recursively follow subdirectories
        (if False, we only list top-level images in `directory`).
      formats: Allowlist of file extensions to index (e.g. ".jpg", ".txt").

    Returns:
      tuple `(filenames, labels)`. `filenames` is a list of relative file
        paths, and `labels` is a list of integer labels corresponding to these
        files.
    '''
def get_training_or_validation_split(samples, labels, validation_split, subset):
    '''Potentially restict samples & labels to a training or validation split.

    Args:
      samples: List of elements.
      labels: List of corresponding labels.
      validation_split: Float, fraction of data to reserve for validation.
      subset: Subset of the data to return.
        Either "training", "validation", or None. If None, we return all of the
        data.

    Returns:
      tuple (samples, labels), potentially restricted to the specified subset.
    '''
def labels_to_dataset(labels, label_mode, num_classes):
    """Create a tf.data.Dataset from the list/tuple of labels.

    Args:
      labels: list/tuple of labels to be converted into a tf.data.Dataset.
      label_mode: String describing the encoding of `labels`. Options are:
      - 'binary' indicates that the labels (there can be only 2) are encoded as
        `float32` scalars with values 0 or 1 (e.g. for `binary_crossentropy`).
      - 'categorical' means that the labels are mapped into a categorical
        vector.  (e.g. for `categorical_crossentropy` loss).
      num_classes: number of classes of labels.

    Returns:
      A `Dataset` instance.
    """
def check_validation_split_arg(validation_split, subset, shuffle, seed) -> None:
    '''Raise errors in case of invalid argument values.

    Args:
      validation_split: float between 0 and 1, fraction of data to reserve for
        validation.
      subset: One of "training", "validation" or "both". Only used if
        `validation_split` is set.
      shuffle: Whether to shuffle the data. Either True or False.
      seed: random seed for shuffling and transformations.
    '''
