from _typeshed import Incomplete
from keras import backend as backend
from keras.engine import base_layer as base_layer, base_preprocessing_layer as base_preprocessing_layer
from keras.utils import image_utils as image_utils, tf_utils as tf_utils

H_AXIS: int
W_AXIS: int

def check_fill_mode_and_interpolation(fill_mode, interpolation) -> None: ...

class Resizing(base_layer.Layer):
    '''A preprocessing layer which resizes images.

    This layer resizes an image input to a target height and width. The input
    should be a 4D (batched) or 3D (unbatched) tensor in `"channels_last"`
    format. Input pixel values can be of any range
    (e.g. `[0., 1.)` or `[0, 255]`) and of integer or floating point dtype.
    By default, the layer will output floats.

    This layer can be called on tf.RaggedTensor batches of input images of
    distinct sizes, and will resize the outputs to dense tensors of uniform
    size.

    For an overview and full list of preprocessing layers, see the preprocessing
    [guide](https://www.tensorflow.org/guide/keras/preprocessing_layers).

    Args:
        height: Integer, the height of the output shape.
        width: Integer, the width of the output shape.
        interpolation: String, the interpolation method.
            Defaults to `"bilinear"`.
            Supports `"bilinear"`, `"nearest"`, `"bicubic"`, `"area"`,
            `"lanczos3"`, `"lanczos5"`, `"gaussian"`, `"mitchellcubic"`.
        crop_to_aspect_ratio: If True, resize the images without aspect
            ratio distortion. When the original aspect ratio differs
            from the target aspect ratio, the output image will be
            cropped so as to return the
            largest possible window in the image (of size `(height, width)`)
            that matches the target aspect ratio. By default
            (`crop_to_aspect_ratio=False`), aspect ratio may not be preserved.
    '''
    height: Incomplete
    width: Incomplete
    interpolation: Incomplete
    crop_to_aspect_ratio: Incomplete
    def __init__(self, height, width, interpolation: str = 'bilinear', crop_to_aspect_ratio: bool = False, **kwargs) -> None: ...
    def call(self, inputs): ...
    def compute_output_shape(self, input_shape): ...
    def get_config(self): ...

class CenterCrop(base_layer.Layer):
    '''A preprocessing layer which crops images.

    This layers crops the central portion of the images to a target size. If an
    image is smaller than the target size, it will be resized and cropped
    so as to return the largest possible window in the image that matches
    the target aspect ratio.

    Input pixel values can be of any range (e.g. `[0., 1.)` or `[0, 255]`) and
    of integer or floating point dtype.
    By default, the layer will output floats.

    For an overview and full list of preprocessing layers, see the preprocessing
    [guide](https://www.tensorflow.org/guide/keras/preprocessing_layers).

    Input shape:
        3D (unbatched) or 4D (batched) tensor with shape:
        `(..., height, width, channels)`, in `"channels_last"` format.

    Output shape:
        3D (unbatched) or 4D (batched) tensor with shape:
        `(..., target_height, target_width, channels)`.

    If the input height/width is even and the target height/width is odd (or
    inversely), the input image is left-padded by 1 pixel.

    Args:
        height: Integer, the height of the output shape.
        width: Integer, the width of the output shape.
    '''
    height: Incomplete
    width: Incomplete
    def __init__(self, height, width, **kwargs) -> None: ...
    def call(self, inputs): ...
    def compute_output_shape(self, input_shape): ...
    def get_config(self): ...

class RandomCrop(base_layer.BaseRandomLayer):
    '''A preprocessing layer which randomly crops images during training.

    During training, this layer will randomly choose a location to crop images
    down to a target size. The layer will crop all the images in the same batch
    to the same cropping location.

    At inference time, and during training if an input image is smaller than the
    target size, the input will be resized and cropped so as to return the
    largest possible window in the image that matches the target aspect ratio.
    If you need to apply random cropping at inference time, set `training` to
    True when calling the layer.

    Input pixel values can be of any range (e.g. `[0., 1.)` or `[0, 255]`) and
    of integer or floating point dtype. By default, the layer will output
    floats.

    For an overview and full list of preprocessing layers, see the preprocessing
    [guide](https://www.tensorflow.org/guide/keras/preprocessing_layers).

    Input shape:
        3D (unbatched) or 4D (batched) tensor with shape:
        `(..., height, width, channels)`, in `"channels_last"` format.

    Output shape:
        3D (unbatched) or 4D (batched) tensor with shape:
        `(..., target_height, target_width, channels)`.

    Args:
        height: Integer, the height of the output shape.
        width: Integer, the width of the output shape.
        seed: Integer. Used to create a random seed.
    '''
    height: Incomplete
    width: Incomplete
    seed: Incomplete
    def __init__(self, height, width, seed: Incomplete | None = None, **kwargs) -> None: ...
    def call(self, inputs, training: bool = True): ...
    def compute_output_shape(self, input_shape): ...
    def get_config(self): ...

class Rescaling(base_layer.Layer):
    """A preprocessing layer which rescales input values to a new range.

    This layer rescales every value of an input (often an image) by multiplying
    by `scale` and adding `offset`.

    For instance:

    1. To rescale an input in the `[0, 255]` range
    to be in the `[0, 1]` range, you would pass `scale=1./255`.

    2. To rescale an input in the `[0, 255]` range to be in the `[-1, 1]` range,
    you would pass `scale=1./127.5, offset=-1`.

    The rescaling is applied both during training and inference. Inputs can be
    of integer or floating point dtype, and by default the layer will output
    floats.

    For an overview and full list of preprocessing layers, see the preprocessing
    [guide](https://www.tensorflow.org/guide/keras/preprocessing_layers).

    Input shape:
        Arbitrary.

    Output shape:
        Same as input.

    Args:
        scale: Float, the scale to apply to the inputs.
        offset: Float, the offset to apply to the inputs.
    """
    scale: Incomplete
    offset: Incomplete
    def __init__(self, scale, offset: float = 0.0, **kwargs) -> None: ...
    def call(self, inputs): ...
    def compute_output_shape(self, input_shape): ...
    def get_config(self): ...

HORIZONTAL: str
VERTICAL: str
HORIZONTAL_AND_VERTICAL: str

class RandomFlip(base_layer.BaseRandomLayer):
    '''A preprocessing layer which randomly flips images during training.

    This layer will flip the images horizontally and or vertically based on the
    `mode` attribute. During inference time, the output will be identical to
    input. Call the layer with `training=True` to flip the input.

    Input pixel values can be of any range (e.g. `[0., 1.)` or `[0, 255]`) and
    of integer or floating point dtype.
    By default, the layer will output floats.

    For an overview and full list of preprocessing layers, see the preprocessing
    [guide](https://www.tensorflow.org/guide/keras/preprocessing_layers).

    Input shape:
        3D (unbatched) or 4D (batched) tensor with shape:
        `(..., height, width, channels)`, in `"channels_last"` format.

    Output shape:
        3D (unbatched) or 4D (batched) tensor with shape:
        `(..., height, width, channels)`, in `"channels_last"` format.

    Args:
        mode: String indicating which flip mode to use. Can be `"horizontal"`,
            `"vertical"`, or `"horizontal_and_vertical"`. Defaults to
            `"horizontal_and_vertical"`. `"horizontal"` is a left-right flip and
            `"vertical"` is a top-bottom flip.
        seed: Integer. Used to create a random seed.
    '''
    mode: Incomplete
    horizontal: bool
    vertical: bool
    seed: Incomplete
    def __init__(self, mode=..., seed: Incomplete | None = None, **kwargs) -> None: ...
    def call(self, inputs, training: bool = True): ...
    def compute_output_shape(self, input_shape): ...
    def get_config(self): ...

class RandomTranslation(base_layer.BaseRandomLayer):
    '''A preprocessing layer which randomly translates images during training.

    This layer will apply random translations to each image during training,
    filling empty space according to `fill_mode`.

    Input pixel values can be of any range (e.g. `[0., 1.)` or `[0, 255]`) and
    of integer or floating point dtype. By default, the layer will output
    floats.

    For an overview and full list of preprocessing layers, see the preprocessing
    [guide](https://www.tensorflow.org/guide/keras/preprocessing_layers).

    Args:
      height_factor: a float represented as fraction of value, or a tuple of
          size 2 representing lower and upper bound for shifting vertically. A
          negative value means shifting image up, while a positive value means
          shifting image down. When represented as a single positive float, this
          value is used for both the upper and lower bound. For instance,
          `height_factor=(-0.2, 0.3)` results in an output shifted by a random
          amount in the range `[-20%, +30%]`.  `height_factor=0.2` results in an
          output height shifted by a random amount in the range `[-20%, +20%]`.
      width_factor: a float represented as fraction of value, or a tuple of size
          2 representing lower and upper bound for shifting horizontally. A
          negative value means shifting image left, while a positive value means
          shifting image right. When represented as a single positive float,
          this value is used for both the upper and lower bound. For instance,
          `width_factor=(-0.2, 0.3)` results in an output shifted left by 20%,
          and shifted right by 30%. `width_factor=0.2` results
          in an output height shifted left or right by 20%.
      fill_mode: Points outside the boundaries of the input are filled according
          to the given mode
          (one of `{"constant", "reflect", "wrap", "nearest"}`).
          - *reflect*: `(d c b a | a b c d | d c b a)` The input is extended by
              reflecting about the edge of the last pixel.
          - *constant*: `(k k k k | a b c d | k k k k)` The input is extended by
              filling all values beyond the edge with the same constant value
              k = 0.
          - *wrap*: `(a b c d | a b c d | a b c d)` The input is extended by
              wrapping around to the opposite edge.
          - *nearest*: `(a a a a | a b c d | d d d d)` The input is extended by
              the nearest pixel.
      interpolation: Interpolation mode. Supported values: `"nearest"`,
          `"bilinear"`.
      seed: Integer. Used to create a random seed.
      fill_value: a float represents the value to be filled outside the
          boundaries when `fill_mode="constant"`.

    Input shape:
        3D (unbatched) or 4D (batched) tensor with shape:
        `(..., height, width, channels)`,  in `"channels_last"` format.

    Output shape:
        3D (unbatched) or 4D (batched) tensor with shape:
        `(..., height, width, channels)`,  in `"channels_last"` format.
    '''
    height_factor: Incomplete
    height_lower: Incomplete
    height_upper: Incomplete
    width_factor: Incomplete
    width_lower: Incomplete
    width_upper: Incomplete
    fill_mode: Incomplete
    fill_value: Incomplete
    interpolation: Incomplete
    seed: Incomplete
    def __init__(self, height_factor, width_factor, fill_mode: str = 'reflect', interpolation: str = 'bilinear', seed: Incomplete | None = None, fill_value: float = 0.0, **kwargs) -> None: ...
    def call(self, inputs, training: bool = True): ...
    def compute_output_shape(self, input_shape): ...
    def get_config(self): ...

def get_translation_matrix(translations, name: Incomplete | None = None):
    """Returns projective transform(s) for the given translation(s).

    Args:
        translations: A matrix of 2-element lists representing `[dx, dy]`
            to translate for each image (for a batch of images).
        name: The name of the op.

    Returns:
        A tensor of shape `(num_images, 8)` projective transforms
            which can be given to `transform`.
    """
def transform(images, transforms, fill_mode: str = 'reflect', fill_value: float = 0.0, interpolation: str = 'bilinear', output_shape: Incomplete | None = None, name: Incomplete | None = None):
    '''Applies the given transform(s) to the image(s).

    Args:
        images: A tensor of shape
            `(num_images, num_rows, num_columns, num_channels)` (NHWC).
            The rank must be statically known
            (the shape is not `TensorShape(None)`).
        transforms: Projective transform matrix/matrices.
            A vector of length 8 or tensor of size N x 8.
            If one row of transforms is [a0, a1, a2, b0, b1, b2,
            c0, c1], then it maps the *output* point `(x, y)`
            to a transformed *input* point
            `(x\', y\') = ((a0 x + a1 y + a2) / k, (b0 x + b1 y + b2) / k)`, where
            `k = c0 x + c1 y + 1`. The transforms are *inverted* compared to the
            transform mapping input points to output points.
            Note that gradients are not backpropagated
            into transformation parameters.
        fill_mode: Points outside the boundaries of the input are filled
            according to the given mode
            (one of `{"constant", "reflect", "wrap", "nearest"}`).
        fill_value: a float represents the value to be filled outside
            the boundaries when `fill_mode="constant"`.
        interpolation: Interpolation mode. Supported values: `"nearest"`,
            `"bilinear"`.
        output_shape: Output dimension after the transform, `[height, width]`.
            If `None`, output is the same size as input image.
        name: The name of the op.

    Fill mode behavior for each valid value is as follows:

    - `"reflect"`: `(d c b a | a b c d | d c b a)`
    The input is extended by reflecting about the edge of the last pixel.

    - `"constant"`: `(k k k k | a b c d | k k k k)`
    The input is extended by filling all
    values beyond the edge with the same constant value k = 0.

    - `"wrap"`: `(a b c d | a b c d | a b c d)`
    The input is extended by wrapping around to the opposite edge.

    - `"nearest"`: `(a a a a | a b c d | d d d d)`
    The input is extended by the nearest pixel.

    Input shape:
        4D tensor with shape: `(samples, height, width, channels)`,
            in `"channels_last"` format.

    Output shape:
        4D tensor with shape: `(samples, height, width, channels)`,
            in `"channels_last"` format.

    Returns:
        Image(s) with the same type and shape as `images`, with the given
        transform(s) applied. Transformed coordinates outside of the input image
        will be filled with zeros.
    '''
def get_rotation_matrix(angles, image_height, image_width, name: Incomplete | None = None):
    """Returns projective transform(s) for the given angle(s).

    Args:
        angles: A scalar angle to rotate all images by,
            or (for batches of images) a vector with an angle to
            rotate each image in the batch. The rank must be
            statically known (the shape is not `TensorShape(None)`).
        image_height: Height of the image(s) to be transformed.
        image_width: Width of the image(s) to be transformed.
        name: The name of the op.

    Returns:
        A tensor of shape (num_images, 8).
            Projective transforms which can be given
            to operation `image_projective_transform_v2`.
            If one row of transforms is
            [a0, a1, a2, b0, b1, b2, c0, c1], then it maps the *output* point
            `(x, y)` to a transformed *input* point
            `(x', y') = ((a0 x + a1 y + a2) / k, (b0 x + b1 y + b2) / k)`,
            where `k = c0 x + c1 y + 1`.
    """

class RandomRotation(base_layer.BaseRandomLayer):
    '''A preprocessing layer which randomly rotates images during training.

    This layer will apply random rotations to each image, filling empty space
    according to `fill_mode`.

    By default, random rotations are only applied during training.
    At inference time, the layer does nothing. If you need to apply random
    rotations at inference time, set `training` to True when calling the layer.

    Input pixel values can be of any range (e.g. `[0., 1.)` or `[0, 255]`) and
    of integer or floating point dtype.
    By default, the layer will output floats.

    For an overview and full list of preprocessing layers, see the preprocessing
    [guide](https://www.tensorflow.org/guide/keras/preprocessing_layers).

    Input shape:
        3D (unbatched) or 4D (batched) tensor with shape:
        `(..., height, width, channels)`, in `"channels_last"` format

    Output shape:
        3D (unbatched) or 4D (batched) tensor with shape:
        `(..., height, width, channels)`, in `"channels_last"` format

    Args:
        factor: a float represented as fraction of 2 Pi, or a tuple of size 2
            representing lower and upper bound for rotating clockwise and
            counter-clockwise. A positive values means rotating
            counter clock-wise,
            while a negative value means clock-wise.
            When represented as a single
            float, this value is used for both the upper and lower bound.
            For instance, `factor=(-0.2, 0.3)`
            results in an output rotation by a random
            amount in the range `[-20% * 2pi, 30% * 2pi]`.
            `factor=0.2` results in an
            output rotating by a random amount
            in the range `[-20% * 2pi, 20% * 2pi]`.
        fill_mode: Points outside the boundaries of the input are filled
            according to the given mode
            (one of `{"constant", "reflect", "wrap", "nearest"}`).
            - *reflect*: `(d c b a | a b c d | d c b a)`
                The input is extended by reflecting about
                the edge of the last pixel.
            - *constant*: `(k k k k | a b c d | k k k k)`
                The input is extended by
                filling all values beyond the edge with
                the same constant value k = 0.
            - *wrap*: `(a b c d | a b c d | a b c d)` The input is extended by
                wrapping around to the opposite edge.
            - *nearest*: `(a a a a | a b c d | d d d d)`
                The input is extended by the nearest pixel.
        interpolation: Interpolation mode. Supported values: `"nearest"`,
            `"bilinear"`.
        seed: Integer. Used to create a random seed.
        fill_value: a float represents the value to be filled outside
            the boundaries when `fill_mode="constant"`.
    '''
    factor: Incomplete
    lower: Incomplete
    upper: Incomplete
    fill_mode: Incomplete
    fill_value: Incomplete
    interpolation: Incomplete
    seed: Incomplete
    def __init__(self, factor, fill_mode: str = 'reflect', interpolation: str = 'bilinear', seed: Incomplete | None = None, fill_value: float = 0.0, **kwargs) -> None: ...
    def call(self, inputs, training: bool = True): ...
    def compute_output_shape(self, input_shape): ...
    def get_config(self): ...

class RandomZoom(base_layer.BaseRandomLayer):
    '''A preprocessing layer which randomly zooms images during training.

    This layer will randomly zoom in or out on each axis of an image
    independently, filling empty space according to `fill_mode`.

    Input pixel values can be of any range (e.g. `[0., 1.)` or `[0, 255]`) and
    of integer or floating point dtype.
    By default, the layer will output floats.

    For an overview and full list of preprocessing layers, see the preprocessing
    [guide](https://www.tensorflow.org/guide/keras/preprocessing_layers).

    Args:
        height_factor: a float represented as fraction of value,
            or a tuple of size 2 representing lower and upper bound
            for zooming vertically. When represented as a single float,
            this value is used for both the upper and
            lower bound. A positive value means zooming out,
            while a negative value
            means zooming in. For instance, `height_factor=(0.2, 0.3)`
            result in an output zoomed out by a random amount
            in the range `[+20%, +30%]`.
            `height_factor=(-0.3, -0.2)` result in an output zoomed
            in by a random amount in the range `[+20%, +30%]`.
        width_factor: a float represented as fraction of value,
            or a tuple of size 2 representing lower and upper bound
            for zooming horizontally. When
            represented as a single float, this value is used
            for both the upper and
            lower bound. For instance, `width_factor=(0.2, 0.3)`
            result in an output
            zooming out between 20% to 30%.
            `width_factor=(-0.3, -0.2)` result in an
            output zooming in between 20% to 30%. Defaults to `None`,
            i.e., zooming vertical and horizontal directions
            by preserving the aspect ratio.
        fill_mode: Points outside the boundaries of the input are
            filled according to the given mode
            (one of `{"constant", "reflect", "wrap", "nearest"}`).
            - *reflect*: `(d c b a | a b c d | d c b a)`
                The input is extended by reflecting about
                the edge of the last pixel.
            - *constant*: `(k k k k | a b c d | k k k k)`
                The input is extended by filling all values beyond
                the edge with the same constant value k = 0.
            - *wrap*: `(a b c d | a b c d | a b c d)` The input is extended by
                wrapping around to the opposite edge.
            - *nearest*: `(a a a a | a b c d | d d d d)`
                The input is extended by the nearest pixel.
        interpolation: Interpolation mode. Supported values: `"nearest"`,
            `"bilinear"`.
        seed: Integer. Used to create a random seed.
        fill_value: a float represents the value to be filled outside
            the boundaries when `fill_mode="constant"`.

    Example:

    >>> input_img = np.random.random((32, 224, 224, 3))
    >>> layer = tf.keras.layers.RandomZoom(.5, .2)
    >>> out_img = layer(input_img)
    >>> out_img.shape
    TensorShape([32, 224, 224, 3])

    Input shape:
        3D (unbatched) or 4D (batched) tensor with shape:
        `(..., height, width, channels)`, in `"channels_last"` format.

    Output shape:
        3D (unbatched) or 4D (batched) tensor with shape:
        `(..., height, width, channels)`, in `"channels_last"` format.
    '''
    height_factor: Incomplete
    height_lower: Incomplete
    height_upper: Incomplete
    width_factor: Incomplete
    width_lower: Incomplete
    width_upper: Incomplete
    fill_mode: Incomplete
    fill_value: Incomplete
    interpolation: Incomplete
    seed: Incomplete
    def __init__(self, height_factor, width_factor: Incomplete | None = None, fill_mode: str = 'reflect', interpolation: str = 'bilinear', seed: Incomplete | None = None, fill_value: float = 0.0, **kwargs) -> None: ...
    def call(self, inputs, training: bool = True): ...
    def compute_output_shape(self, input_shape): ...
    def get_config(self): ...

def get_zoom_matrix(zooms, image_height, image_width, name: Incomplete | None = None):
    """Returns projective transform(s) for the given zoom(s).

    Args:
        zooms: A matrix of 2-element lists representing `[zx, zy]`
            to zoom for each image (for a batch of images).
        image_height: Height of the image(s) to be transformed.
        image_width: Width of the image(s) to be transformed.
        name: The name of the op.

    Returns:
        A tensor of shape `(num_images, 8)`. Projective transforms which can be
            given to operation `image_projective_transform_v2`.
            If one row of transforms is
            `[a0, a1, a2, b0, b1, b2, c0, c1]`, then it maps the *output* point
            `(x, y)` to a transformed *input* point
            `(x', y') = ((a0 x + a1 y + a2) / k, (b0 x + b1 y + b2) / k)`,
            where `k = c0 x + c1 y + 1`.
    """

class RandomContrast(base_layer.BaseRandomLayer):
    '''A preprocessing layer which randomly adjusts contrast during training.

    This layer will randomly adjust the contrast of an image or images
    by a random factor. Contrast is adjusted independently
    for each channel of each image during training.

    For each channel, this layer computes the mean of the image pixels in the
    channel and then adjusts each component `x` of each pixel to
    `(x - mean) * contrast_factor + mean`.

    Input pixel values can be of any range (e.g. `[0., 1.)` or `[0, 255]`) and
    in integer or floating point dtype.
    By default, the layer will output floats.
    The output value will be clipped to the range `[0, 255]`, the valid
    range of RGB colors.

    For an overview and full list of preprocessing layers, see the preprocessing
    [guide](https://www.tensorflow.org/guide/keras/preprocessing_layers).

    Input shape:
        3D (unbatched) or 4D (batched) tensor with shape:
        `(..., height, width, channels)`, in `"channels_last"` format.

    Output shape:
        3D (unbatched) or 4D (batched) tensor with shape:
        `(..., height, width, channels)`, in `"channels_last"` format.

    Args:
        factor: a positive float represented as fraction of value, or a tuple of
            size 2 representing lower and upper bound.
            When represented as a single float, lower = upper.
            The contrast factor will be randomly picked between
            `[1.0 - lower, 1.0 + upper]`. For any pixel x in the channel,
            the output will be `(x - mean) * factor + mean`
            where `mean` is the mean value of the channel.
        seed: Integer. Used to create a random seed.
    '''
    factor: Incomplete
    lower: Incomplete
    upper: Incomplete
    seed: Incomplete
    def __init__(self, factor, seed: Incomplete | None = None, **kwargs) -> None: ...
    def call(self, inputs, training: bool = True): ...
    def compute_output_shape(self, input_shape): ...
    def get_config(self): ...

class RandomBrightness(base_layer.BaseRandomLayer):
    """A preprocessing layer which randomly adjusts brightness during training.

    This layer will randomly increase/reduce the brightness for the input RGB
    images. At inference time, the output will be identical to the input.
    Call the layer with `training=True` to adjust the brightness of the input.

    Note that different brightness adjustment factors
    will be apply to each the images in the batch.

    For an overview and full list of preprocessing layers, see the preprocessing
    [guide](https://www.tensorflow.org/guide/keras/preprocessing_layers).

    Args:
        factor: Float or a list/tuple of 2 floats between -1.0 and 1.0. The
            factor is used to determine the lower bound and upper bound of the
            brightness adjustment. A float value will be chosen randomly between
            the limits. When -1.0 is chosen, the output image will be black, and
            when 1.0 is chosen, the image will be fully white.
            When only one float is provided, eg, 0.2,
            then -0.2 will be used for lower bound and 0.2
            will be used for upper bound.
        value_range: Optional list/tuple of 2 floats
            for the lower and upper limit
            of the values of the input data. Defaults to [0.0, 255.0].
            Can be changed to e.g. [0.0, 1.0] if the image input
            has been scaled before this layer.
            The brightness adjustment will be scaled to this range, and the
            output values will be clipped to this range.
        seed: optional integer, for fixed RNG behavior.

    Inputs: 3D (HWC) or 4D (NHWC) tensor, with float or int dtype. Input pixel
        values can be of any range (e.g. `[0., 1.)` or `[0, 255]`)

    Output: 3D (HWC) or 4D (NHWC) tensor with brightness adjusted based on the
        `factor`. By default, the layer will output floats.
        The output value will be clipped to the range `[0, 255]`,
        the valid range of RGB colors, and
        rescaled based on the `value_range` if needed.

    Sample usage:

    ```python
    random_bright = tf.keras.layers.RandomBrightness(factor=0.2)

    # An image with shape [2, 2, 3]
    image = [[[1, 2, 3], [4 ,5 ,6]], [[7, 8, 9], [10, 11, 12]]]

    # Assume we randomly select the factor to be 0.1, then it will apply
    # 0.1 * 255 to all the channel
    output = random_bright(image, training=True)

    # output will be int64 with 25.5 added to each channel and round down.
    tf.Tensor([[[26.5, 27.5, 28.5]
                [29.5, 30.5, 31.5]]
               [[32.5, 33.5, 34.5]
                [35.5, 36.5, 37.5]]],
              shape=(2, 2, 3), dtype=int64)
    ```
    """
    def __init__(self, factor, value_range=(0, 255), seed: Incomplete | None = None, **kwargs) -> None: ...
    def call(self, inputs, training: bool = True): ...
    def get_config(self): ...

class RandomHeight(base_layer.BaseRandomLayer):
    '''A preprocessing layer which randomly varies image height during training.

    This layer adjusts the height of a batch of images by a random factor.
    The input should be a 3D (unbatched) or 4D (batched) tensor in the
    `"channels_last"` image data format. Input pixel values can be of any range
    (e.g. `[0., 1.)` or `[0, 255]`) and of integer or floating point dtype. By
    default, the layer will output floats.


    By default, this layer is inactive during inference.

    For an overview and full list of preprocessing layers, see the preprocessing
    [guide](https://www.tensorflow.org/guide/keras/preprocessing_layers).

    Args:
        factor: A positive float (fraction of original height),
            or a tuple of size 2 representing lower and upper bound
            for resizing vertically. When represented as a single float,
            this value is used for both the upper and
            lower bound. For instance, `factor=(0.2, 0.3)` results
            in an output with
            height changed by a random amount in the range `[20%, 30%]`.
            `factor=(-0.2, 0.3)` results in an output with height
            changed by a random amount in the range `[-20%, +30%]`.
            `factor=0.2` results in an output with
            height changed by a random amount in the range `[-20%, +20%]`.
        interpolation: String, the interpolation method.
            Defaults to `"bilinear"`.
            Supports `"bilinear"`, `"nearest"`, `"bicubic"`, `"area"`,
            `"lanczos3"`, `"lanczos5"`, `"gaussian"`, `"mitchellcubic"`.
        seed: Integer. Used to create a random seed.

    Input shape:
        3D (unbatched) or 4D (batched) tensor with shape:
        `(..., height, width, channels)`, in `"channels_last"` format.

    Output shape:
        3D (unbatched) or 4D (batched) tensor with shape:
        `(..., random_height, width, channels)`.
    '''
    factor: Incomplete
    height_lower: Incomplete
    height_upper: Incomplete
    interpolation: Incomplete
    seed: Incomplete
    def __init__(self, factor, interpolation: str = 'bilinear', seed: Incomplete | None = None, **kwargs) -> None: ...
    def call(self, inputs, training: bool = True): ...
    def compute_output_shape(self, input_shape): ...
    def get_config(self): ...

class RandomWidth(base_layer.BaseRandomLayer):
    '''A preprocessing layer which randomly varies image width during training.

    This layer will randomly adjusts the width of a batch of images of a
    batch of images by a random factor. The input should be a 3D (unbatched) or
    4D (batched) tensor in the `"channels_last"` image data format. Input pixel
    values can be of any range (e.g. `[0., 1.)` or `[0, 255]`) and of integer or
    floating point dtype. By default, the layer will output floats.

    By default, this layer is inactive during inference.

    For an overview and full list of preprocessing layers, see the preprocessing
    [guide](https://www.tensorflow.org/guide/keras/preprocessing_layers).

    Args:
        factor: A positive float (fraction of original width),
            or a tuple of size 2 representing lower and upper bound
            for resizing vertically. When represented as a single float,
            this value is used for both the upper and
            lower bound. For instance, `factor=(0.2, 0.3)`
            results in an output with
            width changed by a random amount in the range `[20%, 30%]`.
            `factor=(-0.2, 0.3)` results in an output with width changed
            by a random amount in the range `[-20%, +30%]`.
            `factor=0.2` results in an output with width changed
            by a random amount in the range `[-20%, +20%]`.
        interpolation: String, the interpolation method.
            Defaults to `bilinear`.
            Supports `"bilinear"`, `"nearest"`, `"bicubic"`, `"area"`,
            `"lanczos3"`, `"lanczos5"`, `"gaussian"`, `"mitchellcubic"`.
        seed: Integer. Used to create a random seed.

    Input shape:
        3D (unbatched) or 4D (batched) tensor with shape:
        `(..., height, width, channels)`, in `"channels_last"` format.

    Output shape:
        3D (unbatched) or 4D (batched) tensor with shape:
        `(..., height, random_width, channels)`.
    '''
    factor: Incomplete
    width_lower: Incomplete
    width_upper: Incomplete
    interpolation: Incomplete
    seed: Incomplete
    def __init__(self, factor, interpolation: str = 'bilinear', seed: Incomplete | None = None, **kwargs) -> None: ...
    def call(self, inputs, training: bool = True): ...
    def compute_output_shape(self, input_shape): ...
    def get_config(self): ...

def convert_inputs(inputs, dtype: Incomplete | None = None): ...
