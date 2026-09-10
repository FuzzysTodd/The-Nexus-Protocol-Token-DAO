from ._commit_api import CommitOperation as CommitOperation, CommitOperationAdd as CommitOperationAdd, CommitOperationCopy as CommitOperationCopy, CommitOperationDelete as CommitOperationDelete
from ._multi_commits import MULTI_COMMIT_PR_CLOSE_COMMENT_FAILURE_BAD_REQUEST_TEMPLATE as MULTI_COMMIT_PR_CLOSE_COMMENT_FAILURE_BAD_REQUEST_TEMPLATE, MULTI_COMMIT_PR_CLOSE_COMMENT_FAILURE_NO_CHANGES_TEMPLATE as MULTI_COMMIT_PR_CLOSE_COMMENT_FAILURE_NO_CHANGES_TEMPLATE, MULTI_COMMIT_PR_CLOSING_COMMENT_TEMPLATE as MULTI_COMMIT_PR_CLOSING_COMMENT_TEMPLATE, MULTI_COMMIT_PR_COMPLETION_COMMENT_TEMPLATE as MULTI_COMMIT_PR_COMPLETION_COMMENT_TEMPLATE, MultiCommitException as MultiCommitException, MultiCommitStep as MultiCommitStep, MultiCommitStrategy as MultiCommitStrategy, multi_commit_create_pull_request as multi_commit_create_pull_request, multi_commit_generate_comment as multi_commit_generate_comment, multi_commit_parse_pr_description as multi_commit_parse_pr_description, plan_multi_commits as plan_multi_commits
from ._space_api import SpaceHardware as SpaceHardware, SpaceRuntime as SpaceRuntime, SpaceStorage as SpaceStorage, SpaceVariable as SpaceVariable
from .community import Discussion as Discussion, DiscussionComment as DiscussionComment, DiscussionStatusChange as DiscussionStatusChange, DiscussionTitleChange as DiscussionTitleChange, DiscussionWithDetails as DiscussionWithDetails, deserialize_event as deserialize_event
from .constants import DEFAULT_REVISION as DEFAULT_REVISION, ENDPOINT as ENDPOINT, REGEX_COMMIT_OID as REGEX_COMMIT_OID, REPO_TYPES as REPO_TYPES, REPO_TYPES_MAPPING as REPO_TYPES_MAPPING, REPO_TYPES_URL_PREFIXES as REPO_TYPES_URL_PREFIXES, REPO_TYPE_MODEL as REPO_TYPE_MODEL, SPACES_SDK_TYPES as SPACES_SDK_TYPES
from .file_download import get_hf_file_metadata as get_hf_file_metadata, hf_hub_url as hf_hub_url
from .utils import BadRequestError as BadRequestError, HfFolder as HfFolder, HfHubHTTPError as HfHubHTTPError, build_hf_headers as build_hf_headers, filter_repo_objects as filter_repo_objects, hf_raise_for_status as hf_raise_for_status, logging as logging, paginate as paginate, parse_datetime as parse_datetime, validate_hf_hub_args as validate_hf_hub_args
from .utils._typing import CallableT as CallableT
from .utils.endpoint_helpers import AttributeDictionary as AttributeDictionary, DatasetFilter as DatasetFilter, DatasetTags as DatasetTags, ModelFilter as ModelFilter, ModelTags as ModelTags
from _typeshed import Incomplete
from concurrent.futures import Future
from dataclasses import dataclass
from datetime import datetime
from huggingface_hub.utils import EntryNotFoundError as EntryNotFoundError, IGNORE_GIT_FOLDER_PATTERNS as IGNORE_GIT_FOLDER_PATTERNS, LocalTokenNotFoundError as LocalTokenNotFoundError, RepositoryNotFoundError as RepositoryNotFoundError, RevisionNotFoundError as RevisionNotFoundError, experimental as experimental, get_session as get_session
from pathlib import Path
from tqdm.auto import tqdm as base_tqdm
from typing import Any, BinaryIO, Callable, Dict, Iterable, Iterator, List, Literal, Tuple, TypeVar, TypedDict, overload

R = TypeVar('R')
CollectionItemType_T: Incomplete
USERNAME_PLACEHOLDER: str
logger: Incomplete

class ReprMixin:
    """Mixin to create the __repr__ for a class"""
    def __init__(self, **kwargs) -> None: ...

def repo_type_and_id_from_hf_id(hf_id: str, hub_url: str | None = None) -> Tuple[str | None, str | None, str]:
    """
    Returns the repo type and ID from a huggingface.co URL linking to a
    repository

    Args:
        hf_id (`str`):
            An URL or ID of a repository on the HF hub. Accepted values are:

            - https://huggingface.co/<repo_type>/<namespace>/<repo_id>
            - https://huggingface.co/<namespace>/<repo_id>
            - hf://<repo_type>/<namespace>/<repo_id>
            - hf://<namespace>/<repo_id>
            - <repo_type>/<namespace>/<repo_id>
            - <namespace>/<repo_id>
            - <repo_id>
        hub_url (`str`, *optional*):
            The URL of the HuggingFace Hub, defaults to https://huggingface.co

    Returns:
        A tuple with three items: repo_type (`str` or `None`), namespace (`str` or
        `None`) and repo_id (`str`).

    Raises:
        - [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError)
            If URL cannot be parsed.
        - [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError)
            If `repo_type` is unknown.
    """

class BlobLfsInfo(TypedDict, total=False):
    size: int
    sha256: str
    pointer_size: int

@dataclass
class CommitInfo:
    '''Data structure containing information about a newly created commit.

    Returned by [`create_commit`].

    Args:
        commit_url (`str`):
            Url where to find the commit.

        commit_message (`str`):
            The summary (first line) of the commit that has been created.

        commit_description (`str`):
            Description of the commit that has been created. Can be empty.

        oid (`str`):
            Commit hash id. Example: `"91c54ad1727ee830252e457677f467be0bfd8a57"`.

        pr_url (`str`, *optional*):
            Url to the PR that has been created, if any. Populated when `create_pr=True`
            is passed.

        pr_revision (`str`, *optional*):
            Revision of the PR that has been created, if any. Populated when
            `create_pr=True` is passed. Example: `"refs/pr/1"`.

        pr_num (`int`, *optional*):
            Number of the PR discussion that has been created, if any. Populated when
            `create_pr=True` is passed. Can be passed as `discussion_num` in
            [`get_discussion_details`]. Example: `1`.
    '''
    commit_url: str
    commit_message: str
    commit_description: str
    oid: str
    pr_url: str | None = ...
    pr_revision: str | None = ...
    pr_num: str | None = ...
    def __post_init__(self) -> None:
        """Populate pr-related fields after initialization.

        See https://docs.python.org/3.10/library/dataclasses.html#post-init-processing.
        """
    def __init__(self, commit_url, commit_message, commit_description, oid, pr_url) -> None: ...

class RepoUrl(str):
    '''Subclass of `str` describing a repo URL on the Hub.

    `RepoUrl` is returned by `HfApi.create_repo`. It inherits from `str` for backward
    compatibility. At initialization, the URL is parsed to populate properties:
    - endpoint (`str`)
    - namespace (`Optional[str]`)
    - repo_name (`str`)
    - repo_id (`str`)
    - repo_type (`Literal["model", "dataset", "space"]`)
    - url (`str`)

    Args:
        url (`Any`):
            String value of the repo url.
        endpoint (`str`, *optional*):
            Endpoint of the Hub. Defaults to <https://huggingface.co>.

    Example:
    ```py
    >>> RepoUrl(\'https://huggingface.co/gpt2\')
    RepoUrl(\'https://huggingface.co/gpt2\', endpoint=\'https://huggingface.co\', repo_type=\'model\', repo_id=\'gpt2\')

    >>> RepoUrl(\'https://hub-ci.huggingface.co/datasets/dummy_user/dummy_dataset\', endpoint=\'https://hub-ci.huggingface.co\')
    RepoUrl(\'https://hub-ci.huggingface.co/datasets/dummy_user/dummy_dataset\', endpoint=\'https://hub-ci.huggingface.co\', repo_type=\'dataset\', repo_id=\'dummy_user/dummy_dataset\')

    >>> RepoUrl(\'hf://datasets/my-user/my-dataset\')
    RepoUrl(\'hf://datasets/my-user/my-dataset\', endpoint=\'https://huggingface.co\', repo_type=\'dataset\', repo_id=\'user/dataset\')

    >>> HfApi.create_repo("dummy_model")
    RepoUrl(\'https://huggingface.co/Wauplin/dummy_model\', endpoint=\'https://huggingface.co\', repo_type=\'model\', repo_id=\'Wauplin/dummy_model\')
    ```

    Raises:
        - [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError)
            If URL cannot be parsed.
        - [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError)
            If `repo_type` is unknown.
    '''
    def __new__(cls, url: Any, endpoint: str | None = None): ...
    endpoint: Incomplete
    namespace: Incomplete
    repo_name: Incomplete
    repo_id: Incomplete
    repo_type: Incomplete
    url: Incomplete
    def __init__(self, url: Any, endpoint: str | None = None) -> None: ...

class RepoFile(ReprMixin):
    """
    Data structure that represents a public file inside a repo, accessible from huggingface.co

    Args:
        rfilename (str):
            file name, relative to the repo root. This is the only attribute that's guaranteed to be here, but under
            certain conditions there can certain other stuff.
        size (`int`, *optional*):
            The file's size, in bytes. This attribute is present when `files_metadata` argument of [`repo_info`] is set
            to `True`. It's `None` otherwise.
        blob_id (`str`, *optional*):
            The file's git OID. This attribute is present when `files_metadata` argument of [`repo_info`] is set to
            `True`. It's `None` otherwise.
        lfs (`BlobLfsInfo`, *optional*):
            The file's LFS metadata. This attribute is present when`files_metadata` argument of [`repo_info`] is set to
            `True` and the file is stored with Git LFS. It's `None` otherwise.
    """
    rfilename: Incomplete
    size: Incomplete
    blob_id: Incomplete
    lfs: Incomplete
    def __init__(self, rfilename: str, size: int | None = None, blobId: str | None = None, lfs: BlobLfsInfo | None = None, **kwargs) -> None: ...

class ModelInfo(ReprMixin):
    '''
    Info about a model accessible from huggingface.co

    Attributes:
        modelId (`str`, *optional*):
            ID of model repository.
        sha (`str`, *optional*):
            repo sha at this particular revision
        lastModified (`str`, *optional*):
            date of last commit to repo
        tags (`List[str]`, *optional*):
            List of tags.
        pipeline_tag (`str`, *optional*):
            Pipeline tag to identify the correct widget.
        siblings (`List[RepoFile]`, *optional*):
            list of ([`huggingface_hub.hf_api.RepoFile`]) objects that constitute the model.
        private (`bool`, *optional*, defaults to `False`):
            is the repo private
        author (`str`, *optional*):
            repo author
        config (`Dict`, *optional*):
            Model configuration information
        securityStatus (`Dict`, *optional*):
            Security status of the model.
            Example: `{"containsInfected": False}`
        kwargs (`Dict`, *optional*):
            Kwargs that will be become attributes of the class.
    '''
    modelId: Incomplete
    sha: Incomplete
    lastModified: Incomplete
    tags: Incomplete
    pipeline_tag: Incomplete
    siblings: Incomplete
    private: Incomplete
    author: Incomplete
    config: Incomplete
    securityStatus: Incomplete
    def __init__(self, *, modelId: str | None = None, sha: str | None = None, lastModified: str | None = None, tags: List[str] | None = None, pipeline_tag: str | None = None, siblings: List[Dict] | None = None, private: bool = False, author: str | None = None, config: Dict | None = None, securityStatus: Dict | None = None, **kwargs) -> None: ...

class DatasetInfo(ReprMixin):
    """
    Info about a dataset accessible from huggingface.co

    Attributes:
        id (`str`, *optional*):
            ID of dataset repository.
        sha (`str`, *optional*):
            repo sha at this particular revision
        lastModified (`str`, *optional*):
            date of last commit to repo
        tags (`List[str]`, *optional*):
            List of tags.
        siblings (`List[RepoFile]`, *optional*):
            list of [`huggingface_hub.hf_api.RepoFile`] objects that constitute the dataset.
        private (`bool`, *optional*, defaults to `False`):
            is the repo private
        author (`str`, *optional*):
            repo author
        description (`str`, *optional*):
            Description of the dataset
        citation (`str`, *optional*):
            Dataset citation
        cardData (`Dict`, *optional*):
            Metadata of the model card as a dictionary.
        kwargs (`Dict`, *optional*):
            Kwargs that will be become attributes of the class.
    """
    id: Incomplete
    sha: Incomplete
    lastModified: Incomplete
    tags: Incomplete
    private: Incomplete
    author: Incomplete
    description: Incomplete
    citation: Incomplete
    cardData: Incomplete
    siblings: Incomplete
    def __init__(self, *, id: str | None = None, sha: str | None = None, lastModified: str | None = None, tags: List[str] | None = None, siblings: List[Dict] | None = None, private: bool = False, author: str | None = None, description: str | None = None, citation: str | None = None, cardData: dict | None = None, **kwargs) -> None: ...

class SpaceInfo(ReprMixin):
    '''
    Info about a Space accessible from huggingface.co

    This is a "dataclass" like container that just sets on itself any attribute
    passed by the server.

    Attributes:
        id (`str`, *optional*):
            id of space
        sha (`str`, *optional*):
            repo sha at this particular revision
        lastModified (`str`, *optional*):
            date of last commit to repo
        siblings (`List[RepoFile]`, *optional*):
            list of [`huggingface_hub.hf_api.RepoFIle`] objects that constitute the Space
        private (`bool`, *optional*, defaults to `False`):
            is the repo private
        author (`str`, *optional*):
            repo author
        kwargs (`Dict`, *optional*):
            Kwargs that will be become attributes of the class.
    '''
    id: Incomplete
    sha: Incomplete
    lastModified: Incomplete
    siblings: Incomplete
    private: Incomplete
    author: Incomplete
    def __init__(self, *, id: str | None = None, sha: str | None = None, lastModified: str | None = None, siblings: List[Dict] | None = None, private: bool = False, author: str | None = None, **kwargs) -> None: ...

class MetricInfo(ReprMixin):
    """
    Info about a public metric accessible from huggingface.co
    """
    id: Incomplete
    description: Incomplete
    citation: Incomplete
    def __init__(self, *, id: str | None = None, description: str | None = None, citation: str | None = None, **kwargs) -> None: ...

class CollectionItem(ReprMixin):
    '''Contains information about an item of a Collection (model, dataset, Space or paper).

    Args:
        item_object_id (`str`):
            Unique ID of the item in the collection.
        item_id (`str`):
            ID of the underlying object on the Hub. Can be either a repo_id or a paper id
            e.g. `"jbilcke-hf/ai-comic-factory"`, `"2307.09288"`.
        item_type (`str`):
            Type of the underlying object. Can be one of `"model"`, `"dataset"`, `"space"` or `"paper"`.
        position (`int`):
            Position of the item in the collection.
        note (`str`, *optional*):
            Note associated with the item, as plain text.
        kwargs (`Dict`, *optional*):
            Any other attribute returned by the server. Those attributes depend on the `item_type`: "author", "private",
            "lastModified", "gated", "title", "likes", "upvotes", etc.
    '''
    item_object_id: Incomplete
    item_id: Incomplete
    item_type: Incomplete
    position: Incomplete
    note: Incomplete
    def __init__(self, _id: str, id: str, type: CollectionItemType_T, position: int, note: Dict | None = None, **kwargs) -> None: ...

class Collection(ReprMixin):
    '''
    Contains information about a Collection on the Hub.

    Args:
        slug (`str`):
            Slug of the collection. E.g. `"TheBloke/recent-models-64f9a55bb3115b4f513ec026"`.
        title (`str`):
            Title of the collection. E.g. `"Recent models"`.
        owner (`str`):
            Owner of the collection. E.g. `"TheBloke"`.
        description (`str`, *optional*):
            Description of the collection, as plain text.
        items (`List[CollectionItem]`):
            List of items in the collection.
        last_updated (`datetime`):
            Date of the last update of the collection.
        position (`int`):
            Position of the collection in the list of collections of the owner.
        private (`bool`):
            Whether the collection is private or not.
        theme (`str`):
            Theme of the collection. E.g. `"green"`.
        url (`str`):
            URL for the collection on the Hub.
    '''
    slug: str
    title: str
    owner: str
    description: str | None
    items: List[CollectionItem]
    last_updated: datetime
    position: int
    private: bool
    theme: str
    url: Incomplete
    def __init__(self, data: Dict, endpoint: str | None = None) -> None: ...

class ModelSearchArguments(AttributeDictionary):
    """
    A nested namespace object holding all possible values for properties of
    models currently hosted in the Hub with tab-completion. If a value starts
    with a number, it will only exist in the dictionary

    Example:

    ```python
    >>> args = ModelSearchArguments()

    >>> args.author.huggingface
    'huggingface'

    >>> args.language.en
    'en'
    ```

    <Tip warning={true}>

    `ModelSearchArguments` is a legacy class meant for exploratory purposes only. Its
    initialization requires listing all models on the Hub which makes it increasingly
    slower as the number of repos on the Hub increases.

    </Tip>
    """
    def __init__(self, api: HfApi | None = None) -> None: ...

class DatasetSearchArguments(AttributeDictionary):
    """
    A nested namespace object holding all possible values for properties of
    datasets currently hosted in the Hub with tab-completion. If a value starts
    with a number, it will only exist in the dictionary

    Example:

    ```python
    >>> args = DatasetSearchArguments()

    >>> args.author.huggingface
    'huggingface'

    >>> args.language.en
    'language:en'
    ```

    <Tip warning={true}>

    `DatasetSearchArguments` is a legacy class meant for exploratory purposes only. Its
    initialization requires listing all datasets on the Hub which makes it increasingly
    slower as the number of repos on the Hub increases.

    </Tip>
    """
    def __init__(self, api: HfApi | None = None) -> None: ...

@dataclass
class GitRefInfo:
    '''
    Contains information about a git reference for a repo on the Hub.

    Args:
        name (`str`):
            Name of the reference (e.g. tag name or branch name).
        ref (`str`):
            Full git ref on the Hub (e.g. `"refs/heads/main"` or `"refs/tags/v1.0"`).
        target_commit (`str`):
            OID of the target commit for the ref (e.g. `"e7da7f221d5bf496a48136c0cd264e630fe9fcc8"`)
    '''
    name: str
    ref: str
    target_commit: str
    def __init__(self, data: Dict) -> None: ...

@dataclass
class GitRefs:
    '''
    Contains information about all git references for a repo on the Hub.

    Object is returned by [`list_repo_refs`].

    Args:
        branches (`List[GitRefInfo]`):
            A list of [`GitRefInfo`] containing information about branches on the repo.
        converts (`List[GitRefInfo]`):
            A list of [`GitRefInfo`] containing information about "convert" refs on the repo.
            Converts are refs used (internally) to push preprocessed data in Dataset repos.
        tags (`List[GitRefInfo]`):
            A list of [`GitRefInfo`] containing information about tags on the repo.
    '''
    branches: List[GitRefInfo]
    converts: List[GitRefInfo]
    tags: List[GitRefInfo]
    def __init__(self, branches, converts, tags) -> None: ...

@dataclass
class GitCommitInfo:
    '''
    Contains information about a git commit for a repo on the Hub. Check out [`list_repo_commits`] for more details.

    Args:
        commit_id (`str`):
            OID of the commit (e.g. `"e7da7f221d5bf496a48136c0cd264e630fe9fcc8"`)
        authors (`List[str]`):
            List of authors of the commit.
        created_at (`datetime`):
            Datetime when the commit was created.
        title (`str`):
            Title of the commit. This is a free-text value entered by the authors.
        message (`str`):
            Description of the commit. This is a free-text value entered by the authors.
        formatted_title (`str`):
            Title of the commit formatted as HTML. Only returned if `formatted=True` is set.
        formatted_message (`str`):
            Description of the commit formatted as HTML. Only returned if `formatted=True` is set.
    '''
    commit_id: str
    authors: List[str]
    created_at: datetime
    title: str
    message: str
    formatted_title: str | None
    formatted_message: str | None
    def __init__(self, data: Dict) -> None: ...

@dataclass
class UserLikes:
    """
    Contains information about a user likes on the Hub.

    Args:
        user (`str`):
            Name of the user for which we fetched the likes.
        total (`int`):
            Total number of likes.
        datasets (`List[str]`):
            List of datasets liked by the user (as repo_ids).
        models (`List[str]`):
            List of models liked by the user (as repo_ids).
        spaces (`List[str]`):
            List of spaces liked by the user (as repo_ids).
    """
    user: str
    total: int
    datasets: List[str]
    models: List[str]
    spaces: List[str]
    def __init__(self, user, total, datasets, models, spaces) -> None: ...

@dataclass
class User:
    """
    Contains information about a user on the Hub.

    Args:
        avatar_url (`str`):
            URL of the user's avatar.
        username (`str`):
            Name of the user on the Hub (unique).
        fullname (`str`):
            User's full name.
    """
    avatar_url: str
    username: str
    fullname: str
    def __init__(self, avatar_url, username, fullname) -> None: ...

def future_compatible(fn: CallableT) -> CallableT:
    '''Wrap a method of `HfApi` to handle `run_as_future=True`.

    A method flagged as "future_compatible" will be called in a thread if `run_as_future=True` and return a
    `concurrent.futures.Future` instance. Otherwise, it will be called normally and return the result.
    '''

class HfApi:
    endpoint: Incomplete
    token: Incomplete
    library_name: Incomplete
    library_version: Incomplete
    user_agent: Incomplete
    def __init__(self, endpoint: str | None = None, token: str | None = None, library_name: str | None = None, library_version: str | None = None, user_agent: Dict | str | None = None) -> None:
        '''Create a HF client to interact with the Hub via HTTP.

        The client is initialized with some high-level settings used in all requests
        made to the Hub (HF endpoint, authentication, user agents...). Using the `HfApi`
        client is preferred but not mandatory as all of its public methods are exposed
        directly at the root of `huggingface_hub`.

        Args:
            endpoint (`str`, *optional*):
                Hugging Face Hub base url. Will default to https://huggingface.co/. Otherwise,
                one can set the `HF_ENDPOINT` environment variable.
            token (`str`, *optional*):
                Hugging Face token. Will default to the locally saved token if
                not provided.
            library_name (`str`, *optional*):
                The name of the library that is making the HTTP request. Will be added to
                the user-agent header. Example: `"transformers"`.
            library_version (`str`, *optional*):
                The version of the library that is making the HTTP request. Will be added
                to the user-agent header. Example: `"4.24.0"`.
            user_agent (`str`, `dict`, *optional*):
                The user agent info in the form of a dictionary or a single string. It will
                be completed with information about the installed packages.
        '''
    def run_as_future(self, fn: Callable[..., R], *args, **kwargs) -> Future[R]:
        """
        Run a method in the background and return a Future instance.

        The main goal is to run methods without blocking the main thread (e.g. to push data during a training).
        Background jobs are queued to preserve order but are not ran in parallel. If you need to speed-up your scripts
        by parallelizing lots of call to the API, you must setup and use your own [ThreadPoolExecutor](https://docs.python.org/3/library/concurrent.futures.html#threadpoolexecutor).

        Note: Most-used methods like [`upload_file`], [`upload_folder`] and [`create_commit`] have a `run_as_future: bool`
        argument to directly call them in the background. This is equivalent to calling `api.run_as_future(...)` on them
        but less verbose.

        Args:
            fn (`Callable`):
                The method to run in the background.
            *args, **kwargs:
                Arguments with which the method will be called.

        Return:
            `Future`: a [Future](https://docs.python.org/3/library/concurrent.futures.html#future-objects) instance to
            get the result of the task.

        Example:
            ```py
            >>> from huggingface_hub import HfApi
            >>> api = HfApi()
            >>> future = api.run_as_future(api.whoami) # instant
            >>> future.done()
            False
            >>> future.result() # wait until complete and return result
            (...)
            >>> future.done()
            True
            ```
        """
    def whoami(self, token: str | None = None) -> Dict:
        '''
        Call HF API to know "whoami".

        Args:
            token (`str`, *optional*):
                Hugging Face token. Will default to the locally saved token if
                not provided.
        '''
    def get_token_permission(self, token: str | None = None) -> Literal['read', 'write', None]:
        '''
        Check if a given `token` is valid and return its permissions.

        For more details about tokens, please refer to https://huggingface.co/docs/hub/security-tokens#what-are-user-access-tokens.

        Args:
            token (`str`, *optional*):
                The token to check for validity. Defaults to the one saved locally.

        Returns:
            `Literal["read", "write", None]`: Permission granted by the token ("read" or "write"). Returns `None` if no
            token passed or token is invalid.
        '''
    def get_model_tags(self) -> ModelTags:
        """
        List all valid model tags as a nested namespace object
        """
    def get_dataset_tags(self) -> DatasetTags:
        """
        List all valid dataset tags as a nested namespace object.
        """
    def list_models(self, *, filter: ModelFilter | str | Iterable[str] | None = None, author: str | None = None, search: str | None = None, emissions_thresholds: Tuple[float, float] | None = None, sort: Literal['lastModified'] | str | None = None, direction: Literal[-1] | None = None, limit: int | None = None, full: bool | None = None, cardData: bool = False, fetch_config: bool = False, token: bool | str | None = None) -> Iterable[ModelInfo]:
        '''
        List models hosted on the Huggingface Hub, given some filters.

        Args:
            filter ([`ModelFilter`] or `str` or `Iterable`, *optional*):
                A string or [`ModelFilter`] which can be used to identify models
                on the Hub.
            author (`str`, *optional*):
                A string which identify the author (user or organization) of the
                returned models
            search (`str`, *optional*):
                A string that will be contained in the returned model ids.
            emissions_thresholds (`Tuple`, *optional*):
                A tuple of two ints or floats representing a minimum and maximum
                carbon footprint to filter the resulting models with in grams.
            sort (`Literal["lastModified"]` or `str`, *optional*):
                The key with which to sort the resulting models. Possible values
                are the properties of the [`huggingface_hub.hf_api.ModelInfo`] class.
            direction (`Literal[-1]` or `int`, *optional*):
                Direction in which to sort. The value `-1` sorts by descending
                order while all other values sort by ascending order.
            limit (`int`, *optional*):
                The limit on the number of models fetched. Leaving this option
                to `None` fetches all models.
            full (`bool`, *optional*):
                Whether to fetch all model data, including the `lastModified`,
                the `sha`, the files and the `tags`. This is set to `True` by
                default when using a filter.
            cardData (`bool`, *optional*):
                Whether to grab the metadata for the model as well. Can contain
                useful information such as carbon emissions, metrics, and
                datasets trained on.
            fetch_config (`bool`, *optional*):
                Whether to fetch the model configs as well. This is not included
                in `full` due to its size.
            token (`bool` or `str`, *optional*):
                A valid authentication token (see https://huggingface.co/settings/token).
                If `None` or `True` and machine is logged in (through `huggingface-cli login`
                or [`~huggingface_hub.login`]), token will be retrieved from the cache.
                If `False`, token is not sent in the request header.

        Returns:
            `Iterable[ModelInfo]`: an iterable of [`huggingface_hub.hf_api.ModelInfo`] objects.

        Example usage with the `filter` argument:

        ```python
        >>> from huggingface_hub import HfApi

        >>> api = HfApi()

        >>> # List all models
        >>> api.list_models()

        >>> # Get all valid search arguments
        >>> args = ModelSearchArguments()

        >>> # List only the text classification models
        >>> api.list_models(filter="text-classification")
        >>> # Using the `ModelFilter`
        >>> filt = ModelFilter(task="text-classification")
        >>> # With `ModelSearchArguments`
        >>> filt = ModelFilter(task=args.pipeline_tags.TextClassification)
        >>> api.list_models(filter=filt)

        >>> # Using `ModelFilter` and `ModelSearchArguments` to find text classification in both PyTorch and TensorFlow
        >>> filt = ModelFilter(
        ...     task=args.pipeline_tags.TextClassification,
        ...     library=[args.library.PyTorch, args.library.TensorFlow],
        ... )
        >>> api.list_models(filter=filt)

        >>> # List only models from the AllenNLP library
        >>> api.list_models(filter="allennlp")
        >>> # Using `ModelFilter` and `ModelSearchArguments`
        >>> filt = ModelFilter(library=args.library.allennlp)
        ```

        Example usage with the `search` argument:

        ```python
        >>> from huggingface_hub import HfApi

        >>> api = HfApi()

        >>> # List all models with "bert" in their name
        >>> api.list_models(search="bert")

        >>> # List all models with "bert" in their name made by google
        >>> api.list_models(search="bert", author="google")
        ```
        '''
    def list_datasets(self, *, filter: DatasetFilter | str | Iterable[str] | None = None, author: str | None = None, search: str | None = None, sort: Literal['lastModified'] | str | None = None, direction: Literal[-1] | None = None, limit: int | None = None, full: bool | None = None, token: str | None = None) -> Iterable[DatasetInfo]:
        '''
        List datasets hosted on the Huggingface Hub, given some filters.

        Args:
            filter ([`DatasetFilter`] or `str` or `Iterable`, *optional*):
                A string or [`DatasetFilter`] which can be used to identify
                datasets on the hub.
            author (`str`, *optional*):
                A string which identify the author of the returned datasets.
            search (`str`, *optional*):
                A string that will be contained in the returned datasets.
            sort (`Literal["lastModified"]` or `str`, *optional*):
                The key with which to sort the resulting datasets. Possible
                values are the properties of the [`huggingface_hub.hf_api.DatasetInfo`] class.
            direction (`Literal[-1]` or `int`, *optional*):
                Direction in which to sort. The value `-1` sorts by descending
                order while all other values sort by ascending order.
            limit (`int`, *optional*):
                The limit on the number of datasets fetched. Leaving this option
                to `None` fetches all datasets.
            full (`bool`, *optional*):
                Whether to fetch all dataset data, including the `lastModified`
                and the `cardData`. Can contain useful information such as the
                PapersWithCode ID.
            token (`bool` or `str`, *optional*):
                A valid authentication token (see https://huggingface.co/settings/token).
                If `None` or `True` and machine is logged in (through `huggingface-cli login`
                or [`~huggingface_hub.login`]), token will be retrieved from the cache.
                If `False`, token is not sent in the request header.

        Returns:
            `Iterable[DatasetInfo]`: an iterable of [`huggingface_hub.hf_api.DatasetInfo`] objects.

        Example usage with the `filter` argument:

        ```python
        >>> from huggingface_hub import HfApi

        >>> api = HfApi()

        >>> # List all datasets
        >>> api.list_datasets()

        >>> # Get all valid search arguments
        >>> args = DatasetSearchArguments()

        >>> # List only the text classification datasets
        >>> api.list_datasets(filter="task_categories:text-classification")
        >>> # Using the `DatasetFilter`
        >>> filt = DatasetFilter(task_categories="text-classification")
        >>> # With `DatasetSearchArguments`
        >>> filt = DatasetFilter(task=args.task_categories.text_classification)
        >>> api.list_models(filter=filt)

        >>> # List only the datasets in russian for language modeling
        >>> api.list_datasets(
        ...     filter=("language:ru", "task_ids:language-modeling")
        ... )
        >>> # Using the `DatasetFilter`
        >>> filt = DatasetFilter(language="ru", task_ids="language-modeling")
        >>> # With `DatasetSearchArguments`
        >>> filt = DatasetFilter(
        ...     language=args.language.ru,
        ...     task_ids=args.task_ids.language_modeling,
        ... )
        >>> api.list_datasets(filter=filt)
        ```

        Example usage with the `search` argument:

        ```python
        >>> from huggingface_hub import HfApi

        >>> api = HfApi()

        >>> # List all datasets with "text" in their name
        >>> api.list_datasets(search="text")

        >>> # List all datasets with "text" in their name made by google
        >>> api.list_datasets(search="text", author="google")
        ```
        '''
    def list_metrics(self) -> List[MetricInfo]:
        """
        Get the public list of all the metrics on huggingface.co

        Returns:
            `List[MetricInfo]`: a list of [`MetricInfo`] objects which.
        """
    def list_spaces(self, *, filter: str | Iterable[str] | None = None, author: str | None = None, search: str | None = None, sort: Literal['lastModified'] | str | None = None, direction: Literal[-1] | None = None, limit: int | None = None, datasets: str | Iterable[str] | None = None, models: str | Iterable[str] | None = None, linked: bool = False, full: bool | None = None, token: str | None = None) -> Iterable[SpaceInfo]:
        '''
        List spaces hosted on the Huggingface Hub, given some filters.

        Args:
            filter (`str` or `Iterable`, *optional*):
                A string tag or list of tags that can be used to identify Spaces on the Hub.
            author (`str`, *optional*):
                A string which identify the author of the returned Spaces.
            search (`str`, *optional*):
                A string that will be contained in the returned Spaces.
            sort (`Literal["lastModified"]` or `str`, *optional*):
                The key with which to sort the resulting Spaces. Possible
                values are the properties of the [`huggingface_hub.hf_api.SpaceInfo`]` class.
            direction (`Literal[-1]` or `int`, *optional*):
                Direction in which to sort. The value `-1` sorts by descending
                order while all other values sort by ascending order.
            limit (`int`, *optional*):
                The limit on the number of Spaces fetched. Leaving this option
                to `None` fetches all Spaces.
            datasets (`str` or `Iterable`, *optional*):
                Whether to return Spaces that make use of a dataset.
                The name of a specific dataset can be passed as a string.
            models (`str` or `Iterable`, *optional*):
                Whether to return Spaces that make use of a model.
                The name of a specific model can be passed as a string.
            linked (`bool`, *optional*):
                Whether to return Spaces that make use of either a model or a dataset.
            full (`bool`, *optional*):
                Whether to fetch all Spaces data, including the `lastModified`
                and the `cardData`.
            token (`bool` or `str`, *optional*):
                A valid authentication token (see https://huggingface.co/settings/token).
                If `None` or `True` and machine is logged in (through `huggingface-cli login`
                or [`~huggingface_hub.login`]), token will be retrieved from the cache.
                If `False`, token is not sent in the request header.

        Returns:
            `Iterable[SpaceInfo]`: an iterable of [`huggingface_hub.hf_api.SpaceInfo`] objects.
        '''
    def like(self, repo_id: str, *, token: str | None = None, repo_type: str | None = None) -> None:
        '''
        Like a given repo on the Hub (e.g. set as favorite).

        See also [`unlike`] and [`list_liked_repos`].

        Args:
            repo_id (`str`):
                The repository to like. Example: `"user/my-cool-model"`.

            token (`str`, *optional*):
                Authentication token. Will default to the stored token.

            repo_type (`str`, *optional*):
                Set to `"dataset"` or `"space"` if liking a dataset or space, `None` or
                `"model"` if liking a model. Default is `None`.

        Raises:
            [`~utils.RepositoryNotFoundError`]:
                If repository is not found (error 404): wrong repo_id/repo_type, private
                but not authenticated or repo does not exist.

        Example:
        ```python
        >>> from huggingface_hub import like, list_liked_repos, unlike
        >>> like("gpt2")
        >>> "gpt2" in list_liked_repos().models
        True
        >>> unlike("gpt2")
        >>> "gpt2" in list_liked_repos().models
        False
        ```
        '''
    def unlike(self, repo_id: str, *, token: str | None = None, repo_type: str | None = None) -> None:
        '''
        Unlike a given repo on the Hub (e.g. remove from favorite list).

        See also [`like`] and [`list_liked_repos`].

        Args:
            repo_id (`str`):
                The repository to unlike. Example: `"user/my-cool-model"`.

            token (`str`, *optional*):
                Authentication token. Will default to the stored token.

            repo_type (`str`, *optional*):
                Set to `"dataset"` or `"space"` if unliking a dataset or space, `None` or
                `"model"` if unliking a model. Default is `None`.

        Raises:
            [`~utils.RepositoryNotFoundError`]:
                If repository is not found (error 404): wrong repo_id/repo_type, private
                but not authenticated or repo does not exist.

        Example:
        ```python
        >>> from huggingface_hub import like, list_liked_repos, unlike
        >>> like("gpt2")
        >>> "gpt2" in list_liked_repos().models
        True
        >>> unlike("gpt2")
        >>> "gpt2" in list_liked_repos().models
        False
        ```
        '''
    def list_liked_repos(self, user: str | None = None, *, token: str | None = None) -> UserLikes:
        '''
        List all public repos liked by a user on huggingface.co.

        This list is public so token is optional. If `user` is not passed, it defaults to
        the logged in user.

        See also [`like`] and [`unlike`].

        Args:
            user (`str`, *optional*):
                Name of the user for which you want to fetch the likes.
            token (`str`, *optional*):
                A valid authentication token (see https://huggingface.co/settings/token).
                Used only if `user` is not passed to implicitly determine the current
                user name.

        Returns:
            [`UserLikes`]: object containing the user name and 3 lists of repo ids (1 for
            models, 1 for datasets and 1 for Spaces).

        Raises:
            [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError)
                If `user` is not passed and no token found (either from argument or from machine).

        Example:
        ```python
        >>> from huggingface_hub import list_liked_repos

        >>> likes = list_liked_repos("julien-c")

        >>> likes.user
        "julien-c"

        >>> likes.models
        ["osanseviero/streamlit_1.15", "Xhaheen/ChatGPT_HF", ...]
        ```
        '''
    def list_repo_likers(self, repo_id: str, *, repo_type: str | None = None, token: str | None = None) -> List[User]:
        '''
        List all users who liked a given repo on the hugging Face Hub.

        See also [`like`] and [`list_liked_repos`].

        Args:
            repo_id (`str`):
                The repository to retrieve . Example: `"user/my-cool-model"`.

            token (`str`, *optional*):
                Authentication token. Will default to the stored token.

            repo_type (`str`, *optional*):
                Set to `"dataset"` or `"space"` if uploading to a dataset or
                space, `None` or `"model"` if uploading to a model. Default is
                `None`.

        Returns:
            `List[User]`: a list of [`User`] objects.
        '''
    def model_info(self, repo_id: str, *, revision: str | None = None, timeout: float | None = None, securityStatus: bool | None = None, files_metadata: bool = False, token: bool | str | None = None) -> ModelInfo:
        """
        Get info on one specific model on huggingface.co

        Model can be private if you pass an acceptable token or are logged in.

        Args:
            repo_id (`str`):
                A namespace (user or an organization) and a repo name separated
                by a `/`.
            revision (`str`, *optional*):
                The revision of the model repository from which to get the
                information.
            timeout (`float`, *optional*):
                Whether to set a timeout for the request to the Hub.
            securityStatus (`bool`, *optional*):
                Whether to retrieve the security status from the model
                repository as well.
            files_metadata (`bool`, *optional*):
                Whether or not to retrieve metadata for files in the repository
                (size, LFS metadata, etc). Defaults to `False`.
            token (`bool` or `str`, *optional*):
                A valid authentication token (see https://huggingface.co/settings/token).
                If `None` or `True` and machine is logged in (through `huggingface-cli login`
                or [`~huggingface_hub.login`]), token will be retrieved from the cache.
                If `False`, token is not sent in the request header.

        Returns:
            [`huggingface_hub.hf_api.ModelInfo`]: The model repository information.

        <Tip>

        Raises the following errors:

            - [`~utils.RepositoryNotFoundError`]
              If the repository to download from cannot be found. This may be because it doesn't exist,
              or because it is set to `private` and you do not have access.
            - [`~utils.RevisionNotFoundError`]
              If the revision to download from cannot be found.

        </Tip>
        """
    def dataset_info(self, repo_id: str, *, revision: str | None = None, timeout: float | None = None, files_metadata: bool = False, token: bool | str | None = None) -> DatasetInfo:
        """
        Get info on one specific dataset on huggingface.co.

        Dataset can be private if you pass an acceptable token.

        Args:
            repo_id (`str`):
                A namespace (user or an organization) and a repo name separated
                by a `/`.
            revision (`str`, *optional*):
                The revision of the dataset repository from which to get the
                information.
            timeout (`float`, *optional*):
                Whether to set a timeout for the request to the Hub.
            files_metadata (`bool`, *optional*):
                Whether or not to retrieve metadata for files in the repository
                (size, LFS metadata, etc). Defaults to `False`.
            token (`bool` or `str`, *optional*):
                A valid authentication token (see https://huggingface.co/settings/token).
                If `None` or `True` and machine is logged in (through `huggingface-cli login`
                or [`~huggingface_hub.login`]), token will be retrieved from the cache.
                If `False`, token is not sent in the request header.

        Returns:
            [`hf_api.DatasetInfo`]: The dataset repository information.

        <Tip>

        Raises the following errors:

            - [`~utils.RepositoryNotFoundError`]
              If the repository to download from cannot be found. This may be because it doesn't exist,
              or because it is set to `private` and you do not have access.
            - [`~utils.RevisionNotFoundError`]
              If the revision to download from cannot be found.

        </Tip>
        """
    def space_info(self, repo_id: str, *, revision: str | None = None, timeout: float | None = None, files_metadata: bool = False, token: bool | str | None = None) -> SpaceInfo:
        """
        Get info on one specific Space on huggingface.co.

        Space can be private if you pass an acceptable token.

        Args:
            repo_id (`str`):
                A namespace (user or an organization) and a repo name separated
                by a `/`.
            revision (`str`, *optional*):
                The revision of the space repository from which to get the
                information.
            timeout (`float`, *optional*):
                Whether to set a timeout for the request to the Hub.
            files_metadata (`bool`, *optional*):
                Whether or not to retrieve metadata for files in the repository
                (size, LFS metadata, etc). Defaults to `False`.
            token (`bool` or `str`, *optional*):
                A valid authentication token (see https://huggingface.co/settings/token).
                If `None` or `True` and machine is logged in (through `huggingface-cli login`
                or [`~huggingface_hub.login`]), token will be retrieved from the cache.
                If `False`, token is not sent in the request header.

        Returns:
            [`~hf_api.SpaceInfo`]: The space repository information.

        <Tip>

        Raises the following errors:

            - [`~utils.RepositoryNotFoundError`]
              If the repository to download from cannot be found. This may be because it doesn't exist,
              or because it is set to `private` and you do not have access.
            - [`~utils.RevisionNotFoundError`]
              If the revision to download from cannot be found.

        </Tip>
        """
    def repo_info(self, repo_id: str, *, revision: str | None = None, repo_type: str | None = None, timeout: float | None = None, files_metadata: bool = False, token: bool | str | None = None) -> ModelInfo | DatasetInfo | SpaceInfo:
        '''
        Get the info object for a given repo of a given type.

        Args:
            repo_id (`str`):
                A namespace (user or an organization) and a repo name separated
                by a `/`.
            revision (`str`, *optional*):
                The revision of the repository from which to get the
                information.
            repo_type (`str`, *optional*):
                Set to `"dataset"` or `"space"` if getting repository info from a dataset or a space,
                `None` or `"model"` if getting repository info from a model. Default is `None`.
            timeout (`float`, *optional*):
                Whether to set a timeout for the request to the Hub.
            files_metadata (`bool`, *optional*):
                Whether or not to retrieve metadata for files in the repository
                (size, LFS metadata, etc). Defaults to `False`.
            token (`bool` or `str`, *optional*):
                A valid authentication token (see https://huggingface.co/settings/token).
                If `None` or `True` and machine is logged in (through `huggingface-cli login`
                or [`~huggingface_hub.login`]), token will be retrieved from the cache.
                If `False`, token is not sent in the request header.

        Returns:
            `Union[SpaceInfo, DatasetInfo, ModelInfo]`: The repository information, as a
            [`huggingface_hub.hf_api.DatasetInfo`], [`huggingface_hub.hf_api.ModelInfo`]
            or [`huggingface_hub.hf_api.SpaceInfo`] object.

        <Tip>

        Raises the following errors:

            - [`~utils.RepositoryNotFoundError`]
              If the repository to download from cannot be found. This may be because it doesn\'t exist,
              or because it is set to `private` and you do not have access.
            - [`~utils.RevisionNotFoundError`]
              If the revision to download from cannot be found.

        </Tip>
        '''
    def repo_exists(self, repo_id: str, *, repo_type: str | None = None, token: str | None = None) -> bool:
        '''
        Checks if a repository exists on the Hugging Face Hub.

        Args:
            repo_id (`str`):
                A namespace (user or an organization) and a repo name separated
                by a `/`.
            repo_type (`str`, *optional*):
                Set to `"dataset"` or `"space"` if getting repository info from a dataset or a space,
                `None` or `"model"` if getting repository info from a model. Default is `None`.
            token (`bool` or `str`, *optional*):
                A valid authentication token (see https://huggingface.co/settings/token).
                If `None` or `True` and machine is logged in (through `huggingface-cli login`
                or [`~huggingface_hub.login`]), token will be retrieved from the cache.
                If `False`, token is not sent in the request header.

        Returns:
            True if the repository exists, False otherwise.

        <Tip>

        Examples:
            ```py
            >>> from huggingface_hub import repo_exists
            >>> repo_exists("huggingface/transformers")
            True
            >>> repo_exists("huggingface/not-a-repo")
            False
            ```

        </Tip>
        '''
    def file_exists(self, repo_id: str, filename: str, *, repo_type: str | None = None, revision: str | None = None, token: str | None = None) -> bool:
        '''
        Checks if a file exists in a repository on the Hugging Face Hub.

        Args:
            repo_id (`str`):
                A namespace (user or an organization) and a repo name separated
                by a `/`.
            filename (`str`):
                The name of the file to check, for example:
                `"config.json"`
            repo_type (`str`, *optional*):
                Set to `"dataset"` or `"space"` if getting repository info from a dataset or a space,
                `None` or `"model"` if getting repository info from a model. Default is `None`.
            revision (`str`, *optional*):
                The revision of the repository from which to get the information. Defaults to `"main"` branch.
            token (`bool` or `str`, *optional*):
                A valid authentication token (see https://huggingface.co/settings/token).
                If `None` or `True` and machine is logged in (through `huggingface-cli login`
                or [`~huggingface_hub.login`]), token will be retrieved from the cache.
                If `False`, token is not sent in the request header.

        Returns:
            True if the file exists, False otherwise.

        <Tip>

        Examples:
            ```py
            >>> from huggingface_hub import file_exists
            >>> file_exists("bigcode/starcoder", "config.json")
            True
            >>> file_exists("bigcode/starcoder", "not-a-file")
            False
            >>> file_exists("bigcode/not-a-repo", "config.json")
            False
            ```

        </Tip>
        '''
    def list_files_info(self, repo_id: str, paths: List[str] | str | None = None, *, expand: bool = False, revision: str | None = None, repo_type: str | None = None, token: bool | str | None = None) -> Iterable[RepoFile]:
        '''
        List files on a repo and get information about them.

        Takes as input a list of paths. Those paths can be either files or folders. Two server endpoints are called:
        1. POST "/paths-info" to get information about the provided paths. Called once.
        2. GET  "/tree?recursive=True" to paginate over the input folders. Called only if a folder path is provided as
           input. Will be called multiple times to follow pagination.
        If no path is provided as input, step 1. is ignored and all files from the repo are listed.

        Args:
            repo_id (`str`):
                A namespace (user or an organization) and a repo name separated by a `/`.
            paths (`Union[List[str], str, None]`, *optional*):
                The paths to get information about. Paths to files are directly resolved. Paths to folders are resolved
                recursively which means that information is returned about all files in the folder and its subfolders.
                If `None`, all files are returned (the default). If a path do not exist, it is ignored without raising
                an exception.
            expand (`bool`, *optional*, defaults to `False`):
                Whether to fetch more information about the files (e.g. last commit and security scan results). This
                operation is more expensive for the server so only 50 results are returned per page (instead of 1000).
                As pagination is implemented in `huggingface_hub`, this is transparent for you except for the time it
                takes to get the results.
            revision (`str`, *optional*):
                The revision of the repository from which to get the information. Defaults to `"main"` branch.
            repo_type (`str`, *optional*):
                The type of the repository from which to get the information (`"model"`, `"dataset"` or `"space"`.
                Defaults to `"model"`.
            token (`bool` or `str`, *optional*):
                A valid authentication token (see https://huggingface.co/settings/token). If `None` or `True` and
                machine is logged in (through `huggingface-cli login` or [`~huggingface_hub.login`]), token will be
                retrieved from the cache. If `False`, token is not sent in the request header.

        Returns:
            `Iterable[RepoFile]`:
                The information about the files, as an iterable of [`RepoFile`] objects. The order of the files is
                not guaranteed.

        Raises:
            [`~utils.RepositoryNotFoundError`]:
                If repository is not found (error 404): wrong repo_id/repo_type, private but not authenticated or repo
                does not exist.
            [`~utils.RevisionNotFoundError`]:
                If revision is not found (error 404) on the repo.

        Examples:

            Get information about files on a repo.
            ```py
            >>> from huggingface_hub import list_files_info
            >>> files_info = list_files_info("lysandre/arxiv-nlp", ["README.md", "config.json"])
            >>> files_info
            <generator object HfApi.list_files_info at 0x7f93b848e730>
            >>> list(files_info)
            [
                RepoFile: {"blob_id": "43bd404b159de6fba7c2f4d3264347668d43af25", "lfs": None, "rfilename": "README.md", "size": 391},
                RepoFile: {"blob_id": "2f9618c3a19b9a61add74f70bfb121335aeef666", "lfs": None, "rfilename": "config.json", "size": 554},
            ]
            ```

            Get even more information about files on a repo (last commit and security scan results)
            ```py
            >>> from huggingface_hub import list_files_info
            >>> files_info = list_files_info("prompthero/openjourney-v4", expand=True)
            >>> list(files_info)
            [
                RepoFile: {
                {\'blob_id\': \'815004af1a321eaed1d93f850b2e94b0c0678e42\',
                \'lastCommit\': {\'date\': \'2023-03-21T09:05:27.000Z\',
                                \'id\': \'47b62b20b20e06b9de610e840282b7e6c3d51190\',
                                \'title\': \'Upload diffusers weights (#48)\'},
                \'lfs\': None,
                \'rfilename\': \'model_index.json\',
                \'security\': {\'avScan\': {\'virusFound\': False, \'virusNames\': None},
                                \'blobId\': \'815004af1a321eaed1d93f850b2e94b0c0678e42\',
                                \'name\': \'model_index.json\',
                                \'pickleImportScan\': None,
                                \'repositoryId\': \'models/prompthero/openjourney-v4\',
                                \'safe\': True},
                \'size\': 584}
                },
                RepoFile: {
                {\'blob_id\': \'d2343d78b33ac03dade1d525538b02b130d0a3a0\',
                \'lastCommit\': {\'date\': \'2023-03-21T09:05:27.000Z\',
                                \'id\': \'47b62b20b20e06b9de610e840282b7e6c3d51190\',
                                \'title\': \'Upload diffusers weights (#48)\'},
                \'lfs\': {\'pointer_size\': 134,
                        \'sha256\': \'dcf4507d99b88db73f3916e2a20169fe74ada6b5582e9af56cfa80f5f3141765\',
                        \'size\': 334711857},
                \'rfilename\': \'vae/diffusion_pytorch_model.bin\',
                \'security\': {\'avScan\': {\'virusFound\': False, \'virusNames\': None},
                                \'blobId\': \'d2343d78b33ac03dade1d525538b02b130d0a3a0\',
                                \'name\': \'vae/diffusion_pytorch_model.bin\',
                                \'pickleImportScan\': {\'highestSafetyLevel\': \'innocuous\',
                                                    \'imports\': [{\'module\': \'torch._utils\',
                                                                \'name\': \'_rebuild_tensor_v2\',
                                                                \'safety\': \'innocuous\'},
                                                                {\'module\': \'collections\', \'name\': \'OrderedDict\', \'safety\': \'innocuous\'},
                                                                {\'module\': \'torch\', \'name\': \'FloatStorage\', \'safety\': \'innocuous\'}]},
                                \'repositoryId\': \'models/prompthero/openjourney-v4\',
                                \'safe\': True},
                \'size\': 334711857}
                },
                (...)
            ]
            ```

            List LFS files from the "vae/" folder in "stabilityai/stable-diffusion-2" repository.

            ```py
            >>> from huggingface_hub import list_files_info
            >>> [info.rfilename for info in list_files_info("stabilityai/stable-diffusion-2", "vae") if info.lfs is not None]
            [\'vae/diffusion_pytorch_model.bin\', \'vae/diffusion_pytorch_model.safetensors\']
            ```

            List all files on a repo.
            ```py
            >>> from huggingface_hub import list_files_info
            >>> [info.rfilename for info in list_files_info("glue", repo_type="dataset")]
            [\'.gitattributes\', \'README.md\', \'dataset_infos.json\', \'glue.py\']
            ```
        '''
    def list_repo_files(self, repo_id: str, *, revision: str | None = None, repo_type: str | None = None, timeout: float | None = None, token: bool | str | None = None) -> List[str]:
        '''
        Get the list of files in a given repo.

        Args:
            repo_id (`str`):
                A namespace (user or an organization) and a repo name separated by a `/`.
            revision (`str`, *optional*):
                The revision of the model repository from which to get the information.
            repo_type (`str`, *optional*):
                Set to `"dataset"` or `"space"` if uploading to a dataset or space, `None` or `"model"` if uploading to
                a model. Default is `None`.
            token (`bool` or `str`, *optional*):
                A valid authentication token (see https://huggingface.co/settings/token). If `None` or `True` and
                machine is logged in (through `huggingface-cli login` or [`~huggingface_hub.login`]), token will be
                retrieved from the cache. If `False`, token is not sent in the request header.

        Returns:
            `List[str]`: the list of files in a given repository.
        '''
    def list_repo_refs(self, repo_id: str, *, repo_type: str | None = None, token: bool | str | None = None) -> GitRefs:
        '''
        Get the list of refs of a given repo (both tags and branches).

        Args:
            repo_id (`str`):
                A namespace (user or an organization) and a repo name separated
                by a `/`.
            repo_type (`str`, *optional*):
                Set to `"dataset"` or `"space"` if listing refs from a dataset or a Space,
                `None` or `"model"` if listing from a model. Default is `None`.
            token (`bool` or `str`, *optional*):
                A valid authentication token (see https://huggingface.co/settings/token).
                If `None` or `True` and machine is logged in (through `huggingface-cli login`
                or [`~huggingface_hub.login`]), token will be retrieved from the cache.
                If `False`, token is not sent in the request header.

        Example:
        ```py
        >>> from huggingface_hub import HfApi
        >>> api = HfApi()
        >>> api.list_repo_refs("gpt2")
        GitRefs(branches=[GitRefInfo(name=\'main\', ref=\'refs/heads/main\', target_commit=\'e7da7f221d5bf496a48136c0cd264e630fe9fcc8\')], converts=[], tags=[])

        >>> api.list_repo_refs("bigcode/the-stack", repo_type=\'dataset\')
        GitRefs(
            branches=[
                GitRefInfo(name=\'main\', ref=\'refs/heads/main\', target_commit=\'18edc1591d9ce72aa82f56c4431b3c969b210ae3\'),
                GitRefInfo(name=\'v1.1.a1\', ref=\'refs/heads/v1.1.a1\', target_commit=\'f9826b862d1567f3822d3d25649b0d6d22ace714\')
            ],
            converts=[],
            tags=[
                GitRefInfo(name=\'v1.0\', ref=\'refs/tags/v1.0\', target_commit=\'c37a8cd1e382064d8aced5e05543c5f7753834da\')
            ]
        )
        ```

        Returns:
            [`GitRefs`]: object containing all information about branches and tags for a
            repo on the Hub.
        '''
    def list_repo_commits(self, repo_id: str, *, repo_type: str | None = None, token: bool | str | None = None, revision: str | None = None, formatted: bool = False) -> List[GitCommitInfo]:
        '''
        Get the list of commits of a given revision for a repo on the Hub.

        Commits are sorted by date (last commit first).

        Args:
            repo_id (`str`):
                A namespace (user or an organization) and a repo name separated by a `/`.
            repo_type (`str`, *optional*):
                Set to `"dataset"` or `"space"` if listing commits from a dataset or a Space, `None` or `"model"` if
                listing from a model. Default is `None`.
            token (`bool` or `str`, *optional*):
                A valid authentication token (see https://huggingface.co/settings/token).
                If `None` or `True` and machine is logged in (through `huggingface-cli login`
                or [`~huggingface_hub.login`]), token will be retrieved from the cache.
                If `False`, token is not sent in the request header.
            revision (`str`, *optional*):
                The git revision to commit from. Defaults to the head of the `"main"` branch.
            formatted (`bool`):
                Whether to return the HTML-formatted title and description of the commits. Defaults to False.

        Example:
        ```py
        >>> from huggingface_hub import HfApi
        >>> api = HfApi()

        # Commits are sorted by date (last commit first)
        >>> initial_commit = api.list_repo_commits("gpt2")[-1]

        # Initial commit is always a system commit containing the `.gitattributes` file.
        >>> initial_commit
        GitCommitInfo(
            commit_id=\'9b865efde13a30c13e0a33e536cf3e4a5a9d71d8\',
            authors=[\'system\'],
            created_at=datetime.datetime(2019, 2, 18, 10, 36, 15, tzinfo=datetime.timezone.utc),
            title=\'initial commit\',
            message=\'\',
            formatted_title=None,
            formatted_message=None
        )

        # Create an empty branch by deriving from initial commit
        >>> api.create_branch("gpt2", "new_empty_branch", revision=initial_commit.commit_id)
        ```

        Returns:
            List[[`GitCommitInfo`]]: list of objects containing information about the commits for a repo on the Hub.

        Raises:
            [`~utils.RepositoryNotFoundError`]:
                If repository is not found (error 404): wrong repo_id/repo_type, private but not authenticated or repo
                does not exist.
            [`~utils.RevisionNotFoundError`]:
                If revision is not found (error 404) on the repo.
        '''
    def super_squash_history(self, repo_id: str, *, branch: str | None = None, commit_message: str | None = None, repo_type: str | None = None, token: str | None = None) -> None:
        '''Squash commit history on a branch for a repo on the Hub.

        Squashing the repo history is useful when you know you\'ll make hundreds of commits and you don\'t want to
        clutter the history. Squashing commits can only be performed from the head of a branch.

        <Tip warning={true}>

        Once squashed, the commit history cannot be retrieved. This is a non-revertible operation.

        </Tip>

        <Tip warning={true}>

        Once the history of a branch has been squashed, it is not possible to merge it back into another branch since
        their history will have diverged.

        </Tip>

        Args:
            repo_id (`str`):
                A namespace (user or an organization) and a repo name separated by a `/`.
            branch (`str`, *optional*):
                The branch to squash. Defaults to the head of the `"main"` branch.
            commit_message (`str`, *optional*):
                The commit message to use for the squashed commit.
            repo_type (`str`, *optional*):
                Set to `"dataset"` or `"space"` if listing commits from a dataset or a Space, `None` or `"model"` if
                listing from a model. Default is `None`.
            token (`str`, *optional*):
                A valid authentication token (see https://huggingface.co/settings/token). If the machine is logged in
                (through `huggingface-cli login` or [`~huggingface_hub.login`]), token can be automatically retrieved
                from the cache.

        Raises:
            [`~utils.RepositoryNotFoundError`]:
                If repository is not found (error 404): wrong repo_id/repo_type, private but not authenticated or repo
                does not exist.
            [`~utils.RevisionNotFoundError`]:
                If the branch to squash cannot be found.
            [`~utils.BadRequestError`]:
                If invalid reference for a branch. You cannot squash history on tags.

        Example:
        ```py
        >>> from huggingface_hub import HfApi
        >>> api = HfApi()

        # Create repo
        >>> repo_id = api.create_repo("test-squash").repo_id

        # Make a lot of commits.
        >>> api.upload_file(repo_id=repo_id, path_in_repo="file.txt", path_or_fileobj=b"content")
        >>> api.upload_file(repo_id=repo_id, path_in_repo="lfs.bin", path_or_fileobj=b"content")
        >>> api.upload_file(repo_id=repo_id, path_in_repo="file.txt", path_or_fileobj=b"another_content")

        # Squash history
        >>> api.super_squash_history(repo_id=repo_id)
        ```
        '''
    def create_repo(self, repo_id: str, *, token: str | None = None, private: bool = False, repo_type: str | None = None, exist_ok: bool = False, space_sdk: str | None = None, space_hardware: SpaceHardware | None = None, space_storage: SpaceStorage | None = None, space_sleep_time: int | None = None, space_secrets: List[Dict[str, str]] | None = None, space_variables: List[Dict[str, str]] | None = None) -> RepoUrl:
        '''Create an empty repo on the HuggingFace Hub.

        Args:
            repo_id (`str`):
                A namespace (user or an organization) and a repo name separated
                by a `/`.
            token (`str`, *optional*):
                An authentication token (See https://huggingface.co/settings/token)
            private (`bool`, *optional*, defaults to `False`):
                Whether the model repo should be private.
            repo_type (`str`, *optional*):
                Set to `"dataset"` or `"space"` if uploading to a dataset or
                space, `None` or `"model"` if uploading to a model. Default is
                `None`.
            exist_ok (`bool`, *optional*, defaults to `False`):
                If `True`, do not raise an error if repo already exists.
            space_sdk (`str`, *optional*):
                Choice of SDK to use if repo_type is "space". Can be "streamlit", "gradio", "docker", or "static".
            space_hardware (`SpaceHardware` or `str`, *optional*):
                Choice of Hardware if repo_type is "space". See [`SpaceHardware`] for a complete list.
            space_storage (`SpaceStorage` or `str`, *optional*):
                Choice of persistent storage tier. Example: `"small"`. See [`SpaceStorage`] for a complete list.
            space_sleep_time (`int`, *optional*):
                Number of seconds of inactivity to wait before a Space is put to sleep. Set to `-1` if you don\'t want
                your Space to sleep (default behavior for upgraded hardware). For free hardware, you can\'t configure
                the sleep time (value is fixed to 48 hours of inactivity).
                See https://huggingface.co/docs/hub/spaces-gpus#sleep-time for more details.
            space_secrets (`List[Dict[str, str]]`, *optional*):
                A list of secret keys to set in your Space. Each item is in the form `{"key": ..., "value": ..., "description": ...}` where description is optional.
                For more details, see https://huggingface.co/docs/hub/spaces-overview#managing-secrets.
            space_variables (`List[Dict[str, str]]`, *optional*):
                A list of public environment variables to set in your Space. Each item is in the form `{"key": ..., "value": ..., "description": ...}` where description is optional.
                For more details, see https://huggingface.co/docs/hub/spaces-overview#managing-secrets-and-environment-variables.

        Returns:
            [`RepoUrl`]: URL to the newly created repo. Value is a subclass of `str` containing
            attributes like `endpoint`, `repo_type` and `repo_id`.
        '''
    def delete_repo(self, repo_id: str, *, token: str | None = None, repo_type: str | None = None, missing_ok: bool = False) -> None:
        '''
        Delete a repo from the HuggingFace Hub. CAUTION: this is irreversible.

        Args:
            repo_id (`str`):
                A namespace (user or an organization) and a repo name separated
                by a `/`.
            token (`str`, *optional*):
                An authentication token (See https://huggingface.co/settings/token)
            repo_type (`str`, *optional*):
                Set to `"dataset"` or `"space"` if uploading to a dataset or
                space, `None` or `"model"` if uploading to a model.
            missing_ok (`bool`, *optional*, defaults to `False`):
                If `True`, do not raise an error if repo does not exist.

        Raises:
            - [`~utils.RepositoryNotFoundError`]
              If the repository to delete from cannot be found and `missing_ok` is set to False (default).
        '''
    def update_repo_visibility(self, repo_id: str, private: bool = False, *, token: str | None = None, organization: str | None = None, repo_type: str | None = None, name: str | None = None) -> Dict[str, bool]:
        '''Update the visibility setting of a repository.

        Args:
            repo_id (`str`, *optional*):
                A namespace (user or an organization) and a repo name separated
                by a `/`.
            private (`bool`, *optional*, defaults to `False`):
                Whether the model repo should be private.
            token (`str`, *optional*):
                An authentication token (See https://huggingface.co/settings/token)
            repo_type (`str`, *optional*):
                Set to `"dataset"` or `"space"` if uploading to a dataset or
                space, `None` or `"model"` if uploading to a model. Default is
                `None`.

        Returns:
            The HTTP response in json.

        <Tip>

        Raises the following errors:

            - [`~utils.RepositoryNotFoundError`]
              If the repository to download from cannot be found. This may be because it doesn\'t exist,
              or because it is set to `private` and you do not have access.

        </Tip>
        '''
    def move_repo(self, from_id: str, to_id: str, *, repo_type: str | None = None, token: str | None = None):
        '''
        Moving a repository from namespace1/repo_name1 to namespace2/repo_name2

        Note there are certain limitations. For more information about moving
        repositories, please see
        https://hf.co/docs/hub/repositories-settings#renaming-or-transferring-a-repo.

        Args:
            from_id (`str`):
                A namespace (user or an organization) and a repo name separated
                by a `/`. Original repository identifier.
            to_id (`str`):
                A namespace (user or an organization) and a repo name separated
                by a `/`. Final repository identifier.
            repo_type (`str`, *optional*):
                Set to `"dataset"` or `"space"` if uploading to a dataset or
                space, `None` or `"model"` if uploading to a model. Default is
                `None`.
            token (`str`, *optional*):
                An authentication token (See https://huggingface.co/settings/token)

        <Tip>

        Raises the following errors:

            - [`~utils.RepositoryNotFoundError`]
              If the repository to download from cannot be found. This may be because it doesn\'t exist,
              or because it is set to `private` and you do not have access.

        </Tip>
        '''
    @overload
    def create_commit(self, repo_id: str, operations: Iterable[CommitOperation], *, commit_message: str, commit_description: str | None = None, token: str | None = None, repo_type: str | None = None, revision: str | None = None, create_pr: bool | None = None, num_threads: int = 5, parent_commit: str | None = None, run_as_future: Literal[False] = ...) -> CommitInfo: ...
    @overload
    def create_commit(self, repo_id: str, operations: Iterable[CommitOperation], *, commit_message: str, commit_description: str | None = None, token: str | None = None, repo_type: str | None = None, revision: str | None = None, create_pr: bool | None = None, num_threads: int = 5, parent_commit: str | None = None, run_as_future: Literal[True] = ...) -> Future[CommitInfo]: ...
    def create_commits_on_pr(self, *, repo_id: str, addition_commits: List[List[CommitOperationAdd]], deletion_commits: List[List[CommitOperationDelete]], commit_message: str, commit_description: str | None = None, token: str | None = None, repo_type: str | None = None, merge_pr: bool = True, num_threads: int = 5, verbose: bool = False) -> str:
        '''Push changes to the Hub in multiple commits.

        Commits are pushed to a draft PR branch. If the upload fails or gets interrupted, it can be resumed. Progress
        is tracked in the PR description. At the end of the process, the PR is set as open and the title is updated to
        match the initial commit message. If `merge_pr=True` is passed, the PR is merged automatically.

        All deletion commits are pushed first, followed by the addition commits. The order of the commits is not
        guaranteed as we might implement parallel commits in the future. Be sure that your are not updating several
        times the same file.

        <Tip warning={true}>

        `create_commits_on_pr` is experimental.  Its API and behavior is subject to change in the future without prior notice.

        </Tip>

        <Tip warning={true}>

        `create_commits_on_pr` assumes that the repo already exists on the Hub. If you get a Client error 404, please
        make sure you are authenticated and that `repo_id` and `repo_type` are set correctly. If repo does not exist,
        create it first using [`~hf_api.create_repo`].

        </Tip>

        Args:
            repo_id (`str`):
                The repository in which the commits will be pushed. Example: `"username/my-cool-model"`.

            addition_commits (`List` of `List` of [`~hf_api.CommitOperationAdd`]):
                A list containing lists of [`~hf_api.CommitOperationAdd`]. Each sublist will result in a commit on the
                PR.

            deletion_commits
                A list containing lists of [`~hf_api.CommitOperationDelete`]. Each sublist will result in a commit on
                the PR. Deletion commits are pushed before addition commits.

            commit_message (`str`):
                The summary (first line) of the commit that will be created. Will also be the title of the PR.

            commit_description (`str`, *optional*):
                The description of the commit that will be created. The description will be added to the PR.

            token (`str`, *optional*):
                Authentication token, obtained with `HfApi.login` method. Will default to the stored token.

            repo_type (`str`, *optional*):
                Set to `"dataset"` or `"space"` if uploading to a dataset or space, `None` or `"model"` if uploading to
                a model. Default is `None`.

            merge_pr (`bool`):
                If set to `True`, the Pull Request is merged at the end of the process. Defaults to `True`.

            num_threads (`int`, *optional*):
                Number of concurrent threads for uploading files. Defaults to 5.

            verbose (`bool`):
                If set to `True`, process will run on verbose mode i.e. print information about the ongoing tasks.
                Defaults to `False`.

        Returns:
            `str`: URL to the created PR.

        Example:
        ```python
        >>> from huggingface_hub import HfApi, plan_multi_commits
        >>> addition_commits, deletion_commits = plan_multi_commits(
        ...     operations=[
        ...          CommitOperationAdd(...),
        ...          CommitOperationAdd(...),
        ...          CommitOperationDelete(...),
        ...          CommitOperationDelete(...),
        ...          CommitOperationAdd(...),
        ...     ],
        ... )
        >>> HfApi().create_commits_on_pr(
        ...     repo_id="my-cool-model",
        ...     addition_commits=addition_commits,
        ...     deletion_commits=deletion_commits,
        ...     (...)
        ...     verbose=True,
        ... )
        ```

        Raises:
            [`MultiCommitException`]:
                If an unexpected issue occur in the process: empty commits, unexpected commits in a PR, unexpected PR
                description, etc.
        '''
    def preupload_lfs_files(self, repo_id: str, additions: Iterable[CommitOperationAdd], *, token: str | None = None, repo_type: str | None = None, revision: str | None = None, create_pr: bool | None = None, num_threads: int = 5, free_memory: bool = True):
        '''Pre-upload LFS files to S3 in preparation on a future commit.

        This method is useful if you are generating the files to upload on-the-fly and you don\'t want to store them
        in memory before uploading them all at once.

        <Tip warning={true}>

        This is a power-user method. You shouldn\'t need to call it directly to make a normal commit.
        Use [`create_commit`] directly instead.

        </Tip>

        <Tip warning={true}>

        Commit operations will be mutated during the process. In particular, the attached `path_or_fileobj` will be
        removed after the upload to save memory (and replaced by an empty `bytes` object). Do not reuse the same
        objects except to pass them to [`create_commit`]. If you don\'t want to remove the attached content from the
        commit operation object, pass `free_memory=False`.

        </Tip>

        Args:
            repo_id (`str`):
                The repository in which you will commit the files, for example: `"username/custom_transformers"`.

            operations (`Iterable` of [`CommitOperationAdd`]):
                The list of files to upload. Warning: the objects in this list will be mutated to include information
                relative to the upload. Do not reuse the same objects for multiple commits.

            token (`str`, *optional*):
                Authentication token. Will default to the stored token.

            repo_type (`str`, *optional*):
                The type of repository to upload to (e.g. `"model"` -default-, `"dataset"` or `"space"`).

            revision (`str`, *optional*):
                The git revision to commit from. Defaults to the head of the `"main"` branch.

            create_pr (`boolean`, *optional*):
                Whether or not you plan to create a Pull Request with that commit. Defaults to `False`.

            num_threads (`int`, *optional*):
                Number of concurrent threads for uploading files. Defaults to 5.
                Setting it to 2 means at most 2 files will be uploaded concurrently.

        Example:
        ```py
        >>> from huggingface_hub import CommitOperationAdd, preupload_lfs_files, create_commit, create_repo

        >>> repo_id = create_repo("test_preupload").repo_id

        # Generate and preupload LFS files one by one
        >>> operations = [] # List of all `CommitOperationAdd` objects that will be generated
        >>> for i in range(5):
        ...     content = ... # generate binary content
        ...     addition = CommitOperationAdd(path_in_repo=f"shard_{i}_of_5.bin", path_or_fileobj=content)
        ...     preupload_lfs_files(repo_id, additions=[addition]) # upload + free memory
        ...     operations.append(addition)

        # Create commit
        >>> create_commit(repo_id, operations=operations, commit_message="Commit all shards")
        ```
        '''
    @overload
    def upload_file(self, *, path_or_fileobj: str | Path | bytes | BinaryIO, path_in_repo: str, repo_id: str, token: str | None = None, repo_type: str | None = None, revision: str | None = None, commit_message: str | None = None, commit_description: str | None = None, create_pr: bool | None = None, parent_commit: str | None = None, run_as_future: Literal[False] = ...) -> str: ...
    @overload
    def upload_file(self, *, path_or_fileobj: str | Path | bytes | BinaryIO, path_in_repo: str, repo_id: str, token: str | None = None, repo_type: str | None = None, revision: str | None = None, commit_message: str | None = None, commit_description: str | None = None, create_pr: bool | None = None, parent_commit: str | None = None, run_as_future: Literal[True] = ...) -> Future[str]: ...
    @overload
    def upload_folder(self, *, repo_id: str, folder_path: str | Path, path_in_repo: str | None = None, commit_message: str | None = None, commit_description: str | None = None, token: str | None = None, repo_type: str | None = None, revision: str | None = None, create_pr: bool | None = None, parent_commit: str | None = None, allow_patterns: List[str] | str | None = None, ignore_patterns: List[str] | str | None = None, delete_patterns: List[str] | str | None = None, multi_commits: bool = False, multi_commits_verbose: bool = False, run_as_future: Literal[False] = ...) -> str: ...
    @overload
    def upload_folder(self, *, repo_id: str, folder_path: str | Path, path_in_repo: str | None = None, commit_message: str | None = None, commit_description: str | None = None, token: str | None = None, repo_type: str | None = None, revision: str | None = None, create_pr: bool | None = None, parent_commit: str | None = None, allow_patterns: List[str] | str | None = None, ignore_patterns: List[str] | str | None = None, delete_patterns: List[str] | str | None = None, multi_commits: bool = False, multi_commits_verbose: bool = False, run_as_future: Literal[True] = ...) -> Future[str]: ...
    def delete_file(self, path_in_repo: str, repo_id: str, *, token: str | None = None, repo_type: str | None = None, revision: str | None = None, commit_message: str | None = None, commit_description: str | None = None, create_pr: bool | None = None, parent_commit: str | None = None) -> CommitInfo:
        '''
        Deletes a file in the given repo.

        Args:
            path_in_repo (`str`):
                Relative filepath in the repo, for example:
                `"checkpoints/1fec34a/weights.bin"`
            repo_id (`str`):
                The repository from which the file will be deleted, for example:
                `"username/custom_transformers"`
            token (`str`, *optional*):
                Authentication token, obtained with `HfApi.login` method. Will
                default to the stored token.
            repo_type (`str`, *optional*):
                Set to `"dataset"` or `"space"` if the file is in a dataset or
                space, `None` or `"model"` if in a model. Default is `None`.
            revision (`str`, *optional*):
                The git revision to commit from. Defaults to the head of the `"main"` branch.
            commit_message (`str`, *optional*):
                The summary / title / first line of the generated commit. Defaults to
                `f"Delete {path_in_repo} with huggingface_hub"`.
            commit_description (`str` *optional*)
                The description of the generated commit
            create_pr (`boolean`, *optional*):
                Whether or not to create a Pull Request with that commit. Defaults to `False`.
                If `revision` is not set, PR is opened against the `"main"` branch. If
                `revision` is set and is a branch, PR is opened against this branch. If
                `revision` is set and is not a branch name (example: a commit oid), an
                `RevisionNotFoundError` is returned by the server.
            parent_commit (`str`, *optional*):
                The OID / SHA of the parent commit, as a hexadecimal string. Shorthands (7 first characters) are also supported.
                If specified and `create_pr` is `False`, the commit will fail if `revision` does not point to `parent_commit`.
                If specified and `create_pr` is `True`, the pull request will be created from `parent_commit`.
                Specifying `parent_commit` ensures the repo has not changed before committing the changes, and can be
                especially useful if the repo is updated / committed to concurrently.


        <Tip>

        Raises the following errors:

            - [`HTTPError`](https://requests.readthedocs.io/en/latest/api/#requests.HTTPError)
              if the HuggingFace API returned an error
            - [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError)
              if some parameter value is invalid
            - [`~utils.RepositoryNotFoundError`]
              If the repository to download from cannot be found. This may be because it doesn\'t exist,
              or because it is set to `private` and you do not have access.
            - [`~utils.RevisionNotFoundError`]
              If the revision to download from cannot be found.
            - [`~utils.EntryNotFoundError`]
              If the file to download cannot be found.

        </Tip>

        '''
    def delete_folder(self, path_in_repo: str, repo_id: str, *, token: str | None = None, repo_type: str | None = None, revision: str | None = None, commit_message: str | None = None, commit_description: str | None = None, create_pr: bool | None = None, parent_commit: str | None = None) -> CommitInfo:
        '''
        Deletes a folder in the given repo.

        Simple wrapper around [`create_commit`] method.

        Args:
            path_in_repo (`str`):
                Relative folder path in the repo, for example: `"checkpoints/1fec34a"`.
            repo_id (`str`):
                The repository from which the folder will be deleted, for example:
                `"username/custom_transformers"`
            token (`str`, *optional*):
                Authentication token, obtained with `HfApi.login` method. Will default
                to the stored token.
            repo_type (`str`, *optional*):
                Set to `"dataset"` or `"space"` if the folder is in a dataset or
                space, `None` or `"model"` if in a model. Default is `None`.
            revision (`str`, *optional*):
                The git revision to commit from. Defaults to the head of the `"main"` branch.
            commit_message (`str`, *optional*):
                The summary / title / first line of the generated commit. Defaults to
                `f"Delete folder {path_in_repo} with huggingface_hub"`.
            commit_description (`str` *optional*)
                The description of the generated commit.
            create_pr (`boolean`, *optional*):
                Whether or not to create a Pull Request with that commit. Defaults to `False`.
                If `revision` is not set, PR is opened against the `"main"` branch. If
                `revision` is set and is a branch, PR is opened against this branch. If
                `revision` is set and is not a branch name (example: a commit oid), an
                `RevisionNotFoundError` is returned by the server.
            parent_commit (`str`, *optional*):
                The OID / SHA of the parent commit, as a hexadecimal string. Shorthands (7 first characters) are also supported.
                If specified and `create_pr` is `False`, the commit will fail if `revision` does not point to `parent_commit`.
                If specified and `create_pr` is `True`, the pull request will be created from `parent_commit`.
                Specifying `parent_commit` ensures the repo has not changed before committing the changes, and can be
                especially useful if the repo is updated / committed to concurrently.
        '''
    def hf_hub_download(self, repo_id: str, filename: str, *, subfolder: str | None = None, repo_type: str | None = None, revision: str | None = None, cache_dir: str | Path | None = None, local_dir: str | Path | None = None, local_dir_use_symlinks: bool | Literal['auto'] = 'auto', force_download: bool = False, force_filename: str | None = None, proxies: Dict | None = None, etag_timeout: float = 10, resume_download: bool = False, token: str | bool | None = None, local_files_only: bool = False, legacy_cache_layout: bool = False) -> str:
        '''Download a given file if it\'s not already present in the local cache.

        The new cache file layout looks like this:
        - The cache directory contains one subfolder per repo_id (namespaced by repo type)
        - inside each repo folder:
            - refs is a list of the latest known revision => commit_hash pairs
            - blobs contains the actual file blobs (identified by their git-sha or sha256, depending on
            whether they\'re LFS files or not)
            - snapshots contains one subfolder per commit, each "commit" contains the subset of the files
            that have been resolved at that particular commit. Each filename is a symlink to the blob
            at that particular commit.

        If `local_dir` is provided, the file structure from the repo will be replicated in this location. You can configure
        how you want to move those files:
        - If `local_dir_use_symlinks="auto"` (default), files are downloaded and stored in the cache directory as blob
            files. Small files (<5MB) are duplicated in `local_dir` while a symlink is created for bigger files. The goal
            is to be able to manually edit and save small files without corrupting the cache while saving disk space for
            binary files. The 5MB threshold can be configured with the `HF_HUB_LOCAL_DIR_AUTO_SYMLINK_THRESHOLD`
            environment variable.
        - If `local_dir_use_symlinks=True`, files are downloaded, stored in the cache directory and symlinked in `local_dir`.
            This is optimal in term of disk usage but files must not be manually edited.
        - If `local_dir_use_symlinks=False` and the blob files exist in the cache directory, they are duplicated in the
            local dir. This means disk usage is not optimized.
        - Finally, if `local_dir_use_symlinks=False` and the blob files do not exist in the cache directory, then the
            files are downloaded and directly placed under `local_dir`. This means if you need to download them again later,
            they will be re-downloaded entirely.

        ```
        [  96]  .
        └── [ 160]  models--julien-c--EsperBERTo-small
            ├── [ 160]  blobs
            │   ├── [321M]  403450e234d65943a7dcf7e05a771ce3c92faa84dd07db4ac20f592037a1e4bd
            │   ├── [ 398]  7cb18dc9bafbfcf74629a4b760af1b160957a83e
            │   └── [1.4K]  d7edf6bd2a681fb0175f7735299831ee1b22b812
            ├── [  96]  refs
            │   └── [  40]  main
            └── [ 128]  snapshots
                ├── [ 128]  2439f60ef33a0d46d85da5001d52aeda5b00ce9f
                │   ├── [  52]  README.md -> ../../blobs/d7edf6bd2a681fb0175f7735299831ee1b22b812
                │   └── [  76]  pytorch_model.bin -> ../../blobs/403450e234d65943a7dcf7e05a771ce3c92faa84dd07db4ac20f592037a1e4bd
                └── [ 128]  bbc77c8132af1cc5cf678da3f1ddf2de43606d48
                    ├── [  52]  README.md -> ../../blobs/7cb18dc9bafbfcf74629a4b760af1b160957a83e
                    └── [  76]  pytorch_model.bin -> ../../blobs/403450e234d65943a7dcf7e05a771ce3c92faa84dd07db4ac20f592037a1e4bd
        ```

        Args:
            repo_id (`str`):
                A user or an organization name and a repo name separated by a `/`.
            filename (`str`):
                The name of the file in the repo.
            subfolder (`str`, *optional*):
                An optional value corresponding to a folder inside the model repo.
            repo_type (`str`, *optional*):
                Set to `"dataset"` or `"space"` if downloading from a dataset or space,
                `None` or `"model"` if downloading from a model. Default is `None`.
            revision (`str`, *optional*):
                An optional Git revision id which can be a branch name, a tag, or a
                commit hash.
            endpoint (`str`, *optional*):
                Hugging Face Hub base url. Will default to https://huggingface.co/. Otherwise, one can set the `HF_ENDPOINT`
                environment variable.
            cache_dir (`str`, `Path`, *optional*):
                Path to the folder where cached files are stored.
            local_dir (`str` or `Path`, *optional*):
                If provided, the downloaded file will be placed under this directory, either as a symlink (default) or
                a regular file (see description for more details).
            local_dir_use_symlinks (`"auto"` or `bool`, defaults to `"auto"`):
                To be used with `local_dir`. If set to "auto", the cache directory will be used and the file will be either
                duplicated or symlinked to the local directory depending on its size. It set to `True`, a symlink will be
                created, no matter the file size. If set to `False`, the file will either be duplicated from cache (if
                already exists) or downloaded from the Hub and not cached. See description for more details.
            force_download (`bool`, *optional*, defaults to `False`):
                Whether the file should be downloaded even if it already exists in
                the local cache.
            proxies (`dict`, *optional*):
                Dictionary mapping protocol to the URL of the proxy passed to
                `requests.request`.
            etag_timeout (`float`, *optional*, defaults to `10`):
                When fetching ETag, how many seconds to wait for the server to send
                data before giving up which is passed to `requests.request`.
            resume_download (`bool`, *optional*, defaults to `False`):
                If `True`, resume a previously interrupted download.
            token (`bool` or `str`, *optional*):
                A valid authentication token (see https://huggingface.co/settings/token).
                If `None` or `True` and machine is logged in (through `huggingface-cli login`
                or [`~huggingface_hub.login`]), token will be retrieved from the cache.
                If `False`, token is not sent in the request header.
            local_files_only (`bool`, *optional*, defaults to `False`):
                If `True`, avoid downloading the file and return the path to the
                local cached file if it exists.
            legacy_cache_layout (`bool`, *optional*, defaults to `False`):
                If `True`, uses the legacy file cache layout i.e. just call [`hf_hub_url`]
                then `cached_download`. This is deprecated as the new cache layout is
                more powerful.

        Returns:
            Local path (string) of file or if networking is off, last version of
            file cached on disk.

        <Tip>

        Raises the following errors:

            - [`EnvironmentError`](https://docs.python.org/3/library/exceptions.html#EnvironmentError)
            if `token=True` and the token cannot be found.
            - [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError)
            if ETag cannot be determined.
            - [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError)
            if some parameter value is invalid
            - [`~utils.RepositoryNotFoundError`]
            If the repository to download from cannot be found. This may be because it doesn\'t exist,
            or because it is set to `private` and you do not have access.
            - [`~utils.RevisionNotFoundError`]
            If the revision to download from cannot be found.
            - [`~utils.EntryNotFoundError`]
            If the file to download cannot be found.
            - [`~utils.LocalEntryNotFoundError`]
            If network is disabled or unavailable and file is not found in cache.

        </Tip>
        '''
    def snapshot_download(self, repo_id: str, *, repo_type: str | None = None, revision: str | None = None, cache_dir: str | Path | None = None, local_dir: str | Path | None = None, local_dir_use_symlinks: bool | Literal['auto'] = 'auto', proxies: Dict | None = None, etag_timeout: float = 10, resume_download: bool = False, force_download: bool = False, token: str | bool | None = None, local_files_only: bool = False, allow_patterns: List[str] | str | None = None, ignore_patterns: List[str] | str | None = None, max_workers: int = 8, tqdm_class: base_tqdm | None = None) -> str:
        '''Download repo files.

        Download a whole snapshot of a repo\'s files at the specified revision. This is useful when you want all files from
        a repo, because you don\'t know which ones you will need a priori. All files are nested inside a folder in order
        to keep their actual filename relative to that folder. You can also filter which files to download using
        `allow_patterns` and `ignore_patterns`.

        If `local_dir` is provided, the file structure from the repo will be replicated in this location. You can configure
        how you want to move those files:
        - If `local_dir_use_symlinks="auto"` (default), files are downloaded and stored in the cache directory as blob
            files. Small files (<5MB) are duplicated in `local_dir` while a symlink is created for bigger files. The goal
            is to be able to manually edit and save small files without corrupting the cache while saving disk space for
            binary files. The 5MB threshold can be configured with the `HF_HUB_LOCAL_DIR_AUTO_SYMLINK_THRESHOLD`
            environment variable.
        - If `local_dir_use_symlinks=True`, files are downloaded, stored in the cache directory and symlinked in `local_dir`.
            This is optimal in term of disk usage but files must not be manually edited.
        - If `local_dir_use_symlinks=False` and the blob files exist in the cache directory, they are duplicated in the
            local dir. This means disk usage is not optimized.
        - Finally, if `local_dir_use_symlinks=False` and the blob files do not exist in the cache directory, then the
            files are downloaded and directly placed under `local_dir`. This means if you need to download them again later,
            they will be re-downloaded entirely.

        An alternative would be to clone the repo but this requires git and git-lfs to be installed and properly
        configured. It is also not possible to filter which files to download when cloning a repository using git.

        Args:
            repo_id (`str`):
                A user or an organization name and a repo name separated by a `/`.
            repo_type (`str`, *optional*):
                Set to `"dataset"` or `"space"` if downloading from a dataset or space,
                `None` or `"model"` if downloading from a model. Default is `None`.
            revision (`str`, *optional*):
                An optional Git revision id which can be a branch name, a tag, or a
                commit hash.
            cache_dir (`str`, `Path`, *optional*):
                Path to the folder where cached files are stored.
            local_dir (`str` or `Path`, *optional*):
                If provided, the downloaded files will be placed under this directory, either as symlinks (default) or
                regular files (see description for more details).
            local_dir_use_symlinks (`"auto"` or `bool`, defaults to `"auto"`):
                To be used with `local_dir`. If set to "auto", the cache directory will be used and the file will be either
                duplicated or symlinked to the local directory depending on its size. It set to `True`, a symlink will be
                created, no matter the file size. If set to `False`, the file will either be duplicated from cache (if
                already exists) or downloaded from the Hub and not cached. See description for more details.
            proxies (`dict`, *optional*):
                Dictionary mapping protocol to the URL of the proxy passed to
                `requests.request`.
            etag_timeout (`float`, *optional*, defaults to `10`):
                When fetching ETag, how many seconds to wait for the server to send
                data before giving up which is passed to `requests.request`.
            resume_download (`bool`, *optional*, defaults to `False):
                If `True`, resume a previously interrupted download.
            force_download (`bool`, *optional*, defaults to `False`):
                Whether the file should be downloaded even if it already exists in the local cache.
            token (`bool` or `str`, *optional*):
                A valid authentication token (see https://huggingface.co/settings/token).
                If `None` or `True` and machine is logged in (through `huggingface-cli login`
                or [`~huggingface_hub.login`]), token will be retrieved from the cache.
                If `False`, token is not sent in the request header.
            local_files_only (`bool`, *optional*, defaults to `False`):
                If `True`, avoid downloading the file and return the path to the
                local cached file if it exists.
            allow_patterns (`List[str]` or `str`, *optional*):
                If provided, only files matching at least one pattern are downloaded.
            ignore_patterns (`List[str]` or `str`, *optional*):
                If provided, files matching any of the patterns are not downloaded.
            max_workers (`int`, *optional*):
                Number of concurrent threads to download files (1 thread = 1 file download).
                Defaults to 8.
            tqdm_class (`tqdm`, *optional*):
                If provided, overwrites the default behavior for the progress bar. Passed
                argument must inherit from `tqdm.auto.tqdm` or at least mimic its behavior.
                Note that the `tqdm_class` is not passed to each individual download.
                Defaults to the custom HF progress bar that can be disabled by setting
                `HF_HUB_DISABLE_PROGRESS_BARS` environment variable.

        Returns:
            Local folder path (string) of repo snapshot

        <Tip>

        Raises the following errors:

        - [`EnvironmentError`](https://docs.python.org/3/library/exceptions.html#EnvironmentError)
        if `token=True` and the token cannot be found.
        - [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError) if
        ETag cannot be determined.
        - [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError)
        if some parameter value is invalid

        </Tip>
        '''
    def create_branch(self, repo_id: str, *, branch: str, revision: str | None = None, token: str | None = None, repo_type: str | None = None, exist_ok: bool = False) -> None:
        '''
        Create a new branch for a repo on the Hub, starting from the specified revision (defaults to `main`).
        To find a revision suiting your needs, you can use [`list_repo_refs`] or [`list_repo_commits`].

        Args:
            repo_id (`str`):
                The repository in which the branch will be created.
                Example: `"user/my-cool-model"`.

            branch (`str`):
                The name of the branch to create.

            revision (`str`, *optional*):
                The git revision to create the branch from. It can be a branch name or
                the OID/SHA of a commit, as a hexadecimal string. Defaults to the head
                of the `"main"` branch.

            token (`str`, *optional*):
                Authentication token. Will default to the stored token.

            repo_type (`str`, *optional*):
                Set to `"dataset"` or `"space"` if creating a branch on a dataset or
                space, `None` or `"model"` if tagging a model. Default is `None`.

            exist_ok (`bool`, *optional*, defaults to `False`):
                If `True`, do not raise an error if branch already exists.

        Raises:
            [`~utils.RepositoryNotFoundError`]:
                If repository is not found (error 404): wrong repo_id/repo_type, private
                but not authenticated or repo does not exist.
            [`~utils.BadRequestError`]:
                If invalid reference for a branch. Ex: `refs/pr/5` or \'refs/foo/bar\'.
            [`~utils.HfHubHTTPError`]:
                If the branch already exists on the repo (error 409) and `exist_ok` is
                set to `False`.
        '''
    def delete_branch(self, repo_id: str, *, branch: str, token: str | None = None, repo_type: str | None = None) -> None:
        '''
        Delete a branch from a repo on the Hub.

        Args:
            repo_id (`str`):
                The repository in which a branch will be deleted.
                Example: `"user/my-cool-model"`.

            branch (`str`):
                The name of the branch to delete.

            token (`str`, *optional*):
                Authentication token. Will default to the stored token.

            repo_type (`str`, *optional*):
                Set to `"dataset"` or `"space"` if creating a branch on a dataset or
                space, `None` or `"model"` if tagging a model. Default is `None`.

        Raises:
            [`~utils.RepositoryNotFoundError`]:
                If repository is not found (error 404): wrong repo_id/repo_type, private
                but not authenticated or repo does not exist.
            [`~utils.HfHubHTTPError`]:
                If trying to delete a protected branch. Ex: `main` cannot be deleted.
            [`~utils.HfHubHTTPError`]:
                If trying to delete a branch that does not exist.

        '''
    def create_tag(self, repo_id: str, *, tag: str, tag_message: str | None = None, revision: str | None = None, token: str | None = None, repo_type: str | None = None, exist_ok: bool = False) -> None:
        '''
        Tag a given commit of a repo on the Hub.

        Args:
            repo_id (`str`):
                The repository in which a commit will be tagged.
                Example: `"user/my-cool-model"`.

            tag (`str`):
                The name of the tag to create.

            tag_message (`str`, *optional*):
                The description of the tag to create.

            revision (`str`, *optional*):
                The git revision to tag. It can be a branch name or the OID/SHA of a
                commit, as a hexadecimal string. Shorthands (7 first characters) are
                also supported. Defaults to the head of the `"main"` branch.

            token (`str`, *optional*):
                Authentication token. Will default to the stored token.

            repo_type (`str`, *optional*):
                Set to `"dataset"` or `"space"` if tagging a dataset or
                space, `None` or `"model"` if tagging a model. Default is
                `None`.

            exist_ok (`bool`, *optional*, defaults to `False`):
                If `True`, do not raise an error if tag already exists.

        Raises:
            [`~utils.RepositoryNotFoundError`]:
                If repository is not found (error 404): wrong repo_id/repo_type, private
                but not authenticated or repo does not exist.
            [`~utils.RevisionNotFoundError`]:
                If revision is not found (error 404) on the repo.
            [`~utils.HfHubHTTPError`]:
                If the branch already exists on the repo (error 409) and `exist_ok` is
                set to `False`.
        '''
    def delete_tag(self, repo_id: str, *, tag: str, token: str | None = None, repo_type: str | None = None) -> None:
        '''
        Delete a tag from a repo on the Hub.

        Args:
            repo_id (`str`):
                The repository in which a tag will be deleted.
                Example: `"user/my-cool-model"`.

            tag (`str`):
                The name of the tag to delete.

            token (`str`, *optional*):
                Authentication token. Will default to the stored token.

            repo_type (`str`, *optional*):
                Set to `"dataset"` or `"space"` if tagging a dataset or space, `None` or
                `"model"` if tagging a model. Default is `None`.

        Raises:
            [`~utils.RepositoryNotFoundError`]:
                If repository is not found (error 404): wrong repo_id/repo_type, private
                but not authenticated or repo does not exist.
            [`~utils.RevisionNotFoundError`]:
                If tag is not found.
        '''
    def get_full_repo_name(self, model_id: str, *, organization: str | None = None, token: bool | str | None = None):
        """
        Returns the repository name for a given model ID and optional
        organization.

        Args:
            model_id (`str`):
                The name of the model.
            organization (`str`, *optional*):
                If passed, the repository name will be in the organization
                namespace instead of the user namespace.
            token (`bool` or `str`, *optional*):
                A valid authentication token (see https://huggingface.co/settings/token).
                If `None` or `True` and machine is logged in (through `huggingface-cli login`
                or [`~huggingface_hub.login`]), token will be retrieved from the cache.
                If `False`, token is not sent in the request header.

        Returns:
            `str`: The repository name in the user's namespace
            ({username}/{model_id}) if no organization is passed, and under the
            organization namespace ({organization}/{model_id}) otherwise.
        """
    def get_repo_discussions(self, repo_id: str, *, repo_type: str | None = None, token: str | None = None) -> Iterator[Discussion]:
        '''
        Fetches Discussions and Pull Requests for the given repo.

        Args:
            repo_id (`str`):
                A namespace (user or an organization) and a repo name separated
                by a `/`.
            repo_type (`str`, *optional*):
                Set to `"dataset"` or `"space"` if fetching from a dataset or
                space, `None` or `"model"` if fetching from a model. Default is
                `None`.
            token (`str`, *optional*):
                An authentication token (See https://huggingface.co/settings/token).

        Returns:
            `Iterator[Discussion]`: An iterator of [`Discussion`] objects.

        Example:
            Collecting all discussions of a repo in a list:

            ```python
            >>> from huggingface_hub import get_repo_discussions
            >>> discussions_list = list(get_repo_discussions(repo_id="bert-base-uncased"))
            ```

            Iterating over discussions of a repo:

            ```python
            >>> from huggingface_hub import get_repo_discussions
            >>> for discussion in get_repo_discussions(repo_id="bert-base-uncased"):
            ...     print(discussion.num, discussion.title)
            ```
        '''
    def get_discussion_details(self, repo_id: str, discussion_num: int, *, repo_type: str | None = None, token: str | None = None) -> DiscussionWithDetails:
        '''Fetches a Discussion\'s / Pull Request \'s details from the Hub.

        Args:
            repo_id (`str`):
                A namespace (user or an organization) and a repo name separated
                by a `/`.
            discussion_num (`int`):
                The number of the Discussion or Pull Request . Must be a strictly positive integer.
            repo_type (`str`, *optional*):
                Set to `"dataset"` or `"space"` if uploading to a dataset or
                space, `None` or `"model"` if uploading to a model. Default is
                `None`.
            token (`str`, *optional*):
                An authentication token (See https://huggingface.co/settings/token)

        Returns: [`DiscussionWithDetails`]

        <Tip>

        Raises the following errors:

            - [`HTTPError`](https://requests.readthedocs.io/en/latest/api/#requests.HTTPError)
              if the HuggingFace API returned an error
            - [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError)
              if some parameter value is invalid
            - [`~utils.RepositoryNotFoundError`]
              If the repository to download from cannot be found. This may be because it doesn\'t exist,
              or because it is set to `private` and you do not have access.

        </Tip>
        '''
    def create_discussion(self, repo_id: str, title: str, *, token: str | None = None, description: str | None = None, repo_type: str | None = None, pull_request: bool = False) -> DiscussionWithDetails:
        '''Creates a Discussion or Pull Request.

        Pull Requests created programmatically will be in `"draft"` status.

        Creating a Pull Request with changes can also be done at once with [`HfApi.create_commit`].

        Args:
            repo_id (`str`):
                A namespace (user or an organization) and a repo name separated
                by a `/`.
            title (`str`):
                The title of the discussion. It can be up to 200 characters long,
                and must be at least 3 characters long. Leading and trailing whitespaces
                will be stripped.
            token (`str`, *optional*):
                An authentication token (See https://huggingface.co/settings/token)
            description (`str`, *optional*):
                An optional description for the Pull Request.
                Defaults to `"Discussion opened with the huggingface_hub Python library"`
            pull_request (`bool`, *optional*):
                Whether to create a Pull Request or discussion. If `True`, creates a Pull Request.
                If `False`, creates a discussion. Defaults to `False`.
            repo_type (`str`, *optional*):
                Set to `"dataset"` or `"space"` if uploading to a dataset or
                space, `None` or `"model"` if uploading to a model. Default is
                `None`.

        Returns: [`DiscussionWithDetails`]

        <Tip>

        Raises the following errors:

            - [`HTTPError`](https://requests.readthedocs.io/en/latest/api/#requests.HTTPError)
              if the HuggingFace API returned an error
            - [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError)
              if some parameter value is invalid
            - [`~utils.RepositoryNotFoundError`]
              If the repository to download from cannot be found. This may be because it doesn\'t exist,
              or because it is set to `private` and you do not have access.

        </Tip>'''
    def create_pull_request(self, repo_id: str, title: str, *, token: str | None = None, description: str | None = None, repo_type: str | None = None) -> DiscussionWithDetails:
        '''Creates a Pull Request . Pull Requests created programmatically will be in `"draft"` status.

        Creating a Pull Request with changes can also be done at once with [`HfApi.create_commit`];

        This is a wrapper around [`HfApi.create_discussion`].

        Args:
            repo_id (`str`):
                A namespace (user or an organization) and a repo name separated
                by a `/`.
            title (`str`):
                The title of the discussion. It can be up to 200 characters long,
                and must be at least 3 characters long. Leading and trailing whitespaces
                will be stripped.
            token (`str`, *optional*):
                An authentication token (See https://huggingface.co/settings/token)
            description (`str`, *optional*):
                An optional description for the Pull Request.
                Defaults to `"Discussion opened with the huggingface_hub Python library"`
            repo_type (`str`, *optional*):
                Set to `"dataset"` or `"space"` if uploading to a dataset or
                space, `None` or `"model"` if uploading to a model. Default is
                `None`.

        Returns: [`DiscussionWithDetails`]

        <Tip>

        Raises the following errors:

            - [`HTTPError`](https://requests.readthedocs.io/en/latest/api/#requests.HTTPError)
              if the HuggingFace API returned an error
            - [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError)
              if some parameter value is invalid
            - [`~utils.RepositoryNotFoundError`]
              If the repository to download from cannot be found. This may be because it doesn\'t exist,
              or because it is set to `private` and you do not have access.

        </Tip>'''
    def comment_discussion(self, repo_id: str, discussion_num: int, comment: str, *, token: str | None = None, repo_type: str | None = None) -> DiscussionComment:
        '''Creates a new comment on the given Discussion.

        Args:
            repo_id (`str`):
                A namespace (user or an organization) and a repo name separated
                by a `/`.
            discussion_num (`int`):
                The number of the Discussion or Pull Request . Must be a strictly positive integer.
            comment (`str`):
                The content of the comment to create. Comments support markdown formatting.
            repo_type (`str`, *optional*):
                Set to `"dataset"` or `"space"` if uploading to a dataset or
                space, `None` or `"model"` if uploading to a model. Default is
                `None`.
            token (`str`, *optional*):
                An authentication token (See https://huggingface.co/settings/token)

        Returns:
            [`DiscussionComment`]: the newly created comment


        Examples:
            ```python

            >>> comment = """
            ... Hello @otheruser!
            ...
            ... # This is a title
            ...
            ... **This is bold**, *this is italic* and ~this is strikethrough~
            ... And [this](http://url) is a link
            ... """

            >>> HfApi().comment_discussion(
            ...     repo_id="username/repo_name",
            ...     discussion_num=34
            ...     comment=comment
            ... )
            # DiscussionComment(id=\'deadbeef0000000\', type=\'comment\', ...)

            ```

        <Tip>

        Raises the following errors:

            - [`HTTPError`](https://requests.readthedocs.io/en/latest/api/#requests.HTTPError)
              if the HuggingFace API returned an error
            - [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError)
              if some parameter value is invalid
            - [`~utils.RepositoryNotFoundError`]
              If the repository to download from cannot be found. This may be because it doesn\'t exist,
              or because it is set to `private` and you do not have access.

        </Tip>
        '''
    def rename_discussion(self, repo_id: str, discussion_num: int, new_title: str, *, token: str | None = None, repo_type: str | None = None) -> DiscussionTitleChange:
        '''Renames a Discussion.

        Args:
            repo_id (`str`):
                A namespace (user or an organization) and a repo name separated
                by a `/`.
            discussion_num (`int`):
                The number of the Discussion or Pull Request . Must be a strictly positive integer.
            new_title (`str`):
                The new title for the discussion
            repo_type (`str`, *optional*):
                Set to `"dataset"` or `"space"` if uploading to a dataset or
                space, `None` or `"model"` if uploading to a model. Default is
                `None`.
            token (`str`, *optional*):
                An authentication token (See https://huggingface.co/settings/token)

        Returns:
            [`DiscussionTitleChange`]: the title change event


        Examples:
            ```python
            >>> new_title = "New title, fixing a typo"
            >>> HfApi().rename_discussion(
            ...     repo_id="username/repo_name",
            ...     discussion_num=34
            ...     new_title=new_title
            ... )
            # DiscussionTitleChange(id=\'deadbeef0000000\', type=\'title-change\', ...)

            ```

        <Tip>

        Raises the following errors:

            - [`HTTPError`](https://requests.readthedocs.io/en/latest/api/#requests.HTTPError)
              if the HuggingFace API returned an error
            - [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError)
              if some parameter value is invalid
            - [`~utils.RepositoryNotFoundError`]
              If the repository to download from cannot be found. This may be because it doesn\'t exist,
              or because it is set to `private` and you do not have access.

        </Tip>
        '''
    def change_discussion_status(self, repo_id: str, discussion_num: int, new_status: Literal['open', 'closed'], *, token: str | None = None, comment: str | None = None, repo_type: str | None = None) -> DiscussionStatusChange:
        '''Closes or re-opens a Discussion or Pull Request.

        Args:
            repo_id (`str`):
                A namespace (user or an organization) and a repo name separated
                by a `/`.
            discussion_num (`int`):
                The number of the Discussion or Pull Request . Must be a strictly positive integer.
            new_status (`str`):
                The new status for the discussion, either `"open"` or `"closed"`.
            comment (`str`, *optional*):
                An optional comment to post with the status change.
            repo_type (`str`, *optional*):
                Set to `"dataset"` or `"space"` if uploading to a dataset or
                space, `None` or `"model"` if uploading to a model. Default is
                `None`.
            token (`str`, *optional*):
                An authentication token (See https://huggingface.co/settings/token)

        Returns:
            [`DiscussionStatusChange`]: the status change event


        Examples:
            ```python
            >>> new_title = "New title, fixing a typo"
            >>> HfApi().rename_discussion(
            ...     repo_id="username/repo_name",
            ...     discussion_num=34
            ...     new_title=new_title
            ... )
            # DiscussionStatusChange(id=\'deadbeef0000000\', type=\'status-change\', ...)

            ```

        <Tip>

        Raises the following errors:

            - [`HTTPError`](https://requests.readthedocs.io/en/latest/api/#requests.HTTPError)
              if the HuggingFace API returned an error
            - [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError)
              if some parameter value is invalid
            - [`~utils.RepositoryNotFoundError`]
              If the repository to download from cannot be found. This may be because it doesn\'t exist,
              or because it is set to `private` and you do not have access.

        </Tip>
        '''
    def merge_pull_request(self, repo_id: str, discussion_num: int, *, token: str | None = None, comment: str | None = None, repo_type: str | None = None):
        '''Merges a Pull Request.

        Args:
            repo_id (`str`):
                A namespace (user or an organization) and a repo name separated
                by a `/`.
            discussion_num (`int`):
                The number of the Discussion or Pull Request . Must be a strictly positive integer.
            comment (`str`, *optional*):
                An optional comment to post with the status change.
            repo_type (`str`, *optional*):
                Set to `"dataset"` or `"space"` if uploading to a dataset or
                space, `None` or `"model"` if uploading to a model. Default is
                `None`.
            token (`str`, *optional*):
                An authentication token (See https://huggingface.co/settings/token)

        Returns:
            [`DiscussionStatusChange`]: the status change event

        <Tip>

        Raises the following errors:

            - [`HTTPError`](https://requests.readthedocs.io/en/latest/api/#requests.HTTPError)
              if the HuggingFace API returned an error
            - [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError)
              if some parameter value is invalid
            - [`~utils.RepositoryNotFoundError`]
              If the repository to download from cannot be found. This may be because it doesn\'t exist,
              or because it is set to `private` and you do not have access.

        </Tip>
        '''
    def edit_discussion_comment(self, repo_id: str, discussion_num: int, comment_id: str, new_content: str, *, token: str | None = None, repo_type: str | None = None) -> DiscussionComment:
        '''Edits a comment on a Discussion / Pull Request.

        Args:
            repo_id (`str`):
                A namespace (user or an organization) and a repo name separated
                by a `/`.
            discussion_num (`int`):
                The number of the Discussion or Pull Request . Must be a strictly positive integer.
            comment_id (`str`):
                The ID of the comment to edit.
            new_content (`str`):
                The new content of the comment. Comments support markdown formatting.
            repo_type (`str`, *optional*):
                Set to `"dataset"` or `"space"` if uploading to a dataset or
                space, `None` or `"model"` if uploading to a model. Default is
                `None`.
            token (`str`, *optional*):
                An authentication token (See https://huggingface.co/settings/token)

        Returns:
            [`DiscussionComment`]: the edited comment

        <Tip>

        Raises the following errors:

            - [`HTTPError`](https://requests.readthedocs.io/en/latest/api/#requests.HTTPError)
              if the HuggingFace API returned an error
            - [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError)
              if some parameter value is invalid
            - [`~utils.RepositoryNotFoundError`]
              If the repository to download from cannot be found. This may be because it doesn\'t exist,
              or because it is set to `private` and you do not have access.

        </Tip>
        '''
    def hide_discussion_comment(self, repo_id: str, discussion_num: int, comment_id: str, *, token: str | None = None, repo_type: str | None = None) -> DiscussionComment:
        '''Hides a comment on a Discussion / Pull Request.

        <Tip warning={true}>
        Hidden comments\' content cannot be retrieved anymore. Hiding a comment is irreversible.
        </Tip>

        Args:
            repo_id (`str`):
                A namespace (user or an organization) and a repo name separated
                by a `/`.
            discussion_num (`int`):
                The number of the Discussion or Pull Request . Must be a strictly positive integer.
            comment_id (`str`):
                The ID of the comment to edit.
            repo_type (`str`, *optional*):
                Set to `"dataset"` or `"space"` if uploading to a dataset or
                space, `None` or `"model"` if uploading to a model. Default is
                `None`.
            token (`str`, *optional*):
                An authentication token (See https://huggingface.co/settings/token)

        Returns:
            [`DiscussionComment`]: the hidden comment

        <Tip>

        Raises the following errors:

            - [`HTTPError`](https://requests.readthedocs.io/en/latest/api/#requests.HTTPError)
              if the HuggingFace API returned an error
            - [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError)
              if some parameter value is invalid
            - [`~utils.RepositoryNotFoundError`]
              If the repository to download from cannot be found. This may be because it doesn\'t exist,
              or because it is set to `private` and you do not have access.

        </Tip>
        '''
    def add_space_secret(self, repo_id: str, key: str, value: str, *, description: str | None = None, token: str | None = None) -> None:
        '''Adds or updates a secret in a Space.

        Secrets allow to set secret keys or tokens to a Space without hardcoding them.
        For more details, see https://huggingface.co/docs/hub/spaces-overview#managing-secrets.

        Args:
            repo_id (`str`):
                ID of the repo to update. Example: `"bigcode/in-the-stack"`.
            key (`str`):
                Secret key. Example: `"GITHUB_API_KEY"`
            value (`str`):
                Secret value. Example: `"your_github_api_key"`.
            description (`str`, *optional*):
                Secret description. Example: `"Github API key to access the Github API"`.
            token (`str`, *optional*):
                Hugging Face token. Will default to the locally saved token if not provided.
        '''
    def delete_space_secret(self, repo_id: str, key: str, *, token: str | None = None) -> None:
        '''Deletes a secret from a Space.

        Secrets allow to set secret keys or tokens to a Space without hardcoding them.
        For more details, see https://huggingface.co/docs/hub/spaces-overview#managing-secrets.

        Args:
            repo_id (`str`):
                ID of the repo to update. Example: `"bigcode/in-the-stack"`.
            key (`str`):
                Secret key. Example: `"GITHUB_API_KEY"`.
            token (`str`, *optional*):
                Hugging Face token. Will default to the locally saved token if not provided.
        '''
    def get_space_variables(self, repo_id: str, *, token: str | None = None) -> Dict[str, SpaceVariable]:
        '''Gets all variables from a Space.

        Variables allow to set environment variables to a Space without hardcoding them.
        For more details, see https://huggingface.co/docs/hub/spaces-overview#managing-secrets-and-environment-variables

        Args:
            repo_id (`str`):
                ID of the repo to query. Example: `"bigcode/in-the-stack"`.
            token (`str`, *optional*):
                Hugging Face token. Will default to the locally saved token if not provided.
        '''
    def add_space_variable(self, repo_id: str, key: str, value: str, *, description: str | None = None, token: str | None = None) -> Dict[str, SpaceVariable]:
        '''Adds or updates a variable in a Space.

        Variables allow to set environment variables to a Space without hardcoding them.
        For more details, see https://huggingface.co/docs/hub/spaces-overview#managing-secrets-and-environment-variables

        Args:
            repo_id (`str`):
                ID of the repo to update. Example: `"bigcode/in-the-stack"`.
            key (`str`):
                Variable key. Example: `"MODEL_REPO_ID"`
            value (`str`):
                Variable value. Example: `"the_model_repo_id"`.
            description (`str`):
                Description of the variable. Example: `"Model Repo ID of the implemented model"`.
            token (`str`, *optional*):
                Hugging Face token. Will default to the locally saved token if not provided.
        '''
    def delete_space_variable(self, repo_id: str, key: str, *, token: str | None = None) -> Dict[str, SpaceVariable]:
        '''Deletes a variable from a Space.

        Variables allow to set environment variables to a Space without hardcoding them.
        For more details, see https://huggingface.co/docs/hub/spaces-overview#managing-secrets-and-environment-variables

        Args:
            repo_id (`str`):
                ID of the repo to update. Example: `"bigcode/in-the-stack"`.
            key (`str`):
                Variable key. Example: `"MODEL_REPO_ID"`
            token (`str`, *optional*):
                Hugging Face token. Will default to the locally saved token if not provided.
        '''
    def get_space_runtime(self, repo_id: str, *, token: str | None = None) -> SpaceRuntime:
        '''Gets runtime information about a Space.

        Args:
            repo_id (`str`):
                ID of the repo to update. Example: `"bigcode/in-the-stack"`.
            token (`str`, *optional*):
                Hugging Face token. Will default to the locally saved token if
                not provided.
        Returns:
            [`SpaceRuntime`]: Runtime information about a Space including Space stage and hardware.
        '''
    def request_space_hardware(self, repo_id: str, hardware: SpaceHardware, *, token: str | None = None, sleep_time: int | None = None) -> SpaceRuntime:
        '''Request new hardware for a Space.

        Args:
            repo_id (`str`):
                ID of the repo to update. Example: `"bigcode/in-the-stack"`.
            hardware (`str` or [`SpaceHardware`]):
                Hardware on which to run the Space. Example: `"t4-medium"`.
            token (`str`, *optional*):
                Hugging Face token. Will default to the locally saved token if not provided.
            sleep_time (`int`, *optional*):
                Number of seconds of inactivity to wait before a Space is put to sleep. Set to `-1` if you don\'t want
                your Space to sleep (default behavior for upgraded hardware). For free hardware, you can\'t configure
                the sleep time (value is fixed to 48 hours of inactivity).
                See https://huggingface.co/docs/hub/spaces-gpus#sleep-time for more details.
        Returns:
            [`SpaceRuntime`]: Runtime information about a Space including Space stage and hardware.

        <Tip>

        It is also possible to request hardware directly when creating the Space repo! See [`create_repo`] for details.

        </Tip>
        '''
    def set_space_sleep_time(self, repo_id: str, sleep_time: int, *, token: str | None = None) -> SpaceRuntime:
        '''Set a custom sleep time for a Space running on upgraded hardware..

        Your Space will go to sleep after X seconds of inactivity. You are not billed when your Space is in "sleep"
        mode. If a new visitor lands on your Space, it will "wake it up". Only upgraded hardware can have a
        configurable sleep time. To know more about the sleep stage, please refer to
        https://huggingface.co/docs/hub/spaces-gpus#sleep-time.

        Args:
            repo_id (`str`):
                ID of the repo to update. Example: `"bigcode/in-the-stack"`.
            sleep_time (`int`, *optional*):
                Number of seconds of inactivity to wait before a Space is put to sleep. Set to `-1` if you don\'t want
                your Space to pause (default behavior for upgraded hardware). For free hardware, you can\'t configure
                the sleep time (value is fixed to 48 hours of inactivity).
                See https://huggingface.co/docs/hub/spaces-gpus#sleep-time for more details.
            token (`str`, *optional*):
                Hugging Face token. Will default to the locally saved token if not provided.
        Returns:
            [`SpaceRuntime`]: Runtime information about a Space including Space stage and hardware.

        <Tip>

        It is also possible to set a custom sleep time when requesting hardware with [`request_space_hardware`].

        </Tip>
        '''
    def pause_space(self, repo_id: str, *, token: str | None = None) -> SpaceRuntime:
        '''Pause your Space.

        A paused Space stops executing until manually restarted by its owner. This is different from the sleeping
        state in which free Spaces go after 48h of inactivity. Paused time is not billed to your account, no matter the
        hardware you\'ve selected. To restart your Space, use [`restart_space`] and go to your Space settings page.

        For more details, please visit [the docs](https://huggingface.co/docs/hub/spaces-gpus#pause).

        Args:
            repo_id (`str`):
                ID of the Space to pause. Example: `"Salesforce/BLIP2"`.
            token (`str`, *optional*):
                Hugging Face token. Will default to the locally saved token if not provided.

        Returns:
            [`SpaceRuntime`]: Runtime information about your Space including `stage=PAUSED` and requested hardware.

        Raises:
            [`~utils.RepositoryNotFoundError`]:
                If your Space is not found (error 404). Most probably wrong repo_id or your space is private but you
                are not authenticated.
            [`~utils.HfHubHTTPError`]:
                403 Forbidden: only the owner of a Space can pause it. If you want to manage a Space that you don\'t
                own, either ask the owner by opening a Discussion or duplicate the Space.
            [`~utils.BadRequestError`]:
                If your Space is a static Space. Static Spaces are always running and never billed. If you want to hide
                a static Space, you can set it to private.
        '''
    def restart_space(self, repo_id: str, *, token: str | None = None, factory_reboot: bool = False) -> SpaceRuntime:
        '''Restart your Space.

        This is the only way to programmatically restart a Space if you\'ve put it on Pause (see [`pause_space`]). You
        must be the owner of the Space to restart it. If you are using an upgraded hardware, your account will be
        billed as soon as the Space is restarted. You can trigger a restart no matter the current state of a Space.

        For more details, please visit [the docs](https://huggingface.co/docs/hub/spaces-gpus#pause).

        Args:
            repo_id (`str`):
                ID of the Space to restart. Example: `"Salesforce/BLIP2"`.
            token (`str`, *optional*):
                Hugging Face token. Will default to the locally saved token if not provided.
            factory_reboot (`bool`, *optional*):
                If `True`, the Space will be rebuilt from scratch without caching any requirements.

        Returns:
            [`SpaceRuntime`]: Runtime information about your Space.

        Raises:
            [`~utils.RepositoryNotFoundError`]:
                If your Space is not found (error 404). Most probably wrong repo_id or your space is private but you
                are not authenticated.
            [`~utils.HfHubHTTPError`]:
                403 Forbidden: only the owner of a Space can restart it. If you want to restart a Space that you don\'t
                own, either ask the owner by opening a Discussion or duplicate the Space.
            [`~utils.BadRequestError`]:
                If your Space is a static Space. Static Spaces are always running and never billed. If you want to hide
                a static Space, you can set it to private.
        '''
    def duplicate_space(self, from_id: str, to_id: str | None = None, *, private: bool | None = None, token: str | None = None, exist_ok: bool = False, hardware: SpaceHardware | None = None, storage: SpaceStorage | None = None, sleep_time: int | None = None, secrets: List[Dict[str, str]] | None = None, variables: List[Dict[str, str]] | None = None) -> RepoUrl:
        '''Duplicate a Space.

        Programmatically duplicate a Space. The new Space will be created in your account and will be in the same state
        as the original Space (running or paused). You can duplicate a Space no matter the current state of a Space.

        Args:
            from_id (`str`):
                ID of the Space to duplicate. Example: `"pharma/CLIP-Interrogator"`.
            to_id (`str`, *optional*):
                ID of the new Space. Example: `"dog/CLIP-Interrogator"`. If not provided, the new Space will have the same
                name as the original Space, but in your account.
            private (`bool`, *optional*):
                Whether the new Space should be private or not. Defaults to the same privacy as the original Space.
            token (`str`, *optional*):
                Hugging Face token. Will default to the locally saved token if not provided.
            exist_ok (`bool`, *optional*, defaults to `False`):
                If `True`, do not raise an error if repo already exists.
            hardware (`SpaceHardware` or `str`, *optional*):
                Choice of Hardware. Example: `"t4-medium"`. See [`SpaceHardware`] for a complete list.
            storage (`SpaceStorage` or `str`, *optional*):
                Choice of persistent storage tier. Example: `"small"`. See [`SpaceStorage`] for a complete list.
            sleep_time (`int`, *optional*):
                Number of seconds of inactivity to wait before a Space is put to sleep. Set to `-1` if you don\'t want
                your Space to sleep (default behavior for upgraded hardware). For free hardware, you can\'t configure
                the sleep time (value is fixed to 48 hours of inactivity).
                See https://huggingface.co/docs/hub/spaces-gpus#sleep-time for more details.
            secrets (`List[Dict[str, str]]`, *optional*):
                A list of secret keys to set in your Space. Each item is in the form `{"key": ..., "value": ..., "description": ...}` where description is optional.
                For more details, see https://huggingface.co/docs/hub/spaces-overview#managing-secrets.
            variables (`List[Dict[str, str]]`, *optional*):
                A list of public environment variables to set in your Space. Each item is in the form `{"key": ..., "value": ..., "description": ...}` where description is optional.
                For more details, see https://huggingface.co/docs/hub/spaces-overview#managing-secrets-and-environment-variables.

        Returns:
            [`RepoUrl`]: URL to the newly created repo. Value is a subclass of `str` containing
            attributes like `endpoint`, `repo_type` and `repo_id`.

        Raises:
            - [`HTTPError`](https://requests.readthedocs.io/en/latest/api/#requests.HTTPError)
              if the HuggingFace API returned an error
            - [`~utils.RepositoryNotFoundError`]
              If one of `from_id` or `to_id` cannot be found. This may be because it doesn\'t exist,
              or because it is set to `private` and you do not have access.

        Example:
        ```python
        >>> from huggingface_hub import duplicate_space

        # Duplicate a Space to your account
        >>> duplicate_space("multimodalart/dreambooth-training")
        RepoUrl(\'https://huggingface.co/spaces/nateraw/dreambooth-training\',...)

        # Can set custom destination id and visibility flag.
        >>> duplicate_space("multimodalart/dreambooth-training", to_id="my-dreambooth", private=True)
        RepoUrl(\'https://huggingface.co/spaces/nateraw/my-dreambooth\',...)
        ```
        '''
    def request_space_storage(self, repo_id: str, storage: SpaceStorage, *, token: str | None = None) -> SpaceRuntime:
        '''Request persistent storage for a Space.

        Args:
            repo_id (`str`):
                ID of the Space to update. Example: `"HuggingFaceH4/open_llm_leaderboard"`.
            storage (`str` or [`SpaceStorage`]):
               Storage tier. Either \'small\', \'medium\', or \'large\'.
            token (`str`, *optional*):
                Hugging Face token. Will default to the locally saved token if not provided.
        Returns:
            [`SpaceRuntime`]: Runtime information about a Space including Space stage and hardware.

        <Tip>

        It is not possible to decrease persistent storage after its granted. To do so, you must delete it
        via [`delete_space_storage`].

        </Tip>
        '''
    def delete_space_storage(self, repo_id: str, *, token: str | None = None) -> SpaceRuntime:
        '''Delete persistent storage for a Space.

        Args:
            repo_id (`str`):
                ID of the Space to update. Example: `"HuggingFaceH4/open_llm_leaderboard"`.
            token (`str`, *optional*):
                Hugging Face token. Will default to the locally saved token if not provided.
        Returns:
            [`SpaceRuntime`]: Runtime information about a Space including Space stage and hardware.
        Raises:
            [`BadRequestError`]
                If space has no persistent storage.

        '''
    def get_collection(self, collection_slug: str, *, token: str | None = None) -> Collection:
        '''Gets information about a Collection on the Hub.

        Args:
            collection_slug (`str`):
                Slug of the collection of the Hub. Example: `"TheBloke/recent-models-64f9a55bb3115b4f513ec026"`.
            token (`str`, *optional*):
                Hugging Face token. Will default to the locally saved token if not provided.

        Returns: [`Collection`]

        Example:

        ```py
        >>> from huggingface_hub import get_collection
        >>> collection = get_collection("TheBloke/recent-models-64f9a55bb3115b4f513ec026")
        >>> collection.title
        \'Recent models\'
        >>> len(collection.items)
        37
        >>> collection.items[0]
        CollectionItem: {
            {\'item_object_id\': \'6507f6d5423b46492ee1413e\',
            \'item_id\': \'TheBloke/TigerBot-70B-Chat-GPTQ\',
            \'author\': \'TheBloke\',
            \'item_type\': \'model\',
            \'lastModified\': \'2023-09-19T12:55:21.000Z\',
            (...)
        }}
        ```
        '''
    def create_collection(self, title: str, *, namespace: str | None = None, description: str | None = None, private: bool = False, exists_ok: bool = False, token: str | None = None) -> Collection:
        '''Create a new Collection on the Hub.

        Args:
            title (`str`):
                Title of the collection to create. Example: `"Recent models"`.
            namespace (`str`, *optional*):
                Namespace of the collection to create (username or org). Will default to the owner name.
            description (`str`, *optional*):
                Description of the collection to create.
            private (`bool`, *optional*):
                Whether the collection should be private or not. Defaults to `False` (i.e. public collection).
            exists_ok (`bool`, *optional*):
                If `True`, do not raise an error if collection already exists.
            token (`str`, *optional*):
                Hugging Face token. Will default to the locally saved token if not provided.

        Returns: [`Collection`]

        Example:

        ```py
        >>> from huggingface_hub import create_collection
        >>> collection = create_collection(
        ...     title="ICCV 2023",
        ...     description="Portfolio of models, papers and demos I presented at ICCV 2023",
        ... )
        >>> collection.slug
        "username/iccv-2023-64f9a55bb3115b4f513ec026"
        ```
        '''
    def update_collection_metadata(self, collection_slug: str, *, title: str | None = None, description: str | None = None, position: int | None = None, private: bool | None = None, theme: str | None = None, token: str | None = None) -> Collection:
        '''Update metadata of a collection on the Hub.

        All arguments are optional. Only provided metadata will be updated.

        Args:
            collection_slug (`str`):
                Slug of the collection to update. Example: `"TheBloke/recent-models-64f9a55bb3115b4f513ec026"`.
            title (`str`):
                Title of the collection to update.
            description (`str`, *optional*):
                Description of the collection to update.
            position (`int`, *optional*):
                New position of the collection in the list of collections of the user.
            private (`bool`, *optional*):
                Whether the collection should be private or not.
            theme (`str`, *optional*):
                Theme of the collection on the Hub.
            token (`str`, *optional*):
                Hugging Face token. Will default to the locally saved token if not provided.

        Returns: [`Collection`]

        Example:

        ```py
        >>> from huggingface_hub import update_collection_metadata
        >>> collection = update_collection_metadata(
        ...     collection_slug="username/iccv-2023-64f9a55bb3115b4f513ec026",
        ...     title="ICCV Oct. 2023"
        ...     description="Portfolio of models, datasets, papers and demos I presented at ICCV Oct. 2023",
        ...     private=False,
        ...     theme="pink",
        ... )
        >>> collection.slug
        "username/iccv-oct-2023-64f9a55bb3115b4f513ec026"
        # ^collection slug got updated but not the trailing ID
        ```
        '''
    def delete_collection(self, collection_slug: str, *, missing_ok: bool = False, token: str | None = None) -> None:
        '''Delete a collection on the Hub.

        Args:
            collection_slug (`str`):
                Slug of the collection to delete. Example: `"TheBloke/recent-models-64f9a55bb3115b4f513ec026"`.
            missing_ok (`bool`, *optional*):
                If `True`, do not raise an error if collection doesn\'t exists.
            token (`str`, *optional*):
                Hugging Face token. Will default to the locally saved token if not provided.

        Example:

        ```py
        >>> from huggingface_hub import delete_collection
        >>> collection = delete_collection("username/useless-collection-64f9a55bb3115b4f513ec026", missing_ok=True)
        ```

        <Tip warning={true}>

        This is a non-revertible action. A deleted collection cannot be restored.

        </Tip>
        '''
    def add_collection_item(self, collection_slug: str, item_id: str, item_type: CollectionItemType_T, *, note: str | None = None, exists_ok: bool = False, token: str | None = None) -> Collection:
        '''Add an item to a collection on the Hub.

        Args:
            collection_slug (`str`):
                Slug of the collection to update. Example: `"TheBloke/recent-models-64f9a55bb3115b4f513ec026"`.
            item_id (`str`):
                ID of the item to add to the collection. It can be the ID of a repo on the Hub (e.g. `"facebook/bart-large-mnli"`)
                or a paper id (e.g. `"2307.09288"`).
            item_type (`str`):
                Type of the item to add. Can be one of `"model"`, `"dataset"`, `"space"` or `"paper"`.
            note (`str`, *optional*):
                A note to attach to the item in the collection. The maximum size for a note is 500 characters.
            exists_ok (`bool`, *optional*):
                If `True`, do not raise an error if item already exists.
            token (`str`, *optional*):
                Hugging Face token. Will default to the locally saved token if not provided.

        Returns: [`Collection`]

        Example:

        ```py
        >>> from huggingface_hub import add_collection_item
        >>> collection = add_collection_item(
        ...     collection_slug="davanstrien/climate-64f99dc2a5067f6b65531bab",
        ...     item_id="pierre-loic/climate-news-articles",
        ...     item_type="dataset"
        ... )
        >>> collection.items[-1].item_id
        "pierre-loic/climate-news-articles"
        # ^item got added to the collection on last position

        # Add item with a note
        >>> add_collection_item(
        ...     collection_slug="davanstrien/climate-64f99dc2a5067f6b65531bab",
        ...     item_id="datasets/climate_fever",
        ...     item_type="dataset"
        ...     note="This dataset adopts the FEVER methodology that consists of 1,535 real-world claims regarding climate-change collected on the internet."
        ... )
        (...)
        ```
        '''
    def update_collection_item(self, collection_slug: str, item_object_id: str, *, note: str | None = None, position: int | None = None, token: str | None = None) -> None:
        '''Update an item in a collection.

        Args:
            collection_slug (`str`):
                Slug of the collection to update. Example: `"TheBloke/recent-models-64f9a55bb3115b4f513ec026"`.
            item_object_id (`str`):
                ID of the item in the collection. This is not the id of the item on the Hub (repo_id or paper id).
                It must be retrieved from a [`CollectionItem`] object. Example: `collection.items[0]._id`.
            note (`str`, *optional*):
                A note to attach to the item in the collection. The maximum size for a note is 500 characters.
            position (`int`, *optional*):
                New position of the item in the collection.
            token (`str`, *optional*):
                Hugging Face token. Will default to the locally saved token if not provided.

        Example:

        ```py
        >>> from huggingface_hub import get_collection, update_collection_item

        # Get collection first
        >>> collection = get_collection("TheBloke/recent-models-64f9a55bb3115b4f513ec026")

        # Update item based on its ID (add note + update position)
        >>> update_collection_item(
        ...     collection_slug="TheBloke/recent-models-64f9a55bb3115b4f513ec026",
        ...     item_object_id=collection.items[-1].item_object_id,
        ...     note="Newly updated model!"
        ...     position=0,
        ... )
        ```
        '''
    def delete_collection_item(self, collection_slug: str, item_object_id: str, *, missing_ok: bool = False, token: str | None = None) -> None:
        '''Delete an item from a collection.

        Args:
            collection_slug (`str`):
                Slug of the collection to update. Example: `"TheBloke/recent-models-64f9a55bb3115b4f513ec026"`.
            item_object_id (`str`):
                ID of the item in the collection. This is not the id of the item on the Hub (repo_id or paper id).
                It must be retrieved from a [`CollectionItem`] object. Example: `collection.items[0]._id`.
            missing_ok (`bool`, *optional*):
                If `True`, do not raise an error if item doesn\'t exists.
            token (`str`, *optional*):
                Hugging Face token. Will default to the locally saved token if not provided.

        Example:

        ```py
        >>> from huggingface_hub import get_collection, delete_collection_item

        # Get collection first
        >>> collection = get_collection("TheBloke/recent-models-64f9a55bb3115b4f513ec026")

        # Delete item based on its ID
        >>> delete_collection_item(
        ...     collection_slug="TheBloke/recent-models-64f9a55bb3115b4f513ec026",
        ...     item_object_id=collection.items[-1].item_object_id,
        ... )
        ```
        '''

api: Incomplete
whoami: Incomplete
get_token_permission: Incomplete
list_models: Incomplete
model_info: Incomplete
list_datasets: Incomplete
dataset_info: Incomplete
list_spaces: Incomplete
space_info: Incomplete
repo_exists: Incomplete
file_exists: Incomplete
repo_info: Incomplete
list_repo_files: Incomplete
list_repo_refs: Incomplete
list_repo_commits: Incomplete
list_files_info: Incomplete
list_metrics: Incomplete
get_model_tags: Incomplete
get_dataset_tags: Incomplete
create_commit: Incomplete
create_repo: Incomplete
delete_repo: Incomplete
update_repo_visibility: Incomplete
super_squash_history: Incomplete
move_repo: Incomplete
upload_file: Incomplete
upload_folder: Incomplete
delete_file: Incomplete
delete_folder: Incomplete
create_commits_on_pr: Incomplete
preupload_lfs_files: Incomplete
create_branch: Incomplete
delete_branch: Incomplete
create_tag: Incomplete
delete_tag: Incomplete
get_full_repo_name: Incomplete
run_as_future: Incomplete
list_liked_repos: Incomplete
list_repo_likers: Incomplete
like: Incomplete
unlike: Incomplete
get_discussion_details: Incomplete
get_repo_discussions: Incomplete
create_discussion: Incomplete
create_pull_request: Incomplete
change_discussion_status: Incomplete
comment_discussion: Incomplete
edit_discussion_comment: Incomplete
rename_discussion: Incomplete
merge_pull_request: Incomplete
add_space_secret: Incomplete
delete_space_secret: Incomplete
get_space_variables: Incomplete
add_space_variable: Incomplete
delete_space_variable: Incomplete
get_space_runtime: Incomplete
request_space_hardware: Incomplete
set_space_sleep_time: Incomplete
pause_space: Incomplete
restart_space: Incomplete
duplicate_space: Incomplete
request_space_storage: Incomplete
delete_space_storage: Incomplete
get_collection: Incomplete
create_collection: Incomplete
update_collection_metadata: Incomplete
delete_collection: Incomplete
add_collection_item: Incomplete
update_collection_item: Incomplete
delete_collection_item: Incomplete
