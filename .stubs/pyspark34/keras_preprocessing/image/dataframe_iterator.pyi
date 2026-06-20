from .iterator import BatchFromFilesMixin as BatchFromFilesMixin, Iterator as Iterator
from .utils import validate_filename as validate_filename
from _typeshed import Incomplete

class DataFrameIterator(BatchFromFilesMixin, Iterator):
    '''Iterator capable of reading images from a directory on disk
        through a dataframe.

    # Arguments
        dataframe: Pandas dataframe containing the filepaths relative to
            `directory` (or absolute paths if `directory` is None) of the
            images in a string column. It should include other column/s
            depending on the `class_mode`:
            - if `class_mode` is `"categorical"` (default value) it must
                include the `y_col` column with the class/es of each image.
                Values in column can be string/list/tuple if a single class
                or list/tuple if multiple classes.
            - if `class_mode` is `"binary"` or `"sparse"` it must include
                the given `y_col` column with class values as strings.
            - if `class_mode` is `"raw"` or `"multi_output"` it should contain
                the columns specified in `y_col`.
            - if `class_mode` is `"input"` or `None` no extra column is needed.
        directory: string, path to the directory to read images from. If `None`,
            data in `x_col` column should be absolute paths.
        image_data_generator: Instance of `ImageDataGenerator` to use for
            random transformations and normalization. If None, no transformations
            and normalizations are made.
        x_col: string, column in `dataframe` that contains the filenames (or
            absolute paths if `directory` is `None`).
        y_col: string or list, column/s in `dataframe` that has the target data.
        weight_col: string, column in `dataframe` that contains the sample
            weights. Default: `None`.
        target_size: tuple of integers, dimensions to resize input images to.
        color_mode: One of `"rgb"`, `"rgba"`, `"grayscale"`.
            Color mode to read images.
        classes: Optional list of strings, classes to use (e.g. `["dogs", "cats"]`).
            If None, all classes in `y_col` will be used.
        class_mode: one of "binary", "categorical", "input", "multi_output",
            "raw", "sparse" or None. Default: "categorical".
            Mode for yielding the targets:
            - `"binary"`: 1D numpy array of binary labels,
            - `"categorical"`: 2D numpy array of one-hot encoded labels.
                Supports multi-label output.
            - `"input"`: images identical to input images (mainly used to
                work with autoencoders),
            - `"multi_output"`: list with the values of the different columns,
            - `"raw"`: numpy array of values in `y_col` column(s),
            - `"sparse"`: 1D numpy array of integer labels,
            - `None`, no targets are returned (the generator will only yield
                batches of image data, which is useful to use in
                `model.predict_generator()`).
        batch_size: Integer, size of a batch.
        shuffle: Boolean, whether to shuffle the data between epochs.
        seed: Random seed for data shuffling.
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
        dtype: Dtype to use for the generated arrays.
        validate_filenames: Boolean, whether to validate image filenames in
        `x_col`. If `True`, invalid images will be ignored. Disabling this option
        can lead to speed-up in the instantiation of this class. Default: `True`.
    '''
    allowed_class_modes: Incomplete
    def __new__(cls, *args, **kwargs): ...
    directory: Incomplete
    class_mode: Incomplete
    dtype: Incomplete
    class_indices: Incomplete
    classes: Incomplete
    filenames: Incomplete
    samples: Incomplete
    def __init__(self, dataframe, directory: Incomplete | None = None, image_data_generator: Incomplete | None = None, x_col: str = 'filename', y_col: str = 'class', weight_col: Incomplete | None = None, target_size=(256, 256), color_mode: str = 'rgb', classes: Incomplete | None = None, class_mode: str = 'categorical', batch_size: int = 32, shuffle: bool = True, seed: Incomplete | None = None, data_format: str = 'channels_last', save_to_dir: Incomplete | None = None, save_prefix: str = '', save_format: str = 'png', subset: Incomplete | None = None, interpolation: str = 'nearest', dtype: str = 'float32', validate_filenames: bool = True) -> None: ...
    def get_classes(self, df, y_col): ...
    @property
    def filepaths(self): ...
    @property
    def labels(self): ...
    @property
    def sample_weight(self): ...
