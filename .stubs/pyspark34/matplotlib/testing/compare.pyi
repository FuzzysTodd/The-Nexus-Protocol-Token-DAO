__all__ = ['calculate_rms', 'comparable_formats', 'compare_images']

class _ConverterError(Exception): ...

class _Converter:
    def __init__(self) -> None: ...
    def __del__(self) -> None: ...

class _GSConverter(_Converter):
    def __call__(self, orig, dest): ...

class _SVGConverter(_Converter):
    def __call__(self, orig, dest) -> None: ...
    def __del__(self) -> None: ...

class _SVGWithMatplotlibFontsConverter(_SVGConverter):
    '''
    A SVG converter which explicitly adds the fonts shipped by Matplotlib to
    Inkspace\'s font search path, to better support `svg.fonttype = "none"`
    (which is in particular used by certain mathtext tests).
    '''
    def __call__(self, orig, dest): ...

def comparable_formats():
    """
    Return the list of file formats that `.compare_images` can compare
    on this system.

    Returns
    -------
    list of str
        E.g. ``['png', 'pdf', 'svg', 'eps']``.

    """
def calculate_rms(expected_image, actual_image):
    """
    Calculate the per-pixel errors, then compute the root mean square error.
    """
def compare_images(expected, actual, tol, in_decorator: bool = False):
    '''
    Compare two "image" files checking differences within a tolerance.

    The two given filenames may point to files which are convertible to
    PNG via the `.converter` dictionary. The underlying RMS is calculated
    with the `.calculate_rms` function.

    Parameters
    ----------
    expected : str
        The filename of the expected image.
    actual : str
        The filename of the actual image.
    tol : float
        The tolerance (a color value difference, where 255 is the
        maximal difference).  The test fails if the average pixel
        difference is greater than this value.
    in_decorator : bool
        Determines the output format. If called from image_comparison
        decorator, this should be True. (default=False)

    Returns
    -------
    None or dict or str
        Return *None* if the images are equal within the given tolerance.

        If the images differ, the return value depends on  *in_decorator*.
        If *in_decorator* is true, a dict with the following entries is
        returned:

        - *rms*: The RMS of the image difference.
        - *expected*: The filename of the expected image.
        - *actual*: The filename of the actual image.
        - *diff_image*: The filename of the difference image.
        - *tol*: The comparison tolerance.

        Otherwise, a human-readable multi-line string representation of this
        information is returned.

    Examples
    --------
    ::

        img1 = "./baseline/plot.png"
        img2 = "./output/plot.png"
        compare_images(img1, img2, 0.001)

    '''
