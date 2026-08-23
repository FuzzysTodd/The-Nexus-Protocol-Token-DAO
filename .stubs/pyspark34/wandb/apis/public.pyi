import io
import wandb
import wandb.apis.reports
import wandb.apis.reports.util
from _typeshed import Incomplete
from typing import Any, Dict, List, Mapping, MutableMapping, Sequence
from wandb import env as env, util as util
from wandb.apis.normalize import normalize_exceptions as normalize_exceptions
from wandb.errors import CommError as CommError
from wandb.sdk.artifacts.artifact_state import ArtifactState as ArtifactState
from wandb.sdk.data_types._dtypes import InvalidType as InvalidType, Type as Type, TypeRegistry as TypeRegistry
from wandb.sdk.launch.errors import LaunchError as LaunchError
from wandb.sdk.launch.utils import LAUNCH_DEFAULT_PROJECT as LAUNCH_DEFAULT_PROJECT, apply_patch as apply_patch, convert_jupyter_notebook_to_script as convert_jupyter_notebook_to_script
from wandb.sdk.lib import ipython as ipython, json_util as json_util, retry as retry, runid as runid
from wandb.sdk.lib.gql_request import GraphQLSession as GraphQLSession
from wandb.sdk.lib.paths import LogicalPath as LogicalPath
from wandb_gql import Client

logger: Incomplete
RETRY_TIMEDELTA: Incomplete
WANDB_INTERNAL_KEYS: Incomplete
PROJECT_FRAGMENT: str
RUN_FRAGMENT: str
FILE_FRAGMENT: str
ARTIFACTS_TYPES_FRAGMENT: str
ARTIFACT_FILES_FRAGMENT: str
SWEEP_FRAGMENT: str

class RetryingClient:
    INFO_QUERY: Incomplete
    def __init__(self, client: Client) -> None: ...
    @property
    def app_url(self): ...
    def execute(self, *args, **kwargs): ...
    @property
    def server_info(self): ...
    def version_supported(self, min_version): ...

class Api:
    """Used for querying the wandb server.

    Examples:
        Most common way to initialize
        >>> wandb.Api()

    Arguments:
        overrides: (dict) You can set `base_url` if you are using a wandb server
            other than https://api.wandb.ai.
            You can also set defaults for `entity`, `project`, and `run`.
    """
    VIEWER_QUERY: Incomplete
    USERS_QUERY: Incomplete
    CREATE_PROJECT: Incomplete
    settings: Incomplete
    def __init__(self, overrides: Incomplete | None = None, timeout: int | None = None, api_key: str | None = None) -> None: ...
    def create_project(self, name: str, entity: str): ...
    def create_run(self, **kwargs):
        """Create a new run."""
    def create_report(self, project: str, entity: str = '', title: str | None = 'Untitled Report', description: str | None = '', width: str | None = 'readable', blocks: wandb.apis.reports.util.Block | None = None) -> wandb.apis.reports.Report: ...
    def create_run_queue(self, name: str, type: RunQueueResourceType, access: RunQueueAccessType, entity: str | None = None, config: dict | None = None) -> None:
        '''Create a new run queue (launch).

        Arguments:
            name: (str) Name of the queue to create
            type: (str) Type of resource to be used for the queue. One of "local-container", "local-process", "kubernetes", "sagemaker", or "gcp-vertex".
            access: (str) Access level for the queue. Either "project" or "user".
            entity: (str) Optional name of the entity to create the queue. If None, will use the configured or default entity.
            config: (dict) Optional default resource configuration to be used for the queue.

        Returns:
            The newly created `RunQueue`

        Raises:
            ValueError if any of the parameters are invalid
            wandb.Error on wandb API errors
        '''
    def load_report(self, path: str) -> wandb.apis.reports.Report:
        """Get report at a given path.

        Arguments:
            path: (str) Path to the target report in the form `entity/project/reports/reportId`.
                You can get this by copy-pasting the URL after your wandb url.  For example:
                `megatruong/report-editing/reports/My-fabulous-report-title--VmlldzoxOTc1Njk0`

        Returns:
            A `BetaReport` object which represents the report at `path`

        Raises:
            wandb.Error if path is invalid
        """
    def create_user(self, email, admin: bool = False):
        """Create a new user.

        Arguments:
            email: (str) The name of the team
            admin: (bool) Whether this user should be a global instance admin

        Returns:
            A `User` object
        """
    def sync_tensorboard(self, root_dir, run_id: Incomplete | None = None, project: Incomplete | None = None, entity: Incomplete | None = None):
        """Sync a local directory containing tfevent files to wandb."""
    @property
    def client(self): ...
    @property
    def user_agent(self): ...
    @property
    def api_key(self): ...
    @property
    def default_entity(self): ...
    @property
    def viewer(self): ...
    def flush(self) -> None:
        """Flush the local cache.

        The api object keeps a local cache of runs, so if the state of the run may
        change while executing your script you must clear the local cache with
        `api.flush()` to get the latest values associated with the run.
        """
    def from_path(self, path):
        '''Return a run, sweep, project or report from a path.

        Examples:
            ```
            project = api.from_path("my_project")
            team_project = api.from_path("my_team/my_project")
            run = api.from_path("my_team/my_project/runs/id")
            sweep = api.from_path("my_team/my_project/sweeps/id")
            report = api.from_path("my_team/my_project/reports/My-Report-Vm11dsdf")
            ```

        Arguments:
            path: (str) The path to the project, run, sweep or report

        Returns:
            A `Project`, `Run`, `Sweep`, or `BetaReport` instance.

        Raises:
            wandb.Error if path is invalid or the object doesn\'t exist
        '''
    def projects(self, entity: Incomplete | None = None, per_page: int = 200):
        """Get projects for a given entity.

        Arguments:
            entity: (str) Name of the entity requested.  If None, will fall back to
                default entity passed to `Api`.  If no default entity, will raise a `ValueError`.
            per_page: (int) Sets the page size for query pagination.  None will use the default size.
                Usually there is no reason to change this.

        Returns:
            A `Projects` object which is an iterable collection of `Project` objects.

        """
    def project(self, name, entity: Incomplete | None = None): ...
    def reports(self, path: str = '', name: Incomplete | None = None, per_page: int = 50):
        '''Get reports for a given project path.

        WARNING: This api is in beta and will likely change in a future release

        Arguments:
            path: (str) path to project the report resides in, should be in the form: "entity/project"
            name: (str) optional name of the report requested.
            per_page: (int) Sets the page size for query pagination.  None will use the default size.
                Usually there is no reason to change this.

        Returns:
            A `Reports` object which is an iterable collection of `BetaReport` objects.
        '''
    def create_team(self, team, admin_username: Incomplete | None = None):
        """Create a new team.

        Arguments:
            team: (str) The name of the team
            admin_username: (str) optional username of the admin user of the team, defaults to the current user.

        Returns:
            A `Team` object
        """
    def team(self, team): ...
    def user(self, username_or_email):
        """Return a user from a username or email address.

        Note: This function only works for Local Admins, if you are trying to get your own user object, please use `api.viewer`.

        Arguments:
            username_or_email: (str) The username or email address of the user

        Returns:
            A `User` object or None if a user couldn't be found
        """
    def users(self, username_or_email):
        """Return all users from a partial username or email address query.

        Note: This function only works for Local Admins, if you are trying to get your own user object, please use `api.viewer`.

        Arguments:
            username_or_email: (str) The prefix or suffix of the user you want to find

        Returns:
            An array of `User` objects
        """
    def runs(self, path: str | None = None, filters: Dict[str, Any] | None = None, order: str = '-created_at', per_page: int = 50, include_sweeps: bool = True):
        '''Return a set of runs from a project that match the filters provided.

        You can filter by `config.*`, `summary_metrics.*`, `tags`, `state`, `entity`, `createdAt`, etc.

        Examples:
            Find runs in my_project where config.experiment_name has been set to "foo"
            ```
            api.runs(path="my_entity/my_project", filters={"config.experiment_name": "foo"})
            ```

            Find runs in my_project where config.experiment_name has been set to "foo" or "bar"
            ```
            api.runs(
                path="my_entity/my_project",
                filters={"$or": [{"config.experiment_name": "foo"}, {"config.experiment_name": "bar"}]}
            )
            ```

            Find runs in my_project where config.experiment_name matches a regex (anchors are not supported)
            ```
            api.runs(
                path="my_entity/my_project",
                filters={"config.experiment_name": {"$regex": "b.*"}}
            )
            ```

            Find runs in my_project where the run name matches a regex (anchors are not supported)
            ```
            api.runs(
                path="my_entity/my_project",
                filters={"display_name": {"$regex": "^foo.*"}}
            )
            ```

            Find runs in my_project sorted by ascending loss
            ```
            api.runs(path="my_entity/my_project", order="+summary_metrics.loss")
            ```

        Arguments:
            path: (str) path to project, should be in the form: "entity/project"
            filters: (dict) queries for specific runs using the MongoDB query language.
                You can filter by run properties such as config.key, summary_metrics.key, state, entity, createdAt, etc.
                For example: {"config.experiment_name": "foo"} would find runs with a config entry
                    of experiment name set to "foo"
                You can compose operations to make more complicated queries,
                    see Reference for the language is at  https://docs.mongodb.com/manual/reference/operator/query
            order: (str) Order can be `created_at`, `heartbeat_at`, `config.*.value`, or `summary_metrics.*`.
                If you prepend order with a + order is ascending.
                If you prepend order with a - order is descending (default).
                The default order is run.created_at from newest to oldest.

        Returns:
            A `Runs` object, which is an iterable collection of `Run` objects.
        '''
    def run(self, path: str = ''):
        """Return a single run by parsing path in the form entity/project/run_id.

        Arguments:
            path: (str) path to run in the form `entity/project/run_id`.
                If `api.entity` is set, this can be in the form `project/run_id`
                and if `api.project` is set this can just be the run_id.

        Returns:
            A `Run` object.
        """
    def queued_run(self, entity, project, queue_name, run_queue_item_id, container_job: bool = False, project_queue: Incomplete | None = None):
        """Return a single queued run based on the path.

        Parses paths of the form entity/project/queue_id/run_queue_item_id.
        """
    def run_queue(self, entity, name):
        """Return the named `RunQueue` for entity.

        To create a new `RunQueue`, use `wandb.Api().create_run_queue(...)`.
        """
    def sweep(self, path: str = ''):
        """Return a sweep by parsing path in the form `entity/project/sweep_id`.

        Arguments:
            path: (str, optional) path to sweep in the form entity/project/sweep_id.  If `api.entity`
                is set, this can be in the form project/sweep_id and if `api.project` is set
                this can just be the sweep_id.

        Returns:
            A `Sweep` object.
        """
    def artifact_types(self, project: Incomplete | None = None): ...
    def artifact_type(self, type_name, project: Incomplete | None = None): ...
    def artifact_versions(self, type_name, name, per_page: int = 50): ...
    def artifact(self, name, type: Incomplete | None = None):
        """Return a single artifact by parsing path in the form `entity/project/name`.

        Arguments:
            name: (str) An artifact name. May be prefixed with entity/project. Valid names
                can be in the following forms:
                    name:version
                    name:alias
            type: (str, optional) The type of artifact to fetch.

        Returns:
            A `Artifact` object.
        """
    def job(self, name, path: Incomplete | None = None): ...
    def list_jobs(self, entity, project): ...

class Attrs:
    def __init__(self, attrs: MutableMapping[str, Any]) -> None: ...
    def snake_to_camel(self, string): ...
    def display(self, height: int = 420, hidden: bool = False) -> bool:
        """Display this object in jupyter."""
    def to_html(self, *args, **kwargs) -> None: ...
    def __getattr__(self, name): ...

class Paginator:
    QUERY: Incomplete
    client: Incomplete
    variables: Incomplete
    per_page: Incomplete
    objects: Incomplete
    index: int
    last_response: Incomplete
    def __init__(self, client: Client, variables: MutableMapping[str, Any], per_page: int | None = None) -> None: ...
    def __iter__(self): ...
    def __len__(self) -> int: ...
    @property
    def length(self) -> None: ...
    @property
    def more(self) -> None: ...
    @property
    def cursor(self) -> None: ...
    def convert_objects(self) -> None: ...
    def update_variables(self) -> None: ...
    def __getitem__(self, index): ...
    def __next__(self): ...
    next = __next__

class User(Attrs):
    CREATE_USER_MUTATION: Incomplete
    DELETE_API_KEY_MUTATION: Incomplete
    GENERATE_API_KEY_MUTATION: Incomplete
    def __init__(self, client, attrs) -> None: ...
    @property
    def user_api(self):
        """An instance of the api using credentials from the user."""
    @classmethod
    def create(cls, api, email, admin: bool = False):
        """Create a new user.

        Arguments:
            api: (`Api`) The api instance to use
            email: (str) The name of the team
            admin: (bool) Whether this user should be a global instance admin

        Returns:
            A `User` object
        """
    @property
    def api_keys(self): ...
    @property
    def teams(self): ...
    def delete_api_key(self, api_key):
        """Delete a user's api key.

        Returns:
            Boolean indicating success

        Raises:
            ValueError if the api_key couldn't be found
        """
    def generate_api_key(self, description: Incomplete | None = None):
        """Generate a new api key.

        Returns:
            The new api key, or None on failure
        """

class Member(Attrs):
    DELETE_MEMBER_MUTATION: Incomplete
    team: Incomplete
    def __init__(self, client, team, attrs) -> None: ...
    def delete(self):
        """Remove a member from a team.

        Returns:
            Boolean indicating success
        """

class Team(Attrs):
    CREATE_TEAM_MUTATION: Incomplete
    CREATE_INVITE_MUTATION: Incomplete
    TEAM_QUERY: Incomplete
    CREATE_SERVICE_ACCOUNT_MUTATION: Incomplete
    name: Incomplete
    def __init__(self, client, name, attrs: Incomplete | None = None) -> None: ...
    @classmethod
    def create(cls, api, team, admin_username: Incomplete | None = None):
        """Create a new team.

        Arguments:
            api: (`Api`) The api instance to use
            team: (str) The name of the team
            admin_username: (str) optional username of the admin user of the team, defaults to the current user.

        Returns:
            A `Team` object
        """
    def invite(self, username_or_email, admin: bool = False):
        """Invite a user to a team.

        Arguments:
            username_or_email: (str) The username or email address of the user you want to invite
            admin: (bool) Whether to make this user a team admin, defaults to False

        Returns:
            True on success, False if user was already invited or didn't exist
        """
    def create_service_account(self, description):
        """Create a service account for the team.

        Arguments:
            description: (str) A description for this service account

        Returns:
            The service account `Member` object, or None on failure
        """
    def load(self, force: bool = False): ...

class Projects(Paginator):
    """An iterable collection of `Project` objects."""
    QUERY: Incomplete
    client: Incomplete
    entity: Incomplete
    def __init__(self, client, entity, per_page: int = 50) -> None: ...
    @property
    def length(self) -> None: ...
    @property
    def more(self): ...
    @property
    def cursor(self): ...
    def convert_objects(self): ...

class Project(Attrs):
    """A project is a namespace for runs."""
    client: Incomplete
    name: Incomplete
    entity: Incomplete
    def __init__(self, client, entity, project, attrs) -> None: ...
    @property
    def path(self): ...
    @property
    def url(self): ...
    def to_html(self, height: int = 420, hidden: bool = False):
        """Generate HTML containing an iframe displaying this project."""
    def artifacts_types(self, per_page: int = 50): ...
    def sweeps(self): ...

class Runs(Paginator):
    """An iterable collection of runs associated with a project and optional filter.

    This is generally used indirectly via the `Api`.runs method.
    """
    QUERY: Incomplete
    entity: Incomplete
    project: Incomplete
    filters: Incomplete
    order: Incomplete
    def __init__(self, client: RetryingClient, entity: str, project: str, filters: Dict[str, Any] | None = None, order: str | None = None, per_page: int = 50, include_sweeps: bool = True) -> None: ...
    @property
    def length(self): ...
    @property
    def more(self): ...
    @property
    def cursor(self): ...
    def convert_objects(self): ...

class Run(Attrs):
    """A single run associated with an entity and project.

    Attributes:
        tags ([str]): a list of tags associated with the run
        url (str): the url of this run
        id (str): unique identifier for the run (defaults to eight characters)
        name (str): the name of the run
        state (str): one of: running, finished, crashed, killed, preempting, preempted
        config (dict): a dict of hyperparameters associated with the run
        created_at (str): ISO timestamp when the run was started
        system_metrics (dict): the latest system metrics recorded for the run
        summary (dict): A mutable dict-like property that holds the current summary.
                    Calling update will persist any changes.
        project (str): the project associated with the run
        entity (str): the name of the entity associated with the run
        user (str): the name of the user who created the run
        path (str): Unique identifier [entity]/[project]/[run_id]
        notes (str): Notes about the run
        read_only (boolean): Whether the run is editable
        history_keys (str): Keys of the history metrics that have been logged
            with `wandb.log({key: value})`
        metadata (str): Metadata about the run from wandb-metadata.json
    """
    client: Incomplete
    project: Incomplete
    sweep: Incomplete
    dir: Incomplete
    def __init__(self, client: RetryingClient, entity: str, project: str, run_id: str, attrs: Mapping | None = None, include_sweeps: bool = True) -> None:
        """Initialize a Run object.

        Run is always initialized by calling api.runs() where api is an instance of
        wandb.Api.
        """
    @property
    def state(self): ...
    @property
    def entity(self): ...
    @property
    def username(self): ...
    @property
    def storage_id(self): ...
    @property
    def id(self): ...
    @id.setter
    def id(self, new_id): ...
    @property
    def name(self): ...
    @name.setter
    def name(self, new_name): ...
    @classmethod
    def create(cls, api, run_id: Incomplete | None = None, project: Incomplete | None = None, entity: Incomplete | None = None):
        """Create a run for the given project."""
    user: Incomplete
    def load(self, force: bool = False): ...
    def wait_until_finished(self) -> None: ...
    def update(self) -> None:
        """Persist changes to the run object to the wandb backend."""
    def delete(self, delete_artifacts: bool = False) -> None:
        """Delete the given run from the wandb backend."""
    def save(self) -> None: ...
    @property
    def json_config(self): ...
    def files(self, names: Incomplete | None = None, per_page: int = 50):
        """Return a file path for each file named.

        Arguments:
            names (list): names of the requested files, if empty returns all files
            per_page (int): number of results per page.

        Returns:
            A `Files` object, which is an iterator over `File` objects.
        """
    def file(self, name):
        """Return the path of a file with a given name in the artifact.

        Arguments:
            name (str): name of requested file.

        Returns:
            A `File` matching the name argument.
        """
    def upload_file(self, path, root: str = '.'):
        '''Upload a file.

        Arguments:
            path (str): name of file to upload.
            root (str): the root path to save the file relative to.  i.e.
                If you want to have the file saved in the run as "my_dir/file.txt"
                and you\'re currently in "my_dir" you would set root to "../".

        Returns:
            A `File` matching the name argument.
        '''
    def history(self, samples: int = 500, keys: Incomplete | None = None, x_axis: str = '_step', pandas: bool = True, stream: str = 'default'):
        '''Return sampled history metrics for a run.

        This is simpler and faster if you are ok with the history records being sampled.

        Arguments:
            samples : (int, optional) The number of samples to return
            pandas : (bool, optional) Return a pandas dataframe
            keys : (list, optional) Only return metrics for specific keys
            x_axis : (str, optional) Use this metric as the xAxis defaults to _step
            stream : (str, optional) "default" for metrics, "system" for machine metrics

        Returns:
            pandas.DataFrame: If pandas=True returns a `pandas.DataFrame` of history
                metrics.
            list of dicts: If pandas=False returns a list of dicts of history metrics.
        '''
    def scan_history(self, keys: Incomplete | None = None, page_size: int = 1000, min_step: Incomplete | None = None, max_step: Incomplete | None = None):
        '''Returns an iterable collection of all history records for a run.

        Example:
            Export all the loss values for an example run

            ```python
            run = api.run("l2k2/examples-numpy-boston/i0wt6xua")
            history = run.scan_history(keys=["Loss"])
            losses = [row["Loss"] for row in history]
            ```


        Arguments:
            keys ([str], optional): only fetch these keys, and only fetch rows that have all of keys defined.
            page_size (int, optional): size of pages to fetch from the api

        Returns:
            An iterable collection over history records (dict).
        '''
    def logged_artifacts(self, per_page: int = 100): ...
    def used_artifacts(self, per_page: int = 100): ...
    def use_artifact(self, artifact, use_as: Incomplete | None = None):
        """Declare an artifact as an input to a run.

        Arguments:
            artifact (`Artifact`): An artifact returned from
                `wandb.Api().artifact(name)`
            use_as (string, optional): A string identifying
                how the artifact is used in the script. Used
                to easily differentiate artifacts used in a
                run, when using the beta wandb launch
                feature's artifact swapping functionality.

        Returns:
            A `Artifact` object.
        """
    def log_artifact(self, artifact, aliases: Incomplete | None = None):
        """Declare an artifact as output of a run.

        Arguments:
            artifact (`Artifact`): An artifact returned from
                `wandb.Api().artifact(name)`
            aliases (list, optional): Aliases to apply to this artifact
        Returns:
            A `Artifact` object.
        """
    @property
    def summary(self): ...
    @property
    def path(self): ...
    @property
    def url(self): ...
    @property
    def metadata(self): ...
    @property
    def lastHistoryStep(self): ...
    def to_html(self, height: int = 420, hidden: bool = False):
        """Generate HTML containing an iframe displaying this run."""

class QueuedRun:
    """A single queued run associated with an entity and project. Call `run = queued_run.wait_until_running()` or `run = queued_run.wait_until_finished()` to access the run."""
    client: Incomplete
    sweep: Incomplete
    container_job: Incomplete
    project_queue: Incomplete
    def __init__(self, client, entity, project, queue_name, run_queue_item_id, container_job: bool = False, project_queue=...) -> None: ...
    @property
    def queue_name(self): ...
    @property
    def id(self): ...
    @property
    def project(self): ...
    @property
    def entity(self): ...
    @property
    def state(self): ...
    def wait_until_finished(self): ...
    def delete(self, delete_artifacts: bool = False) -> None:
        """Delete the given queued run from the wandb backend."""
    def wait_until_running(self): ...

RunQueueResourceType: Incomplete
RunQueueAccessType: Incomplete

class RunQueue:
    def __init__(self, client: RetryingClient, name: str, entity: str, _access: RunQueueAccessType | None = None, _default_resource_config_id: int | None = None, _default_resource_config: dict | None = None) -> None: ...
    @property
    def name(self): ...
    @property
    def entity(self): ...
    @property
    def access(self) -> RunQueueAccessType: ...
    @property
    def type(self) -> RunQueueResourceType: ...
    @property
    def default_resource_config(self): ...
    @property
    def id(self) -> str: ...
    @property
    def items(self) -> List[QueuedRun]:
        """Up to the first 100 queued runs. Modifying this list will not modify the queue or any enqueued items!"""
    def delete(self) -> None:
        """Delete the run queue from the wandb backend."""
    @classmethod
    def create(cls, name: str, resource: RunQueueResourceType, access: RunQueueAccessType, entity: str | None = None, config: dict | None = None) -> RunQueue: ...

class Sweep(Attrs):
    """A set of runs associated with a sweep.

    Examples:
        Instantiate with:
        ```
        api = wandb.Api()
        sweep = api.sweep(path/to/sweep)
        ```

    Attributes:
        runs: (`Runs`) list of runs
        id: (str) sweep id
        project: (str) name of project
        config: (str) dictionary of sweep configuration
        state: (str) the state of the sweep
        expected_run_count: (int) number of expected runs for the sweep
    """
    QUERY: Incomplete
    LEGACY_QUERY: Incomplete
    client: Incomplete
    project: Incomplete
    id: Incomplete
    runs: Incomplete
    def __init__(self, client, entity, project, sweep_id, attrs: Incomplete | None = None) -> None: ...
    @property
    def entity(self): ...
    @property
    def username(self): ...
    @property
    def config(self): ...
    def load(self, force: bool = False): ...
    @property
    def order(self): ...
    def best_run(self, order: Incomplete | None = None):
        """Return the best run sorted by the metric defined in config or the order passed in."""
    @property
    def expected_run_count(self) -> int | None:
        """Return the number of expected runs in the sweep or None for infinite runs."""
    @property
    def path(self): ...
    @property
    def url(self): ...
    @property
    def name(self): ...
    @classmethod
    def get(cls, client, entity: Incomplete | None = None, project: Incomplete | None = None, sid: Incomplete | None = None, order: Incomplete | None = None, query: Incomplete | None = None, **kwargs):
        """Execute a query against the cloud backend."""
    def to_html(self, height: int = 420, hidden: bool = False):
        """Generate HTML containing an iframe displaying this sweep."""

class Files(Paginator):
    """An iterable collection of `File` objects."""
    QUERY: Incomplete
    run: Incomplete
    def __init__(self, client, run, names: Incomplete | None = None, per_page: int = 50, upload: bool = False) -> None: ...
    @property
    def length(self): ...
    @property
    def more(self): ...
    @property
    def cursor(self): ...
    def update_variables(self) -> None: ...
    def convert_objects(self): ...

class File(Attrs):
    """File is a class associated with a file saved by wandb.

    Attributes:
        name (string): filename
        url (string): path to file
        direct_url (string): path to file in the bucket
        md5 (string): md5 of file
        mimetype (string): mimetype of file
        updated_at (string): timestamp of last update
        size (int): size of file in bytes

    """
    client: Incomplete
    def __init__(self, client, attrs) -> None: ...
    @property
    def size(self): ...
    def download(self, root: str = '.', replace: bool = False, exist_ok: bool = False) -> io.TextIOWrapper:
        '''Downloads a file previously saved by a run from the wandb server.

        Arguments:
            replace (boolean): If `True`, download will overwrite a local file
                if it exists. Defaults to `False`.
            root (str): Local directory to save the file.  Defaults to ".".
            exist_ok (boolean): If `True`, will not raise ValueError if file already
                exists and will not re-download unless replace=True. Defaults to `False`.

        Raises:
            `ValueError` if file already exists, replace=False and exist_ok=False.
        '''
    def delete(self) -> None: ...

class Reports(Paginator):
    """Reports is an iterable collection of `BetaReport` objects."""
    QUERY: Incomplete
    project: Incomplete
    name: Incomplete
    def __init__(self, client, project, name: Incomplete | None = None, entity: Incomplete | None = None, per_page: int = 50) -> None: ...
    @property
    def length(self): ...
    @property
    def more(self): ...
    @property
    def cursor(self): ...
    def update_variables(self) -> None: ...
    def convert_objects(self): ...

class QueryGenerator:
    """QueryGenerator is a helper object to write filters for runs."""
    INDIVIDUAL_OP_TO_MONGO: Incomplete
    MONGO_TO_INDIVIDUAL_OP: Incomplete
    GROUP_OP_TO_MONGO: Incomplete
    MONGO_TO_GROUP_OP: Incomplete
    def __init__(self) -> None: ...
    @classmethod
    def format_order_key(cls, key: str): ...
    def key_to_server_path(self, key): ...
    def server_path_to_key(self, path): ...
    def keys_to_order(self, keys): ...
    def order_to_keys(self, order): ...
    def filter_to_mongo(self, filter): ...
    def mongo_to_filter(self, filter): ...

class PythonMongoishQueryGenerator:
    SPACER: str
    DECIMAL_SPACER: str
    FRONTEND_NAME_MAPPING: Incomplete
    FRONTEND_NAME_MAPPING_REVERSED: Incomplete
    AST_OPERATORS: Incomplete
    AST_FIELDS: Incomplete
    run_set: Incomplete
    panel_metrics_helper: Incomplete
    def __init__(self, run_set) -> None: ...
    def python_to_mongo(self, filterstr): ...
    def front_to_back(self, name): ...
    def back_to_front(self, name): ...
    def pc_front_to_back(self, name): ...
    def pc_back_to_front(self, name): ...

class PanelMetricsHelper:
    FRONTEND_NAME_MAPPING: Incomplete
    FRONTEND_NAME_MAPPING_REVERSED: Incomplete
    RUN_MAPPING: Incomplete
    RUN_MAPPING_REVERSED: Incomplete
    def front_to_back(self, name): ...
    def back_to_front(self, name): ...
    def special_front_to_back(self, name): ...
    def special_back_to_front(self, name): ...

class BetaReport(Attrs):
    """BetaReport is a class associated with reports created in wandb.

    WARNING: this API will likely change in a future release

    Attributes:
        name (string): report name
        description (string): report description;
        user (User): the user that created the report
        spec (dict): the spec off the report;
        updated_at (string): timestamp of last update
    """
    client: Incomplete
    project: Incomplete
    entity: Incomplete
    query_generator: Incomplete
    def __init__(self, client, attrs, entity: Incomplete | None = None, project: Incomplete | None = None) -> None: ...
    @property
    def sections(self): ...
    def runs(self, section, per_page: int = 50, only_selected: bool = True): ...
    @property
    def updated_at(self): ...
    @property
    def url(self): ...
    def to_html(self, height: int = 1024, hidden: bool = False):
        """Generate HTML containing an iframe displaying this report."""

class HistoryScan:
    QUERY: Incomplete
    client: Incomplete
    run: Incomplete
    page_size: Incomplete
    min_step: Incomplete
    max_step: Incomplete
    page_offset: Incomplete
    scan_offset: int
    rows: Incomplete
    def __init__(self, client, run, min_step, max_step, page_size: int = 1000) -> None: ...
    def __iter__(self): ...
    def __next__(self): ...
    next = __next__

class SampledHistoryScan:
    QUERY: Incomplete
    client: Incomplete
    run: Incomplete
    keys: Incomplete
    page_size: Incomplete
    min_step: Incomplete
    max_step: Incomplete
    page_offset: Incomplete
    scan_offset: int
    rows: Incomplete
    def __init__(self, client, run, keys, min_step, max_step, page_size: int = 1000) -> None: ...
    def __iter__(self): ...
    def __next__(self): ...
    next = __next__

class ProjectArtifactTypes(Paginator):
    QUERY: Incomplete
    entity: Incomplete
    project: Incomplete
    def __init__(self, client: Client, entity: str, project: str, name: str | None = None, per_page: int | None = 50) -> None: ...
    @property
    def length(self) -> None: ...
    @property
    def more(self): ...
    @property
    def cursor(self): ...
    def update_variables(self) -> None: ...
    def convert_objects(self): ...

def server_supports_artifact_collections_gql_edges(client: RetryingClient, warn: bool = False) -> bool: ...
def artifact_collection_edge_name(server_supports_artifact_collections: bool) -> str: ...
def artifact_collection_plural_edge_name(server_supports_artifact_collections: bool) -> str: ...

class ProjectArtifactCollections(Paginator):
    entity: Incomplete
    project: Incomplete
    type_name: Incomplete
    QUERY: Incomplete
    def __init__(self, client: Client, entity: str, project: str, type_name: str, per_page: int | None = 50) -> None: ...
    @property
    def length(self): ...
    @property
    def more(self): ...
    @property
    def cursor(self): ...
    def update_variables(self) -> None: ...
    def convert_objects(self): ...

class RunArtifacts(Paginator):
    run: Incomplete
    run_key: str
    QUERY: Incomplete
    def __init__(self, client: Client, run: Run, mode: str = 'logged', per_page: int | None = 50) -> None: ...
    @property
    def length(self): ...
    @property
    def more(self): ...
    @property
    def cursor(self): ...
    def convert_objects(self): ...

class ArtifactType:
    client: Incomplete
    entity: Incomplete
    project: Incomplete
    type: Incomplete
    def __init__(self, client: Client, entity: str, project: str, type_name: str, attrs: Mapping[str, Any] | None = None) -> None: ...
    def load(self): ...
    @property
    def id(self): ...
    @property
    def name(self): ...
    def collections(self, per_page: int = 50):
        """Artifact collections."""
    def collection(self, name): ...

class ArtifactCollection:
    client: Incomplete
    entity: Incomplete
    project: Incomplete
    name: Incomplete
    type: Incomplete
    def __init__(self, client: Client, entity: str, project: str, name: str, type: str, attrs: Mapping[str, Any] | None = None) -> None: ...
    @property
    def id(self): ...
    def versions(self, per_page: int = 50):
        """Artifact versions."""
    @property
    def aliases(self):
        """Artifact Collection Aliases."""
    def load(self): ...
    def is_sequence(self) -> bool:
        """Return True if this is a sequence."""
    def delete(self) -> None:
        """Delete the entire artifact collection."""

class ArtifactVersions(Paginator):
    """An iterable collection of artifact versions associated with a project and optional filter.

    This is generally used indirectly via the `Api`.artifact_versions method.
    """
    entity: Incomplete
    collection_name: Incomplete
    type: Incomplete
    project: Incomplete
    filters: Incomplete
    order: Incomplete
    QUERY: Incomplete
    def __init__(self, client: Client, entity: str, project: str, collection_name: str, type: str, filters: Mapping[str, Any] | None = None, order: str | None = None, per_page: int = 50) -> None: ...
    @property
    def length(self): ...
    @property
    def more(self): ...
    @property
    def cursor(self): ...
    def convert_objects(self): ...

class ArtifactFiles(Paginator):
    QUERY: Incomplete
    artifact: Incomplete
    def __init__(self, client: Client, artifact: wandb.Artifact, names: Sequence[str] | None = None, per_page: int = 50) -> None: ...
    @property
    def path(self): ...
    @property
    def length(self): ...
    @property
    def more(self): ...
    @property
    def cursor(self): ...
    def update_variables(self) -> None: ...
    def convert_objects(self): ...

class Job:
    def __init__(self, api: Api, name, path: str | None = None) -> None: ...
    @property
    def name(self): ...
    def set_entrypoint(self, entrypoint: List[str]): ...
    def call(self, config, project: Incomplete | None = None, entity: Incomplete | None = None, queue: Incomplete | None = None, resource: str = 'local-container', resource_args: Incomplete | None = None, project_queue: Incomplete | None = None): ...
