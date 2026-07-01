import abc
from . import config as config, utils as utils
from .arrow_dataset import Dataset as Dataset
from .arrow_reader import ArrowReader as ArrowReader, DatasetNotOnHfGcsError as DatasetNotOnHfGcsError, HF_GCP_BASE_URL as HF_GCP_BASE_URL, MissingFilesOnHfGcsError as MissingFilesOnHfGcsError, ReadInstruction as ReadInstruction
from .arrow_writer import ArrowWriter as ArrowWriter, BeamWriter as BeamWriter, ParquetWriter as ParquetWriter, SchemaInferenceError as SchemaInferenceError
from .data_files import DataFilesDict as DataFilesDict, sanitize_patterns as sanitize_patterns
from .dataset_dict import DatasetDict as DatasetDict, IterableDatasetDict as IterableDatasetDict
from .download.download_config import DownloadConfig as DownloadConfig
from .download.download_manager import DownloadManager as DownloadManager, DownloadMode as DownloadMode
from .download.mock_download_manager import MockDownloadManager as MockDownloadManager
from .download.streaming_download_manager import StreamingDownloadManager as StreamingDownloadManager, xopen as xopen
from .features import Features as Features
from .filesystems import is_remote_filesystem as is_remote_filesystem, rename as rename
from .fingerprint import Hasher as Hasher
from .info import DatasetInfo as DatasetInfo, DatasetInfosDict as DatasetInfosDict, PostProcessedInfo as PostProcessedInfo
from .iterable_dataset import ArrowExamplesIterable as ArrowExamplesIterable, ExamplesIterable as ExamplesIterable, IterableDataset as IterableDataset
from .keyhash import DuplicatedKeysError as DuplicatedKeysError
from .naming import INVALID_WINDOWS_CHARACTERS_IN_PATH as INVALID_WINDOWS_CHARACTERS_IN_PATH, camelcase_to_snakecase as camelcase_to_snakecase
from .splits import Split as Split, SplitDict as SplitDict, SplitGenerator as SplitGenerator, SplitInfo as SplitInfo
from .streaming import extend_dataset_builder_for_streaming as extend_dataset_builder_for_streaming
from .utils import logging as logging
from .utils.file_utils import cached_path as cached_path, is_remote_url as is_remote_url
from .utils.filelock import FileLock as FileLock
from .utils.info_utils import VerificationMode as VerificationMode, get_size_checksum_dict as get_size_checksum_dict, verify_checksums as verify_checksums, verify_splits as verify_splits
from .utils.py_utils import classproperty as classproperty, convert_file_size_to_int as convert_file_size_to_int, has_sufficient_disk_space as has_sufficient_disk_space, iflatmap_unordered as iflatmap_unordered, map_nested as map_nested, memoize as memoize, size_str as size_str, temporary_assignment as temporary_assignment
from _typeshed import Incomplete
from dataclasses import dataclass
from typing import Dict

logger: Incomplete

class InvalidConfigName(ValueError): ...
class DatasetBuildError(Exception): ...
class ManualDownloadError(DatasetBuildError): ...
class DatasetGenerationError(DatasetBuildError): ...
class FileFormatError(DatasetBuildError): ...

@dataclass
class BuilderConfig:
    """Base class for `DatasetBuilder` data configuration.

    `DatasetBuilder` subclasses with data configuration options should subclass
    `BuilderConfig` and add their own properties.

    Attributes:
        name (`str`, defaults to `default`):
            The name of the configuration.
        version (`Version` or `str`, defaults to `0.0.0`):
            The version of the configuration.
        data_dir (`str`, *optional*):
            Path to the directory containing the source data.
        data_files (`str` or `Sequence` or `Mapping`, *optional*):
            Path(s) to source data file(s).
        description (`str`, *optional*):
            A human description of the configuration.
    """
    name: str = ...
    version: utils.Version | str | None = ...
    data_dir: str | None = ...
    data_files: DataFilesDict | None = ...
    description: str | None = ...
    def __post_init__(self) -> None: ...
    def __eq__(self, o): ...
    def create_config_id(self, config_kwargs: dict, custom_features: Features | None = None) -> str:
        """
        The config id is used to build the cache directory.
        By default it is equal to the config name.
        However the name of a config is not sufficient to have a unique identifier for the dataset being generated
        since it doesn't take into account:
        - the config kwargs that can be used to overwrite attributes
        - the custom features used to write the dataset
        - the data_files for json/text/csv/pandas datasets

        Therefore the config id is just the config name with an optional suffix based on these.
        """
    def __init__(self, name, version, data_dir, data_files, description) -> None: ...

class DatasetBuilder(metaclass=abc.ABCMeta):
    '''Abstract base class for all datasets.

    `DatasetBuilder` has 3 key methods:

        - [`DatasetBuilder.info`]: Documents the dataset, including feature
          names, types, shapes, version, splits, citation, etc.
        - [`DatasetBuilder.download_and_prepare`]: Downloads the source data
          and writes it to disk.
        - [`DatasetBuilder.as_dataset`]: Generates a [`Dataset`].

    Some `DatasetBuilder`s expose multiple variants of the
    dataset by defining a [`BuilderConfig`] subclass and accepting a
    config object (or name) on construction. Configurable datasets expose a
    pre-defined set of configurations in [`DatasetBuilder.builder_configs`].

    Args:
        cache_dir (`str`, *optional*):
            Directory to cache data. Defaults to `"~/.cache/huggingface/datasets"`.
        dataset_name (`str`, *optional*):
            Name of the dataset, if different from the builder name. Useful for packaged builders
            like csv, imagefolder, audiofolder, etc. to reflect the difference between datasets
            that use the same packaged builder.
        config_name (`str`, *optional*):
            Name of the dataset configuration.
            It affects the data generated on disk. Different configurations will have their own subdirectories and
            versions.
            If not provided, the default configuration is used (if it exists).

            <Added version="2.3.0">

            Parameter `name` was renamed to `config_name`.

            </Added>
        hash (`str`, *optional*):
            Hash specific to the dataset code. Used to update the caching directory when the
            dataset loading script code is updated (to avoid reusing old data).
            The typical caching directory (defined in `self._relative_data_dir`) is `name/version/hash/`.
        base_path (`str`, *optional*):
            Base path for relative paths that are used to download files.
            This can be a remote URL.
        features ([`Features`], *optional*):
            Features types to use with this dataset.
            It can be used to change the [`Features`] types of a dataset, for example.
        token (`str` or `bool`, *optional*):
            String or boolean to use as Bearer token for remote files on the
            Datasets Hub. If `True`, will get token from `"~/.huggingface"`.
        repo_id (`str`, *optional*):
            ID of the dataset repository.
            Used to distinguish builders with the same name but not coming from the same namespace, for example "squad"
            and "lhoestq/squad" repo IDs. In the latter, the builder name would be "lhoestq___squad".
        data_files (`str` or `Sequence` or `Mapping`, *optional*):
            Path(s) to source data file(s).
            For builders like "csv" or "json" that need the user to specify data files. They can be either
            local or remote files. For convenience, you can use a `DataFilesDict`.
        data_dir (`str`, *optional*):
            Path to directory containing source data file(s).
            Use only if `data_files` is not passed, in which case it is equivalent to passing
            `os.path.join(data_dir, "**")` as `data_files`.
            For builders that require manual download, it must be the path to the local directory containing the
            manually downloaded data.
        storage_options (`dict`, *optional*):
            Key/value pairs to be passed on to the dataset file-system backend, if any.
        writer_batch_size (`int`, *optional*):
            Batch size used by the ArrowWriter.
            It defines the number of samples that are kept in memory before writing them
            and also the length of the arrow chunks.
            None means that the ArrowWriter will use its default value.
        name (`str`): Configuration name for the dataset.

            <Deprecated version="2.3.0">

            Use `config_name` instead.

            </Deprecated>

        **config_kwargs (additional keyword arguments): Keyword arguments to be passed to the corresponding builder
            configuration class, set on the class attribute [`DatasetBuilder.BUILDER_CONFIG_CLASS`]. The builder
            configuration class is [`BuilderConfig`] or a subclass of it.
    '''
    VERSION: Incomplete
    BUILDER_CONFIG_CLASS = BuilderConfig
    BUILDER_CONFIGS: Incomplete
    DEFAULT_CONFIG_NAME: Incomplete
    DEFAULT_WRITER_BATCH_SIZE: Incomplete
    name: Incomplete
    hash: Incomplete
    base_path: Incomplete
    token: Incomplete
    use_auth_token: Incomplete
    repo_id: Incomplete
    storage_options: Incomplete
    dataset_name: Incomplete
    info: Incomplete
    dl_manager: Incomplete
    def __init__(self, cache_dir: str | None = None, dataset_name: str | None = None, config_name: str | None = None, hash: str | None = None, base_path: str | None = None, info: DatasetInfo | None = None, features: Features | None = None, token: bool | str | None = None, use_auth_token: str = 'deprecated', repo_id: str | None = None, data_files: str | list | dict | DataFilesDict | None = None, data_dir: str | None = None, storage_options: dict | None = None, writer_batch_size: int | None = None, name: str = 'deprecated', **config_kwargs) -> None: ...
    @property
    def manual_download_instructions(self) -> str | None: ...
    @classmethod
    def get_all_exported_dataset_infos(cls) -> DatasetInfosDict:
        '''Empty dict if doesn\'t exist

        Example:

        ```py
        >>> from datasets import load_dataset_builder
        >>> ds_builder = load_dataset_builder(\'rotten_tomatoes\')
        >>> ds_builder.get_all_exported_dataset_infos()
        {\'default\': DatasetInfo(description="Movie Review Dataset.
This is a dataset of containing 5,331 positive and 5,331 negative processed
sentences from Rotten Tomatoes movie reviews. This data was first used in Bo
Pang and Lillian Lee, ``Seeing stars: Exploiting class relationships for
sentiment categorization with respect to rating scales.\'\', Proceedings of the
ACL, 2005.
", citation=\'@InProceedings{Pang+Lee:05a,
  author =       {Bo Pang and Lillian Lee},
  title =        {Seeing stars: Exploiting class relationships for sentiment
                  categorization with respect to rating scales},
  booktitle =    {Proceedings of the ACL},
  year =         2005
}
\', homepage=\'http://www.cs.cornell.edu/people/pabo/movie-review-data/\', license=\'\', features={\'text\': Value(dtype=\'string\', id=None), \'label\': ClassLabel(num_classes=2, names=[\'neg\', \'pos\'], id=None)}, post_processed=None, supervised_keys=SupervisedKeysData(input=\'\', output=\'\'), task_templates=[TextClassification(task=\'text-classification\', text_column=\'text\', label_column=\'label\')], builder_name=\'rotten_tomatoes_movie_review\', config_name=\'default\', version=1.0.0, splits={\'train\': SplitInfo(name=\'train\', num_bytes=1074810, num_examples=8530, dataset_name=\'rotten_tomatoes_movie_review\'), \'validation\': SplitInfo(name=\'validation\', num_bytes=134679, num_examples=1066, dataset_name=\'rotten_tomatoes_movie_review\'), \'test\': SplitInfo(name=\'test\', num_bytes=135972, num_examples=1066, dataset_name=\'rotten_tomatoes_movie_review\')}, download_checksums={\'https://storage.googleapis.com/seldon-datasets/sentence_polarity_v1/rt-polaritydata.tar.gz\': {\'num_bytes\': 487770, \'checksum\': \'a05befe52aafda71d458d188a1c54506a998b1308613ba76bbda2e5029409ce9\'}}, download_size=487770, post_processing_size=None, dataset_size=1345461, size_in_bytes=1833231)}
        ```
        '''
    def get_exported_dataset_info(self) -> DatasetInfo:
        '''Empty `DatasetInfo` if doesn\'t exist

        Example:

        ```py
        >>> from datasets import load_dataset_builder
        >>> ds_builder = load_dataset_builder(\'rotten_tomatoes\')
        >>> ds_builder.get_exported_dataset_info()
        DatasetInfo(description="Movie Review Dataset.
This is a dataset of containing 5,331 positive and 5,331 negative processed
sentences from Rotten Tomatoes movie reviews. This data was first used in Bo
Pang and Lillian Lee, ``Seeing stars: Exploiting class relationships for
sentiment categorization with respect to rating scales.\'\', Proceedings of the
ACL, 2005.
", citation=\'@InProceedings{Pang+Lee:05a,
  author =       {Bo Pang and Lillian Lee},
  title =        {Seeing stars: Exploiting class relationships for sentiment
                  categorization with respect to rating scales},
  booktitle =    {Proceedings of the ACL},
  year =         2005
}
\', homepage=\'http://www.cs.cornell.edu/people/pabo/movie-review-data/\', license=\'\', features={\'text\': Value(dtype=\'string\', id=None), \'label\': ClassLabel(num_classes=2, names=[\'neg\', \'pos\'], id=None)}, post_processed=None, supervised_keys=SupervisedKeysData(input=\'\', output=\'\'), task_templates=[TextClassification(task=\'text-classification\', text_column=\'text\', label_column=\'label\')], builder_name=\'rotten_tomatoes_movie_review\', config_name=\'default\', version=1.0.0, splits={\'train\': SplitInfo(name=\'train\', num_bytes=1074810, num_examples=8530, dataset_name=\'rotten_tomatoes_movie_review\'), \'validation\': SplitInfo(name=\'validation\', num_bytes=134679, num_examples=1066, dataset_name=\'rotten_tomatoes_movie_review\'), \'test\': SplitInfo(name=\'test\', num_bytes=135972, num_examples=1066, dataset_name=\'rotten_tomatoes_movie_review\')}, download_checksums={\'https://storage.googleapis.com/seldon-datasets/sentence_polarity_v1/rt-polaritydata.tar.gz\': {\'num_bytes\': 487770, \'checksum\': \'a05befe52aafda71d458d188a1c54506a998b1308613ba76bbda2e5029409ce9\'}}, download_size=487770, post_processing_size=None, dataset_size=1345461, size_in_bytes=1833231)
        ```
        '''
    @classmethod
    def builder_configs(cls):
        """Dictionary of pre-defined configurations for this builder class."""
    @property
    def cache_dir(self): ...
    @classmethod
    def get_imported_module_dir(cls):
        """Return the path of the module of this class or subclass."""
    def download_and_prepare(self, output_dir: str | None = None, download_config: DownloadConfig | None = None, download_mode: DownloadMode | str | None = None, verification_mode: VerificationMode | str | None = None, ignore_verifications: str = 'deprecated', try_from_hf_gcs: bool = True, dl_manager: DownloadManager | None = None, base_path: str | None = None, use_auth_token: str = 'deprecated', file_format: str = 'arrow', max_shard_size: int | str | None = None, num_proc: int | None = None, storage_options: dict | None = None, **download_and_prepare_kwargs):
        '''Downloads and prepares dataset for reading.

        Args:
            output_dir (`str`, *optional*):
                Output directory for the dataset.
                Default to this builder\'s `cache_dir`, which is inside `~/.cache/huggingface/datasets` by default.

                <Added version="2.5.0"/>
            download_config (`DownloadConfig`, *optional*):
                Specific download configuration parameters.
            download_mode ([`DownloadMode`] or `str`, *optional*):
                Select the download/generate mode, default to `REUSE_DATASET_IF_EXISTS`.
            verification_mode ([`VerificationMode`] or `str`, defaults to `BASIC_CHECKS`):
                Verification mode determining the checks to run on the downloaded/processed dataset information (checksums/size/splits/...).

                <Added version="2.9.1"/>
            ignore_verifications (`bool`, defaults to `False`):
                Ignore the verifications of the downloaded/processed dataset information (checksums/size/splits/...).

                <Deprecated version="2.9.1">

                `ignore_verifications` was deprecated in version 2.9.1 and will be removed in 3.0.0.
                Please use `verification_mode` instead.

                </Deprecated>
            try_from_hf_gcs (`bool`):
                If `True`, it will try to download the already prepared dataset from the HF Google cloud storage.
            dl_manager (`DownloadManager`, *optional*):
                Specific `DownloadManger` to use.
            base_path (`str`, *optional*):
                Base path for relative paths that are used to download files. This can be a remote url.
                If not specified, the value of the `base_path` attribute (`self.base_path`) will be used instead.
            use_auth_token (`Union[str, bool]`, *optional*):
                Optional string or boolean to use as Bearer token for remote files on the Datasets Hub.
                If True, or not specified, will get token from ~/.huggingface.

                <Deprecated version="2.7.1">

                Pass `use_auth_token` to `load_dataset_builder` instead.

                </Deprecated>
            file_format (`str`, *optional*):
                Format of the data files in which the dataset will be written.
                Supported formats: "arrow", "parquet". Default to "arrow" format.
                If the format is "parquet", then image and audio data are embedded into the Parquet files instead of pointing to local files.

                <Added version="2.5.0"/>
            max_shard_size (`Union[str, int]`, *optional*):
                Maximum number of bytes written per shard, default is "500MB".
                The size is based on uncompressed data size, so in practice your shard files may be smaller than
                `max_shard_size` thanks to Parquet compression for example.

                <Added version="2.5.0"/>
            num_proc (`int`, *optional*, defaults to `None`):
                Number of processes when downloading and generating the dataset locally.
                Multiprocessing is disabled by default.

                <Added version="2.7.0"/>
            storage_options (`dict`, *optional*):
                Key/value pairs to be passed on to the caching file-system backend, if any.

                <Added version="2.5.0"/>
            **download_and_prepare_kwargs (additional keyword arguments): Keyword arguments.

        Example:

        Download and prepare the dataset as Arrow files that can be loaded as a Dataset using `builder.as_dataset()`:

        ```py
        >>> from datasets import load_dataset_builder
        >>> builder = load_dataset_builder("rotten_tomatoes")
        >>> builder.download_and_prepare()
        ```

        Download and prepare the dataset as sharded Parquet files locally:

        ```py
        >>> from datasets import load_dataset_builder
        >>> builder = load_dataset_builder("rotten_tomatoes")
        >>> builder.download_and_prepare("./output_dir", file_format="parquet")
        ```

        Download and prepare the dataset as sharded Parquet files in a cloud storage:

        ```py
        >>> from datasets import load_dataset_builder
        >>> storage_options = {"key": aws_access_key_id, "secret": aws_secret_access_key}
        >>> builder = load_dataset_builder("rotten_tomatoes")
        >>> builder.download_and_prepare("s3://my-bucket/my_rotten_tomatoes", storage_options=storage_options, file_format="parquet")
        ```
        '''
    def download_post_processing_resources(self, dl_manager) -> None: ...
    def as_dataset(self, split: Split | None = None, run_post_process: bool = True, verification_mode: VerificationMode | str | None = None, ignore_verifications: str = 'deprecated', in_memory: bool = False) -> Dataset | DatasetDict:
        '''Return a Dataset for the specified split.

        Args:
            split (`datasets.Split`):
                Which subset of the data to return.
            run_post_process (`bool`, defaults to `True`):
                Whether to run post-processing dataset transforms and/or add
                indexes.
            verification_mode ([`VerificationMode`] or `str`, defaults to `BASIC_CHECKS`):
                Verification mode determining the checks to run on the
                downloaded/processed dataset information (checksums/size/splits/...).

                <Added version="2.9.1"/>
            ignore_verifications (`bool`, defaults to `False`):
                Whether to ignore the verifications of the
                downloaded/processed dataset information (checksums/size/splits/...).

                <Deprecated version="2.9.1">

                `ignore_verifications` was deprecated in version 2.9.1 and will be removed in 3.0.0.
                Please use `verification_mode` instead.

                </Deprecated>
            in_memory (`bool`, defaults to `False`):
                Whether to copy the data in-memory.

        Returns:
            datasets.Dataset

        Example:

        ```py
        >>> from datasets import load_dataset_builder
        >>> builder = load_dataset_builder(\'rotten_tomatoes\')
        >>> builder.download_and_prepare()
        >>> ds = builder.as_dataset(split=\'train\')
        >>> ds
        Dataset({
            features: [\'text\', \'label\'],
            num_rows: 8530
        })
        ```
        '''
    def as_streaming_dataset(self, split: str | None = None, base_path: str | None = None) -> Dict[str, IterableDataset] | IterableDataset: ...

class GeneratorBasedBuilder(DatasetBuilder, metaclass=abc.ABCMeta):
    """Base class for datasets with data generation based on dict generators.

    `GeneratorBasedBuilder` is a convenience class that abstracts away much
    of the data writing and reading of `DatasetBuilder`. It expects subclasses to
    implement generators of feature dictionaries across the dataset splits
    (`_split_generators`). See the method docstrings for details.
    """
class ArrowBasedBuilder(DatasetBuilder, metaclass=abc.ABCMeta):
    """Base class for datasets with data generation based on Arrow loading functions (CSV/JSON/Parquet)."""
class MissingBeamOptions(ValueError): ...

class BeamBasedBuilder(DatasetBuilder, metaclass=abc.ABCMeta):
    """Beam-based Builder."""
    def __init__(self, *args, beam_runner: Incomplete | None = None, beam_options: Incomplete | None = None, **kwargs) -> None: ...
    def as_streaming_dataset(self, split: str | None = None) -> Dict[str, IterableDataset] | IterableDataset: ...
