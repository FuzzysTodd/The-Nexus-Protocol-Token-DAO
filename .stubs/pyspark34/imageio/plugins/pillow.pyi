import numpy as np
from ..core.request import IOMode as IOMode, InitializationError as InitializationError, Request as Request, URI_BYTES as URI_BYTES
from ..core.v3_plugin_api import ImageProperties as ImageProperties, PluginV3 as PluginV3
from ..typing import ArrayLike as ArrayLike
from _typeshed import Incomplete
from typing import Any, Dict, Iterator, List

class PillowPlugin(PluginV3):
    images_to_write: Incomplete
    save_args: Incomplete
    def __init__(self, request: Request) -> None:
        """Instantiate a new Pillow Plugin Object

        Parameters
        ----------
        request : {Request}
            A request object representing the resource to be operated on.

        """
    def close(self) -> None: ...
    def read(self, *, index: int = None, mode: str = None, rotate: bool = False, apply_gamma: bool = False, writeable_output: bool = True, pilmode: str = None, exifrotate: bool = None, as_gray: bool = None) -> np.ndarray:
        '''
        Parses the given URI and creates a ndarray from it.

        Parameters
        ----------
        index : int
            If the ImageResource contains multiple ndimages, and index is an
            integer, select the index-th ndimage from among them and return it.
            If index is an ellipsis (...), read all ndimages in the file and
            stack them along a new batch dimension and return them. If index is
            None, this plugin reads the first image of the file (index=0) unless
            the image is a GIF or APNG, in which case all images are read
            (index=...).
        mode : str
            Convert the image to the given mode before returning it. If None,
            the mode will be left unchanged. Possible modes can be found at:
            https://pillow.readthedocs.io/en/stable/handbook/concepts.html#modes
        rotate : bool
            If True and the image contains an EXIF orientation tag,
            apply the orientation before returning the ndimage.
        apply_gamma : bool
            If True and the image contains metadata about gamma, apply gamma
            correction to the image.
        writable_output : bool
            If True, ensure that the image is writable before returning it to
            the user. This incurs a full copy of the pixel data if the data
            served by pillow is read-only. Consequentially, setting this flag to
            False improves performance for some images.
        pilmode : str
            Deprecated, use `mode` instead.
        exifrotate : bool
            Deprecated, use `rotate` instead.
        as_gray : bool
            Deprecated. Exists to raise a constructive error message.

        Returns
        -------
        ndimage : ndarray
            A numpy array containing the loaded image data

        Notes
        -----
        If you read a paletted image (e.g. GIF) then the plugin will apply the
        palette by default. Should you wish to read the palette indices of each
        pixel use ``mode="P"``. The coresponding color pallete can be found in
        the image\'s metadata using the ``palette`` key when metadata is
        extracted using the ``exclude_applied=False`` kwarg. The latter is
        needed, as palettes are applied by default and hence excluded by default
        to keep metadata and pixel data consistent.

        '''
    def iter(self, *, mode: str = None, rotate: bool = False, apply_gamma: bool = False, writeable_output: bool = True) -> Iterator[np.ndarray]:
        """
        Iterate over all ndimages/frames in the URI

        Parameters
        ----------
        mode : {str, None}
            Convert the image to the given mode before returning it. If None,
            the mode will be left unchanged. Possible modes can be found at:
            https://pillow.readthedocs.io/en/stable/handbook/concepts.html#modes
        rotate : {bool}
            If set to ``True`` and the image contains an EXIF orientation tag,
            apply the orientation before returning the ndimage.
        apply_gamma : {bool}
            If ``True`` and the image contains metadata about gamma, apply gamma
            correction to the image.
        writable_output : bool
            If True, ensure that the image is writable before returning it to
            the user. This incurs a full copy of the pixel data if the data
            served by pillow is read-only. Consequentially, setting this flag to
            False improves performance for some images.
        """
    def write(self, ndimage: ArrayLike | List[ArrayLike], *, mode: str = None, format: str = None, is_batch: bool = None, **kwargs) -> bytes | None:
        """
        Write an ndimage to the URI specified in path.

        If the URI points to a file on the current host and the file does not
        yet exist it will be created. If the file exists already, it will be
        appended if possible; otherwise, it will be replaced.

        If necessary, the image is broken down along the leading dimension to
        fit into individual frames of the chosen format. If the format doesn't
        support multiple frames, and IOError is raised.

        Parameters
        ----------
        image : ndarray or list
            The ndimage to write. If a list is given each element is expected to
            be an ndimage.
        mode : str
            Specify the image's color format. If None (default), the mode is
            inferred from the array's shape and dtype. Possible modes can be
            found at:
            https://pillow.readthedocs.io/en/stable/handbook/concepts.html#modes
        format : str
            Optional format override. If omitted, the format to use is
            determined from the filename extension. If a file object was used
            instead of a filename, this parameter must always be used.
        is_batch : bool
            Explicitly tell the writer that ``image`` is a batch of images
            (True) or not (False). If None, the writer will guess this from the
            provided ``mode`` or ``image.shape``. While the latter often works,
            it may cause problems for small images due to aliasing of spatial
            and color-channel axes.
        kwargs : ...
            Extra arguments to pass to pillow. If a writer doesn't recognise an
            option, it is silently ignored. The available options are described
            in pillow's `image format documentation
            <https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html>`_
            for each writer.

        Notes
        -----
        When writing batches of very narrow (2-4 pixels wide) gray images set
        the ``mode`` explicitly to avoid the batch being identified as a colored
        image.

        """
    def get_meta(self, *, index: int = 0) -> Dict[str, Any]: ...
    def metadata(self, index: int = None, exclude_applied: bool = True) -> Dict[str, Any]:
        """Read ndimage metadata.

        Parameters
        ----------
        index : {integer, None}
            If the ImageResource contains multiple ndimages, and index is an
            integer, select the index-th ndimage from among them and return its
            metadata. If index is an ellipsis (...), read and return global
            metadata. If index is None, this plugin reads metadata from the
            first image of the file (index=0) unless the image is a GIF or APNG,
            in which case global metadata is read (index=...).
        exclude_applied : bool
            If True, exclude metadata fields that are applied to the image while
            reading. For example, if the binary data contains a rotation flag,
            the image is rotated by default and the rotation flag is excluded
            from the metadata to avoid confusion.

        Returns
        -------
        metadata : dict
            A dictionary of format-specific metadata.

        """
    def properties(self, index: int = None) -> ImageProperties:
        """Standardized ndimage metadata
        Parameters
        ----------
        index : int
            If the ImageResource contains multiple ndimages, and index is an
            integer, select the index-th ndimage from among them and return its
            properties. If index is an ellipsis (...), read and return the
            properties of all ndimages in the file stacked along a new batch
            dimension. If index is None, this plugin reads and returns the
            properties of the first image (index=0) unless the image is a GIF or
            APNG, in which case it reads and returns the properties all images
            (index=...).

        Returns
        -------
        properties : ImageProperties
            A dataclass filled with standardized image metadata.

        Notes
        -----
        This does not decode pixel data and is fast for large images.

        """
