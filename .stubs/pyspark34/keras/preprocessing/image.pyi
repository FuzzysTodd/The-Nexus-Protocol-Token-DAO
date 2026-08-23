from _typeshed import Incomplete
from keras import backend as backend
from keras.utils import data_utils as data_utils, image_utils as image_utils, io_utils as io_utils
from scipy import linalg as linalg

class Iterator(data_utils.Sequence):
    """Base class for image data iterators.

    Deprecated: `tf.keras.preprocessing.image.Iterator` is not recommended for
    new code. Prefer loading images with
    `tf.keras.utils.image_dataset_from_directory` and transforming the output
    `tf.data.Dataset` with preprocessing layers. For more information, see the
    tutorials for [loading images](
    https://www.tensorflow.org/tutorials/load_data/images) and
    [augmenting images](
    https://www.tensorflow.org/tutorials/images/data_augmentation), as well as
    the [preprocessing layer guide](
    https://www.tensorflow.org/guide/keras/preprocessing_layers).

    Every `Iterator` must implement the `_get_batches_of_transformed_samples`
    method.

    Args:
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

        Returns:
            The next batch.
        """

class BatchFromFilesMixin:
    """Adds methods related to getting batches from filenames.

    It includes the logic to transform image files to batches.
    """
    image_data_generator: Incomplete
    target_size: Incomplete
    keep_aspect_ratio: Incomplete
    color_mode: Incomplete
    data_format: Incomplete
    image_shape: Incomplete
    save_to_dir: Incomplete
    save_prefix: Incomplete
    save_format: Incomplete
    interpolation: Incomplete
    split: Incomplete
    subset: Incomplete
    def set_processing_attrs(self, image_data_generator, target_size, color_mode, data_format, save_to_dir, save_prefix, save_format, subset, interpolation, keep_aspect_ratio) -> None:
        '''Sets attributes to use later for processing files into a batch.

        Args:
            image_data_generator: Instance of `ImageDataGenerator`
                to use for random transformations and normalization.
            target_size: tuple of integers, dimensions to resize input images
            to.
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
            interpolation: Interpolation method used to resample the image if
                the target size is different from that of the loaded image.
                Supported methods are "nearest", "bilinear", and "bicubic". If
                PIL version 1.1.3 or newer is installed, "lanczos" is also
                supported. If PIL version 3.4.0 or newer is installed, "box" and
                "hamming" are also supported. By default, "nearest" is used.
            keep_aspect_ratio: Boolean, whether to resize images to a target
                size without aspect ratio distortion. The image is cropped in
                the center with target aspect ratio before resizing.
        '''
    @property
    def filepaths(self) -> None:
        """List of absolute paths to image files."""
    @property
    def labels(self) -> None:
        """Class labels of every observation."""
    @property
    def sample_weight(self) -> None: ...

class DirectoryIterator(BatchFromFilesMixin, Iterator):
    '''Iterator capable of reading images from a directory on disk.

    Deprecated: `tf.keras.preprocessing.image.DirectoryIterator` is not
    recommended for new code. Prefer loading images with
    `tf.keras.utils.image_dataset_from_directory` and transforming the output
    `tf.data.Dataset` with preprocessing layers. For more information, see the
    tutorials for [loading images](
    https://www.tensorflow.org/tutorials/load_data/images) and
    [augmenting images](
    https://www.tensorflow.org/tutorials/images/data_augmentation), as well as
    the [preprocessing layer guide](
    https://www.tensorflow.org/guide/keras/preprocessing_layers).

    Args:
        directory: Path to the directory to read images from. Each subdirectory
          in this directory will be considered to contain images from one class,
          or alternatively you could specify class subdirectories via the
          `classes` argument.
        image_data_generator: Instance of `ImageDataGenerator` to use for random
          transformations and normalization.
        target_size: tuple of integers, dimensions to resize input images to.
        color_mode: One of `"rgb"`, `"rgba"`, `"grayscale"`. Color mode to read
          images.
        classes: Optional list of strings, names of subdirectories containing
          images from each class (e.g. `["dogs", "cats"]`). It will be computed
          automatically if not set.
        class_mode: Mode for yielding the targets:
            - `"binary"`: binary targets (if there are only two classes),
            - `"categorical"`: categorical targets,
            - `"sparse"`: integer targets,
            - `"input"`: targets are images identical to input images (mainly
              used to work with autoencoders),
            - `None`: no targets get yielded (only input images are yielded).
        batch_size: Integer, size of a batch.
        shuffle: Boolean, whether to shuffle the data between epochs.
        seed: Random seed for data shuffling.
        data_format: String, one of `channels_first`, `channels_last`.
        save_to_dir: Optional directory where to save the pictures being
          yielded, in a viewable format. This is useful for visualizing the
          random transformations being applied, for debugging purposes.
        save_prefix: String prefix to use for saving sample images (if
          `save_to_dir` is set).
        save_format: Format to use for saving sample images (if `save_to_dir` is
          set).
        subset: Subset of data (`"training"` or `"validation"`) if
          validation_split is set in ImageDataGenerator.
        interpolation: Interpolation method used to resample the image if the
          target size is different from that of the loaded image. Supported
          methods are "nearest", "bilinear", and "bicubic". If PIL version 1.1.3
          or newer is installed, "lanczos" is also supported. If PIL version
          3.4.0 or newer is installed, "box" and "hamming" are also supported.
          By default, "nearest" is used.
        keep_aspect_ratio: Boolean, whether to resize images to a target size
            without aspect ratio distortion. The image is cropped in the center
            with target aspect ratio before resizing.
        dtype: Dtype to use for generated arrays.
    '''
    allowed_class_modes: Incomplete
    directory: Incomplete
    classes: Incomplete
    class_mode: Incomplete
    dtype: Incomplete
    samples: int
    num_classes: Incomplete
    class_indices: Incomplete
    filenames: Incomplete
    def __init__(self, directory, image_data_generator, target_size=(256, 256), color_mode: str = 'rgb', classes: Incomplete | None = None, class_mode: str = 'categorical', batch_size: int = 32, shuffle: bool = True, seed: Incomplete | None = None, data_format: Incomplete | None = None, save_to_dir: Incomplete | None = None, save_prefix: str = '', save_format: str = 'png', follow_links: bool = False, subset: Incomplete | None = None, interpolation: str = 'nearest', keep_aspect_ratio: bool = False, dtype: Incomplete | None = None) -> None: ...
    @property
    def filepaths(self): ...
    @property
    def labels(self): ...
    @property
    def sample_weight(self) -> None: ...

class NumpyArrayIterator(Iterator):
    '''Iterator yielding data from a Numpy array.

    Deprecated: `tf.keras.preprocessing.image.NumpyArrayIterator` is not
    recommended for new code. Prefer loading images with
    `tf.keras.utils.image_dataset_from_directory` and transforming the output
    `tf.data.Dataset` with preprocessing layers. For more information, see the
    tutorials for [loading images](
    https://www.tensorflow.org/tutorials/load_data/images) and
    [augmenting images](
    https://www.tensorflow.org/tutorials/images/data_augmentation), as well as
    the [preprocessing layer guide](
    https://www.tensorflow.org/guide/keras/preprocessing_layers).

    Args:
        x: Numpy array of input data or tuple. If tuple, the second elements is
          either another numpy array or a list of numpy arrays, each of which
          gets passed through as an output without any modifications.
        y: Numpy array of targets data.
        image_data_generator: Instance of `ImageDataGenerator` to use for random
          transformations and normalization.
        batch_size: Integer, size of a batch.
        shuffle: Boolean, whether to shuffle the data between epochs.
        sample_weight: Numpy array of sample weights.
        seed: Random seed for data shuffling.
        data_format: String, one of `channels_first`, `channels_last`.
        save_to_dir: Optional directory where to save the pictures being
          yielded, in a viewable format. This is useful for visualizing the
          random transformations being applied, for debugging purposes.
        save_prefix: String prefix to use for saving sample images (if
          `save_to_dir` is set).
        save_format: Format to use for saving sample images (if `save_to_dir` is
          set).
        subset: Subset of data (`"training"` or `"validation"`) if
          validation_split is set in ImageDataGenerator.
        ignore_class_split: Boolean (default: False), ignore difference
          in number of classes in labels across train and validation
          split (useful for non-classification tasks)
        dtype: Dtype to use for the generated arrays.
    '''
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
    def __init__(self, x, y, image_data_generator, batch_size: int = 32, shuffle: bool = False, sample_weight: Incomplete | None = None, seed: Incomplete | None = None, data_format: Incomplete | None = None, save_to_dir: Incomplete | None = None, save_prefix: str = '', save_format: str = 'png', subset: Incomplete | None = None, ignore_class_split: bool = False, dtype: Incomplete | None = None) -> None: ...

def validate_filename(filename, white_list_formats):
    """Check if a filename refers to a valid file.

    Args:
        filename: String, absolute path to a file
        white_list_formats: Set, allowed file extensions
    Returns:
        A boolean value indicating if the filename is valid or not
    """

class DataFrameIterator(BatchFromFilesMixin, Iterator):
    '''Iterator capable of reading images from a directory as a dataframe.

    Args:
        dataframe: Pandas dataframe containing the filepaths relative to
          `directory` (or absolute paths if `directory` is None) of the images
          in a string column. It should include other column/s depending on the
          `class_mode`: - if `class_mode` is `"categorical"` (default value) it
          must include the `y_col` column with the class/es of each image.
          Values in column can be string/list/tuple if a single class or
          list/tuple if multiple classes.
            - if `class_mode` is `"binary"` or `"sparse"` it must include the
              given `y_col` column with class values as strings.
            - if `class_mode` is `"raw"` or `"multi_output"` it should contain
              the columns specified in `y_col`.
            - if `class_mode` is `"input"` or `None` no extra column is needed.
        directory: string, path to the directory to read images from. If `None`,
          data in `x_col` column should be absolute paths.
        image_data_generator: Instance of `ImageDataGenerator` to use for random
          transformations and normalization. If None, no transformations and
          normalizations are made.
        x_col: string, column in `dataframe` that contains the filenames (or
          absolute paths if `directory` is `None`).
        y_col: string or list, column/s in `dataframe` that has the target data.
        weight_col: string, column in `dataframe` that contains the sample
            weights. Default: `None`.
        target_size: tuple of integers, dimensions to resize input images to.
        color_mode: One of `"rgb"`, `"rgba"`, `"grayscale"`. Color mode to read
          images.
        classes: Optional list of strings, classes to use (e.g. `["dogs",
          "cats"]`). If None, all classes in `y_col` will be used.
        class_mode: one of "binary", "categorical", "input", "multi_output",
          "raw", "sparse" or None. Default: "categorical".
          Mode for yielding the targets:
            - `"binary"`: 1D numpy array of binary labels,
            - `"categorical"`: 2D numpy array of one-hot encoded labels.
              Supports multi-label output.
            - `"input"`: images identical to input images (mainly used to work
              with autoencoders),
            - `"multi_output"`: list with the values of the different columns,
            - `"raw"`: numpy array of values in `y_col` column(s),
            - `"sparse"`: 1D numpy array of integer labels, - `None`, no targets
              are returned (the generator will only yield batches of image data,
              which is useful to use in `model.predict()`).
        batch_size: Integer, size of a batch.
        shuffle: Boolean, whether to shuffle the data between epochs.
        seed: Random seed for data shuffling.
        data_format: String, one of `channels_first`, `channels_last`.
        save_to_dir: Optional directory where to save the pictures being
          yielded, in a viewable format. This is useful for visualizing the
          random transformations being applied, for debugging purposes.
        save_prefix: String prefix to use for saving sample images (if
          `save_to_dir` is set).
        save_format: Format to use for saving sample images (if `save_to_dir` is
          set).
        subset: Subset of data (`"training"` or `"validation"`) if
          validation_split is set in ImageDataGenerator.
        interpolation: Interpolation method used to resample the image if the
          target size is different from that of the loaded image. Supported
          methods are "nearest", "bilinear", and "bicubic". If PIL version 1.1.3
          or newer is installed, "lanczos" is also supported. If PIL version
          3.4.0 or newer is installed, "box" and "hamming" are also supported.
          By default, "nearest" is used.
        keep_aspect_ratio: Boolean, whether to resize images to a target size
          without aspect ratio distortion. The image is cropped in the center
          with target aspect ratio before resizing.
        dtype: Dtype to use for the generated arrays.
        validate_filenames: Boolean, whether to validate image filenames in
          `x_col`. If `True`, invalid images will be ignored. Disabling this
          option can lead to speed-up in the instantiation of this class.
          Default: `True`.
    '''
    allowed_class_modes: Incomplete
    directory: Incomplete
    class_mode: Incomplete
    dtype: Incomplete
    class_indices: Incomplete
    classes: Incomplete
    filenames: Incomplete
    samples: Incomplete
    def __init__(self, dataframe, directory: Incomplete | None = None, image_data_generator: Incomplete | None = None, x_col: str = 'filename', y_col: str = 'class', weight_col: Incomplete | None = None, target_size=(256, 256), color_mode: str = 'rgb', classes: Incomplete | None = None, class_mode: str = 'categorical', batch_size: int = 32, shuffle: bool = True, seed: Incomplete | None = None, data_format: str = 'channels_last', save_to_dir: Incomplete | None = None, save_prefix: str = '', save_format: str = 'png', subset: Incomplete | None = None, interpolation: str = 'nearest', keep_aspect_ratio: bool = False, dtype: str = 'float32', validate_filenames: bool = True) -> None: ...
    def get_classes(self, df, y_col): ...
    @property
    def filepaths(self): ...
    @property
    def labels(self): ...
    @property
    def sample_weight(self): ...

def flip_axis(x, axis): ...

class ImageDataGenerator:
    '''Generate batches of tensor image data with real-time data augmentation.

    Deprecated: `tf.keras.preprocessing.image.ImageDataGenerator` is not
    recommended for new code. Prefer loading images with
    `tf.keras.utils.image_dataset_from_directory` and transforming the output
    `tf.data.Dataset` with preprocessing layers. For more information, see the
    tutorials for [loading images](
    https://www.tensorflow.org/tutorials/load_data/images) and
    [augmenting images](
    https://www.tensorflow.org/tutorials/images/data_augmentation), as well as
    the [preprocessing layer guide](
    https://www.tensorflow.org/guide/keras/preprocessing_layers).

     The data will be looped over (in batches).

    Args:
        featurewise_center: Boolean. Set input mean to 0 over the dataset,
          feature-wise.
        samplewise_center: Boolean. Set each sample mean to 0.
        featurewise_std_normalization: Boolean. Divide inputs by std of the
          dataset, feature-wise.
        samplewise_std_normalization: Boolean. Divide each input by its std.
        zca_epsilon: epsilon for ZCA whitening. Default is 1e-6.
        zca_whitening: Boolean. Apply ZCA whitening.
        rotation_range: Int. Degree range for random rotations.
        width_shift_range: Float, 1-D array-like or int
            - float: fraction of total width, if < 1, or pixels if >= 1.
            - 1-D array-like: random elements from the array.
            - int: integer number of pixels from interval `(-width_shift_range,
              +width_shift_range)` - With `width_shift_range=2` possible values
              are integers `[-1, 0, +1]`, same as with `width_shift_range=[-1,
              0, +1]`, while with `width_shift_range=1.0` possible values are
              floats in the interval [-1.0, +1.0).
        height_shift_range: Float, 1-D array-like or int
            - float: fraction of total height, if < 1, or pixels if >= 1.
            - 1-D array-like: random elements from the array.
            - int: integer number of pixels from interval `(-height_shift_range,
              +height_shift_range)` - With `height_shift_range=2` possible
              values are integers `[-1, 0, +1]`, same as with
              `height_shift_range=[-1, 0, +1]`, while with
              `height_shift_range=1.0` possible values are floats in the
              interval [-1.0, +1.0).
        brightness_range: Tuple or list of two floats. Range for picking a
          brightness shift value from.
        shear_range: Float. Shear Intensity (Shear angle in counter-clockwise
          direction in degrees)
        zoom_range: Float or [lower, upper]. Range for random zoom. If a float,
          `[lower, upper] = [1-zoom_range, 1+zoom_range]`.
        channel_shift_range: Float. Range for random channel shifts.
        fill_mode: One of {"constant", "nearest", "reflect" or "wrap"}. Default
          is \'nearest\'. Points outside the boundaries of the input are filled
          according to the given mode:
            - \'constant\': kkkkkkkk|abcd|kkkkkkkk (cval=k)
            - \'nearest\':  aaaaaaaa|abcd|dddddddd
            - \'reflect\':  abcddcba|abcd|dcbaabcd
            - \'wrap\':  abcdabcd|abcd|abcdabcd
        cval: Float or Int. Value used for points outside the boundaries when
          `fill_mode = "constant"`.
        horizontal_flip: Boolean. Randomly flip inputs horizontally.
        vertical_flip: Boolean. Randomly flip inputs vertically.
        rescale: rescaling factor. Defaults to None. If None or 0, no rescaling
          is applied, otherwise we multiply the data by the value provided
          (after applying all other transformations).
        preprocessing_function: function that will be applied on each input. The
          function will run after the image is resized and augmented.
            The function should take one argument: one image (Numpy tensor with
              rank 3), and should output a Numpy tensor with the same shape.
        data_format: Image data format, either "channels_first" or
          "channels_last". "channels_last" mode means that the images should
          have shape `(samples, height, width, channels)`, "channels_first" mode
          means that the images should have shape `(samples, channels, height,
          width)`.  It defaults to the `image_data_format` value found in your
          Keras config file at `~/.keras/keras.json`. If you never set it, then
          it will be "channels_last".
        validation_split: Float. Fraction of images reserved for validation
          (strictly between 0 and 1).
        dtype: Dtype to use for the generated arrays.

    Raises:
      ValueError: If the value of the argument, `data_format` is other than
            `"channels_last"` or `"channels_first"`.
      ValueError: If the value of the argument, `validation_split` > 1
            or `validation_split` < 0.

    Examples:

    Example of using `.flow(x, y)`:

    ```python
    (x_train, y_train), (x_test, y_test) = cifar10.load_data()
    y_train = utils.to_categorical(y_train, num_classes)
    y_test = utils.to_categorical(y_test, num_classes)
    datagen = ImageDataGenerator(
        featurewise_center=True,
        featurewise_std_normalization=True,
        rotation_range=20,
        width_shift_range=0.2,
        height_shift_range=0.2,
        horizontal_flip=True,
        validation_split=0.2)
    # compute quantities required for featurewise normalization
    # (std, mean, and principal components if ZCA whitening is applied)
    datagen.fit(x_train)
    # fits the model on batches with real-time data augmentation:
    model.fit(datagen.flow(x_train, y_train, batch_size=32,
             subset=\'training\'),
             validation_data=datagen.flow(x_train, y_train,
             batch_size=8, subset=\'validation\'),
             steps_per_epoch=len(x_train) / 32, epochs=epochs)
    # here\'s a more "manual" example
    for e in range(epochs):
        print(\'Epoch\', e)
        batches = 0
        for x_batch, y_batch in datagen.flow(x_train, y_train, batch_size=32):
            model.fit(x_batch, y_batch)
            batches += 1
            if batches >= len(x_train) / 32:
                # we need to break the loop by hand because
                # the generator loops indefinitely
                break
    ```

    Example of using `.flow_from_directory(directory)`:

    ```python
    train_datagen = ImageDataGenerator(
            rescale=1./255,
            shear_range=0.2,
            zoom_range=0.2,
            horizontal_flip=True)
    test_datagen = ImageDataGenerator(rescale=1./255)
    train_generator = train_datagen.flow_from_directory(
            \'data/train\',
            target_size=(150, 150),
            batch_size=32,
            class_mode=\'binary\')
    validation_generator = test_datagen.flow_from_directory(
            \'data/validation\',
            target_size=(150, 150),
            batch_size=32,
            class_mode=\'binary\')
    model.fit(
            train_generator,
            steps_per_epoch=2000,
            epochs=50,
            validation_data=validation_generator,
            validation_steps=800)
    ```

    Example of transforming images and masks together.

    ```python
    # we create two instances with the same arguments
    data_gen_args = dict(featurewise_center=True,
                         featurewise_std_normalization=True,
                         rotation_range=90,
                         width_shift_range=0.1,
                         height_shift_range=0.1,
                         zoom_range=0.2)
    image_datagen = ImageDataGenerator(**data_gen_args)
    mask_datagen = ImageDataGenerator(**data_gen_args)
    # Provide the same seed and keyword arguments to the fit and flow methods
    seed = 1
    image_datagen.fit(images, augment=True, seed=seed)
    mask_datagen.fit(masks, augment=True, seed=seed)
    image_generator = image_datagen.flow_from_directory(
        \'data/images\',
        class_mode=None,
        seed=seed)
    mask_generator = mask_datagen.flow_from_directory(
        \'data/masks\',
        class_mode=None,
        seed=seed)
    # combine generators into one which yields image and masks
    train_generator = zip(image_generator, mask_generator)
    model.fit(
        train_generator,
        steps_per_epoch=2000,
        epochs=50)
    ```
    '''
    featurewise_center: Incomplete
    samplewise_center: Incomplete
    featurewise_std_normalization: Incomplete
    samplewise_std_normalization: Incomplete
    zca_whitening: Incomplete
    zca_epsilon: Incomplete
    rotation_range: Incomplete
    width_shift_range: Incomplete
    height_shift_range: Incomplete
    shear_range: Incomplete
    zoom_range: Incomplete
    channel_shift_range: Incomplete
    fill_mode: Incomplete
    cval: Incomplete
    horizontal_flip: Incomplete
    vertical_flip: Incomplete
    rescale: Incomplete
    preprocessing_function: Incomplete
    dtype: Incomplete
    interpolation_order: Incomplete
    data_format: Incomplete
    channel_axis: int
    row_axis: int
    col_axis: int
    mean: Incomplete
    std: Incomplete
    zca_whitening_matrix: Incomplete
    brightness_range: Incomplete
    def __init__(self, featurewise_center: bool = False, samplewise_center: bool = False, featurewise_std_normalization: bool = False, samplewise_std_normalization: bool = False, zca_whitening: bool = False, zca_epsilon: float = 1e-06, rotation_range: int = 0, width_shift_range: float = 0.0, height_shift_range: float = 0.0, brightness_range: Incomplete | None = None, shear_range: float = 0.0, zoom_range: float = 0.0, channel_shift_range: float = 0.0, fill_mode: str = 'nearest', cval: float = 0.0, horizontal_flip: bool = False, vertical_flip: bool = False, rescale: Incomplete | None = None, preprocessing_function: Incomplete | None = None, data_format: Incomplete | None = None, validation_split: float = 0.0, interpolation_order: int = 1, dtype: Incomplete | None = None) -> None: ...
    def flow(self, x, y: Incomplete | None = None, batch_size: int = 32, shuffle: bool = True, sample_weight: Incomplete | None = None, seed: Incomplete | None = None, save_to_dir: Incomplete | None = None, save_prefix: str = '', save_format: str = 'png', ignore_class_split: bool = False, subset: Incomplete | None = None):
        '''Takes data & label arrays, generates batches of augmented data.

        Args:
            x: Input data. Numpy array of rank 4 or a tuple. If tuple, the first
              element should contain the images and the second element another
              numpy array or a list of numpy arrays that gets passed to the
              output without any modifications. Can be used to feed the model
              miscellaneous data along with the images. In case of grayscale
              data, the channels axis of the image array should have value 1, in
              case of RGB data, it should have value 3, and in case of RGBA
              data, it should have value 4.
            y: Labels.
            batch_size: Int (default: 32).
            shuffle: Boolean (default: True).
            sample_weight: Sample weights.
            seed: Int (default: None).
            save_to_dir: None or str (default: None). This allows you to
              optionally specify a directory to which to save the augmented
              pictures being generated (useful for visualizing what you are
              doing).
            save_prefix: Str (default: `\'\'`). Prefix to use for filenames of
              saved pictures (only relevant if `save_to_dir` is set).
            save_format: one of "png", "jpeg", "bmp", "pdf", "ppm", "gif",
              "tif", "jpg" (only relevant if `save_to_dir` is set). Default:
              "png".
            ignore_class_split: Boolean (default: False), ignore difference
              in number of classes in labels across train and validation
              split (useful for non-classification tasks)
            subset: Subset of data (`"training"` or `"validation"`) if
              `validation_split` is set in `ImageDataGenerator`.

        Returns:
            An `Iterator` yielding tuples of `(x, y)`
                where `x` is a numpy array of image data
                (in the case of a single image input) or a list
                of numpy arrays (in the case with
                additional inputs) and `y` is a numpy array
                of corresponding labels. If \'sample_weight\' is not None,
                the yielded tuples are of the form `(x, y, sample_weight)`.
                If `y` is None, only the numpy array `x` is returned.
        Raises:
          ValueError: If the Value of the argument, `subset` is other than
                "training" or "validation".

        '''
    def flow_from_directory(self, directory, target_size=(256, 256), color_mode: str = 'rgb', classes: Incomplete | None = None, class_mode: str = 'categorical', batch_size: int = 32, shuffle: bool = True, seed: Incomplete | None = None, save_to_dir: Incomplete | None = None, save_prefix: str = '', save_format: str = 'png', follow_links: bool = False, subset: Incomplete | None = None, interpolation: str = 'nearest', keep_aspect_ratio: bool = False):
        '''Takes the path to a directory & generates batches of augmented data.

        Args:
            directory: string, path to the target directory. It should contain
              one subdirectory per class. Any PNG, JPG, BMP, PPM or TIF images
              inside each of the subdirectories directory tree will be included
              in the generator. See [this script](
              https://gist.github.com/fchollet/0830affa1f7f19fd47b06d4cf89ed44d)
              for more details.
            target_size: Tuple of integers `(height, width)`, defaults to `(256,
              256)`. The dimensions to which all images found will be resized.
            color_mode: One of "grayscale", "rgb", "rgba". Default: "rgb".
              Whether the images will be converted to have 1, 3, or 4 channels.
            classes: Optional list of class subdirectories (e.g. `[\'dogs\',
              \'cats\']`). Default: None. If not provided, the list of classes
              will be automatically inferred from the subdirectory
              names/structure under `directory`, where each subdirectory will be
              treated as a different class (and the order of the classes, which
              will map to the label indices, will be alphanumeric). The
              dictionary containing the mapping from class names to class
              indices can be obtained via the attribute `class_indices`.
            class_mode: One of "categorical", "binary", "sparse",
                "input", or None. Default: "categorical".
                Determines the type of label arrays that are returned:
                - "categorical" will be 2D one-hot encoded labels,
                - "binary" will be 1D binary labels,
                    "sparse" will be 1D integer labels,
                - "input" will be images identical
                    to input images (mainly used to work with autoencoders).
                - If None, no labels are returned
                  (the generator will only yield batches of image data,
                  which is useful to use with `model.predict_generator()`).
                  Please note that in case of class_mode None,
                  the data still needs to reside in a subdirectory
                  of `directory` for it to work correctly.
            batch_size: Size of the batches of data (default: 32).
            shuffle: Whether to shuffle the data (default: True) If set to
              False, sorts the data in alphanumeric order.
            seed: Optional random seed for shuffling and transformations.
            save_to_dir: None or str (default: None). This allows you to
              optionally specify a directory to which to save the augmented
              pictures being generated (useful for visualizing what you are
              doing).
            save_prefix: Str. Prefix to use for filenames of saved pictures
              (only relevant if `save_to_dir` is set).
            save_format: one of "png", "jpeg", "bmp", "pdf", "ppm", "gif",
              "tif", "jpg" (only relevant if `save_to_dir` is set). Default:
              "png".
            follow_links: Whether to follow symlinks inside
                class subdirectories (default: False).
            subset: Subset of data (`"training"` or `"validation"`) if
              `validation_split` is set in `ImageDataGenerator`.
            interpolation: Interpolation method used to resample the image if
              the target size is different from that of the loaded image.
              Supported methods are `"nearest"`, `"bilinear"`, and `"bicubic"`.
              If PIL version 1.1.3 or newer is installed, `"lanczos"` is also
              supported. If PIL version 3.4.0 or newer is installed, `"box"` and
              `"hamming"` are also supported. By default, `"nearest"` is used.
            keep_aspect_ratio: Boolean, whether to resize images to a target
              size without aspect ratio distortion. The image is cropped in
              the center with target aspect ratio before resizing.

        Returns:
            A `DirectoryIterator` yielding tuples of `(x, y)`
                where `x` is a numpy array containing a batch
                of images with shape `(batch_size, *target_size, channels)`
                and `y` is a numpy array of corresponding labels.
        '''
    def flow_from_dataframe(self, dataframe, directory: Incomplete | None = None, x_col: str = 'filename', y_col: str = 'class', weight_col: Incomplete | None = None, target_size=(256, 256), color_mode: str = 'rgb', classes: Incomplete | None = None, class_mode: str = 'categorical', batch_size: int = 32, shuffle: bool = True, seed: Incomplete | None = None, save_to_dir: Incomplete | None = None, save_prefix: str = '', save_format: str = 'png', subset: Incomplete | None = None, interpolation: str = 'nearest', validate_filenames: bool = True, **kwargs):
        '''Takes the dataframe and the path to a directory + generates batches.

         The generated batches contain augmented/normalized data.

        **A simple tutorial can be found **[here](
                                    http://bit.ly/keras_flow_from_dataframe).

        Args:
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
                - if `class_mode` is `"raw"` or `"multi_output"` it should
                    contain the columns specified in `y_col`.
                - if `class_mode` is `"input"` or `None` no extra column is
                    needed.
            directory: string, path to the directory to read images from. If
              `None`, data in `x_col` column should be absolute paths.
            x_col: string, column in `dataframe` that contains the filenames (or
              absolute paths if `directory` is `None`).
            y_col: string or list, column/s in `dataframe` that has the target
              data.
            weight_col: string, column in `dataframe` that contains the sample
                weights. Default: `None`.
            target_size: tuple of integers `(height, width)`, default: `(256,
              256)`. The dimensions to which all images found will be resized.
            color_mode: one of "grayscale", "rgb", "rgba". Default: "rgb".
              Whether the images will be converted to have 1 or 3 color
              channels.
            classes: optional list of classes (e.g. `[\'dogs\', \'cats\']`). Default
              is None. If not provided, the list of classes will be
              automatically inferred from the `y_col`, which will map to the
              label indices, will be alphanumeric). The dictionary containing
              the mapping from class names to class indices can be obtained via
              the attribute `class_indices`.
            class_mode: one of "binary", "categorical", "input", "multi_output",
                "raw", sparse" or None. Default: "categorical".
                Mode for yielding the targets:
                - `"binary"`: 1D numpy array of binary labels,
                - `"categorical"`: 2D numpy array of one-hot encoded labels.
                  Supports multi-label output.
                - `"input"`: images identical to input images (mainly used to
                  work with autoencoders),
                - `"multi_output"`: list with the values of the different
                  columns,
                - `"raw"`: numpy array of values in `y_col` column(s),
                - `"sparse"`: 1D numpy array of integer labels,
                - `None`, no targets are returned (the generator will only yield
                  batches of image data, which is useful to use in
                  `model.predict()`).
            batch_size: size of the batches of data (default: 32).
            shuffle: whether to shuffle the data (default: True)
            seed: optional random seed for shuffling and transformations.
            save_to_dir: None or str (default: None). This allows you to
              optionally specify a directory to which to save the augmented
              pictures being generated (useful for visualizing what you are
              doing).
            save_prefix: str. Prefix to use for filenames of saved pictures
              (only relevant if `save_to_dir` is set).
            save_format: one of "png", "jpeg", "bmp", "pdf", "ppm", "gif",
              "tif", "jpg" (only relevant if `save_to_dir` is set). Default:
              "png".
            subset: Subset of data (`"training"` or `"validation"`) if
              `validation_split` is set in `ImageDataGenerator`.
            interpolation: Interpolation method used to resample the image if
              the target size is different from that of the loaded image.
              Supported methods are `"nearest"`, `"bilinear"`, and `"bicubic"`.
              If PIL version 1.1.3 or newer is installed, `"lanczos"` is also
              supported. If PIL version 3.4.0 or newer is installed, `"box"` and
              `"hamming"` are also supported. By default, `"nearest"` is used.
            validate_filenames: Boolean, whether to validate image filenames in
              `x_col`. If `True`, invalid images will be ignored. Disabling this
              option can lead to speed-up in the execution of this function.
              Defaults to `True`.
            **kwargs: legacy arguments for raising deprecation warnings.

        Returns:
            A `DataFrameIterator` yielding tuples of `(x, y)`
            where `x` is a numpy array containing a batch
            of images with shape `(batch_size, *target_size, channels)`
            and `y` is a numpy array of corresponding labels.
        '''
    def standardize(self, x):
        """Applies the normalization configuration in-place to a batch of
        inputs.

        `x` is changed in-place since the function is mainly used internally
        to standardize images and feed them to your network. If a copy of `x`
        would be created instead it would have a significant performance cost.
        If you want to apply this method without changing the input in-place
        you can call the method creating a copy before:

        standardize(np.copy(x))

        Args:
            x: Batch of inputs to be normalized.

        Returns:
            The inputs, normalized.
        """
    def get_random_transform(self, img_shape, seed: Incomplete | None = None):
        """Generates random parameters for a transformation.

        Args:
            img_shape: Tuple of integers.
                Shape of the image that is transformed.
            seed: Random seed.

        Returns:
            A dictionary containing randomly chosen parameters describing the
            transformation.
        """
    def apply_transform(self, x, transform_parameters):
        """Applies a transformation to an image according to given parameters.

        Args:
            x: 3D tensor, single image.
            transform_parameters: Dictionary with string - parameter pairs
                describing the transformation.
                Currently, the following parameters
                from the dictionary are used:
                - `'theta'`: Float. Rotation angle in degrees.
                - `'tx'`: Float. Shift in the x direction.
                - `'ty'`: Float. Shift in the y direction.
                - `'shear'`: Float. Shear angle in degrees.
                - `'zx'`: Float. Zoom in the x direction.
                - `'zy'`: Float. Zoom in the y direction.
                - `'flip_horizontal'`: Boolean. Horizontal flip.
                - `'flip_vertical'`: Boolean. Vertical flip.
                - `'channel_shift_intensity'`: Float. Channel shift intensity.
                - `'brightness'`: Float. Brightness shift intensity.

        Returns:
            A transformed version of the input (same shape).
        """
    def random_transform(self, x, seed: Incomplete | None = None):
        """Applies a random transformation to an image.

        Args:
            x: 3D tensor, single image.
            seed: Random seed.

        Returns:
            A randomly transformed version of the input (same shape).
        """
    def fit(self, x, augment: bool = False, rounds: int = 1, seed: Incomplete | None = None) -> None:
        """Fits the data generator to some sample data.

        This computes the internal data stats related to the
        data-dependent transformations, based on an array of sample data.

        Only required if `featurewise_center` or
        `featurewise_std_normalization` or `zca_whitening` are set to True.

        When `rescale` is set to a value, rescaling is applied to
        sample data before computing the internal data stats.

        Args:
            x: Sample data. Should have rank 4.
             In case of grayscale data,
             the channels axis should have value 1, in case
             of RGB data, it should have value 3, and in case
             of RGBA data, it should have value 4.
            augment: Boolean (default: False).
                Whether to fit on randomly augmented samples.
            rounds: Int (default: 1).
                If using data augmentation (`augment=True`),
                this is how many augmentation passes over the data to use.
            seed: Int (default: None). Random seed.
        """

def random_rotation(x, rg, row_axis: int = 1, col_axis: int = 2, channel_axis: int = 0, fill_mode: str = 'nearest', cval: float = 0.0, interpolation_order: int = 1):
    """Performs a random rotation of a Numpy image tensor.

    Deprecated: `tf.keras.preprocessing.image.random_rotation` does not operate
    on tensors and is not recommended for new code. Prefer
    `tf.keras.layers.RandomRotation` which provides equivalent functionality as
    a preprocessing layer. For more information, see the tutorial for
    [augmenting images](
    https://www.tensorflow.org/tutorials/images/data_augmentation), as well as
    the [preprocessing layer guide](
    https://www.tensorflow.org/guide/keras/preprocessing_layers).

    Args:
        x: Input tensor. Must be 3D.
        rg: Rotation range, in degrees.
        row_axis: Index of axis for rows in the input tensor.
        col_axis: Index of axis for columns in the input tensor.
        channel_axis: Index of axis for channels in the input tensor.
        fill_mode: Points outside the boundaries of the input
            are filled according to the given mode
            (one of `{'constant', 'nearest', 'reflect', 'wrap'}`).
        cval: Value used for points outside the boundaries
            of the input if `mode='constant'`.
        interpolation_order: int, order of spline interpolation.
            see `ndimage.interpolation.affine_transform`

    Returns:
        Rotated Numpy image tensor.
    """
def random_shift(x, wrg, hrg, row_axis: int = 1, col_axis: int = 2, channel_axis: int = 0, fill_mode: str = 'nearest', cval: float = 0.0, interpolation_order: int = 1):
    """Performs a random spatial shift of a Numpy image tensor.

    Deprecated: `tf.keras.preprocessing.image.random_shift` does not operate on
    tensors and is not recommended for new code. Prefer
    `tf.keras.layers.RandomTranslation` which provides equivalent functionality
    as a preprocessing layer. For more information, see the tutorial for
    [augmenting images](
    https://www.tensorflow.org/tutorials/images/data_augmentation), as well as
    the [preprocessing layer guide](
    https://www.tensorflow.org/guide/keras/preprocessing_layers).

    Args:
        x: Input tensor. Must be 3D.
        wrg: Width shift range, as a float fraction of the width.
        hrg: Height shift range, as a float fraction of the height.
        row_axis: Index of axis for rows in the input tensor.
        col_axis: Index of axis for columns in the input tensor.
        channel_axis: Index of axis for channels in the input tensor.
        fill_mode: Points outside the boundaries of the input
            are filled according to the given mode
            (one of `{'constant', 'nearest', 'reflect', 'wrap'}`).
        cval: Value used for points outside the boundaries
            of the input if `mode='constant'`.
        interpolation_order: int, order of spline interpolation.
            see `ndimage.interpolation.affine_transform`

    Returns:
        Shifted Numpy image tensor.
    """
def random_shear(x, intensity, row_axis: int = 1, col_axis: int = 2, channel_axis: int = 0, fill_mode: str = 'nearest', cval: float = 0.0, interpolation_order: int = 1):
    """Performs a random spatial shear of a Numpy image tensor.

    Args:
        x: Input tensor. Must be 3D.
        intensity: Transformation intensity in degrees.
        row_axis: Index of axis for rows in the input tensor.
        col_axis: Index of axis for columns in the input tensor.
        channel_axis: Index of axis for channels in the input tensor.
        fill_mode: Points outside the boundaries of the input
            are filled according to the given mode
            (one of `{'constant', 'nearest', 'reflect', 'wrap'}`).
        cval: Value used for points outside the boundaries
            of the input if `mode='constant'`.
        interpolation_order: int, order of spline interpolation.
            see `ndimage.interpolation.affine_transform`

    Returns:
        Sheared Numpy image tensor.
    """
def random_zoom(x, zoom_range, row_axis: int = 1, col_axis: int = 2, channel_axis: int = 0, fill_mode: str = 'nearest', cval: float = 0.0, interpolation_order: int = 1):
    """Performs a random spatial zoom of a Numpy image tensor.

    Deprecated: `tf.keras.preprocessing.image.random_zoom` does not operate on
    tensors and is not recommended for new code. Prefer
    `tf.keras.layers.RandomZoom` which provides equivalent functionality as
    a preprocessing layer. For more information, see the tutorial for
    [augmenting images](
    https://www.tensorflow.org/tutorials/images/data_augmentation), as well as
    the [preprocessing layer guide](
    https://www.tensorflow.org/guide/keras/preprocessing_layers).

    Args:
        x: Input tensor. Must be 3D.
        zoom_range: Tuple of floats; zoom range for width and height.
        row_axis: Index of axis for rows in the input tensor.
        col_axis: Index of axis for columns in the input tensor.
        channel_axis: Index of axis for channels in the input tensor.
        fill_mode: Points outside the boundaries of the input
            are filled according to the given mode
            (one of `{'constant', 'nearest', 'reflect', 'wrap'}`).
        cval: Value used for points outside the boundaries
            of the input if `mode='constant'`.
        interpolation_order: int, order of spline interpolation.
            see `ndimage.interpolation.affine_transform`

    Returns:
        Zoomed Numpy image tensor.

    Raises:
        ValueError: if `zoom_range` isn't a tuple.
    """
def apply_channel_shift(x, intensity, channel_axis: int = 0):
    """Performs a channel shift.

    Args:
        x: Input tensor. Must be 3D.
        intensity: Transformation intensity.
        channel_axis: Index of axis for channels in the input tensor.

    Returns:
        Numpy image tensor.
    """
def random_channel_shift(x, intensity_range, channel_axis: int = 0):
    """Performs a random channel shift.

    Args:
        x: Input tensor. Must be 3D.
        intensity_range: Transformation intensity.
        channel_axis: Index of axis for channels in the input tensor.

    Returns:
        Numpy image tensor.
    """
def apply_brightness_shift(x, brightness, scale: bool = True):
    """Performs a brightness shift.

    Args:
        x: Input tensor. Must be 3D.
        brightness: Float. The new brightness value.
        scale: Whether to rescale the image such that minimum and maximum values
            are 0 and 255 respectively. Default: True.

    Returns:
        Numpy image tensor.

    Raises:
        ImportError: if PIL is not available.
    """
def random_brightness(x, brightness_range, scale: bool = True):
    """Performs a random brightness shift.

    Deprecated: `tf.keras.preprocessing.image.random_brightness` does not
    operate on tensors and is not recommended for new code. Prefer
    `tf.keras.layers.RandomBrightness` which provides equivalent functionality
    as a preprocessing layer. For more information, see the tutorial for
    [augmenting images](
    https://www.tensorflow.org/tutorials/images/data_augmentation), as well as
    the [preprocessing layer guide](
    https://www.tensorflow.org/guide/keras/preprocessing_layers).

    Args:
        x: Input tensor. Must be 3D.
        brightness_range: Tuple of floats; brightness range.
        scale: Whether to rescale the image such that minimum and maximum values
            are 0 and 255 respectively. Default: True.

    Returns:
        Numpy image tensor.

    Raises:
        ValueError if `brightness_range` isn't a tuple.
    """
def transform_matrix_offset_center(matrix, x, y): ...
def apply_affine_transform(x, theta: int = 0, tx: int = 0, ty: int = 0, shear: int = 0, zx: int = 1, zy: int = 1, row_axis: int = 1, col_axis: int = 2, channel_axis: int = 0, fill_mode: str = 'nearest', cval: float = 0.0, order: int = 1):
    """Applies an affine transformation specified by the parameters given.

    Args:
        x: 3D numpy array - a 2D image with one or more channels.
        theta: Rotation angle in degrees.
        tx: Width shift.
        ty: Heigh shift.
        shear: Shear angle in degrees.
        zx: Zoom in x direction.
        zy: Zoom in y direction
        row_axis: Index of axis for rows (aka Y axis) in the input
            image. Direction: left to right.
        col_axis: Index of axis for columns (aka X axis) in the input
            image. Direction: top to bottom.
        channel_axis: Index of axis for channels in the input image.
        fill_mode: Points outside the boundaries of the input
            are filled according to the given mode
            (one of `{'constant', 'nearest', 'reflect', 'wrap'}`).
        cval: Value used for points outside the boundaries
            of the input if `mode='constant'`.
        order: int, order of interpolation

    Returns:
        The transformed version of the input.

    Raises:
        ImportError: if SciPy is not available.
    """
