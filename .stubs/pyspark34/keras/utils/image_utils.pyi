from PIL import Image as pil_image
from _typeshed import Incomplete
from keras import backend as backend

pil_image_resampling: Incomplete
pil_image_resampling = pil_image
ResizeMethod: Incomplete

def smart_resize(x, size, interpolation: str = 'bilinear'):
    """Resize images to a target size without aspect ratio distortion.

    Warning: `tf.keras.preprocessing.image.smart_resize` is not recommended for
    new code. Prefer `tf.keras.layers.Resizing`, which provides the same
    functionality as a preprocessing layer and adds `tf.RaggedTensor` support.
    See the [preprocessing layer guide](
    https://www.tensorflow.org/guide/keras/preprocessing_layers)
    for an overview of preprocessing layers.

    TensorFlow image datasets typically yield images that have each a different
    size. However, these images need to be batched before they can be
    processed by Keras layers. To be batched, images need to share the same
    height and width.

    You could simply do:

    ```python
    size = (200, 200)
    ds = ds.map(lambda img: tf.image.resize(img, size))
    ```

    However, if you do this, you distort the aspect ratio of your images, since
    in general they do not all have the same aspect ratio as `size`. This is
    fine in many cases, but not always (e.g. for GANs this can be a problem).

    Note that passing the argument `preserve_aspect_ratio=True` to `resize`
    will preserve the aspect ratio, but at the cost of no longer respecting the
    provided target size. Because `tf.image.resize` doesn't crop images,
    your output images will still have different sizes.

    This calls for:

    ```python
    size = (200, 200)
    ds = ds.map(lambda img: smart_resize(img, size))
    ```

    Your output images will actually be `(200, 200)`, and will not be distorted.
    Instead, the parts of the image that do not fit within the target size
    get cropped out.

    The resizing process is:

    1. Take the largest centered crop of the image that has the same aspect
    ratio as the target size. For instance, if `size=(200, 200)` and the input
    image has size `(340, 500)`, we take a crop of `(340, 340)` centered along
    the width.
    2. Resize the cropped image to the target size. In the example above,
    we resize the `(340, 340)` crop to `(200, 200)`.

    Args:
      x: Input image or batch of images (as a tensor or NumPy array). Must be in
        format `(height, width, channels)` or `(batch_size, height, width,
        channels)`.
      size: Tuple of `(height, width)` integer. Target size.
      interpolation: String, interpolation to use for resizing. Defaults to
        `'bilinear'`. Supports `bilinear`, `nearest`, `bicubic`, `area`,
        `lanczos3`, `lanczos5`, `gaussian`, `mitchellcubic`.

    Returns:
      Array with shape `(size[0], size[1], channels)`. If the input image was a
      NumPy array, the output is a NumPy array, and if it was a TF tensor,
      the output is a TF tensor.
    """
def get_interpolation(interpolation): ...
def array_to_img(x, data_format: Incomplete | None = None, scale: bool = True, dtype: Incomplete | None = None):
    '''Converts a 3D Numpy array to a PIL Image instance.

    Usage:

    ```python
    from PIL import Image
    img = np.random.random(size=(100, 100, 3))
    pil_img = tf.keras.utils.array_to_img(img)
    ```


    Args:
        x: Input data, in any form that can be converted to a Numpy array.
        data_format: Image data format, can be either `"channels_first"` or
          `"channels_last"`. Defaults to `None`, in which case the global
          setting `tf.keras.backend.image_data_format()` is used (unless you
          changed it, it defaults to `"channels_last"`).
        scale: Whether to rescale the image such that minimum and maximum values
          are 0 and 255 respectively. Defaults to `True`.
        dtype: Dtype to use. Default to `None`, in which case the global setting
          `tf.keras.backend.floatx()` is used (unless you changed it, it
          defaults to `"float32"`)

    Returns:
        A PIL Image instance.

    Raises:
        ImportError: if PIL is not available.
        ValueError: if invalid `x` or `data_format` is passed.
    '''
def img_to_array(img, data_format: Incomplete | None = None, dtype: Incomplete | None = None):
    '''Converts a PIL Image instance to a Numpy array.

    Usage:

    ```python
    from PIL import Image
    img_data = np.random.random(size=(100, 100, 3))
    img = tf.keras.utils.array_to_img(img_data)
    array = tf.keras.utils.image.img_to_array(img)
    ```


    Args:
        img: Input PIL Image instance.
        data_format: Image data format, can be either `"channels_first"` or
          `"channels_last"`. Defaults to `None`, in which case the global
          setting `tf.keras.backend.image_data_format()` is used (unless you
          changed it, it defaults to `"channels_last"`).
        dtype: Dtype to use. Default to `None`, in which case the global setting
          `tf.keras.backend.floatx()` is used (unless you changed it, it
          defaults to `"float32"`).

    Returns:
        A 3D Numpy array.

    Raises:
        ValueError: if invalid `img` or `data_format` is passed.
    '''
def save_img(path, x, data_format: Incomplete | None = None, file_format: Incomplete | None = None, scale: bool = True, **kwargs) -> None:
    '''Saves an image stored as a Numpy array to a path or file object.

    Args:
        path: Path or file object.
        x: Numpy array.
        data_format: Image data format, either `"channels_first"` or
          `"channels_last"`.
        file_format: Optional file format override. If omitted, the format to
          use is determined from the filename extension. If a file object was
          used instead of a filename, this parameter should always be used.
        scale: Whether to rescale image values to be within `[0, 255]`.
        **kwargs: Additional keyword arguments passed to `PIL.Image.save()`.
    '''
def load_img(path, grayscale: bool = False, color_mode: str = 'rgb', target_size: Incomplete | None = None, interpolation: str = 'nearest', keep_aspect_ratio: bool = False):
    '''Loads an image into PIL format.

    Usage:

    ```python
    image = tf.keras.utils.load_img(image_path)
    input_arr = tf.keras.utils.img_to_array(image)
    input_arr = np.array([input_arr])  # Convert single image to a batch.
    predictions = model.predict(input_arr)
    ```

    Args:
        path: Path to image file.
        grayscale: DEPRECATED use `color_mode="grayscale"`.
        color_mode: One of `"grayscale"`, `"rgb"`, `"rgba"`. Default: `"rgb"`.
          The desired image format.
        target_size: Either `None` (default to original size) or tuple of ints
          `(img_height, img_width)`.
        interpolation: Interpolation method used to resample the image if the
          target size is different from that of the loaded image. Supported
          methods are `"nearest"`, `"bilinear"`, and `"bicubic"`. If PIL version
          1.1.3 or newer is installed, `"lanczos"` is also supported. If PIL
          version 3.4.0 or newer is installed, `"box"` and `"hamming"` are also
          supported. By default, `"nearest"` is used.
        keep_aspect_ratio: Boolean, whether to resize images to a target
                size without aspect ratio distortion. The image is cropped in
                the center with target aspect ratio before resizing.

    Returns:
        A PIL Image instance.

    Raises:
        ImportError: if PIL is not available.
        ValueError: if interpolation method is not supported.
    '''
