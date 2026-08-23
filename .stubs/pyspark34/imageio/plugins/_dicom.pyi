from _typeshed import Incomplete

logger: Incomplete
sys_is_little_endian: Incomplete
MINIDICT: Incomplete
ItemTag: Incomplete
ItemDelimiterTag: Incomplete
SequenceDelimiterTag: Incomplete
GROUPS: Incomplete
VRS: Incomplete

class NotADicomFile(Exception): ...
class CompressedDicom(RuntimeError): ...

class SimpleDicomReader:
    '''
    This class provides reading of pixel data from DICOM files. It is
    focussed on getting the pixel data, not the meta info.

    To use, first create an instance of this class (giving it
    a file object or filename). Next use the info attribute to
    get a dict of the meta data. The loading of pixel data is
    deferred until get_numpy_array() is called.

    Comparison with Pydicom
    -----------------------

    This code focusses on getting the pixel data out, which allows some
    shortcuts, resulting in the code being much smaller.

    Since the processing of data elements is much cheaper (it skips a lot
    of tags), this code is about 3x faster than pydicom (except for the
    deflated DICOM files).

    This class does borrow some code (and ideas) from the pydicom
    project, and (to the best of our knowledge) has the same limitations
    as pydicom with regard to the type of files that it can handle.

    Limitations
    -----------

    For more advanced DICOM processing, please check out pydicom.

      * Only a predefined subset of data elements (meta information) is read.
      * This is a reader; it can not write DICOM files.
      * (just like pydicom) it can handle none of the compressed DICOM
        formats except for "Deflated Explicit VR Little Endian"
        (1.2.840.10008.1.2.1.99).

    '''
    is_implicit_VR: bool
    is_little_endian: bool
    def __init__(self, file) -> None: ...
    @property
    def info(self): ...
    def __iter__(self): ...
    def __getattr__(self, key): ...
    def get_numpy_array(self):
        """Get numpy arra for this DICOM file, with the correct shape,
        and pixel values scaled appropriately.
        """

class DicomSeries:
    """DicomSeries
    This class represents a serie of dicom files (SimpleDicomReader
    objects) that belong together. If these are multiple files, they
    represent the slices of a volume (like for CT or MRI).
    """
    def __init__(self, suid, progressIndicator) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self): ...
    def __getitem__(self, index): ...
    @property
    def suid(self): ...
    @property
    def shape(self):
        """The shape of the data (nz, ny, nx)."""
    @property
    def sampling(self):
        """The sampling (voxel distances) of the data (dz, dy, dx)."""
    @property
    def info(self):
        """A dictionary containing the information as present in the
        first dicomfile of this serie. None if there are no entries."""
    @property
    def description(self):
        """A description of the dicom series. Used fields are
        PatientName, shape of the data, SeriesDescription, and
        ImageComments.
        """
    def get_numpy_array(self):
        """Get (load) the data that this DicomSeries represents, and return
        it as a numpy array. If this serie contains multiple images, the
        resulting array is 3D, otherwise it's 2D.
        """

def list_files(files, path) -> None:
    """List all files in the directory, recursively."""
def process_directory(request, progressIndicator, readPixelData: bool = False):
    """
    Reads dicom files and returns a list of DicomSeries objects, which
    contain information about the data, and can be used to load the
    image or volume data.

    if readPixelData is True, the pixel data of all series is read. By
    default the loading of pixeldata is deferred until it is requested
    using the DicomSeries.get_pixel_array() method. In general, both
    methods should be equally fast.
    """
def splitSerieIfRequired(serie, series, progressIndicator) -> None:
    """
    Split the serie in multiple series if this is required. The choice
    is based on examing the image position relative to the previous
    image. If it differs too much, it is assumed that there is a new
    dataset. This can happen for example in unspitted gated CT data.
    """
