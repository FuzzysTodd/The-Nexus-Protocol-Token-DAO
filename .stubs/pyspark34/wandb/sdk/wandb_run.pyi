import wandb
from . import wandb_config as wandb_config, wandb_metric as wandb_metric, wandb_summary as wandb_summary
from .data_types._dtypes import TypeRegistry as TypeRegistry
from .interface.interface import FilesDict as FilesDict, GlobStr as GlobStr, InterfaceBase as InterfaceBase, PolicyName as PolicyName
from .interface.summary_record import SummaryRecord as SummaryRecord
from .lib import config_util as config_util, deprecate as deprecate, filenames as filenames, filesystem as filesystem, ipython as ipython, module as module, proto_util as proto_util, redirect as redirect, telemetry as telemetry
from .lib.exit_hooks import ExitHooks as ExitHooks
from .lib.gitlib import GitRepo as GitRepo
from .lib.mailbox import MailboxError as MailboxError, MailboxHandle as MailboxHandle, MailboxProbe as MailboxProbe, MailboxProgress as MailboxProgress
from .lib.printer import PrinterJupyter as PrinterJupyter, PrinterTerm as PrinterTerm, get_printer as get_printer
from .lib.proto_util import message_to_dict as message_to_dict
from .lib.reporting import Reporter as Reporter
from .lib.wburls import wburls as wburls
from .wandb_alerts import AlertLevel as AlertLevel
from .wandb_settings import Settings as Settings
from _typeshed import Incomplete
from dataclasses import dataclass
from datetime import datetime, timedelta
from enum import IntEnum
from types import TracebackType
from typing import Any, Callable, Dict, List, NamedTuple, Sequence, TextIO, Tuple, Type, TypedDict
from wandb import errors as errors, trigger as trigger
from wandb.apis import internal as internal, public as public
from wandb.apis.internal import Api as Api
from wandb.proto.wandb_internal_pb2 import CheckVersionResponse as CheckVersionResponse, GetSummaryResponse as GetSummaryResponse, InternalMessagesResponse as InternalMessagesResponse, JobInfoResponse as JobInfoResponse, MetricRecord as MetricRecord, PollExitResponse as PollExitResponse, Result as Result, RunRecord as RunRecord, SampledHistoryResponse as SampledHistoryResponse, ServerInfoResponse as ServerInfoResponse
from wandb.sdk.artifacts.artifact import Artifact as Artifact
from wandb.sdk.internal import job_builder as job_builder
from wandb.sdk.lib.import_hooks import register_post_import_hook as register_post_import_hook, unregister_post_import_hook as unregister_post_import_hook
from wandb.sdk.lib.paths import FilePathStr as FilePathStr, LogicalPath as LogicalPath, StrPath as StrPath
from wandb.util import add_import_hook as add_import_hook, parse_artifact_string as parse_artifact_string
from wandb.viz import CustomChart as CustomChart, Visualize as Visualize, custom_chart as custom_chart

class GitSourceDict(TypedDict):
    remote: str
    commit: str
    entrypoint: List[str]
    args: Sequence[str]

class ArtifactSourceDict(TypedDict):
    artifact: str
    entrypoint: List[str]
    args: Sequence[str]

class ImageSourceDict(TypedDict):
    image: str
    args: Sequence[str]

class JobSourceDict(TypedDict, total=False):
    source_type: str
    source: GitSourceDict | ArtifactSourceDict | ImageSourceDict
    input_types: Dict[str, Any]
    output_types: Dict[str, Any]
    runtime: str | None

logger: Incomplete
EXIT_TIMEOUT: int
RE_LABEL: Incomplete

class TeardownStage(IntEnum):
    EARLY: int
    LATE: int

class TeardownHook(NamedTuple):
    call: Callable[[], None]
    stage: TeardownStage

class RunStatusChecker:
    """Periodically polls the background process for relevant updates.

    - check if the user has requested a stop.
    - check the network status.
    - check the run sync status.
    """
    def __init__(self, interface: InterfaceBase, stop_polling_interval: int = 15, retry_polling_interval: int = 5) -> None: ...
    def start(self) -> None: ...
    def check_network_status(self) -> None: ...
    def check_stop_status(self) -> None: ...
    def check_internal_messages(self) -> None: ...
    def stop(self) -> None: ...
    def join(self) -> None: ...

class _run_decorator:
    class Dummy: ...

@dataclass
class RunStatus:
    sync_items_total: int = ...
    sync_items_pending: int = ...
    sync_time: datetime | None = ...
    def __init__(self, sync_items_total, sync_items_pending, sync_time) -> None: ...

class Run:
    """A unit of computation logged by wandb. Typically, this is an ML experiment.

    Create a run with `wandb.init()`:
    <!--yeadoc-test:run-object-basic-->
    ```python
    import wandb

    run = wandb.init()
    ```

    There is only ever at most one active `wandb.Run` in any process,
    and it is accessible as `wandb.run`:
    <!--yeadoc-test:global-run-object-->
    ```python
    import wandb

    assert wandb.run is None

    wandb.init()

    assert wandb.run is not None
    ```
    anything you log with `wandb.log` will be sent to that run.

    If you want to start more runs in the same script or notebook, you'll need to
    finish the run that is in-flight. Runs can be finished with `wandb.finish` or
    by using them in a `with` block:
    <!--yeadoc-test:run-context-manager-->
    ```python
    import wandb

    wandb.init()
    wandb.finish()

    assert wandb.run is None

    with wandb.init() as run:
        pass  # log data here

    assert wandb.run is None
    ```

    See the documentation for `wandb.init` for more on creating runs, or check out
    [our guide to `wandb.init`](https://docs.wandb.ai/guides/track/launch).

    In distributed training, you can either create a single run in the rank 0 process
    and then log information only from that process, or you can create a run in each process,
    logging from each separately, and group the results together with the `group` argument
    to `wandb.init`. For more details on distributed training with W&B, check out
    [our guide](https://docs.wandb.ai/guides/track/log/distributed-training).

    Currently, there is a parallel `Run` object in the `wandb.Api`. Eventually these
    two objects will be merged.

    Attributes:
        summary: (Summary) Single values set for each `wandb.log()` key. By
            default, summary is set to the last value logged. You can manually
            set summary to the best value, like max accuracy, instead of the
            final value.
    """
    def __init__(self, settings: Settings, config: Dict[str, Any] | None = None, sweep_config: Dict[str, Any] | None = None, launch_config: Dict[str, Any] | None = None) -> None: ...
    def __setattr__(self, attr: str, value: object) -> None: ...
    def __deepcopy__(self, memo: Dict[int, Any]) -> Run: ...
    @property
    def settings(self) -> Settings:
        """A frozen copy of run's Settings object."""
    @property
    def dir(self) -> str:
        """The directory where files associated with the run are saved."""
    @property
    def config(self) -> wandb_config.Config:
        """Config object associated with this run."""
    @property
    def config_static(self) -> wandb_config.ConfigStatic: ...
    @property
    def name(self) -> str | None:
        """Display name of the run.

        Display names are not guaranteed to be unique and may be descriptive.
        By default, they are randomly generated.
        """
    @name.setter
    def name(self, name: str) -> None: ...
    @property
    def notes(self) -> str | None:
        """Notes associated with the run, if there are any.

        Notes can be a multiline string and can also use markdown and latex equations
        inside `$$`, like `$x + 3$`.
        """
    @notes.setter
    def notes(self, notes: str) -> None: ...
    @property
    def tags(self) -> Tuple | None:
        """Tags associated with the run, if there are any."""
    @tags.setter
    def tags(self, tags: Sequence) -> None: ...
    @property
    def id(self) -> str:
        """Identifier for this run."""
    @property
    def sweep_id(self) -> str | None:
        """ID of the sweep associated with the run, if there is one."""
    @property
    def path(self) -> str:
        """Path to the run.

        Run paths include entity, project, and run ID, in the format
        `entity/project/run_id`.
        """
    @property
    def start_time(self) -> float:
        """Unix timestamp (in seconds) of when the run started."""
    @property
    def starting_step(self) -> int:
        """The first step of the run."""
    @property
    def resumed(self) -> bool:
        """True if the run was resumed, False otherwise."""
    @property
    def step(self) -> int:
        """Current value of the step.

        This counter is incremented by `wandb.log`.
        """
    def project_name(self) -> str: ...
    @property
    def mode(self) -> str:
        """For compatibility with `0.9.x` and earlier, deprecate eventually."""
    @property
    def offline(self) -> bool: ...
    @property
    def disabled(self) -> bool: ...
    @property
    def group(self) -> str:
        """Name of the group associated with the run.

        Setting a group helps the W&B UI organize runs in a sensible way.

        If you are doing a distributed training you should give all of the
            runs in the training the same group.
        If you are doing cross-validation you should give all the cross-validation
            folds the same group.
        """
    @property
    def job_type(self) -> str: ...
    @property
    def project(self) -> str:
        """Name of the W&B project associated with the run."""
    def log_code(self, root: str | None = '.', name: str | None = None, include_fn: Callable[[str, str], bool] | Callable[[str], bool] = ..., exclude_fn: Callable[[str, str], bool] | Callable[[str], bool] = ...) -> Artifact | None:
        '''Save the current state of your code to a W&B Artifact.

        By default, it walks the current directory and logs all files that end with `.py`.

        Arguments:
            root: The relative (to `os.getcwd()`) or absolute path to recursively find code from.
            name: (str, optional) The name of our code artifact. By default, we\'ll name
                the artifact `source-$PROJECT_ID-$ENTRYPOINT_RELPATH`. There may be scenarios where you want
                many runs to share the same artifact. Specifying name allows you to achieve that.
            include_fn: A callable that accepts a file path and (optionally) root path and
                returns True when it should be included and False otherwise. This
                defaults to: `lambda path, root: path.endswith(".py")`
            exclude_fn: A callable that accepts a file path and (optionally) root path and
                returns `True` when it should be excluded and `False` otherwise. This
                defaults to a function that excludes all files within `<root>/.wandb/`
                and `<root>/wandb/` directories.

        Examples:
            Basic usage
            ```python
            run.log_code()
            ```

            Advanced usage
            ```python
            run.log_code(
                "../",
                include_fn=lambda path: path.endswith(".py") or path.endswith(".ipynb"),
                exclude_fn=lambda path, root: os.path.relpath(path, root).startswith("cache/"),
            )
            ```

        Returns:
            An `Artifact` object if code was logged
        '''
    def get_url(self) -> str | None:
        """Return the url for the W&B run, if there is one.

        Offline runs will not have a url.
        """
    def get_project_url(self) -> str | None:
        """Return the url for the W&B project associated with the run, if there is one.

        Offline runs will not have a project url.
        """
    def get_sweep_url(self) -> str | None:
        """Return the url for the sweep associated with the run, if there is one."""
    @property
    def url(self) -> str | None:
        """The W&B url associated with the run."""
    @property
    def entity(self) -> str:
        """The name of the W&B entity associated with the run.

        Entity can be a username or the name of a team or organization.
        """
    def display(self, height: int = 420, hidden: bool = False) -> bool:
        """Display this run in jupyter."""
    def to_html(self, height: int = 420, hidden: bool = False) -> str:
        """Generate HTML containing an iframe displaying the current run."""
    def log(self, data: Dict[str, Any], step: int | None = None, commit: bool | None = None, sync: bool | None = None) -> None:
        '''Log a dictionary of data to the current run\'s history.

        Use `wandb.log` to log data from runs, such as scalars, images, video,
        histograms, plots, and tables.

        See our [guides to logging](https://docs.wandb.ai/guides/track/log) for
        live examples, code snippets, best practices, and more.

        The most basic usage is `wandb.log({"train-loss": 0.5, "accuracy": 0.9})`.
        This will save the loss and accuracy to the run\'s history and update
        the summary values for these metrics.

        Visualize logged data in the workspace at [wandb.ai](https://wandb.ai),
        or locally on a [self-hosted instance](https://docs.wandb.ai/guides/hosting)
        of the W&B app, or export data to visualize and explore locally, e.g. in
        Jupyter notebooks, with [our API](https://docs.wandb.ai/guides/track/public-api-guide).

        In the UI, summary values show up in the run table to compare single values across runs.
        Summary values can also be set directly with `wandb.run.summary["key"] = value`.

        Logged values don\'t have to be scalars. Logging any wandb object is supported.
        For example `wandb.log({"example": wandb.Image("myimage.jpg")})` will log an
        example image which will be displayed nicely in the W&B UI.
        See the [reference documentation](https://docs.wandb.com/ref/python/data-types)
        for all of the different supported types or check out our
        [guides to logging](https://docs.wandb.ai/guides/track/log) for examples,
        from 3D molecular structures and segmentation masks to PR curves and histograms.
        `wandb.Table`s can be used to logged structured data. See our
        [guide to logging tables](https://docs.wandb.ai/guides/data-vis/log-tables)
        for details.

        Logging nested metrics is encouraged and is supported in the W&B UI.
        If you log with a nested dictionary like `wandb.log({"train":
        {"acc": 0.9}, "val": {"acc": 0.8}})`, the metrics will be organized into
        `train` and `val` sections in the W&B UI.

        wandb keeps track of a global step, which by default increments with each
        call to `wandb.log`, so logging related metrics together is encouraged.
        If it\'s inconvenient to log related metrics together
        calling `wandb.log({"train-loss": 0.5}, commit=False)` and then
        `wandb.log({"accuracy": 0.9})` is equivalent to calling
        `wandb.log({"train-loss": 0.5, "accuracy": 0.9})`.

        `wandb.log` is not intended to be called more than a few times per second.
        If you want to log more frequently than that it\'s better to aggregate
        the data on the client side or you may get degraded performance.

        Arguments:
            data: (dict, optional) A dict of serializable python objects i.e `str`,
                `ints`, `floats`, `Tensors`, `dicts`, or any of the `wandb.data_types`.
            commit: (boolean, optional) Save the metrics dict to the wandb server
                and increment the step.  If false `wandb.log` just updates the current
                metrics dict with the data argument and metrics won\'t be saved until
                `wandb.log` is called with `commit=True`.
            step: (integer, optional) The global step in processing. This persists
                any non-committed earlier steps but defaults to not committing the
                specified step.
            sync: (boolean, True) This argument is deprecated and currently doesn\'t
                change the behaviour of `wandb.log`.

        Examples:
            For more and more detailed examples, see
            [our guides to logging](https://docs.wandb.com/guides/track/log).

            ### Basic usage
            <!--yeadoc-test:init-and-log-basic-->
            ```python
            import wandb

            run = wandb.init()
            run.log({"accuracy": 0.9, "epoch": 5})
            ```

            ### Incremental logging
            <!--yeadoc-test:init-and-log-incremental-->
            ```python
            import wandb

            run = wandb.init()
            run.log({"loss": 0.2}, commit=False)
            # Somewhere else when I\'m ready to report this step:
            run.log({"accuracy": 0.8})
            ```

            ### Histogram
            <!--yeadoc-test:init-and-log-histogram-->
            ```python
            import numpy as np
            import wandb

            # sample gradients at random from normal distribution
            gradients = np.random.randn(100, 100)
            run = wandb.init()
            run.log({"gradients": wandb.Histogram(gradients)})
            ```

            ### Image from numpy
            <!--yeadoc-test:init-and-log-image-numpy-->
            ```python
            import numpy as np
            import wandb

            run = wandb.init()
            examples = []
            for i in range(3):
                pixels = np.random.randint(low=0, high=256, size=(100, 100, 3))
                image = wandb.Image(pixels, caption=f"random field {i}")
                examples.append(image)
            run.log({"examples": examples})
            ```

            ### Image from PIL
            <!--yeadoc-test:init-and-log-image-pillow-->
            ```python
            import numpy as np
            from PIL import Image as PILImage
            import wandb

            run = wandb.init()
            examples = []
            for i in range(3):
                pixels = np.random.randint(low=0, high=256, size=(100, 100, 3), dtype=np.uint8)
                pil_image = PILImage.fromarray(pixels, mode="RGB")
                image = wandb.Image(pil_image, caption=f"random field {i}")
                examples.append(image)
            run.log({"examples": examples})
            ```

            ### Video from numpy
            <!--yeadoc-test:init-and-log-video-numpy-->
            ```python
            import numpy as np
            import wandb

            run = wandb.init()
            # axes are (time, channel, height, width)
            frames = np.random.randint(low=0, high=256, size=(10, 3, 100, 100), dtype=np.uint8)
            run.log({"video": wandb.Video(frames, fps=4)})
            ```

            ### Matplotlib Plot
            <!--yeadoc-test:init-and-log-matplotlib-->
            ```python
            from matplotlib import pyplot as plt
            import numpy as np
            import wandb

            run = wandb.init()
            fig, ax = plt.subplots()
            x = np.linspace(0, 10)
            y = x * x
            ax.plot(x, y)  # plot y = x^2
            run.log({"chart": fig})
            ```

            ### PR Curve
            ```python
            import wandb

            run = wandb.init()
            run.log({"pr": wandb.plots.precision_recall(y_test, y_probas, labels)})
            ```

            ### 3D Object
            ```python
            import wandb

            run = wandb.init()
            run.log(
                {
                    "generated_samples": [
                        wandb.Object3D(open("sample.obj")),
                        wandb.Object3D(open("sample.gltf")),
                        wandb.Object3D(open("sample.glb")),
                    ]
                }
            )
            ```

        Raises:
            wandb.Error: if called before `wandb.init`
            ValueError: if invalid data is passed

        '''
    def save(self, glob_str: str | None = None, base_path: str | None = None, policy: PolicyName = 'live') -> bool | List[str]:
        """Ensure all files matching `glob_str` are synced to wandb with the policy specified.

        Arguments:
            glob_str: (string) a relative or absolute path to a unix glob or regular
                path.  If this isn't specified the method is a noop.
            base_path: (string) the base path to run the glob relative to
            policy: (string) on of `live`, `now`, or `end`
                - live: upload the file as it changes, overwriting the previous version
                - now: upload the file once now
                - end: only upload file when the run ends
        """
    def restore(self, name: str, run_path: str | None = None, replace: bool = False, root: str | None = None) -> None | TextIO: ...
    def finish(self, exit_code: int | None = None, quiet: bool | None = None) -> None:
        """Mark a run as finished, and finish uploading all data.

        This is used when creating multiple runs in the same process. We automatically
        call this method when your script exits or if you use the run context manager.

        Arguments:
            exit_code: Set to something other than 0 to mark a run as failed
            quiet: Set to true to minimize log output
        """
    def join(self, exit_code: int | None = None) -> None:
        """Deprecated alias for `finish()` - use finish instead."""
    def status(self) -> RunStatus:
        """Get sync info from the internal backend, about the current run's sync status."""
    @staticmethod
    def plot_table(vega_spec_name: str, data_table: wandb.Table, fields: Dict[str, Any], string_fields: Dict[str, Any] | None = None) -> CustomChart:
        """Create a custom plot on a table.

        Arguments:
            vega_spec_name: the name of the spec for the plot
            data_table: a wandb.Table object containing the data to
                be used on the visualization
            fields: a dict mapping from table keys to fields that the custom
                visualization needs
            string_fields: a dict that provides values for any string constants
                the custom visualization needs
        """
    def define_metric(self, name: str, step_metric: str | wandb_metric.Metric | None = None, step_sync: bool | None = None, hidden: bool | None = None, summary: str | None = None, goal: str | None = None, overwrite: bool | None = None, **kwargs: Any) -> wandb_metric.Metric:
        '''Define metric properties which will later be logged with `wandb.log()`.

        Arguments:
            name: Name of the metric.
            step_metric: Independent variable associated with the metric.
            step_sync: Automatically add `step_metric` to history if needed.
                Defaults to True if step_metric is specified.
            hidden: Hide this metric from automatic plots.
            summary: Specify aggregate metrics added to summary.
                Supported aggregations: "min,max,mean,best,last,none"
                Default aggregation is `copy`
                Aggregation `best` defaults to `goal`==`minimize`
            goal: Specify direction for optimizing the metric.
                Supported directions: "minimize,maximize"

        Returns:
            A metric object is returned that can be further specified.

        '''
    def watch(self, models, criterion: Incomplete | None = None, log: str = 'gradients', log_freq: int = 100, idx: Incomplete | None = None, log_graph: bool = False) -> None: ...
    def unwatch(self, models: Incomplete | None = None) -> None: ...
    def link_artifact(self, artifact: Artifact, target_path: str, aliases: List[str] | None = None) -> None:
        '''Link the given artifact to a portfolio (a promoted collection of artifacts).

        The linked artifact will be visible in the UI for the specified portfolio.

        Arguments:
            artifact: the (public or local) artifact which will be linked
            target_path: `str` - takes the following forms: {portfolio}, {project}/{portfolio},
                or {entity}/{project}/{portfolio}
            aliases: `List[str]` - optional alias(es) that will only be applied on this linked artifact
                                   inside the portfolio.
            The alias "latest" will always be applied to the latest version of an artifact that is linked.

        Returns:
            None

        '''
    def use_artifact(self, artifact_or_name: str | Artifact, type: str | None = None, aliases: List[str] | None = None, use_as: str | None = None) -> Artifact:
        """Declare an artifact as an input to a run.

        Call `download` or `file` on the returned object to get the contents locally.

        Arguments:
            artifact_or_name: (str or Artifact) An artifact name.
                May be prefixed with entity/project/. Valid names
                can be in the following forms:
                    - name:version
                    - name:alias
                    - digest
                You can also pass an Artifact object created by calling `wandb.Artifact`
            type: (str, optional) The type of artifact to use.
            aliases: (list, optional) Aliases to apply to this artifact
            use_as: (string, optional) Optional string indicating what purpose the artifact was used with.
                                       Will be shown in UI.

        Returns:
            An `Artifact` object.
        """
    def log_artifact(self, artifact_or_path: Artifact | StrPath, name: str | None = None, type: str | None = None, aliases: List[str] | None = None) -> Artifact:
        '''Declare an artifact as an output of a run.

        Arguments:
            artifact_or_path: (str or Artifact) A path to the contents of this artifact,
                can be in the following forms:
                    - `/local/directory`
                    - `/local/directory/file.txt`
                    - `s3://bucket/path`
                You can also pass an Artifact object created by calling
                `wandb.Artifact`.
            name: (str, optional) An artifact name. May be prefixed with entity/project.
                Valid names can be in the following forms:
                    - name:version
                    - name:alias
                    - digest
                This will default to the basename of the path prepended with the current
                run id  if not specified.
            type: (str) The type of artifact to log, examples include `dataset`, `model`
            aliases: (list, optional) Aliases to apply to this artifact,
                defaults to `["latest"]`

        Returns:
            An `Artifact` object.
        '''
    def upsert_artifact(self, artifact_or_path: Artifact | str, name: str | None = None, type: str | None = None, aliases: List[str] | None = None, distributed_id: str | None = None) -> Artifact:
        '''Declare (or append to) a non-finalized artifact as output of a run.

        Note that you must call run.finish_artifact() to finalize the artifact.
        This is useful when distributed jobs need to all contribute to the same artifact.

        Arguments:
            artifact_or_path: (str or Artifact) A path to the contents of this artifact,
                can be in the following forms:
                    - `/local/directory`
                    - `/local/directory/file.txt`
                    - `s3://bucket/path`
                You can also pass an Artifact object created by calling
                `wandb.Artifact`.
            name: (str, optional) An artifact name. May be prefixed with entity/project.
                Valid names can be in the following forms:
                    - name:version
                    - name:alias
                    - digest
                This will default to the basename of the path prepended with the current
                run id  if not specified.
            type: (str) The type of artifact to log, examples include `dataset`, `model`
            aliases: (list, optional) Aliases to apply to this artifact,
                defaults to `["latest"]`
            distributed_id: (string, optional) Unique string that all distributed jobs share. If None,
                defaults to the run\'s group name.

        Returns:
            An `Artifact` object.
        '''
    def finish_artifact(self, artifact_or_path: Artifact | str, name: str | None = None, type: str | None = None, aliases: List[str] | None = None, distributed_id: str | None = None) -> Artifact:
        '''Finishes a non-finalized artifact as output of a run.

        Subsequent "upserts" with the same distributed ID will result in a new version.

        Arguments:
            artifact_or_path: (str or Artifact) A path to the contents of this artifact,
                can be in the following forms:
                    - `/local/directory`
                    - `/local/directory/file.txt`
                    - `s3://bucket/path`
                You can also pass an Artifact object created by calling
                `wandb.Artifact`.
            name: (str, optional) An artifact name. May be prefixed with entity/project.
                Valid names can be in the following forms:
                    - name:version
                    - name:alias
                    - digest
                This will default to the basename of the path prepended with the current
                run id  if not specified.
            type: (str) The type of artifact to log, examples include `dataset`, `model`
            aliases: (list, optional) Aliases to apply to this artifact,
                defaults to `["latest"]`
            distributed_id: (string, optional) Unique string that all distributed jobs share. If None,
                defaults to the run\'s group name.

        Returns:
            An `Artifact` object.
        '''
    def alert(self, title: str, text: str, level: str | AlertLevel | None = None, wait_duration: int | float | timedelta | None = None) -> None:
        """Launch an alert with the given title and text.

        Arguments:
            title: (str) The title of the alert, must be less than 64 characters long.
            text: (str) The text body of the alert.
            level: (str or wandb.AlertLevel, optional) The alert level to use, either: `INFO`, `WARN`, or `ERROR`.
            wait_duration: (int, float, or timedelta, optional) The time to wait (in seconds) before sending another
                alert with this title.
        """
    def __enter__(self) -> Run: ...
    def __exit__(self, exc_type: Type[BaseException], exc_val: BaseException, exc_tb: TracebackType) -> bool: ...
    def mark_preempting(self) -> None:
        """Mark this run as preempting.

        Also tells the internal process to immediately report this to server.
        """

def restore(name: str, run_path: str | None = None, replace: bool = False, root: str | None = None) -> None | TextIO:
    """Download the specified file from cloud storage.

    File is placed into the current directory or run directory.
    By default, will only download the file if it doesn't already exist.

    Arguments:
        name: the name of the file
        run_path: optional path to a run to pull files from, i.e. `username/project_name/run_id`
            if wandb.init has not been called, this is required.
        replace: whether to download the file even if it already exists locally
        root: the directory to download the file to.  Defaults to the current
            directory or the run directory if wandb.init was called.

    Returns:
        None if it can't find the file, otherwise a file object open for reading

    Raises:
        wandb.CommError: if we can't connect to the wandb backend
        ValueError: if the file is not found or can't find run_path
    """
def finish(exit_code: int | None = None, quiet: bool | None = None) -> None:
    """Mark a run as finished, and finish uploading all data.

    This is used when creating multiple runs in the same process.
    We automatically call this method when your script exits.

    Arguments:
        exit_code: Set to something other than 0 to mark a run as failed
        quiet: Set to true to minimize log output
    """
