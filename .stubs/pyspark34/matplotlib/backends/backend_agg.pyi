from _typeshed import Incomplete
from matplotlib import cbook as cbook
from matplotlib.backend_bases import FigureCanvasBase as FigureCanvasBase, FigureManagerBase as FigureManagerBase, RendererBase as RendererBase, _Backend
from matplotlib.font_manager import get_font as get_font
from matplotlib.ft2font import LOAD_DEFAULT as LOAD_DEFAULT, LOAD_FORCE_AUTOHINT as LOAD_FORCE_AUTOHINT, LOAD_NO_AUTOHINT as LOAD_NO_AUTOHINT, LOAD_NO_HINTING as LOAD_NO_HINTING
from matplotlib.mathtext import MathTextParser as MathTextParser
from matplotlib.path import Path as Path
from matplotlib.transforms import Bbox as Bbox, BboxBase as BboxBase

def get_hinting_flag(): ...

class RendererAgg(RendererBase):
    """
    The renderer handles all the drawing primitives using a graphics
    context instance that controls the colors/styles
    """
    lock: Incomplete
    dpi: Incomplete
    width: Incomplete
    height: Incomplete
    mathtext_parser: Incomplete
    bbox: Incomplete
    def __init__(self, width, height, dpi) -> None: ...
    def draw_path(self, gc, path, transform, rgbFace: Incomplete | None = None) -> None: ...
    def draw_mathtext(self, gc, x, y, s, prop, angle) -> None:
        """Draw mathtext using :mod:`matplotlib.mathtext`."""
    def draw_text(self, gc, x, y, s, prop, angle, ismath: bool = False, mtext: Incomplete | None = None): ...
    def get_text_width_height_descent(self, s, prop, ismath): ...
    def draw_tex(self, gc, x, y, s, prop, angle, *, mtext: Incomplete | None = None) -> None: ...
    def get_canvas_width_height(self): ...
    def points_to_pixels(self, points): ...
    def buffer_rgba(self): ...
    def tostring_argb(self): ...
    def tostring_rgb(self): ...
    def clear(self) -> None: ...
    def option_image_nocomposite(self): ...
    def option_scale_image(self): ...
    def restore_region(self, region, bbox: Incomplete | None = None, xy: Incomplete | None = None) -> None:
        """
        Restore the saved region. If bbox (instance of BboxBase, or
        its extents) is given, only the region specified by the bbox
        will be restored. *xy* (a pair of floats) optionally
        specifies the new position (the LLC of the original region,
        not the LLC of the bbox) where the region will be restored.

        >>> region = renderer.copy_from_bbox()
        >>> x1, y1, x2, y2 = region.get_extents()
        >>> renderer.restore_region(region, bbox=(x1+dx, y1, x2, y2),
        ...                         xy=(x1-dx, y1))

        """
    def start_filter(self) -> None:
        """
        Start filtering. It simply creates a new canvas (the old one is saved).
        """
    def stop_filter(self, post_processing) -> None:
        """
        Save the plot in the current canvas as an image and apply
        the *post_processing* function.

           def post_processing(image, dpi):
             # ny, nx, depth = image.shape
             # image (numpy array) has RGBA channels and has a depth of 4.
             ...
             # create a new_image (numpy array of 4 channels, size can be
             # different). The resulting image may have offsets from
             # lower-left corner of the original image
             return new_image, offset_x, offset_y

        The saved renderer is restored and the returned image from
        post_processing is plotted (using draw_image) on it.
        """

class FigureCanvasAgg(FigureCanvasBase):
    def copy_from_bbox(self, bbox): ...
    def restore_region(self, region, bbox: Incomplete | None = None, xy: Incomplete | None = None): ...
    renderer: Incomplete
    def draw(self) -> None: ...
    def get_renderer(self, cleared: bool = False): ...
    def tostring_rgb(self):
        """
        Get the image as RGB `bytes`.

        `draw` must be called at least once before this function will work and
        to update the renderer for any subsequent changes to the Figure.
        """
    def tostring_argb(self):
        """
        Get the image as ARGB `bytes`.

        `draw` must be called at least once before this function will work and
        to update the renderer for any subsequent changes to the Figure.
        """
    def buffer_rgba(self):
        """
        Get the image as a `memoryview` to the renderer's buffer.

        `draw` must be called at least once before this function will work and
        to update the renderer for any subsequent changes to the Figure.
        """
    def print_raw(self, filename_or_obj) -> None: ...
    print_rgba = print_raw
    def print_png(self, filename_or_obj, *, metadata: Incomplete | None = None, pil_kwargs: Incomplete | None = None) -> None:
        """
        Write the figure to a PNG file.

        Parameters
        ----------
        filename_or_obj : str or path-like or file-like
            The file to write to.

        metadata : dict, optional
            Metadata in the PNG file as key-value pairs of bytes or latin-1
            encodable strings.
            According to the PNG specification, keys must be shorter than 79
            chars.

            The `PNG specification`_ defines some common keywords that may be
            used as appropriate:

            - Title: Short (one line) title or caption for image.
            - Author: Name of image's creator.
            - Description: Description of image (possibly long).
            - Copyright: Copyright notice.
            - Creation Time: Time of original image creation
              (usually RFC 1123 format).
            - Software: Software used to create the image.
            - Disclaimer: Legal disclaimer.
            - Warning: Warning of nature of content.
            - Source: Device used to create the image.
            - Comment: Miscellaneous comment;
              conversion from other image format.

            Other keywords may be invented for other purposes.

            If 'Software' is not given, an autogenerated value for Matplotlib
            will be used.  This can be removed by setting it to *None*.

            For more details see the `PNG specification`_.

            .. _PNG specification:                 https://www.w3.org/TR/2003/REC-PNG-20031110/#11keywords

        pil_kwargs : dict, optional
            Keyword arguments passed to `PIL.Image.Image.save`.

            If the 'pnginfo' key is present, it completely overrides
            *metadata*, including the default 'Software' key.
        """
    def print_to_buffer(self): ...
    def print_jpg(self, filename_or_obj, *, pil_kwargs: Incomplete | None = None) -> None: ...
    print_jpeg = print_jpg
    def print_tif(self, filename_or_obj, *, pil_kwargs: Incomplete | None = None) -> None: ...
    print_tiff = print_tif
    def print_webp(self, filename_or_obj, *, pil_kwargs: Incomplete | None = None) -> None: ...

class _BackendAgg(_Backend):
    backend_version: str
    FigureCanvas = FigureCanvasAgg
    FigureManager = FigureManagerBase
