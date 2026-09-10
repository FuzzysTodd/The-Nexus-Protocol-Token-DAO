import numpy as np
from ..core import Request as Request
from ..core.request import IOMode as IOMode, InitializationError as InitializationError, URI_BYTES as URI_BYTES
from ..core.v3_plugin_api import ImageProperties as ImageProperties, PluginV3 as PluginV3
from typing import Any, Dict, List, Tuple

class PyAVPlugin(PluginV3):
    """Support for pyAV as backend.

    Parameters
    ----------
    request : iio.Request
        A request object that represents the users intent. It provides a
        standard interface to access various the various ImageResources and
        serves them to the plugin as a file object (or file). Check the docs for
        details.

    """
    frames_written: int
    def __init__(self, request: Request, *, container: str = None) -> None:
        """Initialize a new Plugin Instance.

        See Plugin's docstring for detailed documentation.

        Notes
        -----
        The implementation here stores the request as a local variable that is
        exposed using a @property below. If you inherit from PluginV3, remember
        to call ``super().__init__(request)``.

        """
    def read(self, *, index: int = ..., format: str = 'rgb24', filter_sequence: List[Tuple[str, str | dict]] = None, filter_graph: Tuple[dict, List] = None, constant_framerate: bool = None, thread_count: int = 0, thread_type: str = None) -> np.ndarray:
        '''Read frames from the video.

        If ``index`` is an integer, this function reads the index-th frame from
        the file. If ``index`` is ... (Ellipsis), this function reads all frames
        from the video, stacks them along the first dimension, and returns a
        batch of frames.

        Parameters
        ----------
        index : int
            The index of the frame to read, e.g. ``index=5`` reads the 5th
            frame. If ``...``, read all the frames in the video and stack them
            along a new, prepended, batch dimension.
        format : str
            Set the returned colorspace. If not None (default: rgb24), convert
            the data into the given format before returning it. If ``None``
            return the data in the encoded format if it can be expressed as a
            strided array; otherwise raise an Exception.
        filter_sequence : List[str, str, dict]
            If not None, apply the given sequence of FFmpeg filters to each
            ndimage. Check the (module-level) plugin docs for details and
            examples.
        filter_graph : (dict, List)
            If not None, apply the given graph of FFmpeg filters to each
            ndimage. The graph is given as a tuple of two dicts. The first dict
            contains a (named) set of nodes, and the second dict contains a set
            of edges between nodes of the previous dict. Check the (module-level)
            plugin docs for details and examples.
        constant_framerate : bool
            If True assume the video\'s framerate is constant. This allows for
            faster seeking inside the file. If False, the video is reset before
            each read and searched from the beginning. If None (default), this
            value will be read from the container format.
        thread_count : int
            How many threads to use when decoding a frame. The default is 0,
            which will set the number using ffmpeg\'s default, which is based on
            the codec, number of available cores, threadding model, and other
            considerations.
        thread_type : str
            The threading model to be used. One of

            - `"SLICE"`: threads assemble parts of the current frame
            - `"FRAME"`: threads may assemble future frames
            - None (default): Uses ``"FRAME"`` if ``index=...`` and ffmpeg\'s
              default otherwise.


        Returns
        -------
        frame : np.ndarray
            A numpy array containing loaded frame data.

        Notes
        -----
        Accessing random frames repeatedly is costly (O(k), where k is the
        average distance between two keyframes). You should do so only sparingly
        if possible. In some cases, it can be faster to bulk-read the video (if
        it fits into memory) and to then access the returned ndarray randomly.

        The current implementation may cause problems for b-frames, i.e.,
        bidirectionaly predicted pictures. I lack test videos to write unit
        tests for this case.

        Reading from an index other than ``...``, i.e. reading a single frame,
        currently doesn\'t support filters that introduce delays.

        '''
    def iter(self, *, format: str = 'rgb24', filter_sequence: List[Tuple[str, str | dict]] = None, filter_graph: Tuple[dict, List] = None, thread_count: int = 0, thread_type: str = None) -> np.ndarray:
        '''Yield frames from the video.

        Parameters
        ----------
        frame : np.ndarray
            A numpy array containing loaded frame data.
        format : str
            Convert the data into the given format before returning it. If None,
            return the data in the encoded format if it can be expressed as a
            strided array; otherwise raise an Exception.
        filter_sequence : List[str, str, dict]
            Set the returned colorspace. If not None (default: rgb24), convert
            the data into the given format before returning it. If ``None``
            return the data in the encoded format if it can be expressed as a
            strided array; otherwise raise an Exception.
        filter_graph : (dict, List)
            If not None, apply the given graph of FFmpeg filters to each
            ndimage. The graph is given as a tuple of two dicts. The first dict
            contains a (named) set of nodes, and the second dict contains a set
            of edges between nodes of the previous dict. Check the (module-level)
            plugin docs for details and examples.
        thread_count : int
            How many threads to use when decoding a frame. The default is 0,
            which will set the number using ffmpeg\'s default, which is based on
            the codec, number of available cores, threadding model, and other
            considerations.
        thread_type : str
            The threading model to be used. One of

            - `"SLICE"` (default): threads assemble parts of the current frame
            - `"FRAME"`: threads may assemble future frames (faster for bulk reading)


        Yields
        ------
        frame : np.ndarray
            A (decoded) video frame.


        '''
    def write(self, ndimage: np.ndarray | List[np.ndarray], *, codec: str = None, is_batch: bool = True, fps: int = 24, in_pixel_format: str = 'rgb24', out_pixel_format: str = None, filter_sequence: List[Tuple[str, str | dict]] = None, filter_graph: Tuple[dict, List] = None) -> bytes | None:
        '''Save a ndimage as a video.

        Given a batch of frames (stacked along the first axis) or a list of
        frames, encode them and add the result to the ImageResource.

        Parameters
        ----------
        ndimage : ArrayLike, List[ArrayLike]
            The ndimage to encode and write to the ImageResource.
        codec : str
            The codec to use when encoding frames. Only needed on first write
            and ignored on subsequent writes.
        is_batch : bool
            If True (default), the ndimage is a batch of images, otherwise it is
            a single image. This parameter has no effect on lists of ndimages.
        fps : str
            The resulting videos frames per second.
        in_pixel_format : str
            The pixel format of the incoming ndarray. Defaults to "rgb24" and can
            be any stridable pix_fmt supported by FFmpeg.
        out_pixel_format : str
            The pixel format to use while encoding frames. If None (default)
            use the codec\'s default.
        filter_sequence : List[str, str, dict]
            If not None, apply the given sequence of FFmpeg filters to each
            ndimage. Check the (module-level) plugin docs for details and
            examples.
        filter_graph : (dict, List)
            If not None, apply the given graph of FFmpeg filters to each
            ndimage. The graph is given as a tuple of two dicts. The first dict
            contains a (named) set of nodes, and the second dict contains a set
            of edges between nodes of the previous dict. Check the (module-level)
            plugin docs for details and examples.

        Returns
        -------
        encoded_image : bytes or None
            If the chosen ImageResource is the special target ``"<bytes>"`` then
            write will return a byte string containing the encoded image data.
            Otherwise, it returns None.

        Notes
        -----
        When writing ``<bytes>``, the video is finalized immediately after the
        first write call and calling write multiple times to append frames is
        not possible.

        '''
    def properties(self, index: int = ..., *, format: str = 'rgb24') -> ImageProperties:
        """Standardized ndimage metadata.

        Parameters
        ----------
        index : int
            The index of the ndimage for which to return properties. If ``...``
            (Ellipsis, default), return the properties for the resulting batch
            of frames.
        format : str
            If not None (default: rgb24), convert the data into the given format
            before returning it. If None return the data in the encoded format
            if that can be expressed as a strided array; otherwise raise an
            Exception.

        Returns
        -------
        properties : ImageProperties
            A dataclass filled with standardized image metadata.

        Notes
        -----
        This function is efficient and won't process any pixel data.

        The provided metadata does not include modifications by any filters
        (through ``filter_sequence`` or ``filter_graph``).

        """
    def metadata(self, index: int = ..., exclude_applied: bool = True, constant_framerate: bool = None) -> Dict[str, Any]:
        """Format-specific metadata.

        Returns a dictionary filled with metadata that is either stored in the
        container, the video stream, or the frame's side-data.

        Parameters
        ----------
        index : int
            If ... (Ellipsis, default) return global metadata (the metadata
            stored in the container and video stream). If not ..., return the
            side data stored in the frame at the given index.
        exclude_applied : bool
            Currently, this parameter has no effect. It exists for compliance with
            the ImageIO v3 API.
        constant_framerate : bool
            If True assume the video's framerate is constant. This allows for
            faster seeking inside the file. If False, the video is reset before
            each read and searched from the beginning. If None (default), this
            value will be read from the container format.

        Returns
        -------
        metadata : dict
            A dictionary filled with format-specific metadata fields and their
            values.

        """
    def close(self) -> None:
        """Close the Video."""
    def __enter__(self) -> PyAVPlugin: ...
    def init_video_stream(self, codec: str, *, fps: float = 24, pixel_format: str = None, max_keyframe_interval: int = None, force_keyframes: bool = None) -> None:
        '''Initialize a new video stream.

        This function adds a new video stream to the ImageResource using the
        selected encoder (codec), framerate, and colorspace.

        Parameters
        ----------
        codec : str
            The codec to use, e.g. ``"x264"`` or ``"vp9"``.
        fps : float
            The desired framerate of the video stream (frames per second).
        pixel_format : str
            The pixel format to use while encoding frames. If None (default) use
            the codec\'s default.
        max_keyframe_interval : int
            The maximum distance between two intra frames (I-frames). Also known
            as GOP size. If unspecified use the codec\'s default. Note that not
            every I-frame is a keyframe; see the notes for details.
        force_keyframes : bool
            If True, limit inter frames dependency to frames within the current
            keyframe interval (GOP), i.e., force every I-frame to be a keyframe.
            If unspecified, use the codec\'s default.

        Notes
        -----
        You can usually leave ``max_keyframe_interval`` and ``force_keyframes``
        at their default values, unless you try to generate seek-optimized video
        or have a similar specialist use-case. In this case, ``force_keyframes``
        controls the ability to seek to _every_ I-frame, and
        ``max_keyframe_interval`` controls how close to a random frame you can
        seek. Low values allow more fine-grained seek at the expense of
        file-size (and thus I/O performance).

        '''
    def write_frame(self, frame: np.ndarray, *, pixel_format: str = 'rgb24') -> None:
        """Add a frame to the video stream.

        This function appends a new frame to the video. It assumes that the
        stream previously has been initialized. I.e., ``init_video_stream`` has
        to be called before calling this function for the write to succeed.

        Parameters
        ----------
        frame : np.ndarray
            The image to be appended/written to the video stream.
        pixel_format : str
            The colorspace (pixel format) of the incoming frame.

        Notes
        -----
        Frames may be held in a buffer, e.g., by the filter pipeline used during
        writing or by FFMPEG to batch them prior to encoding. Make sure to
        ``.close()`` the plugin or to use a context manager to ensure that all
        frames are written to the ImageResource.

        """
    def set_video_filter(self, filter_sequence: List[Tuple[str, str | dict]] = None, filter_graph: Tuple[dict, List] = None) -> None:
        """Set the filter(s) to use.

        This function creates a new FFMPEG filter graph to use when reading or
        writing video. In the case of reading, frames are passed through the
        filter graph before begin returned and, in case of writing, frames are
        passed through the filter before being written to the video.

        Parameters
        ----------
        filter_sequence : List[str, str, dict]
            If not None, apply the given sequence of FFmpeg filters to each
            ndimage. Check the (module-level) plugin docs for details and
            examples.
        filter_graph : (dict, List)
            If not None, apply the given graph of FFmpeg filters to each
            ndimage. The graph is given as a tuple of two dicts. The first dict
            contains a (named) set of nodes, and the second dict contains a set
            of edges between nodes of the previous dict. Check the
            (module-level) plugin docs for details and examples.

        Notes
        -----
        Changing a filter graph with lag during reading or writing will
        currently cause frames in the filter queue to be lost.

        """
    @property
    def container_metadata(self):
        """Container-specific metadata.

        A dictionary containing metadata stored at the container level.

        """
    @property
    def video_stream_metadata(self):
        """Stream-specific metadata.

        A dictionary containing metadata stored at the stream level.

        """
