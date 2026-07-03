import numpy as np
from ..core.request import IOMode as IOMode, InitializationError as InitializationError, Request as Request
from ..core.v3_plugin_api import ImageProperties as ImageProperties, PluginV3 as PluginV3
from _typeshed import Incomplete
from datetime import datetime
from typing import Any, Callable, Dict, Iterator, List, Mapping, Sequence, Tuple

logger: Incomplete

class Spec:
    '''SPE file specification data

    Tuples of (offset, datatype, count), where offset is the offset in the SPE
    file and datatype is the datatype as used in `numpy.fromfile`()

    `data_start` is the offset of actual image data.

    `dtypes` translates SPE datatypes (0...4) to numpy ones, e. g. dtypes[0]
    is dtype("<f") (which is np.float32).

    `controllers` maps the `type` metadata to a human readable name

    `readout_modes` maps the `readoutMode` metadata to something human readable
    although this may not be accurate since there is next to no documentation
    to be found.
    '''
    basic: Incomplete
    metadata: Incomplete
    data_start: int
    dtypes: Incomplete
    controllers: Incomplete
    readout_modes: Incomplete
    no_decode: Incomplete

class SDTControlSpec:
    """Extract metadata written by the SDT-control software

    Some of it is encoded in the comment strings
    (see :py:meth:`parse_comments`). Also, date and time are encoded in a
    peculiar way (see :py:meth:`get_datetime`). Use :py:meth:`extract_metadata`
    to update the metadata dict.
    """
    months: Incomplete
    sequence_types: Incomplete
    class CommentDesc:
        """Describe how to extract a metadata entry from a comment string"""
        n: int
        slice: slice
        cvt: Callable[[str], Any]
        scale: None | float
        def __init__(self, n: int, slice: slice, cvt: Callable[[str], Any] = ..., scale: float | None = None) -> None: ...
    comment_fields: Incomplete
    @staticmethod
    def get_comment_version(comments: Sequence[str]) -> Tuple[int, int]:
        '''Get the version of SDT-control metadata encoded in the comments

        Parameters
        ----------
        comments
            List of SPE file comments, typically ``metadata["comments"]``.

        Returns
        -------
        Major and minor version. ``-1, -1`` if detection failed.
        '''
    @staticmethod
    def parse_comments(comments: Sequence[str], version: Tuple[int, int]) -> Dict[str, Any]:
        '''Extract SDT-control metadata from comments

        Parameters
        ----------
        comments
            List of SPE file comments, typically ``metadata["comments"]``.
        version
            Major and minor version of SDT-control metadata format

        Returns
        -------
        Dict of metadata
        '''
    @staticmethod
    def get_datetime(date: str, time: str) -> datetime | None:
        '''Turn date and time saved by SDT-control into proper datetime object

        Parameters
        ----------
        date
            SPE file date, typically ``metadata["date"]``.
        time
            SPE file date, typically ``metadata["time_local"]``.

        Returns
        -------
        File\'s datetime if parsing was succsessful, else None.
        '''
    @staticmethod
    def extract_metadata(meta: Mapping, char_encoding: str = 'latin1'):
        """Extract SDT-control metadata from SPE metadata

        SDT-control stores some metadata in comments and other fields.
        Extract them and remove unused entries.

        Parameters
        ----------
        meta
            SPE file metadata. Modified in place.
        char_encoding
            Character encoding used to decode strings in the metadata.
        """

class SpePlugin(PluginV3):
    def __init__(self, request: Request, check_filesize: bool = True, char_encoding: str | None = None, sdt_meta: bool | None = None) -> None:
        """Instantiate a new SPE file plugin object

        Parameters
        ----------
        request : Request
            A request object representing the resource to be operated on.
        check_filesize : bool
            If True, compute the number of frames from the filesize, compare it
            to the frame count in the file header, and raise a warning if the
            counts don't match. (Certain software may create files with
        char_encoding : str
            Deprecated. Exists for backwards compatibility; use ``char_encoding`` of
            ``metadata`` instead.
        sdt_meta : bool
            Deprecated. Exists for backwards compatibility; use ``sdt_control`` of
            ``metadata`` instead.

        """
    def read(self, *, index: int = ...) -> np.ndarray:
        """Read a frame or all frames from the file

        Parameters
        ----------
        index : int
            Select the index-th frame from the file. If index is `...`,
            select all frames and stack them along a new axis.

        Returns
        -------
        A Numpy array of pixel values.

        """
    def iter(self) -> Iterator[np.ndarray]:
        """Iterate over the frames in the file

        Yields
        ------
        A Numpy array of pixel values.
        """
    def metadata(self, index: int = ..., exclude_applied: bool = True, char_encoding: str = 'latin1', sdt_control: bool = True) -> Dict[str, Any]:
        '''SPE specific metadata.

        Parameters
        ----------
        index : int
            Ignored as SPE files only store global metadata.
        exclude_applied : bool
            Ignored. Exists for API compatibility.
        char_encoding : str
            The encoding to use when parsing strings.
        sdt_control : bool
            If `True`, decode special metadata written by the
            SDT-control software if present.

        Returns
        -------
        metadata : dict
            Key-value pairs of metadata.

        Notes
        -----
        SPE v3 stores metadata as XML, whereas SPE v2 uses a binary format.

        .. rubric:: Supported SPE v2 Metadata fields

        ROIs : list of dict
            Regions of interest used for recording images. Each dict has the
            "top_left" key containing x and y coordinates of the top left corner,
            the "bottom_right" key with x and y coordinates of the bottom right
            corner, and the "bin" key with number of binned pixels in x and y
            directions.
        comments : list of str
            The SPE format allows for 5 comment strings of 80 characters each.
        controller_version : int
            Hardware version
        logic_output : int
            Definition of output BNC
        amp_hi_cap_low_noise : int
            Amp switching mode
        mode : int
            Timing mode
        exp_sec : float
            Alternative exposure in seconds
        date : str
            Date string
        detector_temp : float
            Detector temperature
        detector_type : int
            CCD / diode array type
        st_diode : int
            Trigger diode
        delay_time : float
            Used with async mode
        shutter_control : int
            Normal, disabled open, or disabled closed
        absorb_live : bool
            on / off
        absorb_mode : int
            Reference strip or file
        can_do_virtual_chip : bool
            True or False whether chip can do virtual chip
        threshold_min_live : bool
            on / off
        threshold_min_val : float
            Threshold minimum value
        threshold_max_live : bool
            on / off
        threshold_max_val : float
            Threshold maximum value
        time_local : str
            Experiment local time
        time_utc : str
            Experiment UTC time
        adc_offset : int
            ADC offset
        adc_rate : int
            ADC rate
        adc_type : int
            ADC type
        adc_resolution : int
            ADC resolution
        adc_bit_adjust : int
            ADC bit adjust
        gain : int
            gain
        sw_version : str
            Version of software which created this file
        spare_4 : bytes
            Reserved space
        readout_time : float
            Experiment readout time
        type : str
            Controller type
        clockspeed_us : float
            Vertical clock speed in microseconds
        readout_mode : ["full frame", "frame transfer", "kinetics", ""]
            Readout mode. Empty string means that this was not set by the
            Software.
        window_size : int
            Window size for Kinetics mode
        file_header_ver : float
            File header version
        chip_size : [int, int]
            x and y dimensions of the camera chip
        virt_chip_size : [int, int]
            Virtual chip x and y dimensions
        pre_pixels : [int, int]
            Pre pixels in x and y dimensions
        post_pixels : [int, int],
            Post pixels in x and y dimensions
        geometric : list of {"rotate", "reverse", "flip"}
            Geometric operations
        sdt_major_version : int
            (only for files created by SDT-control)
            Major version of SDT-control software
        sdt_minor_version : int
            (only for files created by SDT-control)
            Minor version of SDT-control software
        sdt_controller_name : str
            (only for files created by SDT-control)
            Controller name
        exposure_time : float
            (only for files created by SDT-control)
            Exposure time in seconds
        color_code : str
            (only for files created by SDT-control)
            Color channels used
        detection_channels : int
            (only for files created by SDT-control)
            Number of channels
        background_subtraction : bool
            (only for files created by SDT-control)
            Whether background subtraction war turned on
        em_active : bool
            (only for files created by SDT-control)
            Whether EM was turned on
        em_gain : int
            (only for files created by SDT-control)
            EM gain
        modulation_active : bool
            (only for files created by SDT-control)
            Whether laser modulation (“attenuate”) was turned on
        pixel_size : float
            (only for files created by SDT-control)
            Camera pixel size
        sequence_type : str
            (only for files created by SDT-control)
            Type of sequnce (standard, TOCCSL, arbitrary, …)
        grid : float
            (only for files created by SDT-control)
            Sequence time unit (“grid size”) in seconds
        n_macro : int
            (only for files created by SDT-control)
            Number of macro loops
        delay_macro : float
            (only for files created by SDT-control)
            Time between macro loops in seconds
        n_mini : int
            (only for files created by SDT-control)
            Number of mini loops
        delay_mini : float
            (only for files created by SDT-control)
            Time between mini loops in seconds
        n_micro : int (only for files created by SDT-control)
            Number of micro loops
        delay_micro : float (only for files created by SDT-control)
            Time between micro loops in seconds
        n_subpics : int
            (only for files created by SDT-control)
            Number of sub-pictures
        delay_shutter : float
            (only for files created by SDT-control)
            Camera shutter delay in seconds
        delay_prebleach : float
            (only for files created by SDT-control)
            Pre-bleach delay in seconds
        bleach_time : float
            (only for files created by SDT-control)
            Bleaching time in seconds
        recovery_time : float
            (only for files created by SDT-control)
            Recovery time in seconds
        comment : str
            (only for files created by SDT-control)
            User-entered comment. This replaces the "comments" field.
        datetime : datetime.datetime
            (only for files created by SDT-control)
            Combines the "date" and "time_local" keys. The latter two plus
            "time_utc" are removed.
        modulation_script : str
            (only for files created by SDT-control)
            Laser modulation script. Replaces the "spare_4" key.
        bleach_piezo_active : bool
            (only for files created by SDT-control)
            Whether piezo for bleaching was enabled
        '''
    def properties(self, index: int = ...) -> ImageProperties:
        """Standardized ndimage metadata.

        Parameters
        ----------
        index : int
            If the index is an integer, select the index-th frame and return
            its properties. If index is an Ellipsis (...), return the
            properties of all frames in the file stacked along a new batch
            dimension.

        Returns
        -------
        properties : ImageProperties
            A dataclass filled with standardized image metadata.
        """

def roi_array_to_dict(a: np.ndarray) -> List[Dict[str, List[int]]]:
    '''Convert the `ROIs` structured arrays to :py:class:`dict`

    Parameters
    ----------
    a
        Structured array containing ROI data

    Returns
    -------
    One dict per ROI. Keys are "top_left", "bottom_right", and "bin",
    values are tuples whose first element is the x axis value and the
    second element is the y axis value.
    '''
