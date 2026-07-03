from _typeshed import Incomplete

__all__ = ['imsave', 'imread', 'imshow', 'memmap', 'TiffFile', 'TiffWriter', 'TiffSequence', 'FileHandle', 'lazyattr', 'natural_sorted', 'decode_lzw', 'stripnull', 'create_output', 'repeat_nd', 'format_size', 'product', 'xml2dict']

def imread(files, **kwargs):
    """Return image data from TIFF file(s) as numpy array.

    Refer to the TiffFile class and member functions for documentation.

    Parameters
    ----------
    files : str, binary stream, or sequence
        File name, seekable binary stream, glob pattern, or sequence of
        file names.
    kwargs : dict
        Parameters 'multifile' and 'is_ome' are passed to the TiffFile class.
        The 'pattern' parameter is passed to the TiffSequence class.
        Other parameters are passed to the asarray functions.
        The first image series is returned if no arguments are provided.

    Examples
    --------
    >>> # get image from first page
    >>> imsave('temp.tif', numpy.random.rand(3, 4, 301, 219))
    >>> im = imread('temp.tif', key=0)
    >>> im.shape
    (4, 301, 219)

    >>> # get images from sequence of files
    >>> ims = imread(['temp.tif', 'temp.tif'])
    >>> ims.shape
    (2, 3, 4, 301, 219)

    """
def imsave(file, data: Incomplete | None = None, shape: Incomplete | None = None, dtype: Incomplete | None = None, bigsize=..., **kwargs):
    """Write numpy array to TIFF file.

    Refer to the TiffWriter class and member functions for documentation.

    Parameters
    ----------
    file : str or binary stream
        File name or writable binary stream, such as an open file or BytesIO.
    data : array_like
        Input image. The last dimensions are assumed to be image depth,
        height, width, and samples.
        If None, an empty array of the specified shape and dtype is
        saved to file.
        Unless 'byteorder' is specified in 'kwargs', the TIFF file byte order
        is determined from the data's dtype or the dtype argument.
    shape : tuple
        If 'data' is None, shape of an empty array to save to the file.
    dtype : numpy.dtype
        If 'data' is None, data-type of an empty array to save to the file.
    bigsize : int
        Create a BigTIFF file if the size of data in bytes is larger than
        this threshold and 'imagej' or 'truncate' are not enabled.
        By default, the threshold is 4 GB minus 32 MB reserved for metadata.
        Use the 'bigtiff' parameter to explicitly specify the type of
        file created.
    kwargs : dict
        Parameters 'append', 'byteorder', 'bigtiff', and 'imagej', are passed
        to TiffWriter(). Other parameters are passed to TiffWriter.save().

    Returns
    -------
    If the image data are written contiguously, return offset and bytecount
    of image data in the file.

    Examples
    --------
    >>> # save a RGB image
    >>> data = numpy.random.randint(0, 255, (256, 256, 3), 'uint8')
    >>> imsave('temp.tif', data, photometric='rgb')

    >>> # save a random array and metadata, using compression
    >>> data = numpy.random.rand(2, 5, 3, 301, 219)
    >>> imsave('temp.tif', data, compress=6, metadata={'axes': 'TZCYX'})

    """
def memmap(filename, shape: Incomplete | None = None, dtype: Incomplete | None = None, page: Incomplete | None = None, series: int = 0, mode: str = 'r+', **kwargs):
    """Return memory-mapped numpy array stored in TIFF file.

    Memory-mapping requires data stored in native byte order, without tiling,
    compression, predictors, etc.
    If 'shape' and 'dtype' are provided, existing files will be overwritten or
    appended to depending on the 'append' parameter.
    Otherwise the image data of a specified page or series in an existing
    file will be memory-mapped. By default, the image data of the first page
    series is memory-mapped.
    Call flush() to write any changes in the array to the file.
    Raise ValueError if the image data in the file is not memory-mappable.

    Parameters
    ----------
    filename : str
        Name of the TIFF file which stores the array.
    shape : tuple
        Shape of the empty array.
    dtype : numpy.dtype
        Data-type of the empty array.
    page : int
        Index of the page which image data to memory-map.
    series : int
        Index of the page series which image data to memory-map.
    mode : {'r+', 'r', 'c'}, optional
        The file open mode. Default is to open existing file for reading and
        writing ('r+').
    kwargs : dict
        Additional parameters passed to imsave() or TiffFile().

    Examples
    --------
    >>> # create an empty TIFF file and write to memory-mapped image
    >>> im = memmap('temp.tif', shape=(256, 256), dtype='float32')
    >>> im[255, 255] = 1.0
    >>> im.flush()
    >>> im.shape, im.dtype
    ((256, 256), dtype('float32'))
    >>> del im

    >>> # memory-map image data in a TIFF file
    >>> im = memmap('temp.tif', page=0)
    >>> im[255, 255]
    1.0

    """

class lazyattr:
    """Attribute whose value is computed on first access."""
    func: Incomplete
    def __init__(self, func) -> None: ...
    def __get__(self, instance, owner): ...

class TiffWriter:
    """Write numpy arrays to TIFF file.

    TiffWriter instances must be closed using the 'close' method, which is
    automatically called when using the 'with' context manager.

    TiffWriter's main purpose is saving nD numpy array's as TIFF,
    not to create any possible TIFF format. Specifically, JPEG compression,
    SubIFDs, ExifIFD, or GPSIFD tags are not supported.

    Examples
    --------
    >>> # successively append images to BigTIFF file
    >>> data = numpy.random.rand(2, 5, 3, 301, 219)
    >>> with TiffWriter('temp.tif', bigtiff=True) as tif:
    ...     for i in range(data.shape[0]):
    ...         tif.save(data[i], compress=6, photometric='minisblack')

    """
    def __init__(self, file, bigtiff: bool = False, byteorder: Incomplete | None = None, append: bool = False, imagej: bool = False) -> None:
        """Open a TIFF file for writing.

        An empty TIFF file is created if the file does not exist, else the
        file is overwritten with an empty TIFF file unless 'append'
        is true. Use bigtiff=True when creating files larger than 4 GB.

        Parameters
        ----------
        file : str, binary stream, or FileHandle
            File name or writable binary stream, such as an open file
            or BytesIO.
        bigtiff : bool
            If True, the BigTIFF format is used.
        byteorder : {'<', '>', '=', '|'}
            The endianness of the data in the file.
            By default, this is the system's native byte order.
        append : bool
            If True and 'file' is an existing standard TIFF file, image data
            and tags are appended to the file.
            Appending data may corrupt specifically formatted TIFF files
            such as LSM, STK, ImageJ, NIH, or FluoView.
        imagej : bool
            If True, write an ImageJ hyperstack compatible file.
            This format can handle data types uint8, uint16, or float32 and
            data shapes up to 6 dimensions in TZCYXS order.
            RGB images (S=3 or S=4) must be uint8.
            ImageJ's default byte order is big-endian but this implementation
            uses the system's native byte order by default.
            ImageJ does not support BigTIFF format or LZMA compression.
            The ImageJ file format is undocumented.

        """
    def save(self, data: Incomplete | None = None, shape: Incomplete | None = None, dtype: Incomplete | None = None, returnoffset: bool = False, photometric: Incomplete | None = None, planarconfig: Incomplete | None = None, tile: Incomplete | None = None, contiguous: bool = True, align: int = 16, truncate: bool = False, compress: int = 0, rowsperstrip: Incomplete | None = None, predictor: bool = False, colormap: Incomplete | None = None, description: Incomplete | None = None, datetime: Incomplete | None = None, resolution: Incomplete | None = None, software: str = 'tifffile.py', metadata={}, ijmetadata: Incomplete | None = None, extratags=()):
        """Write numpy array and tags to TIFF file.

        The data shape's last dimensions are assumed to be image depth,
        height (length), width, and samples.
        If a colormap is provided, the data's dtype must be uint8 or uint16
        and the data values are indices into the last dimension of the
        colormap.
        If 'shape' and 'dtype' are specified, an empty array is saved.
        This option cannot be used with compression or multiple tiles.
        Image data are written uncompressed in one strip per plane by default.
        Dimensions larger than 2 to 4 (depending on photometric mode, planar
        configuration, and SGI mode) are flattened and saved as separate pages.
        The SampleFormat and BitsPerSample tags are derived from the data type.

        Parameters
        ----------
        data : numpy.ndarray or None
            Input image array.
        shape : tuple or None
            Shape of the empty array to save. Used only if 'data' is None.
        dtype : numpy.dtype or None
            Data-type of the empty array to save. Used only if 'data' is None.
        returnoffset : bool
            If True and the image data in the file is memory-mappable, return
            the offset and number of bytes of the image data in the file.
        photometric : {'MINISBLACK', 'MINISWHITE', 'RGB', 'PALETTE', 'CFA'}
            The color space of the image data.
            By default, this setting is inferred from the data shape and the
            value of colormap.
            For CFA images, DNG tags must be specified in 'extratags'.
        planarconfig : {'CONTIG', 'SEPARATE'}
            Specifies if samples are stored contiguous or in separate planes.
            By default, this setting is inferred from the data shape.
            If this parameter is set, extra samples are used to store grayscale
            images.
            'CONTIG': last dimension contains samples.
            'SEPARATE': third last dimension contains samples.
        tile : tuple of int
            The shape (depth, length, width) of image tiles to write.
            If None (default), image data are written in strips.
            The tile length and width must be a multiple of 16.
            If the tile depth is provided, the SGI ImageDepth and TileDepth
            tags are used to save volume data.
            Unless a single tile is used, tiles cannot be used to write
            contiguous files.
            Few software can read the SGI format, e.g. MeVisLab.
        contiguous : bool
            If True (default) and the data and parameters are compatible with
            previous ones, if any, the image data are stored contiguously after
            the previous one. Parameters 'photometric' and 'planarconfig'
            are ignored. Parameters 'description', datetime', and 'extratags'
            are written to the first page of a contiguous series only.
        align : int
            Byte boundary on which to align the image data in the file.
            Default 16. Use mmap.ALLOCATIONGRANULARITY for memory-mapped data.
            Following contiguous writes are not aligned.
        truncate : bool
            If True, only write the first page including shape metadata if
            possible (uncompressed, contiguous, not tiled).
            Other TIFF readers will only be able to read part of the data.
        compress : int or 'LZMA', 'ZSTD'
            Values from 0 to 9 controlling the level of zlib compression.
            If 0 (default), data are written uncompressed.
            Compression cannot be used to write contiguous files.
            If 'LZMA' or 'ZSTD', LZMA or ZSTD compression is used, which is
            not available on all platforms.
        rowsperstrip : int
            The number of rows per strip used for compression.
            Uncompressed data are written in one strip per plane.
        predictor : bool
            If True, apply horizontal differencing to integer type images
            before compression.
        colormap : numpy.ndarray
            RGB color values for the corresponding data value.
            Must be of shape (3, 2**(data.itemsize*8)) and dtype uint16.
        description : str
            The subject of the image. Must be 7-bit ASCII. Cannot be used with
            the ImageJ format. Saved with the first page only.
        datetime : datetime
            Date and time of image creation in '%Y:%m:%d %H:%M:%S' format.
            If None (default), the current date and time is used.
            Saved with the first page only.
        resolution : (float, float[, str]) or ((int, int), (int, int)[, str])
            X and Y resolutions in pixels per resolution unit as float or
            rational numbers. A third, optional parameter specifies the
            resolution unit, which must be None (default for ImageJ),
            'INCH' (default), or 'CENTIMETER'.
        software : str
            Name of the software used to create the file. Must be 7-bit ASCII.
            Saved with the first page only.
        metadata : dict
            Additional meta data to be saved along with shape information
            in JSON or ImageJ formats in an ImageDescription tag.
            If None, do not write a second ImageDescription tag.
            Strings must be 7-bit ASCII. Saved with the first page only.
        ijmetadata : dict
            Additional meta data to be saved in application specific
            IJMetadata and IJMetadataByteCounts tags. Refer to the
            imagej_metadata_tags function for valid keys and values.
            Saved with the first page only.
        extratags : sequence of tuples
            Additional tags as [(code, dtype, count, value, writeonce)].

            code : int
                The TIFF tag Id.
            dtype : str
                Data type of items in 'value' in Python struct format.
                One of B, s, H, I, 2I, b, h, i, 2i, f, d, Q, or q.
            count : int
                Number of data values. Not used for string or byte string
                values.
            value : sequence
                'Count' values compatible with 'dtype'.
                Byte strings must contain count values of dtype packed as
                binary data.
            writeonce : bool
                If True, the tag is written to the first page only.

        """
    def close(self) -> None:
        """Write remaining pages and close file handle."""
    def __enter__(self): ...
    def __exit__(self, exc_type: type[BaseException] | None, exc_value: BaseException | None, traceback: types.TracebackType | None) -> None: ...

class TiffFile:
    """Read image and metadata from TIFF file.

    TiffFile instances must be closed using the 'close' method, which is
    automatically called when using the 'with' context manager.

    Attributes
    ----------
    pages : TiffPages
        Sequence of TIFF pages in file.
    series : list of TiffPageSeries
        Sequences of closely related TIFF pages. These are computed
        from OME, LSM, ImageJ, etc. metadata or based on similarity
        of page properties such as shape, dtype, and compression.
    byteorder : '>', '<'
        The endianness of data in the file.
        '>': big-endian (Motorola).
        '>': little-endian (Intel).
    is_flag : bool
        If True, file is of a certain format.
        Flags are: bigtiff, movie, shaped, ome, imagej, stk, lsm, fluoview,
        nih, vista, 'micromanager, metaseries, mdgel, mediacy, tvips, fei,
        sem, scn, svs, scanimage, andor, epics, pilatus, qptiff.

    All attributes are read-only.

    Examples
    --------
    >>> # read image array from TIFF file
    >>> imsave('temp.tif', numpy.random.rand(5, 301, 219))
    >>> with TiffFile('temp.tif') as tif:
    ...     data = tif.asarray()
    >>> data.shape
    (5, 301, 219)

    """
    isnative: Incomplete
    is_bigtiff: bool
    byteorder: Incomplete
    offsetsize: int
    offsetformat: Incomplete
    tagnosize: int
    tagnoformat: Incomplete
    tagsize: int
    tagformat1: Incomplete
    tagformat2: Incomplete
    pages: Incomplete
    def __init__(self, arg, name: Incomplete | None = None, offset: Incomplete | None = None, size: Incomplete | None = None, multifile: bool = True, movie: Incomplete | None = None, **kwargs) -> None:
        """Initialize instance from file.

        Parameters
        ----------
        arg : str or open file
            Name of file or open file object.
            The file objects are closed in TiffFile.close().
        name : str
            Optional name of file in case 'arg' is a file handle.
        offset : int
            Optional start position of embedded file. By default, this is
            the current file position.
        size : int
            Optional size of embedded file. By default, this is the number
            of bytes from the 'offset' to the end of the file.
        multifile : bool
            If True (default), series may include pages from multiple files.
            Currently applies to OME-TIFF only.
        movie : bool
            If True, assume that later pages differ from first page only by
            data offsets and byte counts. Significantly increases speed and
            reduces memory usage when reading movies with thousands of pages.
            Enabling this for non-movie files will result in data corruption
            or crashes. Python 3 only.
        kwargs : bool
            'is_ome': If False, disable processing of OME-XML metadata.

        """
    @property
    def filehandle(self):
        """Return file handle."""
    @property
    def filename(self):
        """Return name of file handle."""
    def fstat(self):
        """Return status of file handle as stat_result object."""
    def close(self) -> None:
        """Close open file handle(s)."""
    def asarray(self, key: Incomplete | None = None, series: Incomplete | None = None, out: Incomplete | None = None, validate: bool = True, maxworkers: int = 1):
        """Return image data from multiple TIFF pages as numpy array.

        By default, the data from the first series is returned.

        Parameters
        ----------
        key : int, slice, or sequence of page indices
            Defines which pages to return as array.
        series : int or TiffPageSeries
            Defines which series of pages to return as array.
        out : numpy.ndarray, str, or file-like object; optional
            Buffer where image data will be saved.
            If None (default), a new array will be created.
            If numpy.ndarray, a writable array of compatible dtype and shape.
            If 'memmap', directly memory-map the image data in the TIFF file
            if possible; else create a memory-mapped array in a temporary file.
            If str or open file, the file name or file object used to
            create a memory-map to an array stored in a binary file on disk.
        validate : bool
            If True (default), validate various tags.
            Passed to TiffPage.asarray().
        maxworkers : int
            Maximum number of threads to concurrently get data from pages.
            Default is 1. If None, up to half the CPU cores are used.
            Reading data from file is limited to a single thread.
            Using multiple threads can significantly speed up this function
            if the bottleneck is decoding compressed data, e.g. in case of
            large LZW compressed LSM files.
            If the bottleneck is I/O or pure Python code, using multiple
            threads might be detrimental.

        """
    def series(self):
        """Return related pages as TiffPageSeries.

        Side effect: after calling this function, TiffFile.pages might contain
        TiffPage and TiffFrame instances.

        """
    def __getattr__(self, name):
        """Return 'is_flag' attributes from first page."""
    def __enter__(self): ...
    def __exit__(self, exc_type: type[BaseException] | None, exc_value: BaseException | None, traceback: types.TracebackType | None) -> None: ...
    def flags(self):
        """Return set of file flags."""
    def is_mdgel(self):
        """File has MD Gel format."""
    @property
    def is_movie(self):
        """Return if file is a movie."""
    def shaped_metadata(self):
        """Return Tifffile metadata from JSON descriptions as dicts."""
    def ome_metadata(self):
        """Return OME XML as dict."""
    def qptiff_metadata(self):
        """Return PerkinElmer-QPI-ImageDescription XML element as dict."""
    def lsm_metadata(self):
        """Return LSM metadata from CZ_LSMINFO tag as dict."""
    def stk_metadata(self):
        """Return STK metadata from UIC tags as dict."""
    def imagej_metadata(self):
        """Return consolidated ImageJ metadata as dict."""
    def fluoview_metadata(self):
        """Return consolidated FluoView metadata as dict."""
    def nih_metadata(self):
        """Return NIH Image metadata from NIHImageHeader tag as dict."""
    def fei_metadata(self):
        """Return FEI metadata from SFEG or HELIOS tags as dict."""
    def sem_metadata(self):
        """Return SEM metadata from CZ_SEM tag as dict."""
    def mdgel_metadata(self):
        """Return consolidated metadata from MD GEL tags as dict."""
    def andor_metadata(self):
        """Return Andor tags as dict."""
    def epics_metadata(self):
        """Return EPICS areaDetector tags as dict."""
    def tvips_metadata(self):
        """Return TVIPS tag as dict."""
    def metaseries_metadata(self):
        """Return MetaSeries metadata from image description as dict."""
    def pilatus_metadata(self):
        """Return Pilatus metadata from image description as dict."""
    def micromanager_metadata(self):
        """Return consolidated MicroManager metadata as dict."""
    def scanimage_metadata(self):
        """Return ScanImage non-varying frame and ROI metadata as dict."""
    @property
    def geotiff_metadata(self):
        """Return GeoTIFF metadata from first page as dict."""

class TiffPages:
    """Sequence of TIFF image file directories."""
    parent: Incomplete
    pages: Incomplete
    complete: bool
    def __init__(self, parent) -> None:
        """Initialize instance from file. Read first TiffPage from file.

        The file position must be at an offset to an offset to a TiffPage.

        """
    @property
    def cache(self):
        """Return if pages/frames are currenly being cached."""
    @cache.setter
    def cache(self, value) -> None:
        """Enable or disable caching of pages/frames. Clear cache if False."""
    @property
    def useframes(self):
        """Return if currently using TiffFrame (True) or TiffPage (False)."""
    @useframes.setter
    def useframes(self, value) -> None:
        """Set to use TiffFrame (True) or TiffPage (False)."""
    @property
    def keyframe(self):
        """Return index of current keyframe."""
    @keyframe.setter
    def keyframe(self, index) -> None:
        """Set current keyframe. Load TiffPage from file if necessary."""
    @property
    def next_page_offset(self):
        """Return offset where offset to a new page can be stored."""
    def load(self) -> None:
        """Read all remaining pages from file."""
    def clear(self, fully: bool = True) -> None:
        """Delete all but first page from cache. Set keyframe to first page."""
    def __bool__(self) -> bool:
        """Return True if file contains any pages."""
    def __len__(self) -> int:
        """Return number of pages in file."""
    def __getitem__(self, key):
        """Return specified page(s) from cache or file."""
    def __iter__(self):
        """Return iterator over all pages."""

class TiffPage:
    """TIFF image file directory (IFD).

    Attributes
    ----------
    index : int
        Index of page in file.
    dtype : numpy.dtype or None
        Data type (native byte order) of the image in IFD.
    shape : tuple
        Dimensions of the image in IFD.
    axes : str
        Axes label codes:
        'X' width, 'Y' height, 'S' sample, 'I' image series|page|plane,
        'Z' depth, 'C' color|em-wavelength|channel, 'E' ex-wavelength|lambda,
        'T' time, 'R' region|tile, 'A' angle, 'P' phase, 'H' lifetime,
        'L' exposure, 'V' event, 'Q' unknown, '_' missing
    tags : dict
        Dictionary of tags in IFD. {tag.name: TiffTag}
    colormap : numpy.ndarray
        Color look up table, if exists.

    All attributes are read-only.

    Notes
    -----
    The internal, normalized '_shape' attribute is 6 dimensional:

    0 : number planes/images  (stk, ij).
    1 : planar samplesperpixel.
    2 : imagedepth Z  (sgi).
    3 : imagelength Y.
    4 : imagewidth X.
    5 : contig samplesperpixel.

    """
    imagewidth: int
    imagelength: int
    imagedepth: int
    tilewidth: int
    tilelength: int
    tiledepth: int
    bitspersample: int
    samplesperpixel: int
    sampleformat: int
    rowsperstrip: Incomplete
    compression: int
    planarconfig: int
    fillorder: int
    photometric: int
    predictor: int
    extrasamples: int
    colormap: Incomplete
    software: str
    description: str
    description1: str
    parent: Incomplete
    index: Incomplete
    shape: Incomplete
    dtype: Incomplete
    axes: str
    tags: Incomplete
    dataoffsets: Incomplete
    databytecounts: Incomplete
    offset: Incomplete
    def __init__(self, parent, index, keyframe: Incomplete | None = None) -> None:
        """Initialize instance from file.

        The file handle position must be at offset to a valid IFD.

        """
    def asarray(self, out: Incomplete | None = None, squeeze: bool = True, lock: Incomplete | None = None, reopen: bool = True, maxsize=..., validate: bool = True):
        """Read image data from file and return as numpy array.

        Raise ValueError if format is unsupported.

        Parameters
        ----------
        out : numpy.ndarray, str, or file-like object; optional
            Buffer where image data will be saved.
            If None (default), a new array will be created.
            If numpy.ndarray, a writable array of compatible dtype and shape.
            If 'memmap', directly memory-map the image data in the TIFF file
            if possible; else create a memory-mapped array in a temporary file.
            If str or open file, the file name or file object used to
            create a memory-map to an array stored in a binary file on disk.
        squeeze : bool
            If True, all length-1 dimensions (except X and Y) are
            squeezed out from the array.
            If False, the shape of the returned array might be different from
            the page.shape.
        lock : {RLock, NullContext}
            A reentrant lock used to syncronize reads from file.
            If None (default), the lock of the parent's filehandle is used.
        reopen : bool
            If True (default) and the parent file handle is closed, the file
            is temporarily re-opened and closed if no exception occurs.
        maxsize: int or None
            Maximum size of data before a ValueError is raised.
            Can be used to catch DOS. Default: 16 TB.
        validate : bool
            If True (default), validate various parameters.
            If None, only validate parameters and return None.

        """
    def asrgb(self, uint8: bool = False, alpha: Incomplete | None = None, colormap: Incomplete | None = None, dmin: Incomplete | None = None, dmax: Incomplete | None = None, *args, **kwargs):
        """Return image data as RGB(A).

        Work in progress.

        """
    def aspage(self): ...
    @property
    def keyframe(self): ...
    @keyframe.setter
    def keyframe(self, index) -> None: ...
    def offsets_bytecounts(self):
        """Return simplified offsets and bytecounts."""
    def is_contiguous(self):
        """Return offset and size of contiguous data, else None.

        Excludes prediction and fill_order.

        """
    def is_final(self):
        """Return if page's image data are stored in final form.

        Excludes byte-swapping.

        """
    def is_memmappable(self):
        """Return if page's image data in file can be memory-mapped."""
    def flags(self):
        """Return set of flags."""
    @property
    def ndim(self):
        """Return number of array dimensions."""
    @property
    def size(self):
        """Return number of elements in array."""
    def andor_tags(self):
        """Return consolidated metadata from Andor tags as dict.

        Remove Andor tags from self.tags.

        """
    def epics_tags(self):
        """Return consolidated metadata from EPICS areaDetector tags as dict.

        Remove areaDetector tags from self.tags.

        """
    def geotiff_tags(self):
        """Return consolidated metadata from GeoTIFF tags as dict."""
    @property
    def is_tiled(self):
        """Page contains tiled image."""
    @property
    def is_reduced(self):
        """Page is reduced image of another image."""
    @property
    def is_chroma_subsampled(self):
        """Page contains chroma subsampled image."""
    def is_imagej(self):
        """Return ImageJ description if exists, else None."""
    def is_shaped(self):
        """Return description containing array shape if exists, else None."""
    @property
    def is_mdgel(self):
        """Page contains MDFileTag tag."""
    @property
    def is_mediacy(self):
        """Page contains Media Cybernetics Id tag."""
    @property
    def is_stk(self):
        """Page contains UIC2Tag tag."""
    @property
    def is_lsm(self):
        """Page contains CZ_LSMINFO tag."""
    @property
    def is_fluoview(self):
        """Page contains FluoView MM_STAMP tag."""
    @property
    def is_nih(self):
        """Page contains NIH image header."""
    @property
    def is_sgi(self):
        """Page contains SGI image and tile depth tags."""
    @property
    def is_vista(self):
        """Software tag is 'ISS Vista'."""
    @property
    def is_metaseries(self):
        """Page contains MDS MetaSeries metadata in ImageDescription tag."""
    @property
    def is_ome(self):
        """Page contains OME-XML in ImageDescription tag."""
    @property
    def is_scn(self):
        """Page contains Leica SCN XML in ImageDescription tag."""
    @property
    def is_micromanager(self):
        """Page contains Micro-Manager metadata."""
    @property
    def is_andor(self):
        """Page contains Andor Technology tags."""
    @property
    def is_pilatus(self):
        """Page contains Pilatus tags."""
    @property
    def is_epics(self):
        """Page contains EPICS areaDetector tags."""
    @property
    def is_tvips(self):
        """Page contains TVIPS metadata."""
    @property
    def is_fei(self):
        """Page contains SFEG or HELIOS metadata."""
    @property
    def is_sem(self):
        """Page contains Zeiss SEM metadata."""
    @property
    def is_svs(self):
        """Page contains Aperio metadata."""
    @property
    def is_scanimage(self):
        """Page contains ScanImage metadata."""
    @property
    def is_qptiff(self):
        """Page contains PerkinElmer tissue images metadata."""
    @property
    def is_geotiff(self):
        """Page contains GeoTIFF metadata."""

class TiffFrame:
    """Lightweight TIFF image file directory (IFD).

    Only a limited number of tag values are read from file, e.g. StripOffsets,
    and StripByteCounts. Other tag values are assumed to be identical with a
    specified TiffPage instance, the keyframe.

    TiffFrame is intended to reduce resource usage and speed up reading data
    from file, not for introspection of metadata.

    Not compatible with Python 2.

    """
    is_mdgel: bool
    tags: Incomplete
    keyframe: Incomplete
    parent: Incomplete
    index: Incomplete
    dataoffsets: Incomplete
    databytecounts: Incomplete
    offset: Incomplete
    def __init__(self, parent, index, keyframe) -> None:
        """Read specified tags from file.

        The file handle position must be at the offset to a valid IFD.

        """
    def aspage(self):
        """Return TiffPage from file."""
    def asarray(self, *args, **kwargs):
        """Read image data from file and return as numpy array."""
    def asrgb(self, *args, **kwargs):
        """Read image data from file and return RGB image as numpy array."""
    @property
    def offsets_bytecounts(self):
        """Return simplified offsets and bytecounts."""
    @property
    def is_contiguous(self):
        """Return offset and size of contiguous data, else None."""
    @property
    def is_memmappable(self):
        """Return if page's image data in file can be memory-mapped."""
    def __getattr__(self, name):
        """Return attribute from keyframe."""

class TiffTag:
    """TIFF tag structure.

    Attributes
    ----------
    name : string
        Name of tag.
    code : int
        Decimal code of tag.
    dtype : str
        Datatype of tag data. One of TIFF DATA_FORMATS.
    count : int
        Number of values.
    value : various types
        Tag data as Python object.
    ImageSourceData : int
        Location of value in file.

    All attributes are read-only.

    """
    class Error(Exception): ...
    valueoffset: Incomplete
    code: Incomplete
    dtype: Incomplete
    count: Incomplete
    value: Incomplete
    def __init__(self, parent, tagheader, **kwargs) -> None:
        """Initialize instance from tag header."""
    @property
    def name(self): ...

class TiffFileError(ValueError): ...

class TiffPageSeries:
    """Series of TIFF pages with compatible shape and data type.

    Attributes
    ----------
    pages : list of TiffPage
        Sequence of TiffPages in series.
    dtype : numpy.dtype
        Data type (native byte order) of the image array in series.
    shape : tuple
        Dimensions of the image array in series.
    axes : str
        Labels of axes in shape. See TiffPage.axes.
    offset : int or None
        Position of image data in file if memory-mappable, else None.

    """
    index: int
    shape: Incomplete
    axes: Incomplete
    dtype: Incomplete
    stype: Incomplete
    name: Incomplete
    transform: Incomplete
    parent: Incomplete
    def __init__(self, pages, shape, dtype, axes, parent: Incomplete | None = None, name: Incomplete | None = None, transform: Incomplete | None = None, stype: Incomplete | None = None, truncated: bool = False) -> None:
        """Initialize instance."""
    def asarray(self, out: Incomplete | None = None):
        """Return image data from series of TIFF pages as numpy array."""
    def offset(self):
        """Return offset to series data in file, if any."""
    @property
    def ndim(self):
        """Return number of array dimensions."""
    @property
    def size(self):
        """Return number of elements in array."""
    @property
    def pages(self):
        """Return sequence of all pages in series."""
    def __len__(self) -> int:
        """Return number of TiffPages in series."""
    def __getitem__(self, key):
        """Return specified TiffPage."""
    def __iter__(self):
        """Return iterator over TiffPages in series."""

class TiffSequence:
    """Sequence of TIFF files.

    The image data in all files must match shape, dtype, etc.

    Attributes
    ----------
    files : list
        List of file names.
    shape : tuple
        Shape of image sequence. Excludes shape of image array.
    axes : str
        Labels of axes in shape.

    Examples
    --------
    >>> # read image stack from sequence of TIFF files
    >>> imsave('temp_C001T001.tif', numpy.random.rand(64, 64))
    >>> imsave('temp_C001T002.tif', numpy.random.rand(64, 64))
    >>> tifs = TiffSequence('temp_C001*.tif')
    >>> tifs.shape
    (1, 2)
    >>> tifs.axes
    'CT'
    >>> data = tifs.asarray()
    >>> data.shape
    (1, 2, 64, 64)

    """
    class ParseError(Exception): ...
    files: Incomplete
    imread: Incomplete
    pattern: Incomplete
    axes: str
    shape: Incomplete
    def __init__(self, files, imread=..., pattern: str = 'axes', *args, **kwargs) -> None:
        """Initialize instance from multiple files.

        Parameters
        ----------
        files : str, pathlib.Path, or sequence thereof
            Glob pattern or sequence of file names.
            Binary streams are not supported.
        imread : function or class
            Image read function or class with asarray function returning numpy
            array from single file.
        pattern : str
            Regular expression pattern that matches axes names and sequence
            indices in file names.
            By default, the pattern matches Olympus OIF and Leica TIFF series.

        """
    def __len__(self) -> int: ...
    def __enter__(self): ...
    def __exit__(self, exc_type, exc_value, traceback) -> None: ...
    def close(self) -> None: ...
    def asarray(self, out: Incomplete | None = None, *args, **kwargs):
        """Read image data from all files and return as numpy array.

        The args and kwargs parameters are passed to the imread function.

        Raise IndexError or ValueError if image shapes do not match.

        """

class FileHandle:
    """Binary file handle.

    A limited, special purpose file handler that can:

    * handle embedded files (for CZI within CZI files)
    * re-open closed files (for multi-file formats, such as OME-TIFF)
    * read and write numpy arrays and records from file like objects

    Only 'rb' and 'wb' modes are supported. Concurrently reading and writing
    of the same stream is untested.

    When initialized from another file handle, do not use it unless this
    FileHandle is closed.

    Attributes
    ----------
    name : str
        Name of the file.
    path : str
        Absolute path to file.
    size : int
        Size of file in bytes.
    is_file : bool
        If True, file has a filno and can be memory-mapped.

    All attributes are read-only.

    """
    is_file: bool
    def __init__(self, file, mode: str = 'rb', name: Incomplete | None = None, offset: Incomplete | None = None, size: Incomplete | None = None) -> None:
        """Initialize file handle from file name or another file handle.

        Parameters
        ----------
        file : str, pathlib.Path, binary stream, or FileHandle
            File name or seekable binary stream, such as an open file
            or BytesIO.
        mode : str
            File open mode in case 'file' is a file name. Must be 'rb' or 'wb'.
        name : str
            Optional name of file in case 'file' is a binary stream.
        offset : int
            Optional start position of embedded file. By default, this is
            the current file position.
        size : int
            Optional size of embedded file. By default, this is the number
            of bytes from the 'offset' to the end of the file.

        """
    def open(self) -> None:
        """Open or re-open file."""
    def read(self, size: int = -1):
        """Read 'size' bytes from file, or until EOF is reached."""
    def write(self, bytestring):
        """Write bytestring to file."""
    def flush(self):
        """Flush write buffers if applicable."""
    def memmap_array(self, dtype, shape, offset: int = 0, mode: str = 'r', order: str = 'C'):
        """Return numpy.memmap of data stored in file."""
    def read_array(self, dtype, count: int = -1, sep: str = '', chunksize=..., out: Incomplete | None = None, native: bool = False):
        '''Return numpy array from file.

        Work around numpy issue #2230, "numpy.fromfile does not accept
        StringIO object" https://github.com/numpy/numpy/issues/2230.

        '''
    def read_record(self, dtype, shape: int = 1, byteorder: Incomplete | None = None):
        """Return numpy record from file."""
    def write_empty(self, size) -> None:
        """Append size bytes to file. Position must be at end of file."""
    def write_array(self, data) -> None:
        """Write numpy array to binary file."""
    def tell(self):
        """Return file's current position."""
    def seek(self, offset, whence: int = 0) -> None:
        """Set file's current position."""
    def close(self) -> None:
        """Close file."""
    def __enter__(self): ...
    def __exit__(self, exc_type: type[BaseException] | None, exc_value: BaseException | None, traceback: types.TracebackType | None) -> None: ...
    def __getattr__(self, name):
        """Return attribute from underlying file object."""
    @property
    def name(self): ...
    @property
    def dirname(self): ...
    @property
    def path(self): ...
    @property
    def size(self): ...
    @property
    def closed(self): ...
    @property
    def lock(self): ...
    @lock.setter
    def lock(self, value) -> None: ...

class NullContext:
    """Null context manager.

    >>> with NullContext():
    ...     pass

    """
    def __enter__(self): ...
    def __exit__(self, exc_type: type[BaseException] | None, exc_value: BaseException | None, traceback: types.TracebackType | None) -> None: ...

class OpenFileCache:
    """Keep files open."""
    past: Incomplete
    files: Incomplete
    lock: Incomplete
    size: Incomplete
    def __init__(self, size, lock: Incomplete | None = None) -> None:
        """Initialize open file cache."""
    def open(self, filehandle) -> None:
        """Re-open file if necessary."""
    def close(self, filehandle) -> None:
        """Close openend file if no longer used."""
    def clear(self) -> None:
        """Close all opened files if not in use."""

class LazyConst:
    """Class whose attributes are computed on first access from its methods."""
    __doc__: Incomplete
    def __init__(self, cls) -> None: ...
    def __getattr__(self, name): ...

class TIFF:
    """Namespace for module constants."""
    def TAGS(): ...
    def TAG_NAMES(): ...
    def TAG_READERS(): ...
    def TAG_TUPLE(): ...
    def TAG_ATTRIBUTES(): ...
    def TAG_ENUM(): ...
    def FILETYPE(): ...
    def OFILETYPE(): ...
    def COMPRESSION(): ...
    def PHOTOMETRIC(): ...
    def THRESHHOLD(): ...
    def FILLORDER(): ...
    def ORIENTATION(): ...
    def PLANARCONFIG(): ...
    def GRAYRESPONSEUNIT(): ...
    def GROUP4OPT(): ...
    def RESUNIT(): ...
    def COLORRESPONSEUNIT(): ...
    def PREDICTOR(): ...
    def EXTRASAMPLE(): ...
    def SAMPLEFORMAT(): ...
    def DATATYPES(): ...
    def DATA_FORMATS(): ...
    def DATA_DTYPES(): ...
    def SAMPLE_DTYPES(): ...
    def COMPESSORS(): ...
    def DECOMPESSORS(): ...
    def FRAME_ATTRS(): ...
    def FILE_FLAGS(): ...
    def FILE_EXTENSIONS(): ...
    def FILEOPEN_FILTER(): ...
    def AXES_LABELS(): ...
    def ANDOR_TAGS(): ...
    def EXIF_TAGS(): ...
    def GPS_TAGS(): ...
    def IOP_TAGS(): ...
    def GEO_KEYS(): ...
    def GEO_CODES(): ...
    def CZ_LSMINFO(): ...
    def CZ_LSMINFO_READERS(): ...
    def CZ_LSMINFO_SCANTYPE(): ...
    def CZ_LSMINFO_DIMENSIONS(): ...
    def CZ_LSMINFO_DATATYPES(): ...
    def CZ_LSMINFO_TYPEOFDATA(): ...
    def CZ_LSMINFO_SCANINFO_ARRAYS(): ...
    def CZ_LSMINFO_SCANINFO_STRUCTS(): ...
    def CZ_LSMINFO_SCANINFO_ATTRIBUTES(): ...
    def NIH_IMAGE_HEADER(): ...
    def NIH_COLORTABLE_TYPE(): ...
    def NIH_LUTMODE_TYPE(): ...
    def NIH_CURVEFIT_TYPE(): ...
    def NIH_UNITS_TYPE(): ...
    def NIH_STACKTYPE_TYPE(): ...
    def TVIPS_HEADER_V1(): ...
    def TVIPS_HEADER_V2(): ...
    def MM_HEADER(): ...
    def MM_DIMENSIONS(): ...
    def UIC_TAGS(): ...
    def PILATUS_HEADER(): ...
    def REVERSE_BITORDER_BYTES(): ...
    def REVERSE_BITORDER_ARRAY(): ...
    def ALLOCATIONGRANULARITY(): ...

def decode_lzw(encoded):
    """Decompress LZW (Lempel-Ziv-Welch) encoded TIFF strip (byte string).

    The strip must begin with a CLEAR code and end with an EOI code.

    This implementation of the LZW decoding algorithm is described in (1) and
    is not compatible with old style LZW compressed files like quad-lzw.tif.

    """
def repeat_nd(a, repeats):
    """Return read-only view into input array with elements repeated.

    Zoom nD image by integer factors using nearest neighbor interpolation
    (box filter).

    Parameters
    ----------
    a : array_like
        Input array.
    repeats : sequence of int
        The number of repetitions to apply along each dimension of input array.

    Example
    -------
    >>> repeat_nd([[1, 2], [3, 4]], (2, 2))
    array([[1, 1, 2, 2],
           [1, 1, 2, 2],
           [3, 3, 4, 4],
           [3, 3, 4, 4]])

    """
def create_output(out, shape, dtype, mode: str = 'w+', suffix: str = '.memmap'):
    """Return numpy array where image data of shape and dtype can be copied.

    The 'out' parameter may have the following values or types:

    None
        An empty array of shape and dtype is created and returned.
    numpy.ndarray
        An existing writable array of compatible dtype and shape. A view of
        the same array is returned after verification.
    'memmap' or 'memmap:tempdir'
        A memory-map to an array stored in a temporary binary file on disk
        is created and returned.
    str or open file
        The file name or file object used to create a memory-map to an array
        stored in a binary file on disk. The created memory-mapped array is
        returned.

    """
def stripnull(string, null: bytes = b'\x00'):
    """Return string truncated at first null character.

    Clean NULL terminated C strings. For unicode strings use null='\\0'.

    >>> stripnull(b'string\\x00')
    b'string'
    >>> stripnull('string\\x00', null='\\0')
    'string'

    """
def format_size(size, threshold: int = 1536):
    """Return file size as string from byte size.

    >>> format_size(1234)
    '1234 B'
    >>> format_size(12345678901)
    '11.50 GiB'

    """
def product(iterable):
    """Return product of sequence of numbers.

    Equivalent of functools.reduce(operator.mul, iterable, 1).
    Multiplying numpy integers might overflow.

    >>> product([2**8, 2**30])
    274877906944
    >>> product([])
    1

    """
def natural_sorted(iterable):
    """Return human sorted list of strings.

    E.g. for sorting file names.

    >>> natural_sorted(['f1', 'f2', 'f10'])
    ['f1', 'f2', 'f10']

    """
def xml2dict(xml, sanitize: bool = True, prefix: Incomplete | None = None):
    '''Return XML as dict.

    >>> xml2dict(\'<?xml version="1.0" ?><root attr="name"><key>1</key></root>\')
    {\'root\': {\'key\': 1, \'attr\': \'name\'}}

    '''
def imshow(data, title: Incomplete | None = None, vmin: int = 0, vmax: Incomplete | None = None, cmap: Incomplete | None = None, bitspersample: Incomplete | None = None, photometric: str = 'RGB', interpolation: Incomplete | None = None, dpi: int = 96, figure: Incomplete | None = None, subplot: int = 111, maxdim: int = 32768, **kwargs):
    """Plot n-dimensional images using matplotlib.pyplot.

    Return figure, subplot and plot axis.
    Requires pyplot already imported C{from matplotlib import pyplot}.

    Parameters
    ----------
    bitspersample : int or None
        Number of bits per channel in integer RGB images.
    photometric : {'MINISWHITE', 'MINISBLACK', 'RGB', or 'PALETTE'}
        The color space of the image data.
    title : str
        Window and subplot title.
    figure : matplotlib.figure.Figure (optional).
        Matplotlib to use for plotting.
    subplot : int
        A matplotlib.pyplot.subplot axis.
    maxdim : int
        maximum image width and length.
    kwargs : optional
        Arguments for matplotlib.pyplot.imshow.

    """
inttypes = int
unicode = str
print_ = print
