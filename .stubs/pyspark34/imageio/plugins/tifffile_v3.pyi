import numpy as np
from ..core.request import InitializationError as InitializationError, Request as Request, URI_BYTES as URI_BYTES
from ..core.v3_plugin_api import ImageProperties as ImageProperties, PluginV3 as PluginV3
from ..typing import ArrayLike as ArrayLike
from _typeshed import Incomplete
from collections.abc import Generator
from typing import Any, Dict

class TifffilePlugin(PluginV3):
    """Support for tifffile as backend.

    Parameters
    ----------
    request : iio.Request
        A request object that represents the users intent. It provides a
        standard interface for a plugin to access the various ImageResources.
        Check the docs for details.
    kwargs : Any
        Additional kwargs are forwarded to tifffile's constructor, i.e.
        to ``TiffFile`` for reading or ``TiffWriter`` for writing.

    """
    def __init__(self, request: Request, **kwargs) -> None: ...
    def read(self, *, index: int = None, page: int = None, **kwargs) -> np.ndarray:
        """Read a ndimage or page.

        The ndimage returned depends on the value of both ``index`` and
        ``page``. ``index`` selects the series to read and ``page`` allows
        selecting a single page from the selected series. If ``index=None``,
        ``page`` is understood as a flat index, i.e., the selection ignores
        individual series inside the file. If both ``index`` and ``page`` are
        ``None``, then all the series are read and returned as a batch.

        Parameters
        ----------
        index : int
            If ``int``, select the ndimage (series) located at that index inside
            the file and return ``page`` from it. If ``None`` and ``page`` is
            ``int`` read the page located at that (flat) index inside the file.
            If ``None`` and ``page=None``, read all ndimages from the file and
            return them as a batch.
        page : int
            If ``None`` return the full selected ndimage. If ``int``, read the
            page at the selected index and return it.
        kwargs : Any
            Additional kwargs are forwarded to TiffFile's ``as_array`` method.

        Returns
        -------
        ndarray : np.ndarray
            The decoded ndimage or page.
        """
    def iter(self, **kwargs) -> np.ndarray:
        """Yield ndimages from the TIFF.

        Parameters
        ----------
        kwargs : Any
            Additional kwargs are forwarded to the TiffPageSeries' ``as_array``
            method.

        Yields
        ------
        ndimage : np.ndarray
            A decoded ndimage.
        """
    def write(self, ndimage: ArrayLike, *, is_batch: bool = False, **kwargs) -> bytes | None:
        '''Save a ndimage as TIFF.

        Parameters
        ----------
        ndimage : ArrayLike
            The ndimage to encode and write to the ImageResource.
        is_batch : bool
            If True, the first dimension of the given ndimage is treated as a
            batch dimension and each element will create a new series.
        kwargs : Any
            Additional kwargs are forwarded to TiffWriter\'s ``write`` method.

        Returns
        -------
        encoded_image : bytes
            If the ImageResource is ``"<bytes>"``, return the encoded bytes.
            Otherwise write returns None.

        Notes
        -----
        Incremental writing is supported. Subsequent calls to ``write`` will
        create new series unless ``contiguous=True`` is used, in which case the
        call to write will append to the current series.

        '''
    def metadata(self, *, index: int = ..., page: int = None, exclude_applied: bool = True) -> Dict[str, Any]:
        """Format-Specific TIFF metadata.

        The metadata returned depends on the value of both ``index`` and
        ``page``. ``index`` selects a series and ``page`` allows selecting a
        single page from the selected series. If ``index=Ellipsis``, ``page`` is
        understood as a flat index, i.e., the selection ignores individual
        series inside the file. If ``index=Ellipsis`` and ``page=None`` then
        global (file-level) metadata is returned.

        Parameters
        ----------
        index : int
            Select the series of which to extract metadata from. If Ellipsis, treat
            page as a flat index into the file's pages.
        page : int
            If not None, select the page of which to extract metadata from. If
            None, read series-level metadata or, if ``index=...`` global,
            file-level metadata.
        exclude_applied : bool
            For API compatibility. Currently ignored.

        Returns
        -------
        metadata : dict
            A dictionary with information regarding the tiff flavor (file-level)
            or tiff tags (page-level).
        """
    def properties(self, *, index: int = None, page: int = None) -> ImageProperties:
        """Standardized metadata.

        The properties returned depend on the value of both ``index`` and
        ``page``. ``index`` selects a series and ``page`` allows selecting a
        single page from the selected series. If ``index=Ellipsis``, ``page`` is
        understood as a flat index, i.e., the selection ignores individual
        series inside the file. If ``index=Ellipsis`` and ``page=None`` then
        global (file-level) properties are returned. If ``index=Ellipsis``
        and ``page=...``, file-level properties for the flattened index are
        returned.

        Parameters
        ----------
        index : int
            If ``int``, select the ndimage (series) located at that index inside
            the file. If ``Ellipsis`` and ``page`` is ``int`` extract the
            properties of the page located at that (flat) index inside the file.
            If ``Ellipsis`` and ``page=None``, return the properties for the
            batch of all ndimages in the file.
        page : int
            If ``None`` return the properties of the full ndimage. If ``...``
            return the properties of the flattened index. If ``int``,
            return the properties of the page at the selected index only.

        Returns
        -------
        image_properties : ImageProperties
            The standardized metadata (properties) of the selected ndimage or series.

        """
    def close(self) -> None: ...
    def iter_pages(self, index=..., **kwargs) -> Generator[Incomplete, None, None]:
        """Yield pages from a TIFF file.

        This generator walks over the flat index of the pages inside an
        ImageResource and yields them in order.

        Parameters
        ----------
        index : int
            The index of the series to yield pages from. If Ellipsis, walk over
            the file's flat index (and ignore individual series).
        kwargs : Any
            Additional kwargs are passed to TiffPage's ``as_array`` method.

        Yields
        ------
        page : np.ndarray
            A page stored inside the TIFF file.

        """
