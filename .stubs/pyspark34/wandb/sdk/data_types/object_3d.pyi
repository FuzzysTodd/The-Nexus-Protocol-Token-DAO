import numpy as np
from . import _dtypes
from ..wandb_run import Run as LocalRun
from ._private import MEDIA_TMP as MEDIA_TMP
from .base_types.media import BatchableMedia as BatchableMedia
from _typeshed import Incomplete
from typing import ClassVar, Sequence, Set, TextIO, Tuple, TypedDict
from wandb import util as util
from wandb.sdk.artifacts.artifact import Artifact as Artifact
from wandb.sdk.lib import runid as runid
from wandb.sdk.lib.paths import LogicalPath as LogicalPath

numeric: Incomplete
FileFormat3D: Incomplete
Point3D = Tuple[numeric, numeric, numeric]
Point3DWithCategory = Tuple[numeric, numeric, numeric, numeric]
Point3DWithColors = Tuple[numeric, numeric, numeric, numeric, numeric, numeric]
Point = Point3D | Point3DWithCategory | Point3DWithColors
PointCloudType: Incomplete
RGBColor = Tuple[int, int, int]

class Box3D(TypedDict):
    corners: Tuple[Point3D, Point3D, Point3D, Point3D, Point3D, Point3D, Point3D, Point3D]
    label: str | None
    color: RGBColor
    score: numeric | None

class Vector3D(TypedDict):
    start: Sequence[Point3D]
    end: Sequence[Point3D]

class Camera(TypedDict):
    viewpoint: Sequence[Point3D]
    target: Sequence[Point3D]

class Object3D(BatchableMedia):
    """Wandb class for 3D point clouds.

    Arguments:
        data_or_path: (numpy array, string, io)
            Object3D can be initialized from a file or a numpy array.

            You can pass a path to a file or an io object and a file_type
            which must be one of SUPPORTED_TYPES

    The shape of the numpy array must be one of either:
    ```
    [[x y z],       ...] nx3
    [[x y z c],     ...] nx4 where c is a category with supported range [1, 14]
    [[x y z r g b], ...] nx6 where is rgb is color
    ```
    """
    SUPPORTED_TYPES: ClassVar[Set[str]]
    SUPPORTED_POINT_CLOUD_TYPES: ClassVar[Set[str]]
    def __init__(self, data_or_path: np.ndarray | str | TextIO | dict, **kwargs: str | FileFormat3D | None) -> None: ...
    @classmethod
    def from_file(cls, data_or_path: TextIO | str, file_type: FileFormat3D | None = None) -> Object3D:
        '''Initializes Object3D from a file or stream.

        Arguments:
            data_or_path (Union["TextIO", str]): A path to a file or a `TextIO` stream.
            file_type (str): Specifies the data format passed to `data_or_path`. Required when `data_or_path` is a
                `TextIO` stream. This parameter is ignored if a file path is provided. The type is taken from the file extension.
        '''
    @classmethod
    def from_numpy(cls, data: np.ndarray) -> Object3D:
        """Initializes Object3D from a numpy array.

        Arguments:
            data (numpy array): Each entry in the array will
                represent one point in the point cloud.


        The shape of the numpy array must be one of either:
        ```
        [[x y z],       ...]  # nx3.
        [[x y z c],     ...]  # nx4 where c is a category with supported range [1, 14].
        [[x y z r g b], ...]  # nx6 where is rgb is color.
        ```
        """
    @classmethod
    def from_point_cloud(cls, points: Sequence['Point'], boxes: Sequence['Box3D'], vectors: Sequence['Vector3D'] | None = None, point_cloud_type: PointCloudType = 'lidar/beta') -> Object3D:
        '''Initializes Object3D from a python object.

        Arguments:
            points (Sequence["Point"]): The points in the point cloud.
            boxes (Sequence["Box3D"]): 3D bounding boxes for labeling the point cloud. Boxes
            are displayed in point cloud visualizations.
            vectors (Optional[Sequence["Vector3D"]]): Each vector is displayed in the point cloud
                visualization. Can be used to indicate directionality of bounding boxes. Defaults to None.
            point_cloud_type ("lidar/beta"): At this time, only the "lidar/beta" type is supported. Defaults to "lidar/beta".
        '''
    @classmethod
    def get_media_subdir(cls) -> str: ...
    def to_json(self, run_or_artifact: LocalRun | Artifact) -> dict: ...
    @classmethod
    def seq_to_json(cls, seq: Sequence['BatchableMedia'], run: LocalRun, key: str, step: int | str) -> dict: ...

class _Object3DFileType(_dtypes.Type):
    name: str
    types: Incomplete
