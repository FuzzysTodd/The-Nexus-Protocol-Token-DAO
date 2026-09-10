from .download.download_config import DownloadConfig as DownloadConfig
from .info import DatasetInfo as DatasetInfo
from .naming import filenames_for_dataset_split as filenames_for_dataset_split
from .splits import Split as Split, SplitInfo as SplitInfo
from .table import InMemoryTable as InMemoryTable, MemoryMappedTable as MemoryMappedTable, Table as Table, concat_tables as concat_tables
from .utils import logging as logging
from .utils.file_utils import cached_path as cached_path
from _typeshed import Incomplete
from dataclasses import dataclass
from typing import List

logger: Incomplete
HF_GCP_BASE_URL: str

class DatasetNotOnHfGcsError(ConnectionError):
    """When you can't get the dataset from the Hf google cloud storage"""
class MissingFilesOnHfGcsError(ConnectionError):
    """When some files are missing on the Hf oogle cloud storage"""

@dataclass(frozen=True)
class FileInstructions:
    """The file instructions associated with a split ReadInstruction.

    Attributes:
        num_examples: `int`, The total number of examples
        file_instructions: List[dict(filename, skip, take)], the files information.
            The filenames contains the relative path, not absolute.
            skip/take indicates which example read in the file: `ds.slice(skip, take)`
    """
    num_examples: int
    file_instructions: List[dict]
    def __init__(self, num_examples, file_instructions) -> None: ...

def make_file_instructions(name: str, split_infos: List['SplitInfo'], instruction: str | ReadInstruction, filetype_suffix: str | None = None, prefix_path: str | None = None) -> FileInstructions:
    """Returns instructions of the split dict.

    Args:
        name (`str`): Name of the dataset.
        split_infos (`list` of `[SplitInfo]`): Dataset splits information.
        instruction ([`ReadInstruction`] or `str`): Reading instruction for a dataset.
        filetype_suffix (`str`, *optional*): Suffix of dataset files, e.g. 'arrow' or 'parquet'.
        prefix_path (`str`, *optional*): Prefix of dataset files, e.g. directory name.

    Returns:
        [`FileInstructions`]
    """

class BaseReader:
    """
    Build a Dataset object out of Instruction instance(s).
    """
    def __init__(self, path: str, info: DatasetInfo | None) -> None:
        """Initializes ArrowReader.

        Args:
            path (str): path where tfrecords are stored.
            info (DatasetInfo): info about the dataset.
        """
    def get_file_instructions(self, name, instruction, split_infos):
        """Return list of dict {'filename': str, 'skip': int, 'take': int}"""
    def read(self, name, instructions, split_infos, in_memory: bool = False):
        """Returns Dataset instance(s).

        Args:
            name (str): name of the dataset.
            instructions (ReadInstruction): instructions to read.
                Instruction can be string and will then be passed to the Instruction
                constructor as it.
            split_infos (list of SplitInfo proto): the available splits for dataset.
            in_memory (bool, default False): Whether to copy the data in-memory.

        Returns:
             kwargs to build a single Dataset instance.
        """
    def read_files(self, files: List[dict], original_instructions: None | ReadInstruction | Split = None, in_memory: bool = False):
        """Returns single Dataset instance for the set of file instructions.

        Args:
            files: List[dict(filename, skip, take)], the files information.
                The filenames contains the relative path, not absolute.
                skip/take indicates which example read in the file: `ds.skip().take()`
            original_instructions: store the original instructions used to build the dataset split in the dataset.
            in_memory (bool, default False): Whether to copy the data in-memory.

        Returns:
            kwargs to build a Dataset instance.
        """
    def download_from_hf_gcs(self, download_config: DownloadConfig, relative_data_dir):
        """
        Download the dataset files from the Hf GCS

        Args:
            dl_cache_dir: `str`, the local cache directory used to download files
            relative_data_dir: `str`, the relative directory of the remote files from
                the `datasets` directory on GCS.

        """

class ArrowReader(BaseReader):
    """
    Build a Dataset object out of Instruction instance(s).
    This Reader uses either memory mapping or file descriptors (in-memory) on arrow files.
    """
    def __init__(self, path: str, info: DatasetInfo | None) -> None:
        """Initializes ArrowReader.

        Args:
            path (str): path where Arrow files are stored.
            info (DatasetInfo): info about the dataset.
        """
    @staticmethod
    def read_table(filename, in_memory: bool = False) -> Table:
        """
        Read table from file.

        Args:
            filename (str): File name of the table.
            in_memory (bool, default=False): Whether to copy the data in-memory.

        Returns:
            pyarrow.Table
        """

class ParquetReader(BaseReader):
    """
    Build a Dataset object out of Instruction instance(s).
    This Reader uses memory mapping on parquet files.
    """
    def __init__(self, path: str, info: DatasetInfo | None) -> None:
        """Initializes ParquetReader.

        Args:
            path (str): path where tfrecords are stored.
            info (DatasetInfo): info about the dataset.
        """

@dataclass(frozen=True)
class _AbsoluteInstruction:
    """A machine friendly slice: defined absolute positive boundaries."""
    splitname: str
    from_: int
    to: int
    def __init__(self, splitname, from_, to) -> None: ...

@dataclass(frozen=True)
class _RelativeInstruction:
    """Represents a single parsed slicing instruction, can use % and negatives."""
    splitname: str
    from_: int | None = ...
    to: int | None = ...
    unit: str | None = ...
    rounding: str | None = ...
    def __post_init__(self) -> None: ...
    def __init__(self, splitname, from_, to, unit, rounding) -> None: ...

class ReadInstruction:
    '''Reading instruction for a dataset.

    Examples::

      # The following lines are equivalent:
      ds = datasets.load_dataset(\'mnist\', split=\'test[:33%]\')
      ds = datasets.load_dataset(\'mnist\', split=datasets.ReadInstruction.from_spec(\'test[:33%]\'))
      ds = datasets.load_dataset(\'mnist\', split=datasets.ReadInstruction(\'test\', to=33, unit=\'%\'))
      ds = datasets.load_dataset(\'mnist\', split=datasets.ReadInstruction(
          \'test\', from_=0, to=33, unit=\'%\'))

      # The following lines are equivalent:
      ds = datasets.load_dataset(\'mnist\', split=\'test[:33%]+train[1:-1]\')
      ds = datasets.load_dataset(\'mnist\', split=datasets.ReadInstruction.from_spec(
          \'test[:33%]+train[1:-1]\'))
      ds = datasets.load_dataset(\'mnist\', split=(
          datasets.ReadInstruction(\'test\', to=33, unit=\'%\') +
          datasets.ReadInstruction(\'train\', from_=1, to=-1, unit=\'abs\')))

      # The following lines are equivalent:
      ds = datasets.load_dataset(\'mnist\', split=\'test[:33%](pct1_dropremainder)\')
      ds = datasets.load_dataset(\'mnist\', split=datasets.ReadInstruction.from_spec(
          \'test[:33%](pct1_dropremainder)\'))
      ds = datasets.load_dataset(\'mnist\', split=datasets.ReadInstruction(
          \'test\', from_=0, to=33, unit=\'%\', rounding="pct1_dropremainder"))

      # 10-fold validation:
      tests = datasets.load_dataset(
          \'mnist\',
          [datasets.ReadInstruction(\'train\', from_=k, to=k+10, unit=\'%\')
          for k in range(0, 100, 10)])
      trains = datasets.load_dataset(
          \'mnist\',
          [datasets.ReadInstruction(\'train\', to=k, unit=\'%\') + datasets.ReadInstruction(\'train\', from_=k+10, unit=\'%\')
          for k in range(0, 100, 10)])

    '''
    def __init__(self, split_name, rounding: Incomplete | None = None, from_: Incomplete | None = None, to: Incomplete | None = None, unit: Incomplete | None = None) -> None:
        """Initialize ReadInstruction.

        Args:
            split_name (str): name of the split to read. Eg: 'train'.
            rounding (str, optional): The rounding behaviour to use when percent slicing is
                used. Ignored when slicing with absolute indices.
                Possible values:
                 - 'closest' (default): The specified percentages are rounded to the
                     closest value. Use this if you want specified percents to be as
                     much exact as possible.
                 - 'pct1_dropremainder': the specified percentages are treated as
                     multiple of 1%. Use this option if you want consistency. Eg:
                         len(5%) == 5 * len(1%).
                     Using this option, one might not be able to use the full set of
                     examples, if the number of those is not a multiple of 100.
            from_ (int):
            to (int): alternative way of specifying slicing boundaries. If any of
                {from_, to, unit} argument is used, slicing cannot be specified as
                string.
            unit (str): optional, one of:
                '%': to set the slicing unit as percents of the split size.
                'abs': to set the slicing unit as absolute numbers.
        """
    @classmethod
    def from_spec(cls, spec):
        """Creates a `ReadInstruction` instance out of a string spec.

        Args:
            spec (`str`):
                Split(s) + optional slice(s) to read + optional rounding
                if percents are used as the slicing unit. A slice can be specified,
                using absolute numbers (`int`) or percentages (`int`).

        Examples:

            ```
            test: test split.
            test + validation: test split + validation split.
            test[10:]: test split, minus its first 10 records.
            test[:10%]: first 10% records of test split.
            test[:20%](pct1_dropremainder): first 10% records, rounded with the pct1_dropremainder rounding.
            test[:-5%]+train[40%:60%]: first 95% of test + middle 20% of train.
            ```

        Returns:
            ReadInstruction instance.
        """
    def to_spec(self): ...
    def __add__(self, other):
        """Returns a new ReadInstruction obj, result of appending other to self."""
    def to_absolute(self, name2len):
        """Translate instruction into a list of absolute instructions.

        Those absolute instructions are then to be added together.

        Args:
            name2len (`dict`):
                Associating split names to number of examples.

        Returns:
            list of _AbsoluteInstruction instances (corresponds to the + in spec).
        """
