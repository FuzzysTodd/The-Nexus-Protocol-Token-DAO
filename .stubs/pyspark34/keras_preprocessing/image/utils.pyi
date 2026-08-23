from _typeshed import Incomplete

def validate_filename(filename, white_list_formats):
    """Check if a filename refers to a valid file.

    # Arguments
        filename: String, absolute path to a file
        white_list_formats: Set, allowed file extensions

    # Returns
        A boolean value indicating if the filename is valid or not
    """
def save_img(path, x, data_format: str = 'channels_last', file_format: Incomplete | None = None, scale: bool = True, **kwargs) -> None:
    '''Saves an image stored as a Numpy array to a path or file object.

    # Arguments
        path: Path or file object.
        x: Numpy array.
        data_format: Image data format,
            either "channels_first" or "channels_last".
        file_format: Optional file format override. If omitted, the
            format to use is determined from the filename extension.
            If a file object was used instead of a filename, this
            parameter should always be used.
        scale: Whether to rescale image values to be within `[0, 255]`.
        **kwargs: Additional keyword arguments passed to `PIL.Image.save()`.
    '''
def load_img(path, grayscale: bool = False, color_mode: str = 'rgb', target_size: Incomplete | None = None, interpolation: str = 'nearest'):
    '''Loads an image into PIL format.

    # Arguments
        path: Path to image file.
        grayscale: DEPRECATED use `color_mode="grayscale"`.
        color_mode: The desired image format. One of "grayscale", "rgb", "rgba".
            "grayscale" supports 8-bit images and 32-bit signed integer images.
            Default: "rgb".
        target_size: Either `None` (default to original size)
            or tuple of ints `(img_height, img_width)`.
        interpolation: Interpolation method used to resample the image if the
            target size is different from that of the loaded image.
            Supported methods are "nearest", "bilinear", and "bicubic".
            If PIL version 1.1.3 or newer is installed, "lanczos" is also
            supported. If PIL version 3.4.0 or newer is installed, "box" and
            "hamming" are also supported.
            Default: "nearest".

    # Returns
        A PIL Image instance.

    # Raises
        ImportError: if PIL is not available.
        ValueError: if interpolation method is not supported.
    '''
def list_pictures(directory, ext=('jpg', 'jpeg', 'bmp', 'png', 'ppm', 'tif', 'tiff')):
    """Lists all pictures in a directory, including all subdirectories.

    # Arguments
        directory: string, absolute path to the directory
        ext: tuple of strings or single string, extensions of the pictures

    # Returns
        a list of paths
    """
def array_to_img(x, data_format: str = 'channels_last', scale: bool = True, dtype: str = 'float32'):
    '''Converts a 3D Numpy array to a PIL Image instance.

    # Arguments
        x: Input Numpy array.
        data_format: Image data format, either "channels_first" or "channels_last".
            Default: "channels_last".
        scale: Whether to rescale the image such that minimum and maximum values
            are 0 and 255 respectively.
            Default: True.
        dtype: Dtype to use.
            Default: "float32".

    # Returns
        A PIL Image instance.

    # Raises
        ImportError: if PIL is not available.
        ValueError: if invalid `x` or `data_format` is passed.
    '''
def img_to_array(img, data_format: str = 'channels_last', dtype: str = 'float32'):
    '''Converts a PIL Image instance to a Numpy array.

    # Arguments
        img: PIL Image instance.
        data_format: Image data format,
            either "channels_first" or "channels_last".
        dtype: Dtype to use for the returned array.

    # Returns
        A 3D Numpy array.

    # Raises
        ValueError: if invalid `img` or `data_format` is passed.
    '''
