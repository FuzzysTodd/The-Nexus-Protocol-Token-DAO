import numpy as np
from ..core import Request as Request
from ..core.request import IOMode as IOMode, InitializationError as InitializationError, URI_BYTES as URI_BYTES
from ..core.v3_plugin_api import ImageProperties as ImageProperties, PluginV3 as PluginV3
from ..typing import ArrayLike as ArrayLike
from _typeshed import Incomplete
from typing import Any, Dict, List

class OpenCVPlugin(PluginV3):
    file_handle: Incomplete
    filename: str
    def __init__(self, request: Request) -> None: ...
    def read(self, *, index: int = None, colorspace: int | str = None, flags: int = ...) -> np.ndarray:
        '''Read an image from the ImageResource.

        Parameters
        ----------
        index : int, Ellipsis
            If int, read the index-th image from the ImageResource. If ``...``,
            read all images from the ImageResource and stack them along a new,
            prepended, batch dimension. If None (default), use ``index=0`` if
            the image contains exactly one image and ``index=...`` otherwise.
        colorspace : str, int
            The colorspace to convert into after loading and before returning
            the image. If None (default) keep grayscale images as is, convert
            images with an alpha channel to ``RGBA`` and all other images to
            ``RGB``. If int, interpret ``colorspace`` as one of OpenCVs
            `conversion flags
            <https://docs.opencv.org/4.x/d8/d01/group__imgproc__color__conversions.html>`_
            and use it for conversion. If str, convert the image into the given
            colorspace. Possible string values are: ``"RGB"``, ``"BGR"``,
            ``"RGBA"``, ``"BGRA"``, ``"GRAY"``, ``"HSV"``, or ``"LAB"``.
        flags : int
            The OpenCV flag(s) to pass to the reader. Refer to the `OpenCV docs
            <https://docs.opencv.org/4.x/d4/da8/group__imgcodecs.html#ga288b8b3da0892bd651fce07b3bbd3a56>`_
            for details.

        Returns
        -------
        ndimage : np.ndarray
            The decoded image as a numpy array.

        '''
    def iter(self, colorspace: int | str = None, flags: int = ...) -> np.ndarray:
        '''Yield images from the ImageResource.

        Parameters
        ----------
        colorspace : str, int
            The colorspace to convert into after loading and before returning
            the image. If None (default) keep grayscale images as is, convert
            images with an alpha channel to ``RGBA`` and all other images to
            ``RGB``. If int, interpret ``colorspace`` as one of OpenCVs
            `conversion flags
            <https://docs.opencv.org/4.x/d8/d01/group__imgproc__color__conversions.html>`_
            and use it for conversion. If str, convert the image into the given
            colorspace. Possible string values are: ``"RGB"``, ``"BGR"``,
            ``"RGBA"``, ``"BGRA"``, ``"GRAY"``, ``"HSV"``, or ``"LAB"``.
        flags : int
            The OpenCV flag(s) to pass to the reader. Refer to the `OpenCV docs
            <https://docs.opencv.org/4.x/d4/da8/group__imgcodecs.html#ga288b8b3da0892bd651fce07b3bbd3a56>`_
            for details.

        Yields
        ------
        ndimage : np.ndarray
            The decoded image as a numpy array.

        '''
    def write(self, ndimage: ArrayLike | List[ArrayLike], is_batch: bool = False, params: List[int] = None) -> bytes | None:
        '''Save an ndimage in the ImageResource.

        Parameters
        ----------
        ndimage : ArrayLike, List[ArrayLike]
            The image data that will be written to the file. It is either a
            single image, a batch of images, or a list of images.
        is_batch : bool
            If True, the provided ndimage is a batch of images. If False (default), the
            provided ndimage is a single image. If the provided ndimage is a list of images,
            this parameter has no effect.
        params : List[int]
            A list of parameters that will be passed to OpenCVs imwrite or
            imwritemulti functions. Possible values are documented in the
            `OpenCV documentation
            <https://docs.opencv.org/4.x/d4/da8/group__imgcodecs.html#gabbc7ef1aa2edfaa87772f1202d67e0ce>`_.

        Returns
        -------
        encoded_image : bytes, None
            If the ImageResource is ``"<bytes>"`` the call to write returns the
            encoded image as a bytes string. Otherwise it returns None.

        '''
    def properties(self, index: int = None, colorspace: int | str = None, flags: int = ...) -> ImageProperties:
        '''Standardized image metadata.

        Parameters
        ----------
        index : int, Ellipsis
            If int, get the properties of the index-th image in the
            ImageResource. If ``...``, get the properties of the image stack
            that contains all images. If None (default), use ``index=0`` if the
            image contains exactly one image and ``index=...`` otherwise.
        colorspace : str, int
            The colorspace to convert into after loading and before returning
            the image. If None (default) keep grayscale images as is, convert
            images with an alpha channel to ``RGBA`` and all other images to
            ``RGB``. If int, interpret ``colorspace`` as one of OpenCVs
            `conversion flags
            <https://docs.opencv.org/4.x/d8/d01/group__imgproc__color__conversions.html>`_
            and use it for conversion. If str, convert the image into the given
            colorspace. Possible string values are: ``"RGB"``, ``"BGR"``,
            ``"RGBA"``, ``"BGRA"``, ``"GRAY"``, ``"HSV"``, or ``"LAB"``.
        flags : int
            The OpenCV flag(s) to pass to the reader. Refer to the `OpenCV docs
            <https://docs.opencv.org/4.x/d4/da8/group__imgcodecs.html#ga288b8b3da0892bd651fce07b3bbd3a56>`_
            for details.

        Returns
        -------
        props : ImageProperties
            A dataclass filled with standardized image metadata.

        Notes
        -----
        Reading properties with OpenCV involves decoding pixel data, because
        OpenCV doesn\'t provide a direct way to access metadata.

        '''
    def metadata(self, index: int = None, exclude_applied: bool = True) -> Dict[str, Any]:
        """Format-specific metadata.

        .. warning::
            OpenCV does not support reading metadata. When called, this function
            will raise a ``NotImplementedError``.

        Parameters
        ----------
        index : int
            This parameter has no effect.
        exclude_applied : bool
            This parameter has no effect.

        """
