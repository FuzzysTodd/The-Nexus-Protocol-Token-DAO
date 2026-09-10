from .iterator import Iterator as Iterator
from .utils import array_to_img as array_to_img
from _typeshed import Incomplete

class NumpyArrayIterator(Iterator):
    '''Iterator yielding data from a Numpy array.

    # Arguments
        x: Numpy array of input data or tuple.
            If tuple, the second elements is either
            another numpy array or a list of numpy arrays,
            each of which gets passed
            through as an output without any modifications.
        y: Numpy array of targets data.
        image_data_generator: Instance of `ImageDataGenerator`
            to use for random transformations and normalization.
        batch_size: Integer, size of a batch.
        shuffle: Boolean, whether to shuffle the data between epochs.
        sample_weight: Numpy array of sample weights.
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
        dtype: Dtype to use for the generated arrays.
    '''
    def __new__(cls, *args, **kwargs): ...
    dtype: Incomplete
    x: Incomplete
    x_misc: Incomplete
    y: Incomplete
    sample_weight: Incomplete
    image_data_generator: Incomplete
    data_format: Incomplete
    save_to_dir: Incomplete
    save_prefix: Incomplete
    save_format: Incomplete
    def __init__(self, x, y, image_data_generator, batch_size: int = 32, shuffle: bool = False, sample_weight: Incomplete | None = None, seed: Incomplete | None = None, data_format: str = 'channels_last', save_to_dir: Incomplete | None = None, save_prefix: str = '', save_format: str = 'png', subset: Incomplete | None = None, dtype: str = 'float32') -> None: ...
