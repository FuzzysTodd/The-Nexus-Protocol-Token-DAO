from .iterator import BatchFromFilesMixin as BatchFromFilesMixin, Iterator as Iterator
from _typeshed import Incomplete

class DirectoryIterator(BatchFromFilesMixin, Iterator):
    '''Iterator capable of reading images from a directory on disk.

    # Arguments
        directory: string, path to the directory to read images from.
            Each subdirectory in this directory will be
            considered to contain images from one class,
            or alternatively you could specify class subdirectories
            via the `classes` argument.
        image_data_generator: Instance of `ImageDataGenerator`
            to use for random transformations and normalization.
        target_size: tuple of integers, dimensions to resize input images to.
        color_mode: One of `"rgb"`, `"rgba"`, `"grayscale"`.
            Color mode to read images.
        classes: Optional list of strings, names of subdirectories
            containing images from each class (e.g. `["dogs", "cats"]`).
            It will be computed automatically if not set.
        class_mode: Mode for yielding the targets:
            `"binary"`: binary targets (if there are only two classes),
            `"categorical"`: categorical targets,
            `"sparse"`: integer targets,
            `"input"`: targets are images identical to input images (mainly
                used to work with autoencoders),
            `None`: no targets get yielded (only input images are yielded).
        batch_size: Integer, size of a batch.
        shuffle: Boolean, whether to shuffle the data between epochs.
            If set to False, sorts the data in alphanumeric order.
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
        follow_links: boolean,follow symbolic links to subdirectories
        subset: Subset of data (`"training"` or `"validation"`) if
            validation_split is set in ImageDataGenerator.
        interpolation: Interpolation method used to resample the image if the
            target size is different from that of the loaded image.
            Supported methods are "nearest", "bilinear", and "bicubic".
            If PIL version 1.1.3 or newer is installed, "lanczos" is also
            supported. If PIL version 3.4.0 or newer is installed, "box" and
            "hamming" are also supported. By default, "nearest" is used.
        dtype: Dtype to use for generated arrays.
    '''
    allowed_class_modes: Incomplete
    def __new__(cls, *args, **kwargs): ...
    directory: Incomplete
    classes: Incomplete
    class_mode: Incomplete
    dtype: Incomplete
    samples: int
    num_classes: Incomplete
    class_indices: Incomplete
    filenames: Incomplete
    def __init__(self, directory, image_data_generator, target_size=(256, 256), color_mode: str = 'rgb', classes: Incomplete | None = None, class_mode: str = 'categorical', batch_size: int = 32, shuffle: bool = True, seed: Incomplete | None = None, data_format: str = 'channels_last', save_to_dir: Incomplete | None = None, save_prefix: str = '', save_format: str = 'png', follow_links: bool = False, subset: Incomplete | None = None, interpolation: str = 'nearest', dtype: str = 'float32') -> None: ...
    @property
    def filepaths(self): ...
    @property
    def labels(self): ...
    @property
    def sample_weight(self) -> None: ...
