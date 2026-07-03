import abc
from .arrow_reader import FileInstructions as FileInstructions, make_file_instructions as make_file_instructions
from .utils.py_utils import NonMutableDict as NonMutableDict, asdict as asdict
from _typeshed import Incomplete
from dataclasses import dataclass
from typing import Dict, List, NamedTuple

@dataclass
class SplitInfo:
    name: str = ...
    num_bytes: int = ...
    num_examples: int = ...
    shard_lengths: List[int] | None = ...
    dataset_name: str | None = ...
    @property
    def file_instructions(self):
        """Returns the list of dict(filename, take, skip)."""
    def __init__(self, name, num_bytes, num_examples, shard_lengths, dataset_name) -> None: ...

@dataclass
class SubSplitInfo:
    """Wrapper around a sub split info.
    This class expose info on the subsplit:
    ```
    ds, info = datasets.load_dataset(..., split='train[75%:]', with_info=True)
    info.splits['train[75%:]'].num_examples
    ```
    """
    instructions: FileInstructions
    @property
    def num_examples(self):
        """Returns the number of example in the subsplit."""
    @property
    def file_instructions(self):
        """Returns the list of dict(filename, take, skip)."""
    def __init__(self, instructions) -> None: ...

class SplitBase(metaclass=abc.ABCMeta):
    """Abstract base class for Split compositionality.

    See the
    [guide on splits](../loading#slice-splits)
    for more information.

    There are three parts to the composition:
        1) The splits are composed (defined, merged, split,...) together before
             calling the `.as_dataset()` function. This is done with the `__add__`,
             `__getitem__`, which return a tree of `SplitBase` (whose leaf
             are the `NamedSplit` objects)

        ```
        split = datasets.Split.TRAIN + datasets.Split.TEST.subsplit(datasets.percent[:50])
        ```

        2) The `SplitBase` is forwarded to the `.as_dataset()` function
             to be resolved into actual read instruction. This is done by the
             `.get_read_instruction()` method which takes the real dataset splits
             (name, number of shards,...) and parse the tree to return a
             `SplitReadInstruction()` object

        ```
        read_instruction = split.get_read_instruction(self.info.splits)
        ```

        3) The `SplitReadInstruction` is then used in the `tf.data.Dataset` pipeline
             to define which files to read and how to skip examples within file.

    """
    @abc.abstractmethod
    def get_read_instruction(self, split_dict):
        """Parse the descriptor tree and compile all read instructions together.

        Args:
            split_dict: `dict`, The `dict[split_name, SplitInfo]` of the dataset

        Returns:
            split_read_instruction: `SplitReadInstruction`
        """
    def __eq__(self, other):
        """Equality: datasets.Split.TRAIN == 'train'."""
    def __ne__(self, other):
        """InEquality: datasets.Split.TRAIN != 'test'."""
    def __add__(self, other):
        """Merging: datasets.Split.TRAIN + datasets.Split.TEST."""
    def subsplit(self, arg: Incomplete | None = None, k: Incomplete | None = None, percent: Incomplete | None = None, weighted: Incomplete | None = None):
        """Divides this split into subsplits.

        There are 3 ways to define subsplits, which correspond to the 3
        arguments `k` (get `k` even subsplits), `percent` (get a slice of the
        dataset with `datasets.percent`), and `weighted` (get subsplits with proportions
        specified by `weighted`).

        Example::

        ```
        # 50% train, 50% test
        train, test = split.subsplit(k=2)
        # 50% train, 25% test, 25% validation
        train, test, validation = split.subsplit(weighted=[2, 1, 1])
        # Extract last 20%
        subsplit = split.subsplit(datasets.percent[-20:])
        ```

        Warning: k and weighted will be converted into percent which mean that
        values below the percent will be rounded up or down. The final split may be
        bigger to deal with remainders. For instance:

        ```
        train, test, valid = split.subsplit(k=3)  # 33%, 33%, 34%
        s1, s2, s3, s4 = split.subsplit(weighted=[2, 2, 1, 1])  # 33%, 33%, 16%, 18%
        ```

        Args:
            arg: If no kwargs are given, `arg` will be interpreted as one of
                `k`, `percent`, or `weighted` depending on the type.
                For example:
                ```
                split.subsplit(10)  # Equivalent to split.subsplit(k=10)
                split.subsplit(datasets.percent[:-20])  # percent=datasets.percent[:-20]
                split.subsplit([1, 1, 2])  # weighted=[1, 1, 2]
                ```
            k: `int` If set, subdivide the split into `k` equal parts.
            percent: `datasets.percent slice`, return a single subsplit corresponding to
                a slice of the original split. For example:
                `split.subsplit(datasets.percent[-20:])  # Last 20% of the dataset`.
            weighted: `list[int]`, return a list of subsplits whose proportions match
                the normalized sum of the list. For example:
                `split.subsplit(weighted=[1, 1, 2])  # 25%, 25%, 50%`.

        Returns:
            A subsplit or list of subsplits extracted from this split object.
        """

class PercentSliceMeta(type):
    def __getitem__(cls, slice_value): ...

class PercentSlice(metaclass=PercentSliceMeta):
    """Syntactic sugar for defining slice subsplits: `datasets.percent[75:-5]`.

    See the
    [guide on splits](../loading#slice-splits)
    for more information.
    """
percent = PercentSlice

class _SplitMerged(SplitBase):
    """Represent two split descriptors merged together."""
    def __init__(self, split1, split2) -> None: ...
    def get_read_instruction(self, split_dict): ...

class _SubSplit(SplitBase):
    """Represent a sub split of a split descriptor."""
    def __init__(self, split, slice_value) -> None: ...
    def get_read_instruction(self, split_dict): ...

class NamedSplit(SplitBase):
    """Descriptor corresponding to a named split (train, test, ...).

    Example:
        Each descriptor can be composed with other using addition or slice:

            ```py
            split = datasets.Split.TRAIN.subsplit(datasets.percent[0:25]) + datasets.Split.TEST
            ```

        The resulting split will correspond to 25% of the train split merged with
        100% of the test split.

        A split cannot be added twice, so the following will fail:

            ```py
            split = (
                    datasets.Split.TRAIN.subsplit(datasets.percent[:25]) +
                    datasets.Split.TRAIN.subsplit(datasets.percent[75:])
            )  # Error
            split = datasets.Split.TEST + datasets.Split.ALL  # Error
            ```

        The slices can be applied only one time. So the following are valid:

            ```py
            split = (
                    datasets.Split.TRAIN.subsplit(datasets.percent[:25]) +
                    datasets.Split.TEST.subsplit(datasets.percent[:50])
            )
            split = (datasets.Split.TRAIN + datasets.Split.TEST).subsplit(datasets.percent[:50])
            ```

        But this is not valid:

            ```py
            train = datasets.Split.TRAIN
            test = datasets.Split.TEST
            split = train.subsplit(datasets.percent[:25]).subsplit(datasets.percent[:25])
            split = (train.subsplit(datasets.percent[:25]) + test).subsplit(datasets.percent[:50])
            ```
    """
    def __init__(self, name) -> None: ...
    def __eq__(self, other):
        """Equality: datasets.Split.TRAIN == 'train'."""
    def __lt__(self, other): ...
    def __hash__(self): ...
    def get_read_instruction(self, split_dict): ...

class NamedSplitAll(NamedSplit):
    """Split corresponding to the union of all defined dataset splits."""
    def __init__(self) -> None: ...
    def get_read_instruction(self, split_dict): ...

class Split:
    '''`Enum` for dataset splits.

    Datasets are typically split into different subsets to be used at various
    stages of training and evaluation.

    - `TRAIN`: the training data.
    - `VALIDATION`: the validation data. If present, this is typically used as
      evaluation data while iterating on a model (e.g. changing hyperparameters,
      model architecture, etc.).
    - `TEST`: the testing data. This is the data to report metrics on. Typically
      you do not want to use this during model iteration as you may overfit to it.
    - `ALL`: the union of all defined dataset splits.

    All splits, including compositions inherit from `datasets.SplitBase`.

    See the [guide](../load_hub#splits) on splits for more information.

    Example:

    ```py
    >>> datasets.SplitGenerator(
    ...     name=datasets.Split.TRAIN,
    ...     gen_kwargs={"split_key": "train", "files": dl_manager.download_and extract(url)},
    ... ),
    ... datasets.SplitGenerator(
    ...     name=datasets.Split.VALIDATION,
    ...     gen_kwargs={"split_key": "validation", "files": dl_manager.download_and extract(url)},
    ... ),
    ... datasets.SplitGenerator(
    ...     name=datasets.Split.TEST,
    ...     gen_kwargs={"split_key": "test", "files": dl_manager.download_and extract(url)},
    ... )
    ```
    '''
    TRAIN: Incomplete
    TEST: Incomplete
    VALIDATION: Incomplete
    ALL: Incomplete
    def __new__(cls, name):
        """Create a custom split with datasets.Split('custom_name')."""

class SlicedSplitInfo(NamedTuple):
    split_info: Incomplete
    slice_value: Incomplete

class SplitReadInstruction:
    """Object containing the reading instruction for the dataset.

    Similarly to `SplitDescriptor` nodes, this object can be composed with itself,
    but the resolution happens instantaneously, instead of keeping track of the
    tree, such as all instructions are compiled and flattened in a single
    SplitReadInstruction object containing the list of files and slice to use.

    Once resolved, the instructions can be accessed with:

    ```
    read_instructions.get_list_sliced_split_info()  # List of splits to use
    ```

    """
    def __init__(self, split_info: Incomplete | None = None) -> None: ...
    def add(self, sliced_split) -> None:
        """Add a SlicedSplitInfo the read instructions."""
    def __add__(self, other):
        """Merging split together."""
    def __getitem__(self, slice_value):
        """Sub-splits."""
    def get_list_sliced_split_info(self): ...

class SplitDict(dict):
    """Split info object."""
    dataset_name: Incomplete
    def __init__(self, *args, dataset_name: Incomplete | None = None, **kwargs) -> None: ...
    def __getitem__(self, key: SplitBase | str): ...
    def __setitem__(self, key: SplitBase | str, value: SplitInfo): ...
    def add(self, split_info: SplitInfo):
        """Add the split info."""
    @property
    def total_num_examples(self):
        """Return the total number of examples."""
    @classmethod
    def from_split_dict(cls, split_infos: List | Dict, dataset_name: str | None = None):
        """Returns a new SplitDict initialized from a Dict or List of `split_infos`."""
    def to_split_dict(self):
        """Returns a list of SplitInfo protos that we have."""
    def copy(self): ...

@dataclass
class SplitGenerator:
    '''Defines the split information for the generator.

    This should be used as returned value of
    `GeneratorBasedBuilder._split_generators`.
    See `GeneratorBasedBuilder._split_generators` for more info and example
    of usage.

    Args:
        name (`str`):
            Name of the `Split` for which the generator will
            create the examples.
        **gen_kwargs (additional keyword arguments):
            Keyword arguments to forward to the `DatasetBuilder._generate_examples` method
            of the builder.

    Example:

    ```py
    >>> datasets.SplitGenerator(
    ...     name=datasets.Split.TRAIN,
    ...     gen_kwargs={"split_key": "train", "files": dl_manager.download_and_extract(url)},
    ... )
    ```
    '''
    name: str
    gen_kwargs: Dict = ...
    split_info: SplitInfo = ...
    def __post_init__(self) -> None: ...
    def __init__(self, name, gen_kwargs) -> None: ...
