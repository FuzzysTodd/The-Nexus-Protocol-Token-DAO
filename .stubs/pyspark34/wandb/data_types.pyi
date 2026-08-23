from .sdk.data_types import _dtypes
from .sdk.data_types.base_types.media import BatchableMedia, Media
from .sdk.data_types.base_types.wb_value import WBValue
from .sdk.data_types.helper_types.bounding_boxes_2d import BoundingBoxes2D as BoundingBoxes2D
from .sdk.data_types.helper_types.classes import Classes as Classes
from .sdk.data_types.helper_types.image_mask import ImageMask as ImageMask
from .sdk.data_types.histogram import Histogram as Histogram
from .sdk.data_types.html import Html as Html
from .sdk.data_types.image import Image as Image
from .sdk.data_types.molecule import Molecule as Molecule
from .sdk.data_types.object_3d import Object3D as Object3D
from .sdk.data_types.plotly import Plotly as Plotly
from .sdk.data_types.saved_model import _SavedModel as _SavedModel
from .sdk.data_types.trace_tree import WBTraceTree as WBTraceTree
from .sdk.data_types.video import Video as Video
from _typeshed import Incomplete
from collections.abc import Generator

__all__ = ['Audio', 'Table', 'Bokeh', 'Histogram', 'Html', 'Image', 'Molecule', 'Object3D', 'Plotly', 'Video', 'WBTraceTree', '_SavedModel', 'ImageMask', 'BoundingBoxes2D', 'Classes']

class _TableLinkMixin:
    def set_table(self, table) -> None: ...

class _TableKey(str, _TableLinkMixin):
    def set_table(self, table, col_name) -> None: ...

class _TableIndex(int, _TableLinkMixin):
    def get_row(self): ...

class Table(Media):
    '''The Table class used to display and analyze tabular data.

    Unlike traditional spreadsheets, Tables support numerous types of data:
    scalar values, strings, numpy arrays, and most subclasses of `wandb.data_types.Media`.
    This means you can embed `Images`, `Video`, `Audio`, and other sorts of rich, annotated media
    directly in Tables, alongside other traditional scalar values.

    This class is the primary class used to generate the Table Visualizer
    in the UI: https://docs.wandb.ai/guides/data-vis/tables.

    Tables can be constructed with initial data using the `data` or
    `dataframe` parameters:
    <!--yeadoc-test:table-construct-dataframe-->
    ```python
    import pandas as pd
    import wandb

    data = {"users": ["geoff", "juergen", "ada"], "feature_01": [1, 117, 42]}
    df = pd.DataFrame(data)

    tbl = wandb.Table(data=df)
    assert all(tbl.get_column("users") == df["users"])
    assert all(tbl.get_column("feature_01") == df["feature_01"])
    ```

    Additionally, users can add data to Tables incrementally by using the
    `add_data`, `add_column`, and `add_computed_column` functions for
    adding rows, columns, and columns computed from data in other columns, respectively:
    <!--yeadoc-test:table-construct-rowwise-->
    ```python
    import wandb

    tbl = wandb.Table(columns=["user"])

    users = ["geoff", "juergen", "ada"]

    [tbl.add_data(user) for user in users]
    assert tbl.get_column("user") == users


    def get_user_name_length(index, row):
        return {"feature_01": len(row["user"])}


    tbl.add_computed_columns(get_user_name_length)
    assert tbl.get_column("feature_01") == [5, 7, 3]
    ```

    Tables can be logged directly to runs using `run.log({"my_table": table})`
    or added to artifacts using `artifact.add(table, "my_table")`:
    <!--yeadoc-test:table-logging-direct-->
    ```python
    import numpy as np
    import wandb

    wandb.init()

    tbl = wandb.Table(columns=["image", "label"])

    images = np.random.randint(0, 255, [2, 100, 100, 3], dtype=np.uint8)
    labels = ["panda", "gibbon"]
    [tbl.add_data(wandb.Image(image), label) for image, label in zip(images, labels)]

    wandb.log({"classifier_out": tbl})
    ```

    Tables added directly to runs as above will produce a corresponding Table Visualizer in the
    Workspace which can be used for further analysis and exporting to reports.

    Tables added to artifacts can be viewed in the Artifact Tab and will render
    an equivalent Table Visualizer directly in the artifact browser.

    Tables expect each value for a column to be of the same type. By default, a column supports
    optional values, but not mixed values. If you absolutely need to mix types,
    you can enable the `allow_mixed_types` flag which will disable type checking
    on the data. This will result in some table analytics features being disabled
    due to lack of consistent typing.

    Arguments:
        columns: (List[str]) Names of the columns in the table.
            Defaults to ["Input", "Output", "Expected"].
        data: (List[List[any]]) 2D row-oriented array of values.
        dataframe: (pandas.DataFrame) DataFrame object used to create the table.
            When set, `data` and `columns` arguments are ignored.
        optional: (Union[bool,List[bool]]) Determines if `None` values are allowed. Default to True
            - If a singular bool value, then the optionality is enforced for all
            columns specified at construction time
            - If a list of bool values, then the optionality is applied to each
            column - should be the same length as `columns`
            applies to all columns. A list of bool values applies to each respective column.
        allow_mixed_types: (bool) Determines if columns are allowed to have mixed types
            (disables type validation). Defaults to False
    '''
    MAX_ROWS: int
    MAX_ARTIFACT_ROWS: int
    def __init__(self, columns: Incomplete | None = None, data: Incomplete | None = None, rows: Incomplete | None = None, dataframe: Incomplete | None = None, dtype: Incomplete | None = None, optional: bool = True, allow_mixed_types: bool = False) -> None:
        """Initialize a Table object.

        Rows is kept for legacy reasons, we use data to mimic the Pandas api.
        """
    def cast(self, col_name, dtype, optional: bool = False):
        """Cast a column to a specific type.

        Arguments:
            col_name: (str) - name of the column to cast
            dtype: (class, wandb.wandb_sdk.interface._dtypes.Type, any) - the target dtype. Can be one of
                normal python class, internal WB type, or an example object (e.g. an instance of wandb.Image or wandb.Classes)
            optional: (bool) - if the column should allow Nones
        """
    def __ne__(self, other): ...
    def __eq__(self, other): ...
    def add_row(self, *row) -> None:
        """Deprecated: use add_data instead."""
    def add_data(self, *data) -> None:
        """Add a row of data to the table.

        Argument length should match column length.
        """
    def bind_to_run(self, *args, **kwargs) -> None: ...
    @classmethod
    def get_media_subdir(cls): ...
    @classmethod
    def from_json(cls, json_obj, source_artifact): ...
    def to_json(self, run_or_artifact): ...
    def iterrows(self) -> Generator[Incomplete, None, None]:
        """Iterate over rows as (ndx, row).

        Yields:
        ------
        index : int
            The index of the row. Using this value in other WandB tables
            will automatically build a relationship between the tables
        row : List[any]
            The data of the row.
        """
    def set_pk(self, col_name) -> None: ...
    def set_fk(self, col_name, table, table_col) -> None: ...
    data: Incomplete
    columns: Incomplete
    def add_column(self, name, data, optional: bool = False) -> None:
        """Add a column of data to the table.

        Arguments:
            name: (str) - the unique name of the column
            data: (list | np.array) - a column of homogenous data
            optional: (bool) - if null-like values are permitted
        """
    def get_column(self, name, convert_to: Incomplete | None = None):
        '''Retrieve a column of data from the table.

        Arguments:
            name: (str) - the name of the column
            convert_to: (str, optional)
                - "numpy": will convert the underlying data to numpy object
        '''
    def get_index(self):
        """Return an array of row indexes for use in other tables to create links."""
    def get_dataframe(self):
        """Returns a pandas.DataFrame of the table."""
    def index_ref(self, index):
        """Get a reference to a particular row index in the table."""
    def add_computed_columns(self, fn) -> None:
        """Add one or more computed columns based on existing data.

        Args:
            fn: A function which accepts one or two parameters, ndx (int) and row (dict),
                which is expected to return a dict representing new columns for that row, keyed
                by the new column names.

                `ndx` is an integer representing the index of the row. Only included if `include_ndx`
                      is set to `True`.

                `row` is a dictionary keyed by existing columns
        """

class _PartitionTablePartEntry:
    """Helper class for PartitionTable to track its parts."""
    entry: Incomplete
    source_artifact: Incomplete
    def __init__(self, entry, source_artifact) -> None: ...
    def get_part(self): ...
    def free(self) -> None: ...

class PartitionedTable(Media):
    """A table which is composed of multiple sub-tables.

    Currently, PartitionedTable is designed to point to a directory within an artifact.
    """
    parts_path: Incomplete
    def __init__(self, parts_path) -> None:
        """Initialize a PartitionedTable.

        Args:
            parts_path (str): path to a directory of tables in the artifact.
        """
    def to_json(self, artifact_or_run): ...
    @classmethod
    def from_json(cls, json_obj, source_artifact): ...
    def iterrows(self) -> Generator[Incomplete, None, None]:
        """Iterate over rows as (ndx, row).

        Yields:
        ------
        index : int
            The index of the row.
        row : List[any]
            The data of the row.
        """
    def __ne__(self, other): ...
    def __eq__(self, other): ...
    def bind_to_run(self, *args, **kwargs) -> None: ...

class Audio(BatchableMedia):
    """Wandb class for audio clips.

    Arguments:
        data_or_path: (string or numpy array) A path to an audio file
            or a numpy array of audio data.
        sample_rate: (int) Sample rate, required when passing in raw
            numpy array of audio data.
        caption: (string) Caption to display with audio.
    """
    def __init__(self, data_or_path, sample_rate: Incomplete | None = None, caption: Incomplete | None = None) -> None:
        """Accept a path to an audio file or a numpy array of audio data."""
    @classmethod
    def get_media_subdir(cls): ...
    @classmethod
    def from_json(cls, json_obj, source_artifact): ...
    def bind_to_run(self, run, key, step, id_: Incomplete | None = None, ignore_copy_err: bool | None = None): ...
    def to_json(self, run): ...
    @classmethod
    def seq_to_json(cls, seq, run, key, step): ...
    @classmethod
    def durations(cls, audio_list): ...
    @classmethod
    def sample_rates(cls, audio_list): ...
    @classmethod
    def captions(cls, audio_list): ...
    def resolve_ref(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...

class JoinedTable(Media):
    """Join two tables for visualization in the Artifact UI.

    Arguments:
        table1 (str, wandb.Table, ArtifactManifestEntry):
            the path to a wandb.Table in an artifact, the table object, or ArtifactManifestEntry
        table2 (str, wandb.Table):
            the path to a wandb.Table in an artifact, the table object, or ArtifactManifestEntry
        join_key (str, [str, str]):
            key or keys to perform the join
    """
    def __init__(self, table1, table2, join_key) -> None: ...
    @classmethod
    def from_json(cls, json_obj, source_artifact): ...
    def to_json(self, artifact_or_run): ...
    def __ne__(self, other): ...
    def __eq__(self, other): ...
    def bind_to_run(self, *args, **kwargs) -> None: ...

class Bokeh(Media):
    """Wandb class for Bokeh plots.

    Arguments:
        val: Bokeh plot
    """
    b_obj: Incomplete
    def __init__(self, data_or_path) -> None: ...
    def get_media_subdir(self): ...
    def to_json(self, run): ...
    @classmethod
    def from_json(cls, json_obj, source_artifact): ...

class Graph(Media):
    """Wandb class for graphs.

    This class is typically used for saving and diplaying neural net models.  It
    represents the graph as an array of nodes and edges.  The nodes can have
    labels that can be visualized by wandb.

    Examples:
        Import a keras model:
        ```
            Graph.from_keras(keras_model)
        ```

    Attributes:
        format (string): Format to help wandb display the graph nicely.
        nodes ([wandb.Node]): List of wandb.Nodes
        nodes_by_id (dict): dict of ids -> nodes
        edges ([(wandb.Node, wandb.Node)]): List of pairs of nodes interpreted as edges
        loaded (boolean): Flag to tell whether the graph is completely loaded
        root (wandb.Node): root node of the graph
    """
    format: Incomplete
    nodes: Incomplete
    nodes_by_id: Incomplete
    edges: Incomplete
    loaded: bool
    criterion: Incomplete
    criterion_passed: bool
    root: Incomplete
    def __init__(self, format: str = 'keras') -> None: ...
    def bind_to_run(self, *args, **kwargs) -> None: ...
    @classmethod
    def get_media_subdir(cls): ...
    def to_json(self, run): ...
    def __getitem__(self, nid): ...
    def pprint(self) -> None: ...
    def add_node(self, node: Incomplete | None = None, **node_kwargs): ...
    def add_edge(self, from_node, to_node): ...
    @classmethod
    def from_keras(cls, model): ...

class Node(WBValue):
    """Node used in `Graph`."""
    in_edges: Incomplete
    out_edges: Incomplete
    obj: Incomplete
    def __init__(self, id: Incomplete | None = None, name: Incomplete | None = None, class_name: Incomplete | None = None, size: Incomplete | None = None, parameters: Incomplete | None = None, output_shape: Incomplete | None = None, is_output: Incomplete | None = None, num_parameters: Incomplete | None = None, node: Incomplete | None = None) -> None: ...
    def to_json(self, run: Incomplete | None = None): ...
    @property
    def id(self):
        """Must be unique in the graph."""
    @id.setter
    def id(self, val): ...
    @property
    def name(self):
        """Usually the type of layer or sublayer."""
    @name.setter
    def name(self, val): ...
    @property
    def class_name(self):
        """Usually the type of layer or sublayer."""
    @class_name.setter
    def class_name(self, val): ...
    @property
    def functions(self): ...
    @functions.setter
    def functions(self, val): ...
    @property
    def parameters(self): ...
    @parameters.setter
    def parameters(self, val): ...
    @property
    def size(self): ...
    @size.setter
    def size(self, val):
        """Tensor size."""
    @property
    def output_shape(self): ...
    @output_shape.setter
    def output_shape(self, val):
        """Tensor output_shape."""
    @property
    def is_output(self): ...
    @is_output.setter
    def is_output(self, val):
        """Tensor is_output."""
    @property
    def num_parameters(self): ...
    @num_parameters.setter
    def num_parameters(self, val):
        """Tensor num_parameters."""
    @property
    def child_parameters(self): ...
    @child_parameters.setter
    def child_parameters(self, val):
        """Tensor child_parameters."""
    @property
    def is_constant(self): ...
    @is_constant.setter
    def is_constant(self, val):
        """Tensor is_constant."""
    @classmethod
    def from_keras(cls, layer): ...

class Edge(WBValue):
    """Edge used in `Graph`."""
    def __init__(self, from_node, to_node) -> None: ...
    def to_json(self, run: Incomplete | None = None): ...
    @property
    def name(self):
        """Optional, not necessarily unique."""
    @name.setter
    def name(self, val): ...
    @property
    def from_node(self): ...
    @from_node.setter
    def from_node(self, val): ...
    @property
    def to_node(self): ...
    @to_node.setter
    def to_node(self, val): ...

class _ImageFileType(_dtypes.Type):
    name: str
    legacy_names: Incomplete
    types: Incomplete
    def __init__(self, box_layers: Incomplete | None = None, box_score_keys: Incomplete | None = None, mask_layers: Incomplete | None = None, class_map: Incomplete | None = None, **kwargs) -> None: ...
    def assign_type(self, wb_type: Incomplete | None = None): ...
    @classmethod
    def from_obj(cls, py_obj): ...

class _TableType(_dtypes.Type):
    name: str
    legacy_names: Incomplete
    types: Incomplete
    def __init__(self, column_types: Incomplete | None = None) -> None: ...
    def assign_type(self, wb_type: Incomplete | None = None): ...
    @classmethod
    def from_obj(cls, py_obj): ...

class _ForeignKeyType(_dtypes.Type):
    name: str
    legacy_names: Incomplete
    types: Incomplete
    def __init__(self, table, col_name) -> None: ...
    def assign_type(self, wb_type: Incomplete | None = None): ...
    @classmethod
    def from_obj(cls, py_obj): ...
    def to_json(self, artifact: Incomplete | None = None): ...
    @classmethod
    def from_json(cls, json_dict, artifact): ...

class _ForeignIndexType(_dtypes.Type):
    name: str
    legacy_names: Incomplete
    types: Incomplete
    def __init__(self, table) -> None: ...
    def assign_type(self, wb_type: Incomplete | None = None): ...
    @classmethod
    def from_obj(cls, py_obj): ...
    def to_json(self, artifact: Incomplete | None = None): ...
    @classmethod
    def from_json(cls, json_dict, artifact): ...

class _PrimaryKeyType(_dtypes.Type):
    name: str
    legacy_names: Incomplete
    def assign_type(self, wb_type: Incomplete | None = None): ...
    @classmethod
    def from_obj(cls, py_obj): ...

class _AudioFileType(_dtypes.Type):
    name: str
    types: Incomplete

class _BokehFileType(_dtypes.Type):
    name: str
    types: Incomplete

class _JoinedTableType(_dtypes.Type):
    name: str
    types: Incomplete

class _PartitionedTableType(_dtypes.Type):
    name: str
    types: Incomplete
