from .utils import array_to_img as array_to_img, img_to_array as img_to_array, load_img as load_img
from _typeshed import Incomplete
from keras_preprocessing import get_keras_submodule as get_keras_submodule

IteratorType: Incomplete
IteratorType = object

class Iterator(IteratorType):
    """Base class for image data iterators.

    Every `Iterator` must implement the `_get_batches_of_transformed_samples`
    method.

    # Arguments
        n: Integer, total number of samples in the dataset to loop over.
        batch_size: Integer, size of a batch.
        shuffle: Boolean, whether to shuffle the data between epochs.
        seed: Random seeding for data shuffling.
    """
    white_list_formats: Incomplete
    n: Incomplete
    batch_size: Incomplete
    seed: Incomplete
    shuffle: Incomplete
    batch_index: int
    total_batches_seen: int
    lock: Incomplete
    index_array: Incomplete
    index_generator: Incomplete
    def __init__(self, n, batch_size, shuffle, seed) -> None: ...
    def __getitem__(self, idx): ...
    def __len__(self) -> int: ...
    def on_epoch_end(self) -> None: ...
    def reset(self) -> None: ...
    def __iter__(self): ...
    def __next__(self, *args, **kwargs): ...
    def next(self):
        """For python 2.x.

        # Returns
            The next batch.
        """

class BatchFromFilesMixin:
    """Adds methods related to getting batches from filenames

    It includes the logic to transform image files to batches.
    """
    image_data_generator: Incomplete
    target_size: Incomplete
    color_mode: Incomplete
    data_format: Incomplete
    image_shape: Incomplete
    save_to_dir: Incomplete
    save_prefix: Incomplete
    save_format: Incomplete
    interpolation: Incomplete
    split: Incomplete
    subset: Incomplete
    def set_processing_attrs(self, image_data_generator, target_size, color_mode, data_format, save_to_dir, save_prefix, save_format, subset, interpolation) -> None:
        '''Sets attributes to use later for processing files into a batch.

        # Arguments
            image_data_generator: Instance of `ImageDataGenerator`
                to use for random transformations and normalization.
            target_size: tuple of integers, dimensions to resize input images to.
            color_mode: One of `"rgb"`, `"rgba"`, `"grayscale"`.
                Color mode to read images.
            data_format: String, one of `channels_first`, `channels_last`.
            save_to_dir: Optional directory where to save the pictures
                being yielded, in a viewable format. This is useful
                for visualizing the random transformations being
                applied, for debugging purposes.
            save_prefix: String prefix to use for saving sample
                images (if `save_to_dir` is set).
            save_format: Format to use for saving sample images
                (if `save_to_dir` is set).
            subset: Subset of data (`"training"` or `"validation"`) if
                validation_split is set in ImageDataGenerator.
            interpolation: Interpolation method used to resample the image if the
                target size is different from that of the loaded image.
                Supported methods are "nearest", "bilinear", and "bicubic".
                If PIL version 1.1.3 or newer is installed, "lanczos" is also
                supported. If PIL version 3.4.0 or newer is installed, "box" and
                "hamming" are also supported. By default, "nearest" is used.
        '''
    @property
    def filepaths(self) -> None:
        """List of absolute paths to image files"""
    @property
    def labels(self) -> None:
        """Class labels of every observation"""
    @property
    def sample_weight(self) -> None: ...
